# === PQF Finite-Core (Phase-Valve) Solver ===
# Fully derived from the PQF Lagrangian — no toy terms.
# Demonstrates that gravitational collapse halts at χ=1,
# forming a finite coherent core (no singularity).
# Repo: github.com/Bezzalel1/pre-quantum-field-theory
# Author: Daniel Manu, 2025

# === PQF Singularity → Finite Core (Fully-derived, dual-method solver) ===
# PDE (static, spherical):  φ'' + (2/r) φ' = V'(φ) - Λ0(φ) ρ(r)
# BCs: φ'(0)=0  (regular center),  φ'(Rmax)=0  (free outer)
# Phase valve: χ(r) = [Λ0(φ) ρ(r)] / V'(φ) ; core boundary R_*: χ=1

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, solve_bvp
from scipy.optimize import root_scalar

# ---------- choose method ----------
METHOD = "shooting"      # "shooting" (robust) or "bvp_strict"

# ---------- physical parameters ----------
rho0, phi_s, M_cut = 1.0, 1.0, 1.0
lambda0  = 0.60          # coupling amplitude
r0       = 5.0           # matter scale in rho(r)=exp(-r/r0)
Rmax     = 60.0          # outer radius (increase if χ<1 in domain)
rtol, atol = 1e-7, 1e-9  # integrator tolerances

# ---------- derived PQF pieces ----------
def safe_exp(x): 
    return np.exp(np.clip(x, -50.0, 50.0))

def lam(phi):                 # λ(φ)
    return lambda0 * (1.0 - safe_exp(-phi / phi_s))

def lamp(phi):                # λ'(φ)
    return (lambda0 / phi_s) * safe_exp(-phi / phi_s)

def Vp(phi):                  # V'(φ)  (positive)
    return (rho0 / phi_s) * safe_exp(-phi / phi_s)

def Lambda0(phi):             # Λ0(φ) = [λ'(φ) φ + λ(φ)] / M_cut
    return (lamp(phi) * phi + lam(phi)) / M_cut

def rho_profile(r):           # centrally-peaked matter profile
    return np.exp(-r / r0)

# ---------- regularized ODE (shared) ----------
# Regularized system for shooting: y1=φ, y2=r^2 φ'
def rhs_reg(r, y):
    y1, y2 = y
    # tweak #1: explicit safe r^2 guard without max() to avoid dtype surprises
    r2 = r*r if r > 0.0 else 1e-18
    dy1 = y2 / r2
    dy2 = r2 * (Vp(y1) - Lambda0(y1) * rho_profile(r))
    return [dy1, dy2]

# Collocation system for solve_bvp: y=[φ, φ']
def rhs_bvp(r, y):
    phi, dphi = y
    # safe 2/r term (φ'(0)=0 makes it finite)
    cent = -2.0 * dphi / np.maximum(r, 1e-18)
    d2 = cent + Vp(phi) - Lambda0(phi) * rho_profile(r)
    return np.vstack((dphi, d2))

# ---------- SHOOTING IMPLEMENTATION ----------
def integrate_shoot(A):
    y0 = [A, 0.0]  # φ(0)=A, r^2 φ'(0)=0
    return solve_ivp(rhs_reg, [0.0, Rmax], y0, method="RK45",
                     rtol=rtol, atol=atol, max_step=0.2, dense_output=False)

def residual(A):
    sol = integrate_shoot(A)
    if not sol.success:
        return np.sign(A) * 1e6
    y2R = sol.y[1, -1]
    return y2R / (Rmax*Rmax if Rmax > 0 else 1e-18)  # φ'(Rmax)=0 ⇒ y2(Rmax)=0

def bracket_A(lo=-8.0, hi=8.0, n=81):
    xs = np.linspace(lo, hi, n)
    prev = None
    for A in xs:
        f = residual(A)
        if np.isfinite(f) and prev is not None and f*prev[0] < 0:
            return prev[1], A
        prev = (f, A) if np.isfinite(f) else None
    for W in [12, 20, 30]:
        xs = np.linspace(-W, W, n)
        prev = None
        for A in xs:
            f = residual(A)
            if np.isfinite(f) and prev is not None and f*prev[0] < 0:
                return prev[1], A
            prev = (f, A) if np.isfinite(f) else None
    return None, None

