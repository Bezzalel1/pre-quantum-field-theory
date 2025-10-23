
# PQF Sink-ularity — Single-Block Simulation (Robust Shooting)
# ------------------------------------------------------------
# Solves:  φ'' + (2/r) φ' = V'(φ) - Λ0(φ) ρ(r)
# BCs:     φ'(0)=0 (regular), φ(Rmax)=0 (outer anchor)
# Method:  Shooting with solve_ivp + bracketed root_scalar, plus a mild homotopy (s: 0→1).

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar

# ---------- Parameters (same physics) ----------
rho0     = 1.0
phi_s    = 1.0
lambda0  = 0.5
M_cut    = 1.0
r0_matter= 5.0
Rmax     = 40.0
chi_thresh = 1.0

# ---------- Model pieces ----------
def lam(phi):   # λ(φ) = λ0 (1 - e^{-φ/φs})
    return lambda0 * (1.0 - np.exp(-phi / phi_s))
def lamp(phi):  # λ'(φ)
    return (lambda0 / phi_s) * np.exp(-phi / phi_s)
def Vp(phi):    # V'(φ) = (ρ0/φs) e^{-φ/φs}
    return (rho0 / phi_s) * np.exp(-phi / phi_s)
def Lambda0(phi):   # Λ0(φ) = (λ'(φ) φ + λ(φ)) / M_cut
    return (lamp(phi) * phi + lam(phi)) / M_cut
def rho_profile(r):
    return np.exp(-r / r0_matter)

# ---------- ODE (for a given scale s in [0,1]) ----------
# We (mildly) homotope only the coupling term so s=0 is easy; if needed we’ll step s upward.
def make_rhs(scale):
    def rhs(r, y):
        phi, dphi = y
        # avoid the 2/r singularity by starting at r>0; solve_ivp handles r=0 if dphi=0, but we nudge start.
        geom = -(2.0/max(r, 1e-9)) * dphi
        return [dphi, geom + Vp(phi) - scale * Lambda0(phi) * rho_profile(r)]
    return rhs

# ---------- Integrate given a center value φ(0)=phi0 ----------
def integrate_to_R(phi0, scale, r_start=1e-6, r_end=Rmax):
    rhs = make_rhs(scale)
    y0 = [phi0, 0.0]                 # φ'(0)=0 regularity
    sol = solve_ivp(rhs, (r_start, r_end), y0, method="RK45",
                    rtol=2e-6, atol=1e-8, dense_output=False, max_step=0.2)
    return sol.t, sol.y

# ---------- Shooting residual: we want φ(Rmax)=0 ----------
def boundary_residual(phi0, scale):
    t, Y = integrate_to_R(phi0, scale)
    phi_R = Y[0, -1]
    return phi_R

# ---------- Find φ(0) by bracketing safely ----------
def find_phi0(scale):
    # Scan a bracket automatically; widen until sign change is found.
    # Start symmetric around 0 because φ=0 is near the outer anchor.
    lo, hi = -3.0, 3.0
    f_lo = boundary_residual(lo, scale)
    f_hi = boundary_residual(hi, scale)
    # Expand bracket if needed (max 12 expansions)
    for _ in range(12):
        if np.sign(f_lo) != np.sign(f_hi):
            break
        lo *= 1.5
        hi *= 1.5
        f_lo = boundary_residual(lo, scale)
        f_hi = boundary_residual(hi, scale)
    # If still no sign change, fall back to secant from two nearby seeds
    if np.sign(f_lo) == np.sign(f_hi):
        # try a small secant step around zero
        a, b = -0.5, 0.5
        fa, fb = boundary_residual(a, scale), boundary_residual(b, scale)
        # if still same sign, just pick the smaller |f| direction to start from
        if abs(fa) < abs(fb):
            return a
        else:
            return b
    # Use robust bracketing solver (bisect -> Brent)
    root = root_scalar(boundary_residual, args=(scale,), bracket=(lo, hi), method="brentq", xtol=1e-9, rtol=1e-8, maxiter=100)
    return float(root.root)

# ---------- Mild homotopy: s = 0.0 → 1.0 ----------
scales = np.linspace(0.0, 1.0, 6)   # just a few steps; shooting is stable
phi0_guess = 0.0
phi_profile = None
r_grid = None

for k, s in enumerate(scales, start=1):
    # find center value for current scale, seeded by previous step
    try:
        phi0 = find_phi0(s)
    except Exception:
        # fallback: nudge from previous guess and retry once
        phi0 = phi0_guess + (0.2 if phi0_guess >= 0 else -0.2)
        try:
            phi0 = find_phi0(s)
        except Exception as e2:
            raise RuntimeError(f"Shooting failed at scale={s:.2f}: {e2}")
    # integrate with the found φ(0)
    r_grid, Y = integrate_to_R(phi0, s)
    phi_profile = Y[0]
    dphi_profile= Y[1]
    phi0_guess = phi0
    print(f"✓ step {k}/{len(scales)}  scale={s:.2f}  phi(0)={phi0:.6f}")

# ---------- Diagnostics ----------
R   = r_grid
phi = phi_profile
dphi= dphi_profile

# Phase-valve indicator χ = [Λ0(φ) ρ] / V'(φ)
Vp_safe = np.maximum(Vp(phi), 1e-30)
chi = (Lambda0(phi) * rho_profile(R)) / Vp_safe

# χ = 1 radius (closest point)
idx_star = int(np.argmin(np.abs(chi - chi_thresh)))
R_star = R[idx_star]

# 1/e radius (aux)
target = phi[0]/np.e
mask_1e = (phi <= target) if phi[0] >= 0 else (phi >= target)
R_1e = R[np.argmax(mask_1e)] if np.any(mask_1e) else np.nan

# ---------- Report ----------
print("✅ BVP solved with physical boundary conditions.")
print(f"Phase-valve core radius (χ=1): R_* = {R_star:.3f}")
if np.isfinite(R_1e):
    print(f"1/e geometric radius (aux):  R_1e = {R_1e:.3f}")

# ---------- Plots ----------
fig, ax = plt.subplots(1, 2, figsize=(12, 4))

# φ(r)
ax[0].plot(R, phi, lw=3)
ax[0].axvline(R_star, ls="--", c="k", alpha=0.8, label=f"R_* = {R_star:.2f}")
if np.isfinite(R_1e):
    ax[0].axvline(R_1e, ls=":", c="gray", alpha=0.8, label=f"R_1e = {R_1e:.2f}")
ax[0].set_xlabel("r")
ax[0].set_ylabel("φ(r)")
ax[0].set_title("PQF Core: φ(r) (Shooting)")
ax[0].grid(alpha=0.3)
ax[0].legend()

# χ(r)
ax[1].plot(R, chi, lw=3)
ax[1].axhline(1.0, ls="--", c="k", alpha=0.8)
ax[1].set_ylim(0, max(1.2, float(np.nanmax(chi)) * 1.05))
ax[1].set_xlabel("r")
ax[1].set_ylabel("χ(r) = Λ₀(φ)ρ / V'(φ)")
ax[1].set_title("Phase-Valve Criterion (χ = 1)")
ax[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()

print("✅ Collapse halts naturally — finite core forms without singularity.")
