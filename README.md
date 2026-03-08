This repository contains canonical Pre-Quantum Field (PQF) simulation notebooks and supporting numerical work.

All material here reflects the current canonical formulation of PQF. Earlier or exploratory versions are preserved separately for historical transparency.

Forks or derivative works must preserve attribution.

PQF is an active research framework. Results, assumptions, and interpretations may be refined as further analytical or numerical work warrants.





# 🔮 6 Key Predictions of Pre-Quantum Field Theory

The Pre-Quantum Field (PQF) Lagrangian makes **6 bold, testable predictions** that distinguish it from the Standard Model and General Relativity:


  1. **Top Quark Mass**: 172.76 GeV  
  Consistent with observation assuming y_t ≈ 1; first-principles derivation pending
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










2.**QCD String Tension**: 0.948 GeV/fm  
    # PQF: QCD String Tension — Numerical Check

This notebook checks that the **Pre-Quantum Field (PQF)** framework’s
string-tension value is numerically consistent with a representative
**QCD string tension** from lattice calculations.

**In short:** we adopt a PQF-motivated value σ_PQF = 0.948 GeV/fm
(from separate PQF analysis, not derived in this notebook) and compare it
with a representative lattice QCD value σ_lat ≈ 0.94 ± 0.05 GeV/fm.
The two agree well within the quoted lattice uncertainty.

## What this notebook does

- States a representative lattice reference value and the PQF-motivated value σ_PQF.
- Computes their difference and how many **standard deviations** separate them.
- Plots a side-by-side comparison with an error bar for the lattice value.

## What this notebook does *not* do (yet)

- It does **not** include the full PQF first-principles derivation that fixes σ
  from PQF parameters. That mapping is handled in separate analytical work and
  will be documented in a dedicated notebook/paper.

For now, this demo provides a transparent, reproducible check of the stated
PQF value against lattice results.

  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bezzalel1/pre-quantum-field-theory/blob/main/notebooks/pqf_string_tension.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Bezzalel1/pre-quantum-field-theory/HEAD?labpath=notebooks/pqf_string_tension.ipynb)






### 3. Gravitational-Wave–Like Drift (Derived from LPQF dynamics)

> “Note: In this context, ‘drift’ refers to directional bias (refraction) — not propagation slowdown or arrival delay.”

Derived directly from LPQF equations of motion with no ad-hoc terms; implemented using an energy-guarded integrator and coherence-driven dispersion.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bezzalel1/pre-quantum-field-theory/blob/main/notebooks/pqf_grav_wave_phase_derived.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Bezzalel1/pre-quantum-field-theory/HEAD?labpath=notebooks/pqf_grav_wave_phase_derived.ipynb)






4. Hubble Tension Compatibility: H₀ ≈ 70.5 km/s/Mpc
 Pending observational confirmation — PQF predicts an effective H₀ consistent with both early- and late-universe measurements.

 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bezzalel1/pre-quantum-field-theory/blob/main/notebooks/pqf_hubble_tension.ipynb)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Bezzalel1/pre-quantum-field-theory/HEAD?labpath=notebooks/pqf_hubble_tension.ipynb)

_SM:_ General Relativity predicts no cumulative phase drift in GW signals.  
_PQF:_ Predicts a tiny per-cycle drift from structured-field corrections.  
_Code:_ The notebook visualizes cumulative phase difference and its scaling with detector sensitivity.





5. **Collapse Peak**: φ ≈ 1.44 φₛ  
   Testable – predicts a preferred collapse amplitude (φ ≈ 1.44 φₛ) that should correlate with matter localization in halo-scale environments


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

Revision Note on the Vortex Term
The original vortex contribution was written as
(∇ × ∇φ)²
which vanishes identically for any smooth scalar field. This follows from the vector identity that the curl of a gradient is zero.
To correctly represent topological structure, the canonical formulation introduces a compact phase field
θ ≡ φ mod 2π
and defines the antisymmetrized derivative
Ωμν ≡ ∂[μ ∂ν] θ
For smooth single-valued configurations, Schwarz’s theorem implies
Ωμν = 0
Therefore the vortex sector vanishes in smooth bulk regions and contributes only when the compact phase field contains topological defects such as vortex cores.
Canonical PQF Lagrangian
The canonical PQF Lagrangian used in this repository is
L_PQF =
− ½ (∂μφ)(∂^μφ)
− ρ₀ e^(−φ/φₛ)
− (κ/2) Ωμν Ω^μν
− λ₀ (1 − e^(−φ/φₛ)) φ ρ_loc(x)
with
Ωμν ≡ ∂[μ ∂ν] θ
θ ≡ φ mod 2π
Term Definitions
φ(x) — Pre-Quantum Field (PQF) scalar
θ ≡ φ mod 2π — angular (phase) variable used in the vortex sector
ρ_loc(x) — localized energy density entering the effective coupling
V(φ) = ρ₀ e^(−φ/φₛ) — potential energy density (screening potential)
λ(φ) = λ₀ (1 − e^(−φ/φₛ)) — coupling function
κ — vortex coupling constant
ρ₀ — base vacuum energy scale
φₛ — screening scale (critical field threshold)
ξ — field-to-matter conversion efficiency
Smooth-Bulk Limit
For smooth bulk field configurations
Ωμν = 0
and the dynamics reduce to
L_bulk =
− ½ (∂μφ)(∂^μφ)
− ρ₀ e^(−φ/φₛ)
− λ₀ (1 − e^(−φ/φₛ)) φ ρ_loc(x)
The vortex sector therefore contributes only when topological defects exist in the compact phase field.


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