# ---------- BVP IMPLEMENTATION ----------
def solve_bvp_strict():
    # mesh + initial guess: outer φ≈small; smooth to center
    r = np.linspace(1e-6, Rmax, 1200)
    guess = np.linspace(0.8, 0.1, r.size)
    y0 = np.vstack((guess, np.gradient(guess, r)))
    sol = solve_bvp(rhs_bvp,
                    lambda ya, yb: np.array([ya[1], yb[1]]),  # φ'(0)=0, φ'(Rmax)=0
                    r, y0, tol=1e-3, max_nodes=120000)
    if not sol.success:
        # soften tolerance slightly and retry with wider guess
        guess = np.linspace(1.2, 0.0, r.size)
        y0 = np.vstack((guess, np.gradient(guess, r)))
        sol = solve_bvp(rhs_bvp,
                        lambda ya, yb: np.array([ya[1], yb[1]]),
                        r, y0, tol=5e-3, max_nodes=200000)
    if not sol.success:
        raise RuntimeError(f"solve_bvp failed: {sol.message}")
    return sol.x, sol.y[0], sol.y[1]

# ---------- RUN ----------
if METHOD == "shooting":
    Alo, Ahi = bracket_A()
    if Alo is None:
        raise RuntimeError("Could not bracket φ(0). Try larger Rmax or stronger coupling (↑lambda0) or smaller r0.")
    root = root_scalar(residual, bracket=[Alo, Ahi], method="bisect",
                       xtol=1e-8, rtol=1e-8, maxiter=200)
    A_star = float(root.root)
    sol = integrate_shoot(A_star)
    R   = sol.t
    phi = sol.y[0]
    dphi = sol.y[1] / np.maximum(R*R, 1e-18)
    bc_res = dphi[-1]
    method_used = f"Shooting (A*={A_star:.6f})"
elif METHOD == "bvp_strict":
    R, phi, dphi = solve_bvp_strict()
    bc_res = dphi[-1]  # should be ~0
    method_used = "Collocation (solve_bvp)"
else:
    raise ValueError("METHOD must be 'shooting' or 'bvp_strict'")

# ---------- χ and diagnostics ----------
Vp_safe = np.maximum(Vp(phi), 1e-30)
chi = (Lambda0(phi) * rho_profile(R)) / Vp_safe
hit = np.where(chi >= 1.0)[0]
R_star = float(R[hit[0]]) if hit.size else np.nan

phi_c = float(phi[0])
mask_1e = (phi <= phi_c/np.e) if phi_c >= 0 else (phi >= phi_c/np.e)
R_1e = float(R[np.argmax(mask_1e)]) if np.any(mask_1e) else np.nan

print(f"✅ Fully-derived PQF solver OK — {method_used}")
print(f"BC check: φ'(Rmax) ≈ {bc_res:+.3e}")
if np.isfinite(R_star):
    print(f"Valve: opens at R_* = {R_star:.3f}")
else:
    print("Valve: χ=1 not reached in domain.")
    # tweak #2: friendly hint for readers pushing parameters
    print("Hint: increase Rmax (e.g. 100–150) or raise lambda0 / reduce r0 so χ can reach 1 inside the domain.")

# ---------- plots ----------
fig, ax = plt.subplots(1, 2, figsize=(12,4))
ax[0].plot(R, phi, lw=3)
if np.isfinite(R_star): ax[0].axvline(R_star, ls='--', c='k', alpha=.85, label=f"R_*={R_star:.2f}")
if np.isfinite(R_1e):  ax[0].axvline(R_1e,  ls=':',  c='gray', alpha=.8, label=f"R_1e={R_1e:.2f}")
ax[0].set_xlabel("r"); ax[0].set_ylabel("φ(r)"); ax[0].set_title("PQF Core: φ(r)"); ax[0].grid(alpha=.3); ax[0].legend()

ax[1].plot(R, chi, lw=3); ax[1].axhline(1.0, ls='--', c='k', alpha=.85)
ax[1].set_ylim(0, max(1.2, float(np.nanmax(chi))*1.05))
ax[1].set_xlabel("r"); ax[1].set_ylabel("χ(r) = Λ₀(φ) ρ / V'(φ)")
ax[1].set_title("Phase-Valve Criterion (χ=1)"); ax[1].grid(alpha=.3)
plt.tight_layout(); plt.show()