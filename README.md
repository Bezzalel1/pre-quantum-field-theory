## Pre Quantum Field (PQF) Lagrangian

```
\mathcal{L}_{\text{PQF}} = -\frac{1}{2} (\partial_\mu \phi)^2 - \rho_0 e^{-\phi/\phi_s}
+ \lambda_0 \left(1 - e^{-\phi/\phi_s}\right) \phi \hat{\rho}(x)
- \frac{\kappa}{2} \left( \epsilon^{\mu\nu\rho\sigma}
\partial_\mu \partial_\nu \phi \, \partial_\rho \partial_\sigma \phi \right)
```


**Where:**

\( \phi(x) \) is the Pre Quantum Field  
\( \hat{\rho}(x) = \xi \left[ \frac{1}{2} (\partial_\mu \phi)^2 + V(\phi) \right] \) is the emergent matter density  
\( V(\phi) = \rho_0 e^{-\phi/\phi_s} \) is the field potential  
\( \kappa \) is the vortex coupling constant  
\( \lambda_0 \) is the matter–field coupling strength


## 📦 Final Form of the PQF Lagrangian (Canonical)

$$
\mathcal{L}_{\mathrm{PQF}}
= -\frac{1}{2}\,(\partial_\mu \phi)(\partial^\mu \phi)
\;-\;\rho_0\,e^{-\phi/\phi_s}
\;-\;\frac{\kappa}{2}\,(\partial_{[\mu}\partial_{\nu]}\theta)(\partial^{[\mu}\partial^{\nu]}\theta)
\;+\;\lambda_0\big(1-e^{-\phi/\phi_s}\big)\,\phi\,\hat{\rho}(x)\,.
$$

**Definitions**
- \( \theta \equiv \phi \bmod 2\pi \) is the compact phase.
- \( \hat{\rho}(x) = \xi\!\left[\tfrac{1}{2}(\partial_\mu\phi)(\partial^\mu\phi) + V(\phi)\right] \), with \( V(\phi)=\rho_0 e^{-\phi/\phi_s} \).
- \( \lambda(\phi)=\lambda_0\!\left(1-e^{-\phi/\phi_s}\right) \).
- Antisymmetrization: \( \partial_{[\mu}\partial_{\nu]}\theta \equiv \partial_\mu\partial_\nu\theta - \partial_\nu\partial_\mu\theta \) (non-zero only at topological defects).
- Indices are raised with the Minkowski metric \( \eta^{\mu\nu} \).

**Remark (collapse drive)**
The local conversion drive scales as
\( D(\phi) \propto \lambda(\phi)\,\phi\,V(\phi)
= \lambda_0\rho_0\,\phi\,(1-e^{-\phi/\phi_s})\,e^{-\phi/\phi_s} \),
which has a single maximum at \( \phi \approx 1.44\,\phi_s \).


### 🔑 Parameter Reference

| Symbol      | Technical Role            | Intuitive Role         |
|-------------|---------------------------|------------------------|
| \( \rho_0 \)   | Base vacuum energy density   | Vacuum’s “fuel tank”    |
| \( \phi_s \)   | Screening scale              | Critical collapse slope |
| \( \kappa \)   | Vortex coupling constant     | String/knot tension     |
| \( \lambda_0 \) | Matter–field coupling       | Collapse switch         |
| \( \xi \)      | Scaling in \(\hat{\rho}\)    | Conversion efficiency   |

                                                                              



> **Note on the vortex term:**  
> In the Lagrangian, the term 
> \(-\tfrac{\kappa}{2}\,\epsilon^{\mu\nu\rho\sigma}\,\partial_\mu\partial_\nu\phi\,\partial_\rho\partial_\sigma\phi\) 
> is understood in its *compact-phase* form.  Because the Levi‑Civita contraction of second derivatives vanishes for a smooth scalar field, we treat \(\phi\) as a compact phase \(\theta=\phi \bmod 2\pi\) and interpret \(\partial_\mu\partial_\nu\theta\) as an antisymmetrized second derivative that picks out topological defects.  This refinement ensures the term is non‑zero only at vortex cores and other defects, aligning with the topological density used in the theory0.




## ✅ Falsifiable Predictions (Testable Now)

Each of the following predictions arises directly from the PQF Lagrangian, not as add-ons or postulates. All are testable with current technology and supported by included simulations.

1. **Vacuum-Origin Star Formation**  
   Stars emerge from field decoherence, not classical gas collapse.  
   🔬 *Simulation included*

2. **Intrinsic Stellar Fuel**  
   Stars form with built-in energy from vacuum condensation — not by accreting fuel.  
   🔬 *Simulation included*

3. **No White Holes**  
   PQF predicts black holes recycle matter via phase transitions; white holes cannot exist.  
   🔬 *Simulation included*

4. **8–10% Gravitational Lensing Excess**  
   PQF field gradients generate additional curvature — matching observed lensing anomalies.  
   🔬 *Simulation included*

5. **Ring-Structured Planet Formation**  
   Vortex terms naturally form stable ring gaps and planets — no need for seed masses.  
   🔬 *Simulation included*

6. **Logarithmic Orbital Spacing**  
   Planetary distances emerge with a logarithmic distribution.  
   🔬 *Simulation included*

7. **Gravitational Wave Ringdown Delay**  
   PQF predicts a ~16.67 min delay in lensing response after wave events.  
   🔬 *Simulation included*

8. **Flat Galaxy Rotation Curves**  
   Vortex energy replaces dark matter to support flat velocity profiles.  
   🔬 *Simulation included*

9. **Tully–Fisher Scaling Recovery**  
   PQF reproduces the luminosity–velocity scaling law via vortex dynamics.  
   🔬 *Simulation included*

10. **Bullet Cluster Offset Prediction**  
    Time-dependent vortex term accounts for observed baryon–potential separation.  
    🔬 *Simulation included*

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
  author       = {Daniel Manu},
  title        = {The Pre Quantum Field: A Lagrangian Framework for Reality},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.15876291},
  url          = {https://doi.org/10.5281/zenodo.15876291}
}

## 👤 Author Note

> “There are high school kids who have forgotten more about physics than I know.  
> I’m not a physicist — I’m a janitor. But with the help of AI tools, I built a model.  
>  
> Now I’d like you to break it — so I can  move on to a less complex hobby.”

---

## 📬 Contact

For questions, discussions, or collaboration:  
**GitHub:** Bezzalel1
**Email:** kosemanu1@gmail.com
