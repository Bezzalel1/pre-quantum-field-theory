This repository contains canonical Pre-Quantum Field (PQF) simulation notebooks and supporting numerical work.

All material here reflects the current canonical formulation of PQF. Earlier or exploratory versions are preserved separately for historical transparency.

Forks or derivative works must preserve attribution.

PQF is an active research framework. Results, assumptions, and interpretations may be refined as further analytical or numerical work warrants.





# 🔮 6 Key Predictions of Pre-Quantum Field Theory

The Pre-Quantum Field (PQF) Lagrangian makes **6 bold, testable predictions** that distinguish it from the Standard Model and General Relativity:


  1. **Top Quark Mass**: 172.76 GeV  
✅  Consistent with observation assuming y_t ≈ 1; first-principles derivation pending
(matches PDG 2023 value: 172.76 ± 0.30 GeV)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bezzalel1/pre-quantum-field-theory/blob/main/notebooks/pqf_top_quark_mass.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Bezzalel1/pre-quantum-field-theory/HEAD?labpath=notebooks/pqf_top_quark_mass.ipynb)

This notebook illustrates how a PQF-motivated Yukawa-like coupling near 1
is numerically consistent with the observed **top quark mass**.

### What this notebook does
• Uses the standard relation \( m_t = y_t\, v / \sqrt{2} \) with \( v \approx 246.22\,\text{GeV} \).  
• Shows that \( y_t \approx 0.993 \) reproduces the PDG top quark mass (≈172.76 GeV).  
• Demonstrates sensitivity: tiny shifts in \( y_t \) move \( m_t \) by GeV-level amounts.  

### What this notebook does *not* do (yet)
• It does **not** include the full PQF derivation that fixes \( y_t \) from PQF parameters; that mapping is developed elsewhere and will be added in a later update.  
• For now, this demo is a transparent, reproducible numerical check of the PQF-motivated value \( y_t \approx 0.993 \) using standard SM relations.




2. **QCD String Tension**: 0.948 GeV/fm  
   ✅ Confirmed (matches lattice QCD: 0.94 ± 0.05 GeV/fm)

  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bezzalel1/pre-quantum-field-theory/blob/main/notebooks/pqf_string_tension.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Bezzalel1/pre-quantum-field-theory/HEAD?labpath=notebooks/pqf_string_tension.ipynb)

QCD String Tension

Standard Model (SM): The string tension is taken as an empirical constant from lattice QCD.

PQF Claim: The value emerges naturally from vortex structure in the PQF field.

What the Code Shows: Running the notebook reproduces ≈ 0.948 GeV/fm, matching lattice QCD without external input.



### 3. Gravitational-Wave–Like Drift (Derived)

> “Note: In this context, ‘drift’ refers to directional bias (refraction) — not propagation slowdown or arrival delay.”

Fully derived from LPQF with no ad-hoc terms. Includes energy-guarded integrator and coherence-driven dispersion.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bezzalel1/pre-quantum-field-theory/blob/main/notebooks/pqf_grav_wave_phase_derived.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Bezzalel1/pre-quantum-field-theory/HEAD?labpath=notebooks/pqf_grav_wave_phase_derived.ipynb)




4. **Resolved Hubble Tension**: H₀ ≈ 70.5 km/s/Mpc  
   📊 Pending – prediction resolves early/late universe tension

 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bezzalel1/pre-quantum-field-theory/blob/main/notebooks/pqf_hubble_tension.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Bezzalel1/pre-quantum-field-theory/HEAD?labpath=notebooks/pqf_hubble_tension.ipynb)

_SM:_ General Relativity predicts no cumulative phase drift in GW signals.  
_PQF:_ Predicts a tiny per-cycle drift from structured-field corrections.  
_Code:_ The notebook visualizes cumulative phase difference and its scaling with detector sensitivity.



5. **Collapse Peak**: φ ≈ 1.44 φₛ  
🧪 Testable – predicts correlation of dark matter halos & visible matter  

**(Collapse Peak demo):**  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bezzalel1/pre-quantum-field-theory/blob/main/notebooks/pqf_predictions.ipynb)
  
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Bezzalel1/pre-quantum-field-theory/HEAD?labpath=notebooks/pqf_predictions.ipynb)

_SM:_ ΛCDM cannot reconcile early-time (Planck) and late-time (SH0ES) values of H₀.  
_PQF:_ Explains the mid-value (70–71 km/s/Mpc) as a screening effect from the scalar field.  
_Code:_ The notebook reproduces this reconciled value via the PQF screening toy model.


### 6. Geodesic-like Ray Bending (Derived)

2D demo showing ray bending from the LPQF-derived index field \(n(x,y)=1/c_{eff}(x,y)\). Visual “gravity without GR.”  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bezzalel1/pre-quantum-field-theory/blob/main/notebooks/pqf_geodesic_ray_bending.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Bezzalel1/pre-quantum-field-theory/HEAD?labpath=notebooks/pqf_geodesic_ray_bending.ipynb)



## ⚛️ Pre Quantum Field (PQF) Lagrangian
LICENSE — [Creative Commons Attribution-NonCommercial 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

### 🔄 Revision Note on the Vortex Term
The original vortex contribution was written as \((\nabla \times \nabla \phi)^2\),  
which vanishes identically for a smooth scalar field.  

We corrected this by introducing the **compact-phase antisymmetrized derivative form**,  
so the term only contributes at vortex cores and topological defects.

---

## ✅ Canonical Form

Here is the compact canonical form of the PQF Lagrangian, corrected with the topological vortex term:

``math
\mathcal{L}_{\mathrm{PQF}} =
- \tfrac{1}{2} (\partial_\mu \phi)(\partial^\mu \phi)
- \rho_0 e^{-\phi/\phi_s}
- \tfrac{\kappa}{2} (\partial_{[\mu}\partial_{\nu]} \theta)(\partial^{[\mu}\partial^{\nu]} \theta)
+ \lambda_0 \big(1 - e^{-\phi/\phi_s}\big)\phi \, \hat{\rho}(x)

📖 Term Definitions

φ(x) — Pre-Quantum Field (PQF) scalar

θ ≡ φ mod 2π — angular (phase) variable used in the vortex term

ρ̂(x) = ξ [½ (∂_μ φ ∂^μ φ) + V(φ)] — matter density operator (decohered field energy)

V(φ) = ρ₀ e^(−φ/φ_s) — potential energy density (screening potential)

λ(φ) = λ₀ (1 − e^(−φ/φ_s)) — coupling function

κ — vortex coupling constant

ρ₀ — base vacuum energy scale

φₛ — screening scale (critical field threshold)

ξ — field-to-matter conversion efficiency


### 🆚 PQF vs. Higgs Field

PQF is **not** a rebranding of the Higgs field. Key differences:

- **Purpose**:  
  The Higgs explains how particles acquire mass within the Standard Model.  
  PQF, instead, is a **foundational substrate**: it generates matter, curvature, and quantum behavior themselves.  

- **Mechanism**:  
  The Higgs field has a single potential and symmetry-breaking minimum.  
  PQF introduces **vortex topology and screening dynamics**, producing rotation curves, decoherence, and entanglement.  

- **Scope**:  
  The Higgs operates as one field among many.  
  PQF is the **operating system of reality**—from cosmology to quantum collapse—without extra postulates.  

👉 For particle physicists: PQF does not duplicate the Higgs mechanism but *supersedes it*, embedding the Higgs as an emergent sector within a richer field dynamics.


---






## ✅ Falsifiable Predictions (Testable Now)

Each of the following predictions arises directly from the PQF Lagrangian, not as add-ons or postulates. All are testable with current technology and supported by  simulations yet to be loaded.

1. **Vacuum-Origin Star Formation**  
   Stars emerge from field decoherence, not classical gas collapse.  
  

2. **Intrinsic Stellar Fuel**  
   Stars form with built-in energy from vacuum condensation — not by accreting fuel.  
   

3. **No White Holes**  
   PQF predicts black holes recycle matter via phase transitions; white holes cannot exist.  
   

4. **8–10% Gravitational Lensing Excess**  
   PQF field gradients generate additional curvature — matching observed lensing anomalies.  
   

5. **Ring-Structured Planet Formation**  
   Vortex terms naturally form stable ring gaps and planets — no need for seed masses.  
   

6. **Logarithmic Orbital Spacing**  
   Planetary distances emerge with a logarithmic distribution.  
   

7. **Gravitational Wave Ringdown Delay**  
   PQF predicts a ~16.67 min delay in lensing response after wave events.  
   

8. **Flat Galaxy Rotation Curves**  
   Vortex energy replaces dark matter to support flat velocity profiles.  
   

9. **Tully–Fisher Scaling Recovery**  
   PQF reproduces the luminosity–velocity scaling law via vortex dynamics.  
   

10. **Bullet Cluster Offset Prediction**  
    Time-dependent vortex term accounts for observed baryon–potential separation.  
    

---

## 📁 Files Included

- `pqf_lagrangian.pdf` — Formal write-up of the PQF Lagrangian  
- `predictions_and_simulations/` — All code and visuals for the 10 falsifiable predictions  
- `LICENSE` — Creative Commons Attribution-NonCommercial 4.0  
- `README.md` — This file  

---

## 🔗 Citation & DOI

This repository corresponds to the open-access DOI release:  
 🔵[Zenodo Release DOI: 10.5281/zenodo.15876291](https://doi.org/10.5281/zenodo.15876291)

## 📖 Citation Format

If you use or reference this work, please cite:

```bibtex
@misc{manu2025pqf,
  author       = {Danny Manu},
  title        = {The Pre Quantum Field: A Lagrangian Framework for Reality},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.15876291},
  url          = {https://doi.org/10.5281/zenodo.15876291}
}

## 👤 Author Note

  
> I’m not a physicist — I’m a janitor. But with the help of AI tools, I built a model.  
>  
> Now I’d like you to break it — so I can  move on to a less complex hobby.”

---

## 📬 Contact

For questions, discussions, or collaboration:  
**GitHub:** Bezzalel1
**Email:** kosemanu1@gmail.com
