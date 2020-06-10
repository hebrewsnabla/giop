# Offline Gaussian IOps 
## Overlay 1 
### IOp(1/5)
`L103`: Mode of optimization.
* 0        Find local minimum.        
* 1        Find a saddle point.        
* N        Find stationary point on the energy surface with N negative eigenvalues of the 2nd deriv. matrix.        
`L107`: Mode of search.
* 0        Locate the maximum in the LST path.        
* 1        Scan the LST path.        
* N000        Which approximation to make. Default is III for Tomasi (interlocking spheres) and IV for general surface.        
* 1000        Apprx.   I:  Don’t Do Self-Polarization or “Compensation”        
* 2000        Apprx.  II:  Do Self-Polarization, But No Compensation.        
* 3000        Apprx. III:  Do Self-Polarization and Compensation.        
* 4000        Apprx.  IV:  Do III, and Allow Surface To “Relax” in Solution if no spheres…        
* N0000        Whether to evaluate densities using orbitals or density matrix. Default is to use density.        
* 10000        Use MOs.        
* 20000        Use density.        
`L121`: Time step, N*0.0001 fs, default 0.1.
### IOp(1/6)
`L102, L103, L105, L107, L109, L113, L114`: Maximum number of steps (or number of steps for an LST scan).
* 0        NSTEP = Max(20,NVAR+10) (L103)        
*          = Min(20,NVAR+10) (L102, L105, L109)        
*          = Min(40,NVAR+20) (L113, L114)        
* N        NSTEP = N        
### IOp(1/7)
`L103, L105, L109, L112, L113, L114`: Convergence on the first derivative and estimated displacement for the optimization, RMS first derivative < ConvF, RMS Est. Displacement < ConvX = 4*ConvF. For L123, similar convergence control for the GS integrator.
* -1        ConvF = 1/600 Hartree/Bohr or Radian        
* 0        ConvF = 0.0003 Hartree/Bohr or Radian        
* N        ConvF = N*10^-6        
`L116, L117`: Convergence on electric field/charges.
* -1        Default value for optimizations: 10^-7.        
* 0        Default value for single-points: 10^-5 in L116, 10^-7 in L117.        
* N        10^-N.        
`L123`: Regular force/displacement convergence for GS2. For EulerPC, N/1000000 displacement conv.
### IOp(1/8)
`L103, L109, L112`: Maximum step size allowed during Opt.
* 0        DXMAXT = 0.1 Bohr or Radian (L103, Estm or UnitFC).        
*          = 0.3 Bohr or Radian (L103, Read or CalcFC).        
*          = 0.2 Bohr or Radian (L105).        
*          = 0.3 Bohr or Radian(L113, L114).        
* N        DXMAXT = 0.01 * N        
`L117`: General control.
* 0        Which type of basin to use to partition the density isosurface. Default is 4.        
* 1        GradVne.        
* 2        GradRho.        
* 3        Don’t Use Basins, Use only the Center of Nuclear Charge.        
* 4        Use Interlocking Spheres.        
* N0        Order of Adam’s-Bashforth-Moulton (ABM) predictor-corrector method to use in solving diff. eqns. for the grad RHO or Vne trajectories. Default is 4; max is 9.        
* N00        Number of small steps per ABM step to be used in starting ABM and when “slow down” is needed in ABM. Default is 5.        
* N000        Which approximation to make. Default is III for Tomasi (interlocking spheres) and IV for general surface.        
* 1000        Apprx. I – Don’t Do Self-Polarization or “Compensation”        
* 2000        Apprx. II – Do Self-Polarization, But No Compensation.        
* 3000        Apprx. III – Do Self-Polarization and Compensation.        
* 4000        Apprx. IV – Do III, and Allow Surface To “Relax” in Solution if no spheres…        
* N0000        Whether to evaluate densities using orbitals or density matrix. Default is to use density.        
* 10000        Use MOs.        
* 20000        Use density.        
`L121`: Time step, N*0.0001 fs, if N>0, -N*0.0001 au if N<0.
### IOp(1/9)
`L103`: Use of Trust radius.
* 0        Whether to update trust radius (DXMaxT, default Yes). Default is Yes for minima, no for TS.        
* 1        No.        
* 2        Yes.        
* 00        Whether to scale or search the sphere when reducing the step size to the trust radius. Default search for minima, scale for transition states.        
* 10        Scale.        
* 20        Search.        
`L106`: Whether to use symmetry to reduce the number of L110 displacements.
* 0        Yes.        
* 1        No.        
* 10        Do not use symmetry to skip steps back.        
* 100        Do not use symmetry to skip equivalent atoms        
`L107`: Whether to maintain symmetry along the search path.
* 0        Yes.        
* 1        No.        
`L117`: Whether to delete points which are too close together and how close to get to the iso surface in search.
* 0        No; Approx. 1.0 D-6 (N=20)        
* 1        Yes, using a default criterion (0.05 Angstroms).        
* -N        Yes, using a (10^-N Angstroms) criteria: 2.0^-N.        
* N        2.0^-N        
`L121`: Whether to read in initial velocities.
* 0        Default (same as 1).        
* 1        Generate random initial velocity.        
* 2        Read in initial Cartesian velocity (Bohr/sec).        
* 3        Read in initial MW Cartesian velocity (sqrt(amu)*Bohr/sec).        
### IOp(1/10)
`L103, L105, L109, L112, L113, L114`: Input of initial Hessian. All values must be in atomic units (Hartree, Bohr, and radians).
* 0        Use defaults (not valid for L109).        
* 1        Read ((FC(I,J),J=1,I),I=1,NVAR) (8F10.6) (L103 only).        
* 2        Read I,J,FC(I,J) (5I3,F20.0) (L103 only). End with a blank card.        
* 3        Read from checkpoint file in internal coordinates.        
* 4        Second derivative matrix calculated analytically. (Not valid for L109).        
* 5        Read Cartesian forces and force constants from the checkpoint file are converted to internal coordinates.        
* 6        Read Cartesian forces followed by Cartesian force constants (both in format 6F12.8) from input stream, followed by a blank line.        
* 7        Use semi-empirical force constants.        
* 8        Use unit matrix (default for L105; only recognized by 103).        
* 9        Estimate force constants using valence force field.        
* 10        Use unit matrix throughout.        
### IOp(1/11)
`L103`: Test of curvature. Bomb the job if the second derivative matrix has the wrong # of negative eigenvalues.
* 0        Default (Test for z-matrix or Cartesian TS but not for LST/QST or for minimum).        
* 1        Don’t test.        
* 2        Test.        
`L117`: Step size for ABM method in Trudge for isodensity method.
* 0        0.05 (N=2).        
* N        0.1/N.        
### IOp(1/12)
`L103`: Optimization control parameters.
* 0        Use default values.        
* 1        Read in new values for all parameters (see INITBS).        
### IOp(1/13)
`L103, L113, L114, L115, L123`: Type of Hessian Update.
* 0        Default (9 for L103 minimization, 7 for L103 TS, D2Corr and L115, Powell for L113 and L114, Bofill in L123).        
* 1        Powell (not in L103).        
* 2        BFGS (not in L103).        
* 3        BFGS, safeguarding positive definiteness (not in L103 or L115).        
* 4        D2Corr (New, only in L103 and L115).        
* 5        D2Corr (Old, only in L103 and L115).        
* 6        D2Corr (BFGS).        
* 7        D2Corr (Bofill Powell+MS for transition states).        
* 8        D2Corr (No update, use initial Hessian).        
* 9        D2Corr (New if energy rises, otherwise BFGS).        
`L118`: Integration method.
`L121`: Multi-time step parameter (NDtrC,NDtrP).
* 0        No multi-time stepping.        
* NN        Iterate density constraints NN times per step.        
* MM00        Do gradient once every MM steps.        
`L123`: Hessian update.
* 0        Default (Bofill).        
* 1        Murtagh-Sargent (SR1) update.        
* 2        Powell-symmetric-Broyden (PSB) update.        
* 3        Bofill’s update.        
* 4        Sqrt(Bofill) update.        
* 5        No update (keep old Hessian).        
### IOp(1/14)
`L103`: Maximum number of bad steps to allow before doing a linear minimization (i.e., no quadratic step).
* -1        0.        
* 0        Default (0 for TS, 1 for minima).        
* N        Allow N — linear only starts with the N+1st.        
### IOp(1/15)
`L103, L109`: Abort if derivatives too large.
* -1 or 0        No force test at all.        
* N        FMAXT = 0.1 * N.        
### IOp(1/16)
`L103, L113, L114`: Maximum allowable magnitude of the eigenvalues of the second derivative matrix. If the limit is exceeded, the size of the eigenvalue is reduced to the maximum, and processing continues.
* 0        EIGMAX = 25.0 Hartree / Bohr^2 or Radian^2        
* N        EIGMAX = 0.1 * N        
### IOp(1/17)
`L103, L113, L114`: Minimum allowable magnitude of the eigenvalues of the second derivative matrix. Similar to IOp(16).
* 0        EIGMIN = 0.0001.        
* N        EIGMIN = 1. / N.        
### IOp(1/18)
`L103`: Coordinate system.
* 0        Proceed normally.        
* 1        Second derivatives will be computed as directed on the variable definition cards. No optimization will occur.        
* 10        Do optimization in Cartesian coordinates.        
* 20        Do full optimization in redundant internal coordinates.        
* 30        Do full optimization in pruned distance matrix coordinates.        
* 40        Do optimization in z-matrix coordinates.        
* 50        Do full optimization in redundant internal coordinates with large molecular tools.        
* 100        Read the AddRedundant input section for each structure.        
* 1000        Do not define H-bonds (default).        
* 2000        Define H-bonds with no related coordinates.        
* 3000        Define H-bonds and related coordinates.        
* 10000        Reduce the number of redundant internals.        
* 20000        Define all redundant internals.        
* 100000        Old definition of redundant internals.        
* 0000000        Default (2000000).        
* 1000000        Skip MM atoms in internal coordinate definitions and do microiterations the old way, in L103.        
* 2000000        Include MM atoms in internal coordinate definitions (no microiterations).        
* 3000000        Skip MM atoms in internal coordinate definitions and do microiterations the new way, in L120.        
* 4000000        Microiterations for pure MM, done in L402.        
### IOp(1/19)
`L103`: Search selection.
* 0        Default (same as 6).        
* 2        Linear and steepest descent.        
* 3        Steepest descent and linear only when essential.        
* 4        Quadratic if curvature is correct; RFO if not. Linear as usual.        
* 5        Quadratic if curvature is correct; RFO if not. No linear search.        
* 6        RFO and linear.        
* 7        RFO without linear.        
* 8        Newton-Raphson and linear.        
* 9        Newton-Raphson only.        
* 10        GDIIS and linear.        
* 11        GDIIS only.        
* 15        GEDIIS.        
`L113, L114`: Search Selection.
* 0        P-RFO or RFO step only (Default).        
* 1        P-RFO or RFO step for “wrong” Hessian otherwise Newton Raphson.        
### IOp(1/20)
`L101, L106, L108, L109, L110`: Input units.
* 0        Angstroms degrees.        
* 1        Bohrs degrees.        
* 2        Angstroms Radians.        
* 3        Bohrs Radians.        
### IOp(1/21)
`L103, L113, L114`: Expert switch.
* 0        Normal mode.        
* 1        Expert mode. Certain cutoffs used to control the optimization will be relaxed. These include FMAXT, DXMAXT, EIGMAX and EIGMIN.        
### IOp(1/22)
`L107`: Whether to reorder coordinates for maximum coincidence.
* 0        Yes.        
* 1        Assume reactant order equals product order.        
* 2        Read in a re-ordering vector from the input.        
`L115/L123`: Kind of search.
* 0        Both directions and generate search vector.        
* 1         Forward direction and generates vector.        
* 2        Backward direction and generates vector.        
* 3        Both directions and generates vector.        
* 4        Forward direction and reads vector 8F10.6.        
* 5        Forward direction and reads vector 8F10.6.        
* 6        Backward direction and reads vector 8F10.6.        
* 7        Both directions and reads vector 8F10.6.        
### IOp(1/23)
No longer used.
### IOp(1/24)
Whether to round tetrahedral angles.
* 0        Default (Yes).        
* 1        Yes, round angles within 0.001 degree.        
* 2        No.        
### IOp(1/25)
Whether SCRF is used with numerical polarizability.
* 0        No.        
* 1        Yes, the field in /Gen/ must be cleared each time.        
### IOp(1/26)
Accuracy of function being optimized:
* -NNMM         Energy 10^-NN, Gradient 10^-MM.        
* -1        Read in values.        
* 0        Default (same as 1).        
* 1        Normal accuracy for HF (energy and gradient both 1.d-7).        
* 2        Accuracy for DFT with SG1 grid (Energy 1.d-5, gradient 1.d-4).        
* 3        Fine grid accuracy for DFT (Energy 1.d-7, gradient 1.d-6).        
* 4        Ultrafine accuracy (E 1.d-7, G 1.d-6).        
* 5        Superfine accuracy (E 1.d-7, G 1.d-7).        
* 6        UltraFine+PCM accuracy (E 5.d-5, G 5.d-6)        
### IOp(1/27)
= IJKL (i.e. 1000*I+100*J+10*K+L).
Transition state searching using QST and redundant internal coordinates
* L = 0,1        Input one structure, either initial guess of the minimizing structure or transition structure without QST.        
* L = 2        Input 2 structures. The first one is the reactant, the second one is the product. The union of the two redundant coordinates is taken as the redundant coordinates for the TS. The values of the TS coordinate are estimated by interpolating the structure of R and P. R and Pare used to guide the QST optimization of the TS.        
* L = 3        Input 3 structures. The first one is the reactant the second one is the product. The third one is the initial guess of the transition structure. R and P are used to guide the QST optimization of the TS.        
* K = 1-9        Interpolation of initial guess of TS between R and P (TS = 0.1*J*R + 0.1*(10-J)*P, default J=5).        
* J = 1        LST constraint in internals.        
* J = 2        QST constraint in internals.        
* J = 3        LST constraint in distance matrix space.        
* J = 4        QST constraint in distance matrix space.        
* I = 0-9        Control parameters for climbing phase of QST (e.g. QSTRad = 0.01*I, default QSTrad = 0.05).        
### IOp(1/28)
`L103`: Number of translations and rotations to remove during redundant coordinate transformations.
* -2        0.        
* -1        Normal (6 or 5 for linear molecules).        
* 0        Default, same as -1.        
* N        N.        
### IOp(1/29)
`L101`: Specification of nuclear centers.
* 0        By z-matrix.        
* 1        By direct coordinate input (must set IOp(29) in L202).        
* 2        Get z-matrix and variables from the checkpoint file.        
* 3        Get Cartesian coordinates only from the checkpoint file.        
* 4        By model builder, model A.        
* 5        By model builder, model B.        
* 6        Get z-matrix from the checkpoint file, but read new values for some variables from the input stream.        
* 7        Get all input (title, charge and multiplicity, structure) from the checkpoint file.        
* 10        Print details of the model-building process.        
* 000        Default (same as 100).        
* 100        Do not abort job if model builder generates a z-matrix with too many variables.        
* 200        Abort job if model builder generates a z-matrix with too many variables.        
* 1000        Read optimization flags in format 50L1 after the z-matrix.        
* 2000        Set all optimization flags to optimize.        
* 3000        Purge flags except the frozen variables.        
* 4000        Rebuild the coordinate system.        
* 5000        (2+3) Purge all flags but keep the coordinate definition.        
* 6000        Generate new redundant coordinates, reading an input section selecting frozen and optimized atoms.        
* 7000        Mark all internal coordinates as frozen before handling ModRed input        
* 00000        Default, same as 10000.        
* 10000        Mark z-matrix constants as frozen variables rather than wired-in constants.        
* 20000        Do not retain symbolic constants.        
* 100000        Generate a symbolic z-matrix using all Cartesians if none is present on the checkpoint file (a hack to make IRCs work with Cartesian input).        
* 200000        Same as 1, but retain the redundant internal coordinate definitions.        
* 1000000         Get input type or chk file name to read from input stream; title and charge/multiplicity for each structure read from input.        
* 2000000        Read input type for each structure from input stream; title and charge/multiplicity are those of last chk file read.        
* 9000000        Same as 0000000.        
* 00000000        Default (read one set of charge/multiplicity
pairs unless both NFrag and ONIOM are set).        
* 10000000        Read ONIOM charge/multiplicity pairs if reading
any. Fragment values will be defaulted from the supermolecule.        
* 20000000        Read fragment charge/multiplicity pairs if reading any. ONIOM model system values will be defaulted from the real system.        
* 30000000        Read two lines, with ONIOM followed by fragment values.        
### IOp(1/30)
`L103`: Are the read-write files to be updated? This option is set for the last call to 103 in frequency calculations in order to preserve the values of the variables for archiving. It also suppresses error termination on large gradients.
* 0        Yes.        
* 1        No, print internal coordinate step but don’t set up for microiterations and don’t update the RWF.        
* 2        Set up for step but don’t update coordinates; for QM/MM iterative frequencies.        
### IOp(1/32)
Title card punch control.
* 0        Don’t punch.        
* 1        Punch.        
### IOp(1/33)
`L101, L102, L103, L106, L109, L110, L113, L114`: Debug print.
* 0        Off.        
* 1        On.        
### IOp(1/34)
`L101, L102, L103`: Debug + Dump print.
* 0        Off.        
* 1        On.        
### IOp(1/35)
`L102-L112`: Restart.
* 0        Normal optimization.        
* 1        First point of a restart. Get geometry, wavefunction, etc. from the checkpoint file.        
### IOp(1/36)
Checkpoint.
* 0        Normal checkpoint of optimization.        
* 1        Suppress checkpointing.        
### IOp(1/38)
`L103, L106, L107, L108, L109, L110, L111, and L112`: Entry control option (Not by L102 and L105).
* 0        Continuation of run.        
* 1        Initial entry.        
* N>1        In L103:  Initial entry of guided optimization using N levels.        
* N0        In L106:  differentiate N^th derivatives once. In L110 and L111: differentiate energy N times.        
* 000        In L106: differentiate with respect to nuclear coordinates.        
* 100        In L106: differentiate with respect to electric field.        
* 200        In L106: differentiate with respect to field and nuclear.        
* 1000        In L106: Save original forces and force constants.        
* 00000        In L106: Assume all quantities available at the central point will also be computed at displaced points.        
* 10000        In L106: No analytic nuclear coordinate derivatives will be done at displaced points, even though they were done at the central point.        
* 000000        L106 control of number of diff. steps.        
* 100000        Do 2-point differentiation (one step each way).        
* 200000        Do 4-point differentiation (two steps each way).        
* 0000000        Default (1).        
* 1000000        Differentiate with respect to translation vectors for PBC for elasticity.        
* 2000000        Do not differentiate with respect to translation vectors.        
### IOp(1/39)
`L106, L109, L110, L111`: Step size control for numerical differentiation.
`L115`: Path step size.
* 0        Use internal default (0.001 Angstroms and 0.001/3 au E-field in L106, 0.005 Å in L109, 0.01 Angstrom in L110, 0.001 au in L111).        
* N        Use step-size of 0.0001*N (angstroms in L106, L109, L110, electric field au in L111). In L106, the electric field step will be 3x smaller.        
* -1        Read step size (up to 2 for L106, 1 for others), free-format.        
* -N>1        Use step-size of 0.0001*N atomic units everywhere.        
`L123`: Step-size.
* 0        Default (0.1 Bohr, except 0.075 Bohr for EulerPC, or original value if restart. DVV default is 0.25 fs).        
* N<0        Supplied step size is in units of sqrt(amu)*Bohr.        
* N>0        Supplied step size is in units of Bohr.        
### IOp(1/40)
`L113, L114`: Hessian recalculation.
* -1        Pick up analytic second derivatives every time.        
* 0        Just update. The default, except for CalcAll.        
* N        Recalculate the Hessian every N steps.        
`L116`:  Whether to read initial E-field.
* 0        Start with 0.0.        
* 1        Read from checkpoint file.        
* 2        Read from input stream.        
`L123`: Truncation error threshold for the modified BS integration routine (EPS).
* 0        Default (10^-8 Bohr).        
* N        10^-N Bohr.        
### IOp(1/41)
Take previous geometry from checkpoint file:
* N > 0        N^th point of geometry optimization (z-matrix only). Converted to -(N+1) if no z-matrix.        
* N < 0        N^th geometry on trajectory file.        
### IOp(1/42)
`L103, L115, L118, L123`: Number of points along the reaction path in each direction, or maximum number of points in one trajectory. Default 10 for IRC, 100 for trajectory.
`L117`: Cutoff to be used in evaluating densities.
* 0        1.0D-10.        
* N        1.0D-N.        
### IOp(1/43)
`L116`: Extent of Reaction Field.
* 0        Dipole.        
* 1        Quadrupole.        
* 2        Octapole.        
* 3        Hexadecapole.        
`L117`: How to define Radii.
* 0        Default is 11.        
* 1        Use internally stored Radii, centers will be on atoms.        
* 2        Read-in centers and radii on cards.        
* 10        Force Merz-Kollman radii (Default).        
* 20        Force CHELP (Francl) recommended radii.        
* 30        Force CHELPG (Breneman) recommended radii.        
* 100        Read in replacement radii for selected atom types as pairs (IAn,Rad) or (Symbol,Rad), terminated by a blank line.        
* 200        Read in replacement radii for selected atoms as pairs (I,Rad), terminated by a blank line.        
Initial radius of spheres to be placed around attractors to “capture” the gradient trajectories. The final radius is then automatically optimized separately for each atom.
* 0        0.1        
* NM        N.M=NM/10        
### IOp(1/44)
`L115, L123,` and `L125`: IRC Type.
* 0        Optimization coordinates (Default 3 in L15 and L123, 2 in L125).        
* 1        Cartesian.        
* 2        Internal (NYI in L123).        
* 3        Mass-weighted Cartesian (NYI in L125).        
* M0        Initial interpolation in L125 (default 2).        
`L117`: Maximum distance between a nucleus and its portion of the isosurface – used in Trudge only to eliminate, from the outset, points which clearly lie in another basin. This parameter should be chosen with the parameter Cont in mind:
* 0        10.0 au.        
* NM        N.M au = NM/10.        
`L121`: Seed for random number generator (ISeed).
* -1        Use system time initialize iseed (Note each run will give different results).        
* 0        Use default seed value (ISeed = 398465).        
* N        Set random number seed to N.        
### IOp(1/45)
`L123`: Options.
* 00        Which IRC integrator to use. Default = 3, except 6 for ONIOM QuadMac/Micro or 1 for GradientOnly.        
* 01        Euler.        
* 02        LQA.        
* 03        HPC.        
* 04        GS2.        
* 05        DVV.        
* 06        Euler-based PC.        
* 10        Coordinate driving schemes.        
* 0xx        Is the integration being done on an empirical surface? Default=2.        
* 1xx        Yes, this is an empirical surface. The energies and derivatives required for the IRC integration are NOT evaluated in this link. Instead it is assumed that an external program communicates the appropriate values with Link 402, etc. Also, the force constant matrix, when needed, is simply diagonalized, i.e. translation and rotation projections are NOT used. Also, all atomic masses are set to 1.        
* 2xx        No.        
* 0xxx        Order of magnitude for the step size relative to the integer value given with the StepSize=N option on the route line — IOp(1/39). Default=2.        
* Nxxx        Integration step size is taken as IOp(1/39)*10^-N.        
* 0xxxx        Whether or not energies reported in the final summary table should be given relative to the TS energy. Default=1.        
* 1xxxx        Yes.        
* 2xxxx        No.        
* 0xxxxx        Whether or not statistics over coordinates should be converted to Angstoms/Degrees when reported in the summary table. Default=1.        
* 1xxxxx        Yes.        
* 2xxxxx        No.        
* 0xxxxxx        Should a URVA input file be written? Default=2.        
* 1xxxxxx        Yes.        
* 2xxxxxx        No.        
* 0xxxxxxx         Should IRC data besaved to the PES data structure file? Default=1.        
* 1xxxxxxx        Yes.        
* 2xxxxxxx        No.        
* 0xxxxxxxx        When second-order methods are employed, should the Newton-Raphson step test be carried out? Default=1.        
* 1xxxxxxxx        Yes.        
* 2xxxxxxxx        No.        
### IOp(1/46)
Order of multipoles in numerical SCRF.
* 0        Dipole.        
* 1        Quadrupole.        
* 2        Octapole.        
* 3        Hexadecapole.        
### IOp(1/47)
Number of redundant internal coordinates to allow for.
* 0        Default: Max(50000,MCV/(100*NStruc))        
* N        N.        
### IOp(1/48)
IRCMax control.
* 1        Do IRCMax.        
* 20        Include zero-point energy.        
### IOp(1/49)
Options to IRC path relaxation (IJKL).
* L        2/1 don’t/do optimize reactant structure. Default: 1.        
* K        2/1 don’t/do optimize product structure. Default: 1.        
* J        3/2/1 don’t/QST3/QST2 optimize TS structure (for QST input). Default: 1.        
* I        2/1 unimolecular/bimolecular reaction. Default: unimolecular.        
### IOp(1/52)
`L101 and L120`: Type of ONIOM calculation.
* 0/1        One layer, normal calculation.        
* 2        Two layers.        
* 3        Three layers.        
* 00        Default (20).        
* 10        Include electrostatics in model systems using MM charges (in case of three-layer ONIOM, this includes the charges in both the small model and the intermediate model system).        
* 20        No electrostatics included in the model systems.        
* 30        As 10, but exclude the MM charges in the calculations on the smallest model system in case of a three-layer calculation.        
* 40        As 10, but exclude the MM charges in the calculations on the intermediate model system in case of a three-layer calculation.        
* 100        Do full square for testing.        
* N000        Use atomic charge type N-1 during microiterations. The default is MK charges.        
* M0000        Type of link atoms for the MM calculation in QM/MM.        
		        0        Default (2).        
		        1        Conventional (Maseras) style.        
		        2        ONIOM style.        
*          
* L00000        Whether to read additional charges with electronic embedding.        
		        0        Default (1).        
		        1        No.        
		        2        Yes.        
*          
* K000000        Whether to create new entries in Common/Mol for the link atoms.        
		        0        No.        
		        1        Yes.        
*          
### IOp(1/53)
`L120`: Action of each invocation of L120.
* 0        Do nothing.        
* 1        Set up point MM on RWF from initial data.        
* 2        Set up point MM on RWF from initial data and restore point MM on checkpoint file if ONIOM data is present there.        
* 3        Restore point M from data on the RWF.        
* 4        Integrate energy.        
* 5        Integrate energy and gradient.        
* 6        Integrate energy, gradient, and Hessian.        
* 7        Restore point MM from RWF but do not create a new model system.        
* NN0        Save necessary information (some RWF’s, energy, gradients, Hessian) of point NN of the ONIOM grid. NN = MaxLev^2 + 1 (currently 17) to restore real system.        
* MM000        Next point to do is MM.        
		Calc Level        
		High        4—7—9        
		        |    |   |        
		Mid        2—5—8        
		        |    |   |        
		Low        1—3—6        
		         S  M  L system size        
*          
### IOp(1/54)
Whether to recover initial energy during IRCMax from checkpoint file.
* 0        No.        
* 1        Yes.        
### IOp(1/55)
`L103`: Options for GDIIS. ICos*1000+IChkC*100+IMix*10+Method form.
`L115`: IRC optimization.
* 0        Default, use gradients to find the next geometry.        
* 1        Use displacements to find the next geometry.        
### IOp(1/56)
Set of atom type names to parse.
* 0        Accept any.        
* 1        Dreiding/UFF.        
* 2        Amber.        
* 3        Amber allowing any symbol, for use with parameters in input stream.        
### IOp(1/57)
Whether to produce connectivity.
* 0        Default (4 if reading geometry from checkpoint file and connectivity is there, otherwise 3).        
* 1        No.        
* 2        Yes, read from input stream.        
* 3        Yes, generate connectivity.        
* 4        Yes, read from checkpoint file.        
* 5        Yes, read from RWF file.        
* 10        Read modifications.        
* 100        Connectivity input is in terms of z-matrix entries, including dummy atoms.        
### IOp(1/58)
`L115`: IRCMax control.
* 1        Do IRC rather than IRCMax.        
* 10        Store compound energy; default for IRCMax.        
* 20        Zero-point energies are available during IRCMax.        
### IOp(1/59)
`L103`: Update of coordinates.
* 0        Default (1).        
* 1        New versions (RedCar/RedQ2X); fall back to ORedCr/RedQX1 if RedCar fails.        
* 2        Old version (ORedCr/RedQX).        
* 3        Old version (ORedCr/RedQX1).        
* 4        New version (ORedCr/RedQ2X) but fall back to ORedCr/RedQX if RedCar fails.        
* MMMM0        IAprBG in Red2BG.        
* 10        Re-use eigenvectors of G only if exact.        
* 20        Re-use eigenvectors of G if they are linearly independent.        
* 30        Test old eigenvectors of G but don’t re-use them.        
* 40        Don’t look at old eigenvectors.        
* 50        Re-use eigenvectors of G if the RMS of the elements of the new G in the old null space is less than the threshold.        
* NN00        RMS < 10^-N, default 4.        
* M0000        Default (1).        
* 10000        Form G-inverse from the B eigen-values/vectors.        
* 20000        Form G-inverse directly from G.        
* 30000        Do G- via diagonalization of G (NYI).        
* 40000        Do G- via SVD on B, returning only the eigenvectors with nontrivial eigenvalues.        
### IOp(1/60)
Interpret extra integer and fp values in z-matrix as scan information.
* 0        Default (No).        
* 1        Yes.        
* 2        No.        
### IOp(1/61)
How ONIOM should leave the RWF at the end of each geometry.
* 0        Default (1).        
* 1        Normal: leave the RWF set up for the low-level calculation on the real system.        
* 2        MOMM: leave the RWF set up for the real system, but with NBasis and NBsUse for the high-level calculation on the model system. Useful for treating the full system as having electrons only on the QM atoms. This is really a hack for two layer QM:MM ONIOM ADMP and should probably be generalized to behave like an ONIOM-PCM-A case.        
* 3        Lowest level is MO, but normal setup at end.        
* 00        Default (10, but 20 if doing EE microiterations).        
* 10        Leave the charges file (605) from the best calculation that produced one.        
* 20        Leave 605 in its normal state (present if from real, low-level).        
### IOp(1/62)
Counterpoise control.
* NN        NN fragments.        
* 1NN        Force use of new ghost atoms (default).        
* 2NN        Force use of old ghost atoms.        
* 1xxx        Counterpoise (default).        
* 2xxx        Fragment guess.        
### IOp(1/63)
Step in counterpoise calculation.
* LMM        L: order of derivatives: 1 = Energy, 2 = Gradient,…        
*          MM: 0 = Supermolecule, 1-NFrag = Fragments with ghost atoms,        
*          NFrag+1-2*NFrag = lone fragments.        
### IOp(1/64)
Molecular mechanics force field selection.
* 0        None.        
* 1        Dreiding.        
* 2        UFF.        
* 3        AMBER.        
* 000        Use only hard-wired.        
* 100        Use soft and hard-wired, hard-wired has priority.        
* 200        Use soft and hard-wired, soft has priority.        
* 300        Use only soft. Lowest 2 digits then have no meaning.        
* 0000        Do not read modifications to parameter set.        
* 1000        Read modifications to parameter set.        
* 00000        With soft parameters, abort when different parameters match to the same degree.        
* 10000        Use the first when there are equivalent matches.        
* 20000        Use the last when there are equivalent matches.        
If IOp(67) = 3, then the default is to apply soft parameters with higher priority.
### IOp(1/65)
Control of which terms are included in MM, corresponding to the ‘classes’ in FncInf.
* 0        Do all (default).        
* 1        Non-bonded.        
* 10        Stretching.        
* 100        Bending.        
* 1000        Torsion.        
* 10000        Out-of-plane.        
* 100000        Stretch-bend.        
### IOp(1/66)
Whether to generate QEQ charges, over-write the values in AtChMM, or to use the values already there.
* 0        Default (2, 1 ⇒ 221).        
* 1        Do QEq here in GenChg.        
* 2        Don’t do QEq.        
* 3        Generate charges here using QEqN.        
* 00        Default (20).        
* 10        Do for atoms which were not explicitly typed.        
* 20        Do for all atoms regardless of typing.        
* 000        Default (200).        
* 100        Do for atoms which have charge specified or defaulted to 0.        
* 200        Do for all atoms regardless of initial charge.        
* `MMMMM000`        IType passed to QEq.        
### IOp(1/67)
Source of MM parameters.
* 0        Default: 2 if reading geometry from checkpoint file, else 1.        
* 1        Generate here, reading from input if requested by IOp(64).        
* 2        Copy from checkpoint file.        
* 3        Pick up non-standard parameters from checkpoint file.        
### IOp(1/70)
`L118`: Type of sampling (Nact).
* 0        Default (same as 3).        
* 1        Orthant sampling.        
* 2        Classical microcanonical normal mode sampling.        
* 3        Fixed normal mode energy.        
* 4        Local mode sampling (thermal sampling based on RTemp).        
* Currently 0, 2, 3 and 4 are working.        
* 10        Read in Hessian from checkpoint for initial sampling.        
`L124`: SCRF flag.
* IJKLLMM        See comments in overlay 3.        
* 00000000        Default (same as 2).        
* 10000000        Do the 1st iteration in gas-phase.        
* 20000000        Do the 1st iteration in solution.        
### IOp(1/71)
`L103`: How often to calculate analyic 2nd derivatives.
* 0        Default (every cycle if IOp(10)=4).        
* N        Every Nth geometry, starting with the initial one.        
`L115`: Whether to print out input files for each structure along an IRC.
* 0        No.        
* 1        Yes.        
`L118`: Hessian update.
* -1        Gradient only.        
* -2        Gradient+Hessian, but never calculate full H (only updates).        
* 0        Full Hessian at every step.        
* NN        Try to do NN updates between full Hessians.        
* 000        Default updating (same as 300).        
* 100        SR1 Hessian updating algorithm.        
* 200        PSB Hessian updating algorithm.        
* 300        Bofill’s Hessian updating algorithm.        
* 400        Sqrt(Bofill) Hessian updating algorithm.        
* 500        No update.        
* 0000        Default (same as 1000).        
* 1000        Reintegrated updated steps.        
* 2000        Suppress reintegration.        
`L123`: Hessian calculation.
* -1        Gradient only.        
* 0        Either only update or CalcAll as determined by IOp(10).        
* N        Recalculate analytic Hessian every N^th calculation.        
### IOp(1/72)
`L121`: Lagrangian constrain method for ADMP (ICType).
* Half*Gamma*Tr[(P*P-P)^2] + Lambda*[Tr(P)-Ne] + Eta*Tr(P*P-P)        
* 0        Default same as 7 if no mass-weighting (IOp(76) < 0). Same as 10 if mass-weighting (IOp(76) > 0).        
* 1        Use Lambda and Eta only. (Gamma=0).        
* 2        Use Lambda, Eta, Gamma. Gamma = .2.        
* 3        Use Lambda, Eta, Gamma. Gamma = 1. Constraints for scalar mass case.        
* 4        Use exact constraint Sum(ij)[Vij*(P^2-P)ij].        
* 5-7        Iterative Scheme same as 4. Different initial guesses. 7 is default for scalar mass case. Constraints for tensorial mass.        
* 8-11        Mass-weighting constraints. Documentation may be found in DVelV1. 10 is default.        
`L124`: Solvent type for external iteration PCM. (ISolv).
### IOp(1/73)
`L123`: Whether to compute projected frequencies: 0/1/2 Default (No)/No/Yes.
`L118` and `L121`: Initial Kinetic energy of the Nuclei (EStrtC).
* 0        Default (.1 Hartree).        
* N>0        N*micro-Hartree.        
* N<0        0.0 Hartree        
### IOp(1/74)
Charge scaling for charge embedding in ONIOM. IJKLMN 6th through 1st nearest neighbors of current layer scaled by I*0.2, J*0.2, etc. 0 Þ 5³ IAtTyp=6 (no scaling); all layers are scaled by at least as much as ones farther out. The default is 500.
* M        Factor for charges one bond away from link atom.        
* K00        Factor for charges three bonds away from link atom. IJ etc.        
*          The actual factors used for each value of IAtTyp are:        
		1: 0.0          2: 0.2        
		3: 0.4          4: 0.6        
		5: 0.8          6: 1.0        
*          
### IOp(1/75)
ADMP control flag (ICntrl).
* 0        Standard ADMP.        
* 1        Read converged density at every step.        
* 2        Fix the nuclear coordinates.        
* 3        Test time reversibility (MaxStp must be even).        
* 00        Default (20).        
* 10        Read stopping parameters from input.        
* 20        Do not read stopping parameters.        
### IOp(1/76)
Fictitious electron mass (EMass). Format of input: +/- XXXXZYYYY.
* YYYY        Default (1000)        
*          IOp(1/76) > 0  YYYY*.0001 amu. MW core functions more than valence functions.        
*          IOp(1/76) < 0  YYYY*.0001 amu. Use uniform scaling for all basis functions.        
*          (Note YYYY > 9999 makes no sense).        
* Z        Mass-weighting option. If IOp(76) < 0, Z is meaningless.        
* XXXX        If PBC: Mass of Box Coordinates (BoxMas) = XXXX*.0001 AMU BoxMas=0        
*          Box coordinates not propagated (default).        
### IOp(1/77)
Initial Kinetic energy of the density matrix (EStrtP) (For UHF, Alpha and Beta each get half this energy) and Option Number to compute initial kinetic energy. Format of Input: XXYYYY (six digits).
IWType = XX
N = YYYY
(For UHF, Alpha and Beta each get half this energy).
* 0        Default (0.0 Hartree).        
* N>0        N*micro-Hartree IWType is used to figure out how the initial velocity is computed (in gnvelp).
If XXYYYY < 0: Initial velocity = 0.0 Hartree (i.e., currently same as N=0 above).        
### IOp(1/78)
`L121`: Sparse.
* -N        Sparse here with cutoff 10^-N, full elsewhere.        
* 0        Use full matrices or sparse based on standard settings.        
* 1        Use sparse fixed form.        
### IOp(1/79)
`L115`:  IRCMax convergence.
`L118, L121`: Stopping Criteria.
* 0        Default, do not analyze pure rotation and vibration for polyatomic molecules.        
* 1        Do pure rotational and harmonic normal mode analysis for polyatomic molecule; EBK theory for diatomic vibrational analysis (require equilibrium information for each of the polyatomic molecules from saved checkpoint files and Morse parameters for diatomic molecule).        
* 2        Do pure rotational and harmonic normal mode analysis for polyatomic molecule; local harmonic vibrational analysis for diatomic molecule (require equilibrium information for each of the fragments from saved checkpoint files).        
* 3        Do pure rotational analysis and select the best normal mode analysis methods (harmonic and anharmonic) for polyatomic molecule; local harmonic vibrational analysis for diatomic molecule (require equilibrium information for each of the fragments from saved checkpoint files).        
* 00        Default, use default stopping criteria.        
* 10        Use user specified stopping criteria.        
### IOp(1/80)
`L106`: 0/1 Cartesian/Normal mode/ Internal coordinate differentiation. 2 is NYI.
`L118`: = 1 to suppress the 5th order correction after surface hop has been made in Trajectory Surface Hopping calculations. Needs also IOp(10/80 = 1)
`L121`: Nuclear Kinetic Energy Thermostat Option (currently only velocity scaling is implemented).
* 0        No Thermostat.        
* 11XXXXX        Velocity scaling, but only for the first XXXXX simulation steps. (This option is useful, if thermostating is only required during equilibration.)        
* 1000000        Velocity scaling, all the way through the simulation.        
### IOp(1/81)
Nuclear KE thermostat in ADMP — temperature is checked and scaled every IOp(81) steps.
### IOp(1/82)
`L121`: Temperature for nuclear KE thermostat.
### IOp(1/83)
Whether to read in frequencies for electric and magnetic perturbations.
* 0        Default (No).        
* 1        Yes unless geom=allcheck.        
* 2        No.        
* 3        Yes, even if geom=allcheck.        
* 00        Default (10).        
* 10        Ensure that the static case is done, by putting a zero frequency at the beginning.        
* 20        Do not put a zero frequency at the beginning.        
* 000        Default (100).        
* 100        Sort the frequencies into increasing order.        
* 200        Do not sort the frequencies (for debugging).        
### IOp(1/84)
Differentiation of frequency-dependent properties.
* 0        No.        
* N        Mask for which properties on file 721 will be differentiated.        
### IOp(1/85)
Band gap calculation in PBC ADMP.
* 0        Default (No).        
* 1        Diagonalize Fock matrix to get band gap, evolution, etc.        
* 2        No.        
### IOp(1/86)
Printing for NMR for ONIOM.
* 0        Default (1).        
* 1        Print tensors and eigenvalues.        
* 2        Print eigenvectors as well.        
### IOp(1/87)
ONIOM integration of density.
* 0        Do not integrate.        
* 1        Integrate current densities.        
* 2        Integrate densities specified by following digits:        
* K0        Density to use from gridpoint 1        
* L00        Density to use from gridpoint 2        
* M000 etc.                
* Values for K, L, M, etc.:        
*          0: SCF        
*          1: MP first order        
*          2: MP2        
*          3: MP3        
*          4: MP4        
*          5: CI one-particle        
*          6: CI        
*          7: QCI/CC        
*          8: Correct to second order        
### IOp(1/88)
Whether to read in atomic masses (isotopes).
* 0        Default (1 if geometry read from input, 4 if geometry read from checkpoint)        
* 1        Use most abundant isotopes.        
* 2        Read isotopes from input. The temperature and pressure are read first, for backwards compatibility.        
* 3        Read isotopes from RWF.        
* 4        Read isotopes from checkpoint.        
* 5        (Generated internally) Isotopes were read from chk file during Guess=Input.        
### IOp(1/89)
Maximum allowed deviation from average nuclear KE during ADMP, in Kelvin.
### IOp(1/90)
To read in the velocity in Cartesian coordinates.
### IOp(1/91)
Nuclear Kinetic Energy Thermostat Option. Average energy (in micro-Hartree) to be maintained during simulation, as required by IOp(80).
### IOp(1/92)
Thermostat Option. Maximum allowed deviation from average nuclear KE specified in IOp(81). Also in micro-Hartree.
### IOp(1/93)
QM/MM TS vector guess.
* 000        Default (112)        
* 1        Retrieve from checkpoint file if available, otherwise diagonalize QM Hessian or read from input.        
* 2        Do not try to retrieve from checkpoint file.        
* 10        Diagonalize QM contribution to Hessian.        
* 20        Read from input.        
* N00        How to deal with ‘suspicious RFO solutions’ (default is 1).        
*          1. Just take the step.        
*          2. Check if there is an eigenvector with wrong curvature. If there is, flip its eigenvalue.        
*          3. Check if there is an eigenvector with wrong curvature. If there is, take a small step into this direction, followed by a linear search. This should step out (or stay in) the wrong region, and fix the eigenvalue.        
### IOp(1/94)
Davidson control for quadratic micro-iterations.
* OP        Number of initial guess vectors (4).        
* MN00        Iteration to scale down number of vectors (5).        
* KL0000        Factor to scale down with; 1 for no scaling (2).        
* J000000        Whether to do geometry steps when the CG is done (2).        
		1        Make the CG steps.        
		2        No displacements.        
		3        Only do displacements at first guess.        
*          
* I0000000        Whether to re-use previous RFO solution or to regenerate guess (1).        
		1        After first step, use previous solution as guess.        
		2        Regenerate guess each time.        
		3        Use previous lowest root, and regenerate remainder.        
*          
* H00000000        Whether (1, default) or not (2) to add 0,…,0,1 guess vector.        
### IOp(1/95)
RFO/Davidson control for quadratic micro-iterations.
* MM        Convergence (7).        
* LLL00        <0: Regular Davidson.        
*         0: Only check convergence on first vector, and iterate the lowest root only. Use all the intermediate vectors.        
*         >0: Only check convergence on first vector, and iterate the new vectors LLL times with the explicit last row/column. This is specifically appropriate for RFO. The last row/column of the Hessian comes after the diagonal elements.        
### IOp(1/96)
Options for generating initial guess vectors for RFO/Davidson diagonalization in coupled QM/MM macro steps. Note that other RFO/Davidson diagonalization controls for coupled QM/MM macro steps are available in IOp(97). Format of input: GHIJKLLMM.
* MM        Number of initial guess vectors to get from CG steps. The default is 0.        
* LL        Number of initial guess vectors from the diagonal of the QM block (4). The default is 4.        
* K        Add 0,…,0,1 guess vector?        
* 0        Default: K = 1;         
* 1        Yes        
* 2        No        
* J        Add the gradient vector to the guesses?        
		0        Default: J = 1        
		1        Yes        
		2        No        
*          
* I        Pre-diagonalize a Hessian/RFO matrix without non-bonding contributions? Note that this control is only valid for IOp(98) > 3; otherwise, I is ignored.        
		0        Default: I = 1        
		1        Yes        
		2        No        
*          
* H        Scale factor for the size of the Davidson sub-space in early iterations.        
		0        Default: H = 4        
		1        Same as no scaling.        
		H        Use a sub-space in early iterations that is H times the number of requested vectors.        
*          
* G        Number of vectors to solve using Davidson diagonization.        
		0        Default: G = 1        
		G        Solve for G vectors.        
*          
### IOp(1/97)
RFO/Davidson control for coupled QM/MM macro step. Note that other RFO/Davidson diagonalization conrols for coupled QM/MM macro steps are available in IOp(96). Format of input: GHIJKLMM.
* MM        Convergence in Davidson iterations. Convergence is set to 10^-MM. The default value is MM=5.        
* L        What is being diagonalized? This option is set explicitly in subroutines before calling the Davidson diagonalization code. Therefore, the value set in this IOp is ignored and serves only as a place holder.        
* 0        the Hessian        
* 1        the augmented-Hessian/RFO matrix        
* K        Check convergence on which roots?        
* 0        Default: For L=0, K=2; For L=1, K=1        
* 1        Check convergence on lowest root only.        
* 2        Check convergence on all roots.        
* J        Appears to be unused.        
* I        Number of Davidson iterations to store.        
* 0        Default: Keep all iterations.        
* 1        Keep only the last iteration.        
* H        Number of new vectors to create in each Davidson iteration.        
* 0        Default: For L=0, H=1; For L=1, H=2.        
* 1        Iterate all roots/vectors.        
* 2        Iterate lowest root/vector only up to the maximum number of iterations that are default in the Davidson code (ignores J above) and keeping vectors from all iteratations (ignores I above).        
* 3        Iterate lowest root/vector only. Note that this option is essentially the same as H=2, though J and I option settings are honored.        
* G        Initial approximation to use for Davidson diagonization.        
* 0        Default: G=2.        
* 1        Use a diagonal Hessian approximation together with the gradient vector. This is best used in RFO applications        
* 2        Use the inverted Hessian for the QM block        
* 3        Use a diagonal Hessian approximation.        
### IOp(1/98)
Control of quadratic micro-iterations and coupled QM/MM quadratic macro step.
* <0        Do not use dynamic convergence criteria for the micro-iterations.        
* 0        Default (11).        
* 1        Regular non-coupled macro step.        
* 2        Coupled macro step, full diagonalization.        
* 3        Coupled macro step, direct /w full Hessian in core.        
* 4        Coupled macro step, direct /w MM Hessian in core.        
* 5        Coupled macro step, fully direct.        
* 6        Go through the QuadMac machinery, but use the fully integrated ONIOM Hessian to calculate the Hessian-vector products. Switch to regular micro-iterations at points without analytic second derivatives.        
* 7        Fully quadratic at 2nd derivative points (1st in CalcFC, all in CalcAll), QuadMac with integrated Hessian at non-2nd derivative points.        
* 10        Regular micro-iterations.        
* 20        Quadratic micro-iterations, full diagonalization.        
* 30        Quadratic micro-iterations, direct with prepared Hessian in core.        
* 40        Quadratic micro-iterations, direct with raw MM Hessian in core.        
* 50        Quadratic micro-iterations, fully direct.        
* 60        No micro-iterations.        
### IOp(1/99)
Accuracy used for the non-bonded interactions in the Hessian-vector product calculations in the fully direct algorithms. Setting this IOp does not affect the MM energy and gradient calculations; only the direct evaluation in the QuadMac optimization step. When IOp(99) < 0, the full accuracy is used.
* MM        Maximum multipole level (8)        
* LLL00        Box size in FMM (12)        
* KKK00000        Cutoff in van der Waals (30)        
### IOp(1/101-104)
`L115, L118`: Phase control in N1, N2, N3, N4.
### IOp(1/105)
Reaction direction.
* 00        Default (Same as 10).        
* 10        Forward direction.        
* 20        Reverse direction        
* 0        Default (Same as 2).        
* 1        Use DVV.        
* 2        Do not use DVV.        
* 00        Default (Same as 10).        
* 10        Follow the rxn path in the forward direction        
* 20        Follow the rxn path in the reverse direction.        
* 000        Default (Same as 200).        
* 100        Time step correction not used.        
* 200        Time step correction used but not to recalculate current DVV step.        
* 300        Time step correction used and current DVV step recalculated.        
* 0000        Default (Same as 1000).        
* 1000        Use DVV stopping criteria.        
* 2000        Do NOT use DVV stopping criteria        
### IOp(1/106)
Damping constant for DVV Dynamic Reaction Path following (v0).
* 0        Default v0 = 0.04 (N=400).        
* N        v0 is set to N*0.0001.        
### IOp(1/107)
Error tolerance for DVV time step correction (Error).
* 0        Default Error = 0.003 (N=30).        
* N        Error = N*0.0001.        
### IOp(1/108)
Gradient magnitude for DVV stopping criteria (Crit1).
* 0        Default (N = 15).        
* <0        Turn off this test.        
* N        N*0.0001        
### IOp(1/109)
Force-velocity angle for DVV stopping criteria (Crit2).
* 0        Default (90 Degrees).        
* <0        Turn off this test.        
* N        Use N Degrees.        
### IOp(1/110)
Scaling of rigid fragment steps during microiterations.
* 0        Do not scale.        
* 1        Scale with 1/NRA (NRA = number of atoms in fragment).        
* 2        Scale with 1/Sqrt(NRA).        
* -n        Scale with 1/n.        
### IOp(1/111)
`L103`: Step-size to use with steepest descent when L103 is having trouble.
* -N        Scale up to RMS step of N/1000 if DXRMS is less.        
* -1        Effectively disables the scaling.        
* 0        Default (50).        
* N        Scale up or down to maximum change in a variable of N/1000.        
### IOp(1/112)
`L101`: Temperature for thermochemistry.
* 0        Default (standard temperature, unless read in).        
* N        N/1000 degrees.        
* 1        Default.        
* -N<1        N/1000000 degrees.        
* -N        N/1000000 degrees.        
### IOp(1/113)
Pressure for thermochemistry.
* 0        Default (1 atmosphere, unless read in).        
* N        N/1000 atmospheres.        
* -1        Default.        
* -N<1        N/1000000 atmospheres.        
### IOp(1/114)
Scale factor for harmonic frequencies for use in thermochemistry and harmonic vibration-rotation analysis.
* 0        Default (1 unless specified by IOp in overlay 7 or read in).        
* -1        Force to 0 (default).        
* N        N/1000000.        
### IOp(1/115)
Compression for MOMM quadratic steps.
* 4        Second derivatives generated over active atoms, with real system terms done iteratively during micro-iterations.        
* N¹4        Full second derivative matrices are used.        
### IOp(1/116)
Options for ONIOM Conical intersections: which calculations have adiabatic couplings done.
* 0        Default (111 all component calculations).        
### IOp(1/118)
Dump structures for each ONIOM system formatted as input.
* 0        Default (No).        
* 1        Yes.        
### IOp(1/119)
Control Initial Lanczos Vector (ILzVec).
* -1        Read guess by card in input file.        
* -2        Use the largest elements of H as a guess.        
* -3        Use the five largest contributions of H as a guess.        
* 0x        For Opt, IRC, dynamics read guess from previous cycle.        
* 1x        For Opt, IRC, dynamics generate a fresh guess for each cycle        
### IOp(1/120)
Flags for QM:QM embedding. NOTE: The standard embedding flags must also be set in the same way as necessary for QM:MM embedding calculations.
* 0        Default – Same as 1.        
* 1        Use Mulliken charges.        
* -1        Use the nuclear charge stored in array AtmChg.        
* -2        Set the charges to zero.        
* 00        Default (Same as 20).        
* 10        Just use the charges that already reside in AtChMM.        
* 20        Update AtChMM using current atomic charges on the RWF.        
This option is only employed immediately following low-level real-system sub-calculations.
### IOp(1/121)
`L106`: Extra items to differentiate.
* 0        Default, none.        
* 1        Differentiate AO density and Fock matrices.        
* 2        NYI.        
### IOp(1/122)
Read secondary structure information.
* 0        Default (4 or 3 if reading geometry from checkpoint or RWF file, otherwise 2).        
* 1        No.        
* 2        Yes, read from input stream if any residue information was provided on the atom definition lines.        
* 3        Yes, read from RWF.        
* 4        Yes, read from checkpoint.        
### IOp(1/123)
Version of /Mol/ to save on disk.
* 0        Default (current, version 2).        
* 1        Version 1 (flag -12345).        
* 2        Version 2 (flag -12346).        
* N<0        Flag value N.        
### IOp(1/124)
Flavor of ONIOM-PCM to use.
* 1        “A,” reaction field from the ONIOM integrated density;        
* 2        “B,” reaction field from the real system low level;        
* 3        “C,” reaction field in the real system low level only;        
* 4        “X,” reaction field in all subcalculations using the real system cavity.        
* 0x        Default (same as 1 unless a semiempirical method is involved);        
* 1x        Integrate the density for ONIOM-PCM-A;        
* 2x        Integrate the potential for ONIOM-PCM-A;        
* 1xx        Flag to indicate ONIOM-PCM-X as first iteration of ONIOM-PCM-A.        
### IOp(1/125)
Solvent charge distribution to add to Hamiltonian.
* 0        None.        
* 1        Read charges and DBFs from input stream in input orientation.        
* 2        Read from RWF.        
* 3        Read from checkpoint file.        
* 4        Same as 1.        
* 5        Read charges and DBFs from input stream in standard orientation.        
* 10        Force units of Angstroms for coordinates.        
* 20        Force units of Bohr for coordinates.        
### IOp(1/126)
Whether to read an input section with atom opt/freeze information.
* 0        Default (2).        
* 1        Yes.        
* 2        No.        
### IOp(1/127)
Use of MM coordinates and forces in GEDIIS:
* 0        Default (-3 for ME, -3 for EE).        
* -3        Don’t pass MM info.        
* -2        Zero MM forces and MM part of step, equivalent to not passing MM info.        
* -1        Zero MM forces but interpolate step in MM coords.        
* N        Use MM forces scaled by 1/N.        
### IOp(1/128)
Initial micro-iterations in L120 before first QM step, and micro-iterations in L120 during numerical differentiation in L103.
* 0        Default (No).        
* 1        Yes.        
* 2        No.        
### IOp(1/129)
`L123`: Whether or not the final statistics printed in the job summary should include coordinate values at each IRC step.
* 0        Default (none).        
* 1        Read user-defined stats from the input file.        
* 0x        Default (do not report all Cartesian coordinates).        
* 1x        Report all Cartesian coordinates.        
* 0xx        Unused.        
* 0xxx        Default (do not report bond coordinates).        
* 1xxx        If redundant internals are on the RWF, then report values for bond coordinates along the IRC.        
* 0xxxx        Default (do not report angle coordinates).        
* 1xxxx        If redundant internals are on the RWF, then report values for angle coordinates along the IRC.        
* 0xxxxx        Default (do not report dihedral coordinates).        
* 1xxxxx        If redundant internals are on the RWF, then report values for dihedral coordinates along the IRC.        
### IOp(1/130)
Eigenvector number to be followed during coordinate driving jobs (IOp(1/19 = 10)).
* 0        Default (1).        
* N        Follow input structure Hessian eigenvector number N.        
### IOp(1/131)
Options for corrector integration in predictor-corrector IRC calulcations (Link 123).
* 00        Should the corrector integration scheme be run in an (macro-cycle) iterative fashion? Default = 2.        
* -01        After each corrector integration, evaluate the actual energy and derivatives, but do not actually use
these. The final IRC will be the same as 1.        
* 01        Never check convergence of the corrector integration. Always do one corrector integration for each predictor integration.        
* 02        Always check for convergence of the corrector integration end point. Convergence is acheived when the change in corrector integration end point geometry is less than the convergence criteria indicated by IOp(7).        
* 03        Same as 2, but never accept convergence after the first corrector integration at a point.        
* 10        This flag iteratively refines the DWI fitted surface if multiple corrector integration macro-cycles are taken by adding the largest standard deviation point from the previous BS cycle.        
* -11        This flag forces a PES evaluation step after each corrector integration. This is similar option -1, except that the actual energy and derivatives are used for the next predictor step rather than the values on the DWI fitted surface at the corrector end-point.        
* 0xx        Should DWI surfaces employ numerical thrid-order terms in Taylor series? Default = 1.        
*         
* 1xx        Use DWI surface with Taylor series expansions truncated at second-order.        
* 2xx        Use DWI surface with Taylor series expansions truncated at third-order using numerical third-derivatives.        
* Nxxx        What power should be used for DWI weights that include delta-x raised to an even power. The value of this option setsthat power to 2*N. Default = N = 1.        
* 0xxxx        How should the first step off of the transition structure point be handled in corrector integration cycles? Note, in all cases, the transition vector is used to define the tangent at the transition structure. Default = 2.        
* 1xxxx        Run the requested number of Euler steps in the standard way. Only the first Euler step taken uses the transition vector.        
* 2xxxx        Take a large step off of the transition structure point along the transition vector. This step is taken to be half of the total requested step size given by TotStp.        
* 3xxxx        This the same as option 2 in concept. The only difference is that the first step off of the transition structure is taken as one-third the total requested step size given by TotStp.        
* 4xxxx        This the same as option 2 in concept. The only difference is that the first step off of the transition structure is taken as one-fourth the total requested step size given by TotStp.        
* 0xxxxx        Should update vectors be used in DWI fits if possible? Default = 1.        
* 1xxxxx        Yes, when possible.        
* 2xxxxx        Never.        
### IOp(1/132)
Whether to check for divalent link atoms in ONIOM input:
* 0        Default (yes).        
* 1        Yes.        
* 2        No.        
### IOp(1/133)
Suppress integration/restore of quantities for Polar=Raman and Polar=ROA ONIOM jobs:
* 0        Default (1).        
* 1        Do not restore or integrate forces, force constants, static electric or magnetic field derivatives.        
* 2        Restore all files.        
### IOp(1/135)
MM non-bonded switching function.
### IOp(1/136)
MM van der Waals outer cutoff in Angstroms.
### IOp(1/137)
MM Coulomb outer cutoff in Angstroms.
### IOp(1/138)
MM soft cutoff range (applied to both vdW and Coulomb, in Angstroms.
### IOp(1/139)
Number of MM microiterations allowed.
* 0        Default, based on NAtoms but at least 5000.        
* N        N        
### IOp(1/140)
Whether to restore the real system from chk file:
* 0        Default (yes if ONIOM).        
* 1        Yes.        
* 2        No.        
### IOp(1/141)
Control of error choice during GEDIIS:
* 0        Default (1).        
* 1        Use RFO steps as error vectors, using the NR step at a point if the RFO fails or gives a Hessian eigenvector.        
* 2        If RFO fails for any point, use the gradient for all points.        
* 3        Always use the gradients as the errors.        
* 4        Use RFO steps as error vectors unless any RFO fails and unless Hessian is marked as untrustworthy; then use gradients instead.        
* 5        Drop back to RFO (no DIIS) if Hessian is untrustworthy. NR steps are used if RFO fails during DIIS.        
### IOp(1/142)
Whether to copy MM charges to link atoms:
* 0        Default (3 if QEq is done; otherwise 1).        
* 1        Copy if link atom charge is zero.        
* 2        Do not copy.        
* 3        Always copy.        
### IOp(1/143)
Hessian during IRC restarts.
* 0        No change in when Hessian is done.        
* 1        Do Hessian at first new point in each direction.        
### IOp(1/144)
Whether to analyze residue geometry.
* 0        Default (Yes, if secondary structure present and N Atoms ≤ 10000).        
* 1        Yes.        
* 2        No.        
### IOp(1/145)
Controls for the new internal coordinate data structure.
* 0        Should the new internal coordinate data structure be set-up for use? (Default = 1).        
* 1        No.        
* 2        Yes. The coordinates are either generated by default (e.g., Option 9×2) or obtained from the user-provided input (e.g., Option 6×2). Alternatively, they can be taken from a chk file if they exist there and if geom=check without any GIC keyword (i.e., IOp(1/145=0) is used.        
* 3        Yes, but do two calls to CrdDef when building the coordinate definitions. The first call adds the coordinates in the same way that Option 2 does. The second call adds coordinates from a list of user-provided input coordinates in the same way as Option 6×2 does. In other words, there will be two sets of coordinates to be merged. The first set is generated by default (e.g., in the case of Option 9×3 without geom=check) or it comes from a chk file (Option 9×3 with geom=check). The second set is provided by the user as a separate input section, and it contains some additional coordinates or modifications to the first set. A blank line can be used instead of the second set’s input section. It is also possible to make the user-provided input’s reading to be the first step and the construction of complementary coordinates by CrdCon to be the second step. The latter is Option 6×3.        
* 0x        Which coordinate derivative terms should be included in the data structure? (Default = 3).        
* 1x        Include only values in the definitions list.        
* 6xx        Read the coordinate definitions from the input file using the symbolic form, (See Routine CrInp1), and then automatically differentiate the active coordinate derivatives as needed.        
* 7xx        Define (the full set of) distance matrix coordinates. This option can be combined with 2xxx to use inverse distance matrix coordinates.        
* 8xx         Read the coordinate definitions from the input file using the OLD symbolic form (See Routine CrDfSy), and then automatically differentiate the active coordinate derivatives as needed.        
* 9xx        Use the new coordinate generation code to create an intermediate RP structure based on the molecular connectivity (See Routine CrdCon), then have CrdDef build the data structure using the intermediate RP data from CrdCon and build derivatives wrt Cartesian coordinates.        
* 0xxx        When building the internal coordinate definitions, should any systematic modifications be done? (Default = 1).        
* 1xxx        No. Simply define the coordinates to be the same as they would have been using the old coordinate code. 2xxx … Invert all bond stretch coordinates.        
* 2xxx        Invert all bond stretch coordinates.        
* 0000000        Default for default is 1 (GIC).        
* 1000000        Default to 1 if not specified.        
* 2000000        Default to 2 if not specified.        
### IOp(1/146)
Control of SCVS:
* 0        Default (03045011).        
* 1        Include forces in virial ratio.        
* 2        Do not include forces in virial ratio.        
* 1x        Use Murdoch’s extrapolation.        
* 2x        Do not use Murdoch’s extrapolation.        
* Nxx        Apply SCVS when max force on nuclei is below 10^-N.        
* Mxxx        The convergence on the virial Eta. Default is 5.        
* Lxxxx        The convergence threshhold on |E| * (2*Eta – 2), where |E| is the magnitude of the kinetic energy is 10^-M. Default is 3.        
* Kxxxxx         The initial order of extrapolation is 10^L        
* JJJxxxxxx          Maximum of KKK SCVS iterations.        
### IOp(1/148)
`L106`: Storage of derivatives.
* 0        Default (221).        
* 1        Normal storage of numerical first derivatives.        
* 2        Store numerical first and diagonal second derivatives.        
* 10        Print differences between numerical and analytic quantities.        
* 20        Do not print differences.        
* N00        Threshold for printing differences is -6-N.        
### IOp(1/150)
`L112`: Initial scale factor. 
* 0        Default (1.0)        
* N        1 + N/100000000        
### IOp(1/151)
How many vectors with negative curvature to use in downhill step during minimization:
* 0        Default (3)        
* -1        None, do regular RFO step.        
* N        Up to N vectors.        
### IOp(1/152)
`L103`: Control of MaxStp (allocated max number of steps in L103).
* 0        Default: compute based on number of variables, NStep, etc.        
* N>0        Make MaxStp at least N.        
* N<0        Make MaxStp at least -N.        
### IOp(1/153)
`L103`: Whether to fill OT file.
* 0        Default: do so for Cartesian and redundant internal coordinate optimizations.        
* 1        Yes        
* 2        No        
### IOp(1/154)
Linear angle test during internal coordinate generation.
* 0        Default (15 degrees, applied to all 3 tests).        
* -N        Threshold N degrees, applied to the angle only.        
* N        Threshold N degrees, applied to all 3 tests.        
### IOp(1/155)
Number of steps to take in guessing a TS during QST2:
* 0        Default (10).        
* N        Divide the overall step into N increments.        
### IOp(1/156)
Automatic generation of internal coordinates.
* 0        Default (1).        
* 1        Generate bonds, angles, and dihedrals.        
* 2        Generate bonds and angles but no dihedrals.        
* 3        Generate bonds only.        
* 4        Generate no coordinates automatically.        
### IOp(1/157)
Maximum step when going down an eigenvector:
* 0        Default (0.6)        
* N        N/1000        
### IOp(1/158)
`L124`: PCM defaults; `L301`: Details.
### IOp(1/159)
Default maximum step in Cartesians during redundant coordinate optimizations.
* -1        Unlimited (10^6 Bohr).        
* 0        Default (3 Bohr).        
* N        N/10 Bohr.        
### IOp(1/160)
Type of fragment calculation:
* 0        Default (11).        
* 1        Force use of new ghost atoms in counterpoise.        
* 2        Force use of old ghost atoms in counterpoise.        
* 10        Counterpoise.        
* 20        Fragment guess.        
* 80        Excitation energy transfer.        
* 0xxx        Default (same as 1).        
* 1xxx        Use full-system PCM cavity for fragments.        
* 2xxx        Use fragment PCM cavity for fragments.        
### IOp(1/161)
`L123`: Hack to save results at each IRC point.
* 0        Default (No).        
* 1        Yes.        
### IOp(1/162)
Frequency of analytic Hessians during IRC corrector cycles.
### IOp(1/163)
Copy of external input section from chk file:
* 0        Default; copy if Geom=AllCheck.        
* 1        Copy regardless.        
* 2        Do not copy.        
### IOp(1/164)
Read of atomic pair potential.
* 0        Default; copy from chk if Geom=AllCheck.        
* 1        Read from input.        
* 2        Do not read.        
* 3        Read from chk.        
### IOp(1/165)
Convergence of MM microiterations.
* 0        Default (10x tighter than macro, except  10x for FOSimult with MM included).        
* N
        Nx tighter.        
### IOp(1/166)
`L103`: Maximum number of vectors in DIIS. Format of input: MMNN.
* 0        Default.        
* NN        Save N vectors (default 10 for GEDIIS, 10 for SimOpt).        
* MMNN        Mix up to MM < NN vectors in DIIS when mixing RFO steps. (Default NN).        
A negative value requests uses of the Hessian eigenvector basis for the step. This is the default and only choice for GEDIIS TS optimizations.
### IOp(1/167)
Version of GEDIIS.
* 0        Default (2).        
* 1        Old.        
* 2        New.        
### IOp(1/168)
GEDIIS switches.
* NN        Switch from RFO to DIIS on RMS force (10^-NN, default 1.d-3).        
* MM00        Switch toEn-DIIS from RFO-DIIS on RMS step (10^-MM, default 2.5d-3).        
* LLL0000        Maximum coefficient allowed in RFO-DIIS before space is reduced (LLL/10, default 10.0).        
* `KKK0000000`        Maximum coefficient allowed in RFO-DIIS before coefficients are adjusted (KKK/10; default 3.0). The minimum value is -KKK/10 + 1.        
### IOp(1/170)
Control for selecting the initial conditions.
* 1        Initial Cartesian coordinates and velocities are read-in from the input file. This data is read in a free-format fashion.        
* 2        Initial Cartesian coordinates and mass-weighted velocities are read-in from the input file. This data is read in a free-format fashion.        
* 3        Initial coordinates are given by the user-input geometry; initial velocities are determined by selecting a random velocity which gives an kinetic energy equal to the value set in IOp(73).        
### IOp(1/172)
`L101`: Whether to print internal coordinates in L101.
* 0        Default (No).        
* 1        Print if present.        
### IOp(1/173)
`L106`: Extra files to differentiate.
* -11        Differentiate the files related to ground-state post-SCF 2nd derivatives (Lagrangian, P, and W).        
* -10        Differentiate the files related to CIS/TD second derivatives (Lagrangian, P, W, and T).        
* -2        Read two lists, each terminated by a blank line, the first the files to differentiate and the second the files where the numerical derivatives will be stored (0 for items which will not be saved).        
* -1        Read a list from an input section, terminated by a blank link. The numerical derivatives will be printed but not stored on disk.        
* N>0        Do file number N, storing derivatives in file 795.        
### IOp(1/174)
Reading parameters for classical electrostatics and dispersion.
* 0        Default, 3 if Geom=AllCheck else 2.        
* 1        Read selected parameters for elements from input.        
* 2        Use default parameters.        
* 3        Read user-specified parameters from chk file if present.        
* 4        Read both user-specified and default parameters from chk file if present.        
### IOp(1/175)
Electronic embedding type:
* 0        Default (1)        
* 1        ONIOM style.        
* 2        QM/MM style.        
### IOp(1/176)
Box size used for generating connectivity.
* 0        Default (8 Bohr).        
* N        N Bohr.        
### IOp(1/179)
Use of subprocesses for energy+derivatives, for debugging:
* 0        Default (1002).        
* 1        Yes.        
* 2        No.        
* 3        Yes, using loop over steps in L106.        
* 4        Yes, using loop over calls to utility in L106.        
* 5        Yes, using Linda.        
* 1x        Debug output and save of subprocess files.        
* 1xx        Full copy of rwf back and forth.        
* 1xxx        Iterate purturbations forward.        
* 2xxx        Iterate purturbations backward.        
### IOp(1/180)
Stopping during subprocess execution, for debugging.
* 0        Don’t stop.        
* N        Stop after running N subprocesses.        
### IOp(1/181)
Maximum number of middle iterations during ONIOM-EE:
* 0        Default (40).        
* N        N.        
## Overlay 2 
### IOp(2/9)
Printing of distance and angle matrices.
* 0        Default: print if ≤50 atoms.        
* 1        Do not print the distance matrix.        
* 2        Print distance matrix.        
* 00        Default: do not print.        
* 10        Do not print the angle matrix.        
* 20        Print the angle matrix, using z-matrix connectivity if possible.        
* 30        Use cutoffs instead of the z-matrix for determining which angles to print.        
* 000        Default: same as 100.        
* 100        Do not print dihedral angles.        
* 200        Print dihedral angles, using the z-matrix for connectivity info.        
* 300        Print dihedral angles, using a distance cutoff for connectivity info.        
* 0000        Default: print only for small cases.        
* 1000        Do not print the Cartesian coordinates in the input orientation.        
* 2000        Do print the Cartesian coordinates in the input orientation.        
### IOp(2/10)
Tetrahedral angle fixing
* 0        Default (don’t test).        
* 1        Angles within 0.001 degree of 109.471 will be set to ACOS(-1/3).        
* 2        Do not test for such angles.        
### IOp(2/11)
Printing of z-matrix and resultant coordinates.
* 0        Default (print if 50 atoms or less).        
* 1         Print.        
* 2        Don’t print.        
### IOp(2/12)
Crowding abort control.
* 0        Default (same as 1).        
* 1        Abort the run for zero atomic distances only.        
* 2        Abort the run if any atoms are within 0.5 Å.        
* 3        Do not abort the run regardless of 0 distances.        
### IOp(2/13)
Punch coordinates.
* 0        No.        
* 1        Yes, in ‘atoms’ format (3E20.12). Note: atoms will not take the atomic numbers, so they are not punched.        
* 2        Yes, in format suitable for coord. input to Gaussian. The atomic numbers and coordinates are punched in (I2,3E20.12).        
### IOp(2/14)
Internal coordinate linear independence.
* 0        Default (same as 2).        
* 1        Perform the test, but do not abort the job.        
* 2        Do not perform the test.        
* 3        If internal cords. are in use, test the variables for linear indep, and abort the job if they’re dep.        
* 10        Compute nuclear forces as well as second derivatives for the test.  This is not correct for the linear independence check, but is useful for debugging the derivative transformation routines.        
* 100        Abort the job if the number of z-matrix variables is not exactly the number of degrees of freedom (i.e., this is not a full optimization).        
### IOp(2/15)
Symmetry control.
* -1        Turns on symmetry; same as 0 for molecules but turns on assignment of space group operations for PBC.        
* 0        Leave symmetry in whatever state it is presently in.        
* 1        Unconditionally turn symmetry off. Note that symmetry is still called, and will determine the framework group. However, the molecule is not oriented.        
* 2        Bring the molecule to a symmetry orientation, but then disable further use of symmetry.        
* 3        Don’t even call Symm.        
* 4        Call Symm once with loose cutoffs, symmetrize the resulting coordinates then confirm symmetry with tight cutoffs.        
* 5        Recover the previous symmetry operations from the RWF, and confirm that the new structure has the same symmetry.        
* 6        Same as 5, but get symmetry info from the checkpoint.        
* 00        Default (10).        
* 10        Do re-orientation for PBC.        
* 20        Suppress re-orientation for PBC.        
* 100        Turn on symmetry operations for PBC.        
### IOp(2/16)
Action taken if the point group changes during an optimization.
* 0        Default (3).        
* 1        Keep going.        
* 2        Keep going, and leave symmetry on, using the old symmetry.        
* 3        Keep going, and leave symmetry on, using the new symmetry.        
* 4        Abort the job.        
### IOp(2/17)
Tolerance for distance comparisons in symmetry determination.
* 0        Default (determined in the symmetry package, currently 1.d-8).        
* N>0        10^-N.        
* N<0        10^N, use same tolerance for orientation.        
### IOp(2/18)
Tolerance for non-distance comparisons in symmetry determination.
* 0        Default (determined in the symmetry package, currently 1.d-7).        
* N>0        10^-N.        
* N<0        10^N, use same tolerance for orientation.        
### IOp(2/19)
Largest allowed point group, as Hollerith string.
### IOp(2/20)
Number (1-3 for X-Z) of axis to help specify which subgroup of the type specified in IOp(2/19) to use.
### IOp(2/21)
Atomic values to use in symmetry assignment/orientation.
* 0        Default (221).        
* 1        Atomic numbers.        
* 2        Atomic masses.        
* 10        Print symmetry coordinates to high precision.        
* 20        Do not print symmetry coordinates to high precision.        
* 100        Save standard orientation as input orientation.        
* 200        Do not save standard orientation as input orientation.        
### IOp(2/29)
Update of coordinates from current z-matrix.
* 0        Default (1).        
* 1        No.        
* 2        Yes, but remove z-matrix.        
* 3        Yes.        
### IOp(2/30)
Read in vector of atom types (for debugging).
* 0        No        
* 1        Yes, format (50I2)        
### IOp(2/40)
Save (initial) structure and possible constraints in RWF 698.
* 0        Default (No).        
* 1        Yes.        
* 2        Pick up structure from RWF 698 on the checkpoint file.        
* 3        Read in structure from input stream.        
### IOp(2/41)
Force constants for harmonic constraints.
* -2        Read in force constants for each Cartesian coordinate.        
* -1        No constraints.        
* 0        Default (no constraint unless reading constraint from checkpoint file).        
* N        N/10^6 Hartree/Bohr^2.        
### IOp(2/42)
Count nearest neighbor interactions.
* 0        No.        
* N        Count atoms within N/100 Å as neighbors.        
### IOp(2/43)
Print standard orientation to high precision.
* 0        No.        
* 1        Yes.        
### IOp(2/44)
Control for symmetry package.
* 00        Default (12, unless COM was specified, in which case 21).        
* 1        Initially.        
* 2        Do not rotate to principal axes.        
* 10        Rotate to old axes for C1, Cs, and Ci.        
* 20        Use principal axes for C1, Cs, and Ci.        
## Overlay 3 
### IOp(3/5)
Type of basis set. The same numbers are used for all basis sets, whether intended for use in expanding AOs (IOp(5)) or in expanding the density (IOp(82)).
* -1        Same as 0.        
* 0        Minimal STO-2G to STO-6G        
* 1        Extended 4-31G,5-31G,6-31G        
* 2        Minimal STO-NG (valence functions only)        
* 3        Extended LP-N1G (valence basis for coreless Hartree-Fock pseudo-potentials)        
* 4        Extended 6-311G (UMP2 frozen core optimized) basis for first row, MacLean-Chandler (12s,9p)–>(631111,52111) for second row. Use IOp(8) to select 5D/6D.        
* 5        Split valence N-21G (or NN-21G) basis for first or second row atoms. (Various implementations may omit second row atoms.) See IOp(6) for determination of the number of Gaussians in the inner shell.        
* 6        LANL ECP basis sets. IOp(3/6) selects options.        
* 7        General; see routine GenBas for input instructions.        
* 8        Dunning/Caltech basis sets. Type selected by IOp(3/6).        
* 9        Stevens/Basch/Krauss/Jasien/Cundari ECP basis sets for H-Lu. Type selected by IOp(3/6) for H-Ar. Literature citations in CEPPot.        
* 10        CBS basis #1 –6-31+g(d,p) on H, He, 6-311+G(2df) on Li – Ne, 6-311+g(3d2f) on Na – Ar.        
* 11        CBS basis #2 –6-31G, use daggers if any polarization.        
* 12        CBS basis #3 – 6-311++G(2df,2p) on H – Ne, 6-311++g(3d2f) on Na – Ar        
* 13        CBS basis #4 –6-31+G(d,p) on H – Si, 6-31+G(df,p) on P, S, Cl        
* 14        CBS basis #5 –Large APNO basis set.        
* 15        CBS basis #6 –Core correlation basis set.        
* 16        Dunning cc basis sets, type selected by IOp(3/6) (=0-4 for V{D,T,Q,5,6}Z) and augmented if IOp(7)=10. IOp(6)=5 for MTsmall basis set.        
* 17        Stuttgart/Dresden ECP basis sets. IOp(3/6) specifies type. Literature citations in SDDPot.        
* 18        Ahlrichs SV basis sets.        
* 19        Ahlrichs TZV basis sets.        
* 20        MIDI! basis sets.        
* 21        EPR-II basis sets.        
* 22        EPR-III basis sets.        
* 23        UGBS basis set.        
* 24        G3large basis set.        
* 25        G3MP2large basis set.        
* 26        Coreless: Li,Be 2SDF, B-Ne 2MWB, rest LANL1MB.        
* 27        DGauss basis sets, selected by IOp(3/6).        
* 28        Auto-generated, useful only for density basis sets.        
* 29        Spherical atomic densities:  a single highly contracted s-Gaussian for each atom. Only useful for fitting sets.        
* 30        One s-Gaussian per atom; dummy basis used for MM.        
* 31        G3largeXP basis set.        
* 32        G3MP2largeXP basis set.        
* 33        G3 basis 1 – "6-31G(d)" basis set.        
* 34        G3 basis 2 – "6-31+G(d)" basis set.        
* 35        G3 basis 3 – "6-31G(2df,d)" basis set.        
* 36        G4 QZ HF basis.        
* 37        G4 5Z HF basis.        
* 38        G4MP2 TZ HF basis.        
* 39        G4MP2 QZ HF basis.        
* 40        Weigand Coulomb fitting set.        
* 41        Ahlrichs SVP Coulomb fitting basis.        
* 42        Ahlrichs TZVP Coulomb fitting basis.        
* 43        Ahlrichs/Weigand def2-SV basis.        
* 44        Ahlrichs/Weigand def2-TZV basis.        
* 45        Ahlrichs/Weigand QZV basis.        
* 46        Fitting set matched to AO basis, or error if there is none. Converted here to matched value.        
* 47        Fitting set matched to AO basis, or /Auto if there is none.        
### IOp(3/6)
Number of Gaussian functions.
* N        STO-NG,N-31G,LP-N1G,STO-NG-VALENCE, N-21G.        
Note if IOp(3/5)=3 and IOp(3/6)=8: LP-31G for Li,Be,B,Na,Mg,Al; LP-41G for other row 1 and 2 atoms.
Default options IOp(6)=0
* If IOp(3/5)=0 N=3   STO-3G        
* If IOp(3/5)=1 N=4   4-31G        
* If IOp(3/5)=2 N=3   STO-3G (valence)        
* If IOp(3/5)=3 N=3        
* If IOp(3/5)=5 N=3        
When IOp(5)=7 (general basis), this option is used to control where the basis is taken from.
* 0        Read general basis from the input stream.        
* 1        Read the general basis from the RW-files and merge with the coordinates in blank common to produce the current basis.        
* 2        Read the general basis from the checkpoint file.        
* 3        Same as 1, for density basis (generated here from 1).        
* 4        Same as 2, for density basis (generated here from 2).        
* 1x        Read from the alternate file and remove functions/ECPs for inactive atoms. Used for counterpoise calculations, where one wants to modify the basis differently during different steps.        
* 2x        Read from the other alternate file, saved before the basis is massaged, uncontracted, etc. This option is useful when doing general basis geometry optimizations or properties using a wavefunction on the checkpoint file. If non-standard ECPs are in use, they are read along with the basis set information.        
When IOp(3/5)=6 (LANL basis and potentials) this selects the type.
* 0        LANL1 ECP, MBS.        
* 1        LANL1 ECP, DZ.        
* 2        LANL2 ECP (where available, otherwise LANL1), MBS.        
* 3        LANL2 ECP (where available, otherwise LANL1), DZ.        
When IOp(3/5)=8 (Dunning bases) this option selects the type.
* 0        Dunning full double-zeta.        
* 1        Dunning valence double-zeta.        
* 2        WAG basis (Dunning VDZ on first row, SHC ECP on second row). See Rappe, Smedley, and Goddard, J. Phys. Chem. 85, 1662 (1981) and J. Phys. Chem. 85, 3546 (1981).        
When IOp(3/5)=9 (CEP basis) this option selects the type (H-Ar only).
* 0         CEP-4G.        
* 1        CEP-31G.        
* 2        CEP-121G.        
When IOp(3/5)=17 (Stuttgart/Dresden ECP bases) this option selects the type according to:
* 6        SDDAll: SDD for Z > 2        
* 7        SDD for Z > 18 with SEG basis for Lanthanides & Actinides, D95 or 6-31G and no ECP otherwise.        
* 8        SDDOld: same as SDD with old Lanthanide & Actinide basis.        
When IOp(3/5)=26 (Coreless basis) this selects the choice of basis (the same ECPs are used regardless).
* 0        Default (3)        
* 1        Primitives which match the ECPs.        
* 2        Functions from extended Huckel theory.        
* 3        VSTO-4G basis for 1st row, along with LP-31G potential.        
* N>3        Huckel basis for method N-1.        
When IOp(3/5)=27 (DGauss basis sets).
* 1        DGDZVP.        
* 2        DZVP2.        
* 3        DGTZVP.        
* 4        DGA1 (fitting basis).        
* 5        DGA2 (fitting basis).        
### IOp(3/7)
Diffuse and polarization functions.
* 0        None.        
* 1        D-functions on heavy atoms (2nd row only for 3-21G).        
* 2        2d-functions on heavy atoms (Scaled up and down by a factor of 2 from the standard single-d values).        
* 3        One set of d-functions and one set of f-functions on heavy atoms. (indicates an extra tight 2df with ccp basis sets.)        
* 4        Two sets of d-functions and one set of f-functions on heavy atoms.        
* 5        Three sets of d-functions.        
* 6        Three sets of d-functions and one set of f-functions.        
* 7        Three sets of d-functions and two sets of f-functions.        
* 8        CBS-Q d(f),d,p polarization basis.        
* 9        Tight d for VnZ+1 (W1 theory).        
* 10        A set of diffuse sp-functions on heavy atoms.        
* 20        Augment non-hydrogens only (cc basis sets only).        
* 30        maug-: Main group(SP), TM(SP).        
* 40        H(SP), Main group(SP), TM(SP).        
* 50        Jul- aug: up to LVal on non-H,He.        
* 60        Jun- aug: up to LVal-1 on non-H,He.        
* 70        May- aug: up to LVal-2 on non-H,He.        
* 80        Apr- aug: up to LVal-3 on non-H,He.        
* 100        P-functions on hydrogens; interpret first digit as pol level for ugbs.        
* 200        2 sets of p-functions on hydrogens.        
* 300        One set of p-functions and one set of d-functions on hydrogens.        
* 400        Two sets of p-functions and one set of d-functions on hydrogens.        
* 500        Three sets of p-functions.        
* 600        Three sets of p-functions and one set of d-functions.        
* 700        (2d,d,p) — 2d on 2nd and later atoms, 1d on 1st row atoms.        
* 1000        Pople-style basis sets:  a diffuse function on hydrogens. Truhlar-style calendar basis sets: inconsistent s and p diffuse functions.        
* N000         Number of times to augment (cc-pvxz basis sets).        
* M0000              Maximum L for diffuse functions is L(valence)-M.        
### IOp(3/8)
Selection of pure/Cartesian functions.
* 0        Selection determined by the basis        
*          N-31G        6D/7F        
*          N-311G        5D/7F        
*          N-21G*        5D        
*          STO-NG*        5D        
*          LP-N1G*        5D        
*          LP-NIG**        5D        
*          General basis        5D/7F        
* 1        Force        5D        
* 2        Force        6DF        
* 10        Force        7F        
* 20        Force        10F        
### IOp(3/9)
`L308`: Where to store dipole velocity integrals.
* 0        Usual place (572).        
* -1        Write over the dipole length integrals (518).        
* N        Store in RWF N.        
### IOp(3/10)
Modification of internally stored bases (default 12000).
* 0        None.        
* 1        Read in general basis data in addition to setting up a standard basis.        
* 10        Massage the data in Common /B/ and Common /Mol/.        
* 20        Massage the data in Common /B/ and Common /Mol/, but don’t change ian if nuc charge changed.        
* 100        Add ghost atoms to /B/ so that every shell is on a separate center.        
* 1000        Split S=P AO basis shells into separate S and P shells.        
* 2000        Do not split S=P AO shells.        
* 10000        Split S=P=D=… AO shells into S=P, D, F, …        
* 20000        Do not split AO S=P=D… shells.        
* 100000        Uncontract the AO basis and removes duplicate primitives.        
* 200000        Uncontract the density basis and removes duplicate primitives.        
* 300000        Uncontract both basis sets and removes duplicate primitives.        
* 400000        Same as 1 but don’t remove the duplicates.        
* 500000        Same as 2 but don’t remove the duplicates.        
* 600000        Same as 3 but don’t remove the duplicates from the AO basis.        
* 700000        Same as 3 but don’t remove the duplicates from the density basis.        
* 800000        Same as 3 but don’t remove the duplicates from both bases.        
* 1000000        Modification 1 for Fermi-contact spin-spin coupling.        
* 2000000        Modification 2 for Fermi-contact spin-spin coupling.        
### IOp(3/11)
Control of two-electron integral storage format.
* 0        Regular integral format is used.        
* 1        Raffenetti ‘1’ integral format is used. Can only be used with the closed shell SCF.        
* 2        Raffenetti ‘2’ integral format. Suitable for use with the open shell (UHF) SCF.        
* 3        Raffenetti ‘3’ integral format. Suitable for use with open shell RHF SCF and the post-SCF procedures, but not yet accepted by them.        
* 9        Use ILSW to decide between Raffenetti 1 and 2.        
### IOp(3/12)
Flag for semi-empirical runs, to account for sparkles, translation vectors and d functions properly.
* 1         CNDO        
* 2        INDO        
* 3        ZINDO/1        
* 4        ZINDO/S        
* 5        MINDO3        
* 6        MNDO        
* 7        AM1        
* 8        PM3        
* 9        DFTB        
* 10        PM6        
* 11        PDDG        
### IOp(3/13)
Nuclear center whose Fermi contact terms are to be added to the core Hamiltonian. The magnitude is specified by IOp(3/15).
### IOp(3/14)
Addition of electrostatic integrals to core Hamiltonian.
* 0        No.        
* -1x        SCRF calculation — multiply moments by fudge factor for charged species.        
* -7        Same as 0.        
* -6        Read coefficients of field, starting with electric field, up through 34 elements (hexadecapoles) in free format, blank terminated.        
* -5        Read components of electric field only from /Gen/ on checkpoint file.        
* -4        Read components of moments off RWF 521 on checkpoint file.        
* -3        Read components of electric field only from /Gen/.        
* -2        Read components of moments off RWF 521.        
* -1        Yes, read 12 cards with x,y,z components of electric field, followed by xx,yy,zz,xy,xz,yz electric field gradient, xxx, yyy, zzz, xyy, xxy, xxz, xzz, yzz, yyz, xyz field second derivatives, and xxxx, yyyy, zzzz, xxxy, xxxz, yyyx, yyyz, zzzx, zzzy, xxyy, xxzz, yyzz, xxyz, yyxz, zzxy field third derivatives in format (3D20.10). (These correspond to dipole, quadrupole, octupole, and hexadecapole perturbations).        
* 1-34        Just component number n in the above order with magnitude given by IOp(3/15).        
The nuclear repulsion energy is also modified appropriately,
and the electric field is stored in Gen(2-4).
### IOp(3/15)
Magnitude of electric field.
* 0         Default.        
* N        N * 0.0001.        
### IOp(3/16)
Pseudopotential option
* 0        Default. ECPs if defined with the basis set.        
* 1        Yes, read if general basis.        
* 2        No.        
* 00        Default (10).        
* 10        Read ECPs for QM atoms.        
* 20        Read ECPs for EE charge centers only.        
* 30        Read two input sections, for QM then EE charge centers.        
* 000        Default (100).        
* 100        Spin-orbit ECP coefficients are used as-is, appropriate for published Stuttgart potentials.        
* 200        Spin-orbit ECP coefficients are scaled by 2/(2l+1), appropriate for CRENBL potentials.        
### IOp(3/17)
Specification of pseudo-potentials
* -2        Same as 0.        
* -1        Read potential in old format.        
* 0        Default, based on IOp(3/5).        
* 1        Use internally stored ‘coreless Hartree-Fock’.        
* 2        Goddard/Smedley SECE/SHC potentials.        
* 3        Stevens/Basch/Krauss CEP potentials.        
* 4        LANL1 potentials.        
* 5        LANL2 potentials.        
* 6-7        Unused.        
* 8        Read in from cards (see pinput for details).        
* 9        Dresden/Stuttgart potentials – SDD combination.        
* 10        Dresden/Stuttgart potentials – SDD for Z > 18, D95V, no ECP otherwise.        
* 11        Dresden/Stuttgart potentials –SDF.        
* 12        Dresden/Stuttgart potentials –SHF.        
* 13        Dresden/Stuttgart potentials –MDF.        
* 14        Dresden/Stuttgart potentials – MHF (first set).        
* 15        Dresden/Stuttgart potentials – MHF (second set).        
* 16        Dresden/Stuttgart potentials – MWB (first set).        
* 17        Dresden/Stuttgart potentials – MWB (second set).        
* 18        Dresden/Stuttgart potentials – MWB (third set).        
* 19        Pseudopotentials for all coreless basis.        
* 20        Alternative potentials for coreless basis.        
* 21        Psuedopotentials for the def2SV, def2TZV, and QZV basis sets.        
### IOp(3/18)
Printing of pseudo-potentials
* 0        Print only when input is from cards or if GFPrint was specified.        
* 1        Print.        
* 2        Don’t print.        
### IOp(3/19)
Specification of substitution potential types.
* 0        Don’t use any substitution potentials.        
* N        Replace the standard potential of this run (EG.CHF), with a substitution potential of type n wherever such substitution potential exists.        
### IOp(3/20)
Size of buffers for integral file.
* 0        Default (Machine dependant; 16384 integer words on VAX, 55296 words on Cray).        
* N        N integer words.        
### IOp(3/21)
Size of buffers for integral derivative file. No longer used.
* 0        Default (3200 integer words).        
* N        N integer words.        
### IOp(3/22)
`L312`: Control of the pre-cutoff in the two-electron d-integral program.
* 0        No pre-cutoff.        
* 1        Pre-cutoffs designed for the 6-31G* basis.        
### IOp(3/23)
Disable use of certain basis functions.
* 0        Use all basis functions.        
* 1        Read in a list of basis function numbers in Format (10I5), terminated by a blank line, and set their diagonal core Hamiltonian elements to +100.0.        
### IOp(3/24)
Printing of Gaussian function table.
* 0        Default (don’t print).        
* 1        Print old-fashioned table.        
* 10        Print as GenBas input.        
* 100        Print in more readable format.        
* 1000        Print shell coordinates.        
* 00000        Print AO basis using default primitive normalization.        
* 10000        Print AO basis using coefficients of raw primitives.        
* 20000        Print AO basis using coefficients of AO normalized primitives.        
* 30000        Print AO basis using coefficients of J normalized primitives.        
* 000000        Print density basis using default primitive normalization.        
* 100000        Print density using coefficients of raw primitives.        
* 200000        Print density using coefficients of AO normalized primitives.        
* 300000        Print density using coefficients of J normalized primitives.        
### IOp(3/25)
Number of last two electron integral links.
* -2        Use integrals from a previous job read /IBF/ from the checkpoint file.        
* -1        We are re-using integrals produced earlier in the current calculation; use the /IBF/ already on the RWF.        
* 0        We are not using two-electron integrals.        
* 1        Direct SCF.        
* >0        Link number.        
### IOp(3/26)
Accuracy option.
* 0        Default. Integrals are computed to 10^-10 accuracy.        
* 1        Test. Do all integrals as well as possible in L311.        
* 2        STO-3G. Use old very inaccurate cutoffs in link 311.        
* 10        Test. Do all integrals as well as possible in L314.        
* 20        Sleazy. Use looser cutoffs in L314.        
### IOp(3/27)
Computing and storing of small two-electron integrals.
* 0        Discard integrals with magnitude less than 10^-12.        
* N        Discard integrals with magnitude less than 10^-N.        
### IOp(3/28)
Special SP code control.
* 0        Default, use IsAlg.        
* 1        All integrals with d’s — L311 does nothing.        
* 2        SP integrals in link 311, d and higher elsewhere.        
* 3        All integrals done in L314 using Prism.        
### IOp(3/29)
`L302`: Accuracy.
* 0        Default (10^-13).        
* N        10^-N.        
### IOp(3/30)
Control of two-electron integral symmetry.
* 0        Two-electron integral symmetry is turned off.        
* 1        Two-electron integral symmetry is turned on. Note, however, the SET2E will interrogate ILSW to see if the symmetry RW-files exist. If they don’t, symmetry has been turned off elsewhere, and SET2E will also turn it off here.        
### IOp(3/31)
Use of symmetry in computing gradient (Obsolete).
### IOp(3/32)
Whether to check the eigenvalues of the overlap matrix.
* 0        Default (205).        
* 1        Yes.        
* 2        No.        
* 3        Yes, and reduce expansion space if linear dependence is found (NYI).        
* 4        Yes, and use Schmidt orthogonalization to reduce expansion space.        
* 5        Yes, using SVD to reduce expansion space.        
* 6        Set up SAOs as with 5 but using diagonalization instead of SVD.        
* 9        Set up a unit matrix for the transformation.        
* 100        Try to make the new set of vectors as much like the previous set, if any.        
* 200        Do SVD ignoring the previous orthonormal set, if any.        
* 1000        Use schmidt orthogonalized to match to previous o.n. set.        
* 2000        Use symmetric orthogonalization with Jacobi diagonalization to match to previous o.n. set.        
* 10000        Check orthonormality of generated set in RAOMat.        
* 20000        Do not check orthonormality of generated set in RAOMat.        
### IOp(3/33)
Integral package printing.
* 0        No integrals are printed.        
* 1        Print one-electron integrals.        
* 3        Print two-electron integrals in standard format.        
* 4        Print two-electron integrals in debug format.        
* 5        Combination of 1 and 3.        
* 6        Combination of 1 and 4.        
### IOp(3/34)
Dump option.
* 0        No dump.        
* 1        Control words printed (as usual).        
* 2        Additionally, Common/B/ is dumped at the beginning of each integral link.        
* 3        Additionally, the integrals are printed (standard format).        
### IOp(3/36)
`L303, L308`: Matrices to compute.
* -1        None.        
* 0        Default (dipole).        
* 1        Dipole.        
* 2        Quadrupole.        
* 3        Octupole.        
* 4        Hexadecapole.        
* 00        Default (same as 20).        
* 10        Do not compute absolute overlaps.        
* 20        Compute absolute overlap over contracted functions.        
* 30        Compute absolute overlap over both contracted and over primitive functions.        
* 000        Default, same as 100.        
* 100        L308 should compute (del r + r del) in addition to Del and r x Del.        
* 200        L308 should just Del and r x Del.        
### IOp(3/37)
`L320`: Whether to sort integrals.
* 0        Default (No).        
* 1        Yes, no longer functional.        
* 2        No.        
### IOp(3/38)
Algorithm for 1e integrals.
* 0        Default in 302, same as 1.        
* 1        Prism.        
* 2        Rys.        
* 00        Default in 308, same as 1.        
* 10        Prism.        
* 20        Explicit spdf code.        
### IOp(3/39)
Initialization of force and force constant RWFs.
* 0        Initialize.        
* 1        Leave alone.        
### IOp(3/41)
Various semi-empirical methods.
* 0        No NDDO        
* 1        NDDO        
* 00        Default use of NDDO beta parameters (arithmetic mean for indo parameters, geometric mean for NDDO/1 or read-in parameters).        
* 10        Arithmetic mean in NDDO.        
* 20        Geometric mean in NDDO.        
* 000        Default parameters (same as 5).        
* 100        Read parameters for atomic numbers 1-18 in the order: Scale (D20.12), followed by ((HDiag(J,I),J=1,3),I=1,18) (Format 3D20.12), followed by ((Beta(J,I),J=1,3),I=1,18)        
* 200        Read parameters from rwf.        
* 300        Read parameters from chk.        
* 400        Original INDO/2 Beta and HDiag Parameters.        
* 500        GNDDO/1 parametrization.        
* 0000        Use STO-3G scale factors.        
* 1000        Use Slater’s rules scale factors.        
* 00000        Default (unit overlap matrix).        
* 10000        Use the unit matrix for the overlap.        
* 20000        Use the real overlap matrix.        
* 100000        Do CNDO/2.        
* 200000        Do INDO/2.        
* 300000        Do ZINDO/1 (NYI).        
* 400000        Do ZINDO/S.        
* 500000        Do MINDO/3 (NYI).        
* 600000        Do MNDO.        
* 700000        Do AM1.        
* 800000        Do PM3.        
* 900000        Do PM3MM.        
* 1000000        Do Harris functionaL through L511.        
* 1100000        Do Harris functional scaling atomic densities for current charge and multiplicity.        
* 1200000        Harris XC but regular Coulomb iteration.        
* 1300000        Harris (XC and atomic densities) through regular code.        
* 1400000        Regular SCF with separate K, for testing.        
* 1500000        J as usual but NDDO for K.        
* 1600000        Used internally as part of 15.        
* 1700000        DFT-SCTB with tabulated parameters.        
* 1800000        DFT-SCTB with analytic expressions.        
* 1900000        EHT-SC.        
* 2000000        Set 2e terms to zero.        
* 2100000        Harris XC and DFTB-style charge iteration.        
* 2200000        Harris XC and improved DFTB-style charge iteration.        
* 2300000        PM6PFD with overlap.        
* 2400000        PM6PFD with overlap and Harris XC.        
* 2500000        PM6PFD with overlap and approximate XC.        
* 2600000        NDDO with Mayer Bond Order correlation corrections.        
* 27-38        Prefix reserved for other methods with 2e integrals.        
* 3900000        PM6.        
* 4000000        PMDDG.        
* 41        PM6E.        
* 42        PM7.        
* 43        PM6 with T transformed to OAO.        
* 44        PM7TS.        
* 45        PM7MOPAC.        
* 46-98        Prefix assumed to be ZDO methods.        
* 9900000        External program        
* 100-        Prefix assumed to be MM methods.        
### IOp(3/42)
`L317`: How to form NDDO core hamiltonian.
* 0        Default (same as 1).        
* 1        Read the integrals sequentially.        
* 2        Load all the integrals into memory.        
### IOp(3/43)
Handling of background charge distribution.
* 00        Same as 11.        
* 1        Consider external charges.        
* 2        Do not consider external charges.        
* 10        Consider self-consistent solvent charges.        
* 20        Do not consider self-consistent solvent charges.        
### IOp(3/44)
`L318`: Using Integral rejection.
* 0        Keep all integrals.        
* 1        neglect four center transformed integrals.        
* 2        neglect four center and 3 center (ab|ac) integrals.        
* 3        neglect four center and three center (0,0) integrals.        
* 4        NDDO approximation — no (ab|xx) and no <a|X|b>        
* 5        NDDO on 2e and V ints only — T and S unchanged.        
* 6        Do not transform 2e integrals, only 1e.        
### IOp(3/45)
`L318`: Transformation matrix.
* 0        Use S^-1/2.        
* 1        Just orthogonalize functions on the same center.        
* 2        Use unit matrix (for debugging).        
Order of multipoles in SCRF for L303.
### IOp(3/46)
Whether to abort the job if badbas detects an error.
* 0        Default (yes).        
* 1        No.        
* 2        Yes.        
### IOp(3/47)
Flags for use in Prism and CalDFT throughout the program.
* -2        Force use of only the MD paths for all calculations.        
* -1        Force use of only the OS path for all calculations. Bit flags.        
* 0        If bit 0 is set (use AllowP array) then read in a list of allowed paths.        
* 1        Use expanded matrix logic for PBC exact exchange.        
* 2        Reverse choice of whether to precompute distance matrix during numerical quadrature.        
* 3        Skip consistency checks for XC quadrature.        
* 4        Do not do extra work to use cutoffs better, currently only affects CalDFT.        
* 5        Reverse normal choice of diagonal/canonical sampling in Prism and PrmRaf. The default is diagonal only on vector machines.        
* 6        Trace input and output using Linda/subprocess.        
* 7        Force single matrix code in CPKS.        
* 8        Force all near field in FMM.        
* 9        Turn off dynamic allocation of parallel work in CalDSu, CoulSu, and FMMEnt.        
* 10        Force square loops, currently only in PrismC.        
* 11        Turn off dynamic work allocation among Linda workers. (Currently turned off anyway).        
* 12        Reverse normal choice of Scat20 vs. replicated Fock matrices. Default is to use replicated matrices only on Fujitsu and NEC.        
* 13        Turn on Schwartz screening only in FoFCou, turning  off heuristic screening.        
* 14        Force separate evaluation of J and K terms.        
* 15        Forbid use of gather/scatter digestion even for small numbers of density matrices.        
* 16        Insist on gather/scatter digestion even for large numbers of matrices. Does not affect FoFRaf, which only does inner loops over matrices.        
* 17        Forbid use of Schwartz screening in FoFCou.        
* 18        Don’t compute on Linda master.        
* 19        Do nuclear contribution in FoFCou even for non-PBC.        
* 20        Do not use special Coulomb algorithm in FoFCou.        
* 21        Force dynamic parallel work logic even for single processor tasks.        
* 22        Turn off use of Sqrt(P) in density-based cutoffs.        
* 23        Use tabulated numerical values for atomic densities instead of Gaussian expansions.        
* 24        Do allocation for parallel 2e integrals but run sequentially.        
* 25        Do
allocation for parallel XC but run sequentially.        
* 26        Make all atoms large in XC quadrature.        
* 27        Make all shells large in XC quadrature.        
* 28        Do not symmetry reduce grid points on unique atoms.        
* 29        Turn on use of pre-computed XC weights.        
* 30        Make Linda workers run sequentially.        
* 31        Reserved for flag for calls to OneElI, etc. in parallel regions.        
### IOp(3/48)
Options for FMM.
RRLLNNTTWW
* RR:        Range (default 2).        
* LL:        LMax (default from tolerance).        
* NN:        Number of levels (default 8).        
* TT:        Tolerance (default 18).        
* WW:        IWS (default 2).        
### IOp(3/49)
More bitwise options for FMM and 2e integrals. The bits are:
* 0        Indicates whether FMM can be used by FoFCou.        
* 1        Uncontract all shell pairs.        
* 2        Apply symmetry to derivative distributions (NYI).        
* 3        Do not save as many multipole expansions as possible in memory.        
* 4        Turn on FMM print.        
* 5        Convert
to sparse storage under FoFCou for testing.        
* 6        Split primitives for better boxification.        
* 7        Default UseUAB/Use 256.        
* 8        UseUAB, if 128 set.        
* 9        Turn off parallelism in FMM (does not use parallel logic).        
* 10        Set up for parallel FMM but run loops sequentially.        
* 11        Do not default to FMM.        
* 12        Force FMM on.        
* 13        Set by PsmSet to indicate whether the NAtoms test for defaulting FMM was passed.        
* 14        Turn on parallelism in FMM during CPHF. Default is off.        
* 15        Force use of old box-box screening.        
* 16        Do not Include 1/R or Erf(R)/R in box-box screening.        
* 17        Force use of non-cubic logic.        
* 18        Turn off box-box screening.        
* 19        Skip FF exchange.        
* 20–22        Pure functional control:        
*          0  Default, same as 1.        
*          1  Convert densities, etc. to Cartesian.        
*          2  Transform 2e integrals to pure before digestion.        
*          3  Generate 2e integrals over real spherical harmonics.        
*          4  Generate 2e integrals over complex spherical harmonics.        
*          5  Generate 2e integrals over spinors.        
*          6  Generate 2e integrals over large and small components.        
### IOp(3/51)
Parameters for FMM box length (MMMMMNNNN):
* MMMMM        Box length when doing Coulomb will be MMMMM/1000 Bohr. The default is 2.5 Bohr.        
* NNNN        Box length when doing Exchange will be NNNN/1000 Bohr. The default is 0.75 Bohr. If doing both Coulomb and exchange at the same time, the max. of the two values is used.        
### IOp(3/52)
Turn off normal evaluation of ECP integrals.
* 0        Default: if needed, ECP integrals are evaluated in L302.        
* 1        Old routines will be used, so L302 does not do ECP ints.        
### IOp(3/53)
Accuracy in ECP integral evaluation.
* 0        Default.        
* -1        No Cutoffs.        
* N        10^-N.        
### IOp(3/55)
Use of sparse storage.
* -100 < N< -4        Cutoff 10^(N+5) for testing new code.        
* -4        Reserved (used for nosparse in parsing).        
* -3        Yes, intermediate accuracy (10^-6).        
* -2        Yes, crude accuracy (10^-6).        
* -1        Yes, default accuracy (10^-8).        
* 0        No.        
* N        Yes, cutoff 10^-N.        
### IOp(3/56)
Cutoff for intermediate matrices during sparse operations.
* 0        100 times smaller than storage cutoff.        
* N        10^-N.        
### IOp(3/57)
Number of core electrons for Stuttgart/Dresden ECP’s.
### IOp(3/58)
Cholesky control options.
### IOp(3/59)
Threshold for throwing away eigenvectors of S.
* 0        Default (10^-6).        
* N        10^-N.        
### IOp(3/60)
Control of orthogonalization and simplification of generalized contraction basis sets.
* -1        Turn off orthogonalization and simplification.        
* 0        Default (2).        
* 1        Orthogonalize and remove primitives with 0 coefficients (exact transformation).        
* 2        Orthogonalize and remove primitives with 0 or small coefficients.        
* N        Orthogonalize and remove primitives with coefficients less than 10^-N.        
### IOp(3/61)
`L302`: Sparse semi-empirical Hamiltonian cutoffs.
* XX        F(Mu,Lambda) atom–atom cutoff criterion (angstroms) Mu, Lambda are basis functions on different atoms. (defaults to 15 angstroms).        
* XX00        F(Mu,Nu) atom–atom cutoff criterion (angstroms) Mu, Nu are basis functions on the same atom. (defaults to no F(Mu,Nu) cutoff).        
### IOp(3/62)
Maximum allowed error in S over orthogonalized basis functions.
* 0        Default (10^-9.        
* N        10^-N.        
### IOp(3/63)
Debug option to test point charge FMM.
* 0        No.        
* 1        Yes.        
* 2        Yes, read parameters.        
* 10        Also do forces.        
### IOp(3/64)
Set value for ILSW derivative flag. Only active if IOp(3/39)=0.
* -2        Set to zero.        
* -1        Set to -1.        
* 0        Leave alone.        
* N        Set to N.        
### IOp(3/65)
Number of k-points.
* -1        Just Gamma point.        
* N        About N points.        
* -N        Old logic for NRecip=N.        
### IOp(3/66)
Override setting of NThInc in lineary dependence cutoff.
* -1        0.        
* 0        Don’t change.        
* N        Set to N.        
### IOp(3/67)
Electric-field dependent functions.
* 0        Default (on if already present in basis read from RWF or checkpoint, otherwise off).        
* 1        No.        
* 2        Yes, with standard values.        
* 3        Yes, with read-in values.        
### IOp(3/70)
SCRF flag.
* 0        Default (1).        
* 1        Use defaults.        
* 2        Read setting from checkpoint.        
* 3        Read setting from the input stream.        
* 4        Read setting from checkpoint and modify them by reading from the input stream.        
* 5        Read from RWF.        
* 0100        Flag for macro-iterations.        
* 1000        SCI-PCM.        
* 2000        D-PCM.        
* 2100        C-PCM.        
* 2200        IEF-PCM.        
* 2300        IVC-PCM.        
* 4000        Onsager.        
* 10000         Generate
COSMOTHERMO output.        
* 20000        Do COSMO style CPCM: Klamt radii, iterative (implies g03defaults)        
* 30000        Do SMD parametrization of non-electrostatic terms.        
* x00000        Flag for PCM family options:        
*          1 = include cavity-field effects.        
*          2 = setting for accurate DeltaG of salvation.        
*          3 = setting to reproduce G03 behavior.        
* 1000000        Flag to skip PCMInp as L124 already did it or we’re doing flavor X of ONIOM-PCM.        
* 2000000        Write the PCM charges on the checkpoint file.        
* 3000000        Read the PCM charges from the checkpoint.        
* 4000000        Read and write the PCM charges from and to the checkpoint file.        
* 5000000        Write the non-equilibrium PCM charges on the checkpoint file.        
* 6000000        Read the non-equilibrium PCM charges from the checkpoint file.        
* 7000000        Write the CC non-equilibrium PCM charges on the checkpoint file.        
* 8000000        Read the CC non-equilibrium PCM charges from the checkpoint file.        
* 9000000        Write the cLR non-equilibrium PCM charges on the checkpoint file.        
* 00000000        Default, same as 30000000.        
* 10000000        Do the PCM electrostatic cavity.        
* 20000000        Do the PCM non-electrostatic cavity.        
* 30000000        Do both the PCM electrostatic and non-electrostatic cavities.        
* 40000000        Do neither the PCM electrostatic nor non-electrostatic cavities.        
### IOp(3/71)
IDeriv level flag (for SCRF setup): 0, 1, 2 for none, 1^st or 2^nd nuclear coordinate derivatives.
### IOp(3/72)
Solvent type flag (for SCRF setup).
### IOp(3/73)
Old ONIOM-PCM flag (currently unused).
### IOp(3/74)
Type of exchange and correlation potentials.
* -79        PBE-QIDH.        
* -78        PBE0-DH.        
* -77        DSD-PBEP86 (double hybrid, DFT-D3).        
* -76        PW6B95-D3.        
* -75        PW6B95.        
* -74        M08-HX.        
* -73        MN15.        
* -72        MN15-L.        
* -71        LC-wHPBE.        
* -70        MN12-SX.        
* -69        N12-SX.        
* -68        MN12-L.        
* -67        N12.        
* -66        M11L.        
* -65        SOGGA11X.        
* -64        M11.        
* -63        SOGGA11.        
* -62        HISSaPBE.        
* -61        HISSbPBE.        
* -60        B2PLYP-D3 (double hybrid, DFT-D3).        
* -59        B97-D (DFT-D3).        
* -58        wB97X-D.        
* -57        wB97X.        
* -56        wB97.        
* -55        M06-2X.        
* -54        M06.        
* -53        M06-L.        
* -52        M06-HF.        
* -51        HSEH1PBE.        
* -50        mPW2PLYP-D (double hybrid).        
* -49        B2PLYP-D (double hybrid).        
* -48        mPW2PLYP (double hybrid).        
* -47        B2PLYP (double hybrid).        
* -46        PAPF-D.        
* -45        PAPF.        
* -44        APF-D.        
* -43        APF.        
* -42        B97-D.        
* -41        LC-wPBE.        
* -40        CAM-B3LYP.        
* -39        OAPF.        
* -38        M052X.        
* -37        M05.        
* -36        HSE1PBE.        
* -35        TPSSh.        
* -34        BMK.        
* -33        X3LYP.        
* -32        t-HCTH hybrid.        
* -31        t-HCTH.        
* -30        OmPW3PBE.        
* -29        OmPW1PBE.        
* -28        OmPW1LYP.        
* -27        OmPW1PW91.        
* -26        PBEH1PBE.        
* -25        HSE2PBE.        
* -24        O3LYP.        
* -23        HCTH407.        
* -22        HCTH147.        
* -21        B97-2.        
* -20        B97-1.        
* -19        HCTH93.        
* -18        B98.        
* -17        B1B95.        
* -16        BA3PBE.        
* -15        BA1PBE.        
* -14        PBE3PBE.        
* -13        PBE1PBE.        
* -12        mPW3PBE.        
* -11        mPW1PBE.        
* -10        mPW1LYP.        
* -9        LG1LYP.        
* -8        B1LYP.        
* -7        mPW91PW91.        
* -6        Becke3 with Perdew 91 correlation.        
* -5        Becke3 using VWN/LYP for correlation.        
* -4        Becke3 with Perdew 86 correlation.        
* -3        Becke "Half and Half" with LYP/VWN correlation.        
* -2        Becke "Half and Half": 0.5 HF + 0.5 LSD.        
* -1        Do only Coulomb part; skip exchange-correlation.        
* 00        Default, same as 100.        
* 01        Vosko-Wilk-Nusair method 5 correlation.        
* 02        Lee-Yang-Parr correlation.        
* 03        Perdew 81 correlation.        
* 04        Perdew 81 + Perdew 86 correlation.        
* 05        VWN 80 (LSD) correlation.        
* 06        VWN 80 (LSD) + Perdew 86 correlation.        
* 07        [unused]        
* 08        PW91.        
* 09        PBE.        
* 10        VSXC.        
* 11        Bc96.        
* 18        VWN5+P86.        
* 19        LYP+VWN5 for scaling.        
* 20        KCIS correlation.        
* 21        Becke-Roussel correlation (NYI).        
* 22        PKZB correlation.        
* 23        TPSSc        
* 24        t-HCTH (JCP 116, 9559 (2002))        
* 25        t-HCTH hybrid (JCP 116, 9559 (2002))        
* 26        BMK (Boese and Martin, JCP 121, 3405 (2004))        
* 27        M05 (Zhao,Schultz,Truhlar, JCP 123 (2005) 161103)        
* 28        M05-2X (Zhao,Schultz,Truhlar, JCTC 2006 in press)        
* 29        OAPF (Austin, Petersson, Frisch, …)        
* 30        B97-D (Grimme, JCC 2006, 27, 1787)        
* 31        APF (Austin, Petersson, Frisch, …)        
* 32        PAPF (Austin, Petersson, Frisch, …)        
* 33        M06-HF (Zhao,Truhlar, JPC A 2006, 110, 13126)        
* 34        M06-L (Zhao,Truhlar, JCP 2006, 125, 194101)        
* 35        M06 (Zhao,Truhlar, Theo Chem Acc 2008, 120, 215)        
* 36        M06-2X (Zhao,Truhlar, Theo Chem Acc 2008, 120, 215)        
* 37        wB97 (J.-D. Chai, M. Head-Gordon, JCP 128, 084106 (2008))        
* 38        wB97X (J.-D. Chai, M. Head-Gordon, JCP 128, 084106 (2008))        
* 39        wB97X-D (J.-D. Chai, M. Head-Gordon, PCCP 10, 6615 (2008))        
* 40        revTPSSc        
* 41        SOGGA11 (Peverati, Zhao, Truhlar, JPCL 2, 1991 (2011))        
* 42        M11 (Peverati, Truhlar, JPCL 2, 2810 (2011))        
* 43        SOGGA11-X (Peverati, Truhlar, JCP 135, 191102 (2011))        
* 44        M11-L (Peverati, Truhlar, JPCL 3, 117 (2012))        
* 45        N12 (Peverati, Truhlar, JCTC 8, 2310 (2012))        
* 46        MN12-L (Peverati, Truhlar, PCCP DOI: 10.1030/c2cp42025b)        
* 47        N12-SX (Peverati, Truhlar, PCCP submitted)        
* 48        MN12-SX (Peverati, Truhlar, PCCP submitted)        
* 49        CVDFT correlation        
* 50        CCDFT correlation        
* 100        Hartree-Fock exchange.        
* 200        Hartree-Fock-Slater exchange (Alpha = 2/3).        
* 300        X-alpha exchange (alpha= 0.7).        
* 400        Becke 1988 exchange.        
* 500        LG exchange (depreciated)        
* 600        PW91 exchange.        
* 700        Gill 96 exchange (depreciated)        
* 800        PW86 exchange (depreciated)        
* 900        mPW exchange.        
* 1000        PBE exchange.        
* 1100        [Reserved to map 300]        
* 1200        VSXC exchange.        
* 1400        B98 (JCP 108,9624(1998) eq.2c ) exchange.        
* 1500        HCTH (JCP 109,6264 (1998) exchange.        
* 1600        B97-1 (CPL 316,160(2000)) exchange.        
* 1700        B97-2 (JCP 115,9233(2001)) exchange.        
* 1800        HCTH147 exchange.        
* 1900        HCTH407 exchange.        
* 2000        OPTX exchange.        
* 2100        OPTX exchange as in O3LYP.        
* 2200        XVa exchange (NYI).        
* 2300        Becke-Roussel ’88 exchange.        
* 2400        PKZB exchange.        
* 2500        TPSSX exchange.        
* 2600        HSE03 (JCP 118,8207(2003)) exchange.        
* 2700        PBEHole (JCP 109,3313(1998)) exchange.        
* 2800        Old mPW exchange (local scaling in non-local term).        
* 2900        t-HCTH (JCP 116, 9559 (2002))        
* 3000        t-HCTH hybrid (JCP 116, 9559 (2002))        
* 3100        X (0.765*B88+0.235*PW91) (PNAS 101(2004) 2673)        
* 3200        BMK (Boese and Martin, JCP 121, 3405 (2004))        
* 3300        M05 (Zhao,Schultz,Truhlar, JCP 123 (2005) 161103)        
* 3400        M05-2X (Zhao,Schultz,Truhlar, JCTC 2006 in press)        
* 3500        OAPF (Austin, Petersson, Frisch, …)        
* 3600        B97-D (Grimme, JCC 2006, 27, 1787)        
* 3700        APF (Austin, Petersson, Frisch, …)        
* 3800        PAPF (Austin, Petersson, Frisch, …)        
* 3900        HSE + Henderson        
* 4000        M06-HF (Zhao,Truhlar, JPC A 2006, 110, 13126)        
* 4100        M06-L (Zhao,Truhlar, JCP 2006, 125, 194101)        
* 4200        M06 (Zhao,Truhlar, Theo Chem Acc 2008, 120, 215)        
* 4300        M06-2X (Zhao,Truhlar, Theo Chem Acc 2008, 120, 215)        
* 4400        wB97 (J.-D. Chai, M. Head-Gordon, JCP 128, 084106 (2008))        
* 4500        wB97X (J.-D. Chai, M. Head-Gordon, JCP 128, 084106 (2008))        
* 4600        wB97X-D (J.-D. Chai, M. Head-Gordon, PCCP 10, 6615 (2008))        
* 4700        HISS (Henderson,Izmaylov,Scuseria,Savin, JCP 127, 22103 (2007))        
* 4800        revTPSSX        
* 4900        SOGGA11 (Peverati, Zhao, Truhlar, JPCL 2, 1991 (2011))        
* 5000        M11 (Peverati, Truhlar, JPCL 2, 2810 (2011))        
* 5100        SOGGA11-X (Peverati, Truhlar, JCP 135, 191102 (2011))        
* 5200        M11-L (Peverati, Truhlar, JPCL 3, 117 (2012))        
* 5300        N12 (Peverati, Truhlar, JCTC 8, 2310 (2012))        
* 5400        MN12-L (Peverati, Truhlar, PCCP DOI: 10.1030/c2cp42025b)        
* 5500        N12-SX (Peverati, Truhlar, PCCP submitted)        
* 5600        MN12-SX (Peverati, Truhlar, PCCP submitted)        
* 5700        [reserved to produce B values for XDM]        
* 5800        [reserved to run HF + XDM]        
* 7000        CVDFT exchange        
So 100 is Hartree-Fock, 200 is Hartree-Fock-Slater, 205 is Local Spin Density, and 402 is BLYP.
* 1xxxxxx        Do Hirao’s long-range correction (JCP 115(2001) 3540).        
* 2xxxxxx         Do Harris XC with full J.        
* 3xxxxxx         Do Harris with the specified functional.        
* 4xxxxxx         Do Harris XC with DFTB-style J.        
* 5xxxxxx        Do Harris XC with improved DFTB-style J.        
### IOp(3/75)
Number of radial and angular points in numerical integration for DFT.
* 0        Default (-5).        
* 1        SG1 pruned grid.        
* 2        Even sleazier grid than SG1 used for CPHF.        
* 3        Pruned (75,194) which is not good for much.        
* 4        FineGrid.        
* -4        FineGrid unless uncontracting, then 199302.        
* 5        UltraFine.        
* -5        UltraFine unless uncontracting, then 199590.        
* 7        SuperFine.        
* -7        SuperFine unless uncontracting, then 299974.        
* IIIJJJ        III radial points, JJJ angular points.        
* -IIIJJJ        III radial points, and a spherical product angular grid with JJJ theta points and 2*JJJ phi points.        
### IOp(3/76)
Mixing of HF and DFT. Negative values correspond to standard combinations of HF exchange, local and non-local exchange, and local and non-local correlation.
* -36        PBE-QIDH coefficients.        
* -35        PBE0-DH coefficients.        
* -34        DSD-PBEP86 coefficients.        
* -33        PW6B95 and PW6B95-D3 coefficients.        
* -32        M08-HX coefficients.        
* -31        MN15 coefficients.        
* -30        SOGGA11-X coefficients.        
* -29        HSEH1, N12-SX and MN12-SX coefficients.        
* -28        M06-2X coefficients.        
* -27        M06, wB97, wB97X, wB97X-D, HISS-B, HISS-A, M11 and LC-wHPBE coefficients.        
* -26        M06-HF coefficients.        
* -25        mPW2PLYP coefficients.        
* -24        B2PLYP coefficients.        
* -23        APF coefficients.        
* -22        Unused.        
* -21        LC-wPBE coefficients.        
* -20        CAM-B3LYP coefficients.        
* -19        OAPF coefficients.        
* -18        M05-2X coefficients.        
* -17        TPSSh coefficients.        
* -16        BMK coefficients.        
* -15        X3LYP coefficients.        
* -14        tHCTH coefficients.        
* -13        B1B95/M05 coefficients.        
* -12        HSE1PBE, HSE2PBE coefficients.        
* -11        Unused        
* -10        O3LYP coefficients.        
* -9        B97-2 coefficients.        
* -8        B97-1 coefficients.        
* -7        HCTH coefficients.        
* -6        B98 coefficients.        
* -5        mPW91PW91 coefficients.        
* -4        Becke3 coefficients: aLSD + (1-a)HF + b(dBx) + VWN + c(LYP-VWN), with a=0.8 b=0.72 c=0.81 Note that Becke actually used Perdew correlation rather than LYP.        
* -3        Becke"Half and Half" 0.5 HF + 0.5 Xc + Corr        
* -2        Coefficients of 0 and 0 (no exchange).        
* -1        Coefficients of 0.0 and 1.0 for DFT and HF, respectively.        
* 0        Default: pure HF, DFT or mixed in accord with IOp(3/76)        
* MMMMMNNNNN        Mixture of MMMMM/10000 DFT exchange and NNNNN/10000 HF exchange.         
The DFT exchange factor multiplies any implied by IOp(74) or set by IOp(77).
### IOp(3/77)
Mixing of local and non-local exchange.
* -1        0 for both.        
* 0        Default (coefficients of 1 and zero or as determined by IOp(76)).        
* MMMMMNNNNN        MMMMM/10000 non-local plus NNNNN/10000 local. Sign is applied to the local term.        
For the HSE03 functional, these coefficients scale the short range (MMMMM) and long range (NNNNN) terms.
### IOp(3/78)
Mixing of local and non-local correlation.
* -1        0 for both.        
* 0        Default (coefficients of 1 and zero as determined by IOp(76)).        
* MMMMMNNNNN        MMMMM/10000 non-local plus NNNNN/10000 local. Sign is applied to the local term.        
In L510, 1 to set up for CAS-MP2 or 2 to do spin-orbit calculation.
### IOp(3/79)
Range cutoff in Becke weights.
* 0        Default (SS weights).        
* -1        Use SS weights.        
* -2        Use Becke weights with default cutoff of 30 au.        
* -3        Use Savin weights.        
* -M<-3        Use SS weights with XCal = M/1000.        
* N        Use Becke weights with cutoff N Bohr.        
### IOp(3/80)
Range for micro-batching in DFT. Negative to turn off screening of basis functions and grid points. 1000000000 turns of micro-batching logic.
### IOp(3/82)
Fitting density basis set for Coulomb in DFT.
* -1        None.        
* 0        Default (-1).        
* N        Same numbering of basis sets as for AO basis, including 7=General basis. See comments for IOp(3/5) and IOp(3/6) 28=Generate automatically from AO basis.        
### IOp(3/83)
Equivalent of IOp(3/6) for density basis. For auto-generated
basis sets:
* MN        -1 keep all generated functions. Otherwise, an AO shell with angular momentum LAO generates a DBF shell with angular momenta 0 up to LDB, where if LVal is the highest valence (occupied) LAO then if LAO ≤ LVal, LDB = 2*LAO, while if LAO > LVal LDB = LAO + Max(LVal,1) + M. If N > 0 then LDB is limited to N-1, i.e., all angular momenta of N or higher are discarded.        
### IOp(3/84)
Equivalent of IOp(3/7) for density basis. For auto-generated basis sets:
* 0        Default (4022).        
* 1        Use all products of AOs.        
* 2        Use only AO primitives squared in fitting basis.        
* 10        Do not split shells.        
* 20        Split F and higher shells away from S=P=D.        
* N00        Use 1.5 + N/4 as the test for similar exponents during auto-generation of fitting sets.        
* 1000        Use old (G03) algorithm.        
* 2000        Use new algorithm.        
* 3000        Use algorithm 3.        
* 4000        New iterative merging of shells, monotonic L.        
### IOp(3/85)
Pure vs. Cartesian functions in density basis.
* 0        Default (pure for read-in basis).        
* 1        Pure.        
* 2        Cartesian.        
### IOp(3/86)
Discard basis functions based on angular momentum.
* 0        No.        
* N        N ≤ Discard basis functions with angular momentum.        
### IOp(3/87)
Discard density basis functions based on angular momentum.
* 0        No.        
* N        N≤ Discard density basis functions with angular momentum.        
### IOp(3/88)
Modification of internally stored density basis.
* 0        None.        
* 1        Read in general basis data in addition to setting up a standard basis.        
* 10        Massage the data in Common /B/ and Common /Mol/.        
* 100        Add ghost atoms to /B/ so that every shell is on a separate center. Also done if req. in IOp(3/10).        
* 1000        Split S=P density basis shells into separate S and P shells.        
* 2000        Do not split S=P density shells.        
* 10000        Split S=P=D=… density shells into S=P, D, F, …        
* 20000        Do not split density S=P=D… shells.        
### IOp(3/89)
Set up for density fitting.
* 0        Default (102 if a fitting set has been included and pure DFT is being used, 1 otherwise).        
* 1        Do not use density fits.        
* 2        Use fits, forming Z = modified A^-1.        
* 3        Use fits, solving iterative with stored A.        
* 4        Use fits, solving iterative with direct products, with A formed to generate preconditioning.        
* 5        Iterative, no formation of A.        
* 6        Form A’ over neutral distributions via multiplies by A.        
* 7        Form A’ over neutral distributions via direct products.        
* 1xx        Form inverse matrix once.        
* 2xx        Solve iteratively with no preconditioning.        
* 3xx        Solve iteratively with diagonal preconditioning.        
* 4xx        Solve iteratively with symmetric block-diagonal preconditioning.        
* 5xx        Solve iteratively with non-symmetric block-diagonal preconditioning.        
* 6xx        Solve non-iterative using precomputed A’^-1.        
* 1xxxx        Put all functions into a single block in forming the preconditioning matrix.        
* 1xxxxx        Form the full preconditioning matrix (not block-diagonal).        
* 0xxxxxx        Default, same as 1xxxxxx.        
* 1xxxxxx        Don’t set up fitting if exact exchange is in use.        
* 2xxxxxx        Set up fitting regardless and do one fit with the converged SCF density.        
* 3xxxxxx        Set up fitting regardless and use for Coulomb during iters. even if exact exchange is
used (NYI).        
* 10000000        Fit using Coulomb operator (default).        
* 20000000        Fit using overlaps.        
### IOp(3/90)
Thresholds for density fitting.
* MMNN        10^-MM on iterative solution, default MM=09.        
*          10^-NN on generalized inverse, default NN=06.        
### IOp(3/91)
Scalar relativistic core Hamiltonian.
* 0        Default (1).        
* 1        Non-relativistic.        
* 2        RESC.        
* 3        Douglass-Kroll-Hess 0th order.        
* 4        Douglass-Kroll-Hess 2nd order.        
* 5        DKH 4th order, including SO terms.        
* 00        Default (10).        
* 10        Do Boettinger scaling of 1e SO to approximate effect of 2e terms.        
* 20        Do not rescale SO terms.        
* 100        Multiply SO terms by 10 for debugging.        
* N00        Multiply SO terms by 10 * 10^N-1 for debugging.        
* 1000        Multiply SO terms by half.        
* 2000        Multiply SO terms by two.        
* 3000        Multiply SO terms by -two.        
### IOp(3/92)
Whether read-in basis sets are in terms of normalized primitives.
* 0        Default (3232).        
* 1        AO coefficients are for raw primitives.        
* 2        AOs have overlap normalization.        
* 3        AOs have Coulomb normalization.        
* 10        DBF coefficients are for raw primitives.        
* 20        DBFs have overlap normalization.        
* 30        DBFs have Coulomb normalization.        
* 100        Do not normalize AOs contraction coefficients.        
* 200        Use overlap normalization for AOs contraction coefficients.        
* 300        Use Coulomb normalization for AOs contraction coefficients.        
* 1000        Do not normalize DBFs contraction coefficients.        
* 2000        Use overlap normalization for DBFs contraction coefficients.        
* 3000        Use Coulomb normalization for DBFs contraction coefficients.        
### IOp(3/93)
Nuclear charge distribution.
* 0        Default (1, unless scalar relativistic).        
* 1        Point nuclei.        
* 2        Single s-Gaussians using formula of Quiney et. al.        
* 3        Very tight single s-Gaussians, for debugging.        
* 4        Same as 2 but exponents are 100x smaller, for debugging.        
* 10x        Include nuclear charge distributions in DBF set.        
* Mxxx        Use method M to handle nuclear charges during density fitting.        
* 00000        Default (1).        
* 10000        Use nuclear density in core Hamiltonian if present.        
* 20000        Do not use nuclear density in core Hamiltonian even if present.        
### IOp(3/94)
Range of PBC cells in Bohr.
* 0        Default (100).        
* N        N Bohr.        
* -M        Multiply usual range by M.        
### IOp(3/95)
Minimum number of PBC cells.
* -N        At least N cells in each direction.        
* 0        Based on range estimate (IOp(3/94)).        
* N        At least N cells total.        
### IOp(3/96)
Number of PBC cells for DFT.
* 0        As many as look significant.        
* N        At least N.        
### IOp(3/97)
Number of PBC cells for exact exchange.
* 0        As many as look significant.        
* N        At least N.        
### IOp(3/98)
Maximum number of density matrices in PBC.
* 0        Default, based on number of cells having overlap with cell 0.        
* N        No more than N matrices.        
### IOp(3/99)
`L302`: Whether to set up precomputed quadrature grid.
* 0        Default (4 if doing DFT, -1 otherwise).        
* -1        No.        
* 1        Yes, storing only grid parameters.        
* 2        Yes, storing grid parameters and weights.        
* 3        Yes, storing grid parameters, weights, and point coordinates.        
* 4        Yes, storing only dimensions.        
### IOp(3/100)
Minimum number of PBC cells for PBC-MP2.
* 0        Same as for HF exchange.        
* N        N.        
### IOp(3/101)
Maximum range of cells.
* -N        No more than N in each direction.        
* 0        No limit.        
* N        No more than N total.        
### IOp(3/102)
Number of density fittings solutions to save from previous SCF iterations. Default is 6 (using 5 previous solutions plus the current right-hand side to generate the initial guess). Negative to use projected equations rather than least-squares.
### IOp(3/103)
Maximum number of vectors allowed in expansion space during iterative density fitting. Default is Max(NDBF/2,1000), where NDBF = # density basis functions.
### IOp(3/104)
Maximum number of iterations during iterative density fitting. Default is Max (1000,NDBF+100).
### IOp(3/105)
Re-use of PBC cell data.
* 0        Default (re-use if present).        
* 1        Reuse.        
* 2        Do not reuse.        
* 3        Read from checkpoint file.        
### IOp(3/106)
Override default number of atoms threshold for turning on FMM (for debugging). This number is scaled up appropriately if symmetry is in use, to compensate for the loss of some symmetry with FMM.
* 0        Default (60)        
* N        N atoms for the C1 case.        
### IOp(3/107)
Omega for short/long range Hartree-Fock exchange.
* 0        Standard HF exchange        
* MMMMMNNNNN        Short range HF exchange with NNNNN/10000 and long range exchange with MMMMM/10000.        
### IOp(3/108)
Omega for short/long range DFT exchange.
* 0        Standard DFT exchange or default from functional.        
* MMMMMNNNNN        Short range DFT exchange with NNNNN /10000 and long range DFT exchange with MMMMM/10000.        
### IOp(3/109)
Omega for short/long range DFT correlation
* 0        Standard DFT correlation or default from functional.        
* MMMMMNNNNN        Short range DFT correlation with NNNNN/10000 and long range DFT correlation with MMMMM/10000.        
### IOp(3/110)
Threshold in precomputed XC quadrature grid, over-riding default or value in IOp(27).
* 0        As implied by IOp(27).        
* N        10^-N.        
### IOp(3/111)
Extra PBC printing. Default is no print.
* 1        Print table of cells.        
### IOp(3/112)
Huckel parameters.
* 0        Default (13).        
* 3        Hoffman parameters.        
* 4        Pykko parameters.        
* 5        Huckel initial guess parameters.        
* 00        Default (10 for Huckel, 20 for DFTB).        
* 10        Use standard parameters.        
* 20        Read parameters to override the standard ones.        
* 30        Read parameters from RWF file 738.        
* 40        Read parameters from checkpoint file 738.        
### IOp(3/113)
Generate SABF data.
* 00        Default (12).        
* 1        Generate AO basis function SABF data if symmetry is on.        
* 2        Make AO SABF data C1 regardless.        
* 10        Generate density basis function SABF data if symmetry is on.        
* 20        Make density basis SABF data C1 regardless.        
### IOp(3/114)
Factor for number of significant basis functions allocation in XC quadrature allocation.
* 0        Default: use amount computed by LdMGrd.        
* N        Scale values by N/10.        
### IOp(3/115)
Factor for number of significant atoms allocation in XC quadrature allocation.
* 0        Default: use amount computed by LdMGrd.        
* N        Scale values by N/10.        
### IOp(3/116)
Type of SCF.
* -2        Take from the checkpoint file.        
* -1        Ignore ILSW and determine on the fly.        
* 0        Take from ILSW.        
* 1        Real RHF.        
* 2        Real UHF.        
* 3        Complex RHF.        
* 4        Complex UHF.        
* 5        Complex, but use ILSW to decide whether RHF/UHF.        
* 7        GHF using real basis functions.        
* 11        Complex RHF, complex spherical harmonic basis.        
* 12        Complex UHF, complex spherical harmonic basis.        
* 15        GHF, complex spin-orbital basis (NYI).        
* 19        GHF, spinor basis (NYI).        
* 23        DF, spinor basis (NYI).        
* 101        Real ROHF.        
* 201        Unrestricted if derivatives are being done but RO single points; used for RO-compound methods.        
### IOp(3/117)
Handling spin-orbit ECPs.
* 0        Default; include them if present and doing GHF.        
* 1        Always compute SO terms.        
* 2        Never compute SO terms.        
### IOp(3/118)
Extra memory for integral evaluation.
* 0        None.        
* N        Add N words to the estimated memory requirements for direct integral evaluation, in all links.        
### IOp(3/119)
Coefficients of short/long range Hartree-Fock exchange.
* 0        Standard HF exchange.        
* MMMMMNNNNN        NNNNN /10000 short range and MMMMM/10000 long range exchange. The signs can be changed by IOp(3/130).        
### IOp(3/120)
Coefficients of short/long range DFT exchange.
* 0        Standard DFT exchange or default from functional.        
* MMMMMNNNNN        NNNNN /10000 short range and MMMMM/10000 long range. The signs can be changed by IOp(3/131).        
### IOp(3/121)
Coefficients of short/long range DFT correlation.
* 0        Standard DFT correlation or default from functional.        
* MMMMMNNNNN        NNNNN /10000 short range and MMMMM/10000 long range. The signs can be changed by IOp(3/132).        
### IOp(3/123)
Phase convention for complex orbitals.
* 0        Normal; largest coefficient set to 1.        
* 1        Largest coefficient set to i in each orbital.        
* 2        Largest coefficient set to i in first orbital, i^2 in second, etc.        
* 3        Largest coefficient set to phase 60 degrees.        
* 4        Largest coefficient set to phase 60 degrees, then 120, etc.        
### IOp(3/124)
Empirical dispersion term.
* 0        Default (same as 2).        
* 1        Add it regardless.        
* 2        Add it for the DFT functionals for which it has been defined and parameterized and for which a specific name has been defined in Link1.        
* 3        Add it for the DFT functionals for which it has been defined and parameterized.        
* 4        Do not add it regardless.        
* 10        Force dispersion type 1 (APF-D).        
* 20        Force dispersion type 2 (Grimme B97-D).        
* 30        Force dispersion type 3 (Grimme DFT-D3).        
* 40        Force dispersion type 4 (Grimme DFT-D3(BJ)).        
* 50        Force dispersion type 5 (Grimme D3, PM7 version).        
* 000        Whether to change Grimme dispersion based on functional. Defaulted based on lowest digit.        
* 100        Do the change.        
* 200        Do not do the change.        
* NNxxx        Use Grimme parameters for hybrid functional NN (see IOp(74)).        
* MMMMxxx        Use Grimme parameters for pure functional MMMM (see IOp(74)).        
* 10000000        Kill the job when atomic parameters are unavailable.        
* 20000000        Continue the calculation even if some of the atomic parameters are unavailable.        
### IOp(3/125)
Scaling of AA/BB and AB components of E(2).
* -3        0 for AB.        
* -2        0 for AA/BB.        
* -1        0 for both.        
* 0        Default (1 for both).        
* MMMMMNNNNN        MMMMM/10000 for AA/BB, NNNNN/10000 for AB.        
### IOp(3/126)
Omega for short/long range 1/r operator in E(2,AA) and E(2,BB) evaluation.
* 0        Standard 1/r operator.        
* N        Short range 1/r operator with N/10000.        
* MMMMMNNNNN        Short range 1/r operator with NNNNN/10000 and long range 1/r operator with MMMMM/10000.        
### IOp(3/127)
Omega for short/long range 1/r operator in E(2,AB) evaluation.
* 0        Standard 1/r operator.        
* MMMMMNNNNN        Short range 1/r operator with NNNNN/10000 and long range 1/r operator with MMMMM/10000.        
### IOp(3/128)
Coefficients of short/long range combination of 1/r operator in E(2,AA) and E(2,BB) evaluation.
* 0        Standard 1/r operator.        
* MMMMMNNNNN        NNNNN/10000 short range and MMMMM/10000 long range. The signs can be changed by IOp(3/133).        
### IOp(3/129)
Coefficients of short/long range combination of 1/r operator in E(2,AB) evaluation.
* 0        Standard 1/r operator.        
* MMMMMNNNNN        NNNNN/10000 short range and MMMMM/10000 long range. The signs can be changed by IOp(3/134).        
### IOp(3/130)
Coefficient of full range of HF exchange.
* -1        0 full range coefficient.        
* 0        Standard full range HF exchange.        
* NNNNN        NNNNN/10000 full range coefficient.        
* 100000        Use the negative of the short range coefficient as set by IOp(3/119).        
* 200000        Set the short range coefficient to zero.        
* 1000000        Use the negative of the long range coefficient as set by IOp(3/119).        
* 2000000        Set the long range coefficient to zero.        
* 10000000        Use the negative of the mid range coefficient as set by IOp(138).        
* 20000000        Set the mid range coefficient to zero.        
### IOp(3/131)
Coefficient of full range of DFT exchange.
* -1        0 full range coefficient.        
* 0        Standard full range DFT exchange.        
* NNNNN        NNNNN/10000 full range coefficient.        
* 100000        Use the negative of the short range coefficient as set by IOp(3/120).        
* 200000        Set the short range coefficient to zero.        
* 1000000        Use the negative of the long range coefficient as set by IOp(3/120).        
* 2000000        Set the long range coefficient to zero.        
### IOp(3/132)
Coefficient of full range of DFT correlation.
* -1        0 full range coefficient.        
* 0        Standard full range DFT correlation.        
* NNNNN        NNNNN/10000 full range coefficient.        
* 100000        Use the negative of the short range coefficient as set by IOp(3/121).        
* 200000        Set the short range coefficient to zero.        
* 1000000        Use the negative of the long range coefficient as set by IOp(3/121).        
* 2000000        Set the long range coefficient to zero.        
* 10000000        Use the negative of the mid range coefficient as set by IOp(138).        
* 20000000        Set the mid range coefficient to zero.        
### IOp(3/133)
Coefficient of full range of 1/r operator in E(2,AA) and E(2,BB) evaluation.
* -1        0 full range coefficient.        
* 0        Standard full range 1/r operator.        
* NNNNN        NNNNN/10000 full range coefficient.        
* 100000        Use the
negative of the short range coefficient as set by IOp(3/128).        
* 1000000        Use the negative of the long range coefficient as set by IOp(3/128).        
### IOp(3/134)
Coefficient of full range of 1/r operator in E(2,AB) evaluation.
* -1        0 full range coefficient.        
* 0        Standard full range 1/r operator.        
* NNNNN        NNNNN/10000 full range coefficient.        
* 100000        Use the negative of the short range coefficient as set by IOp(3/129).        
* 1000000        Use the negative of the long range coefficient as set by IOp(3/129).        
### IOp(3/135)
Setup for semi-empirical.
* 0        Default (1 for AM1/PMn full-matrix, 2 for sparse and other methods).        
* 1        New code.        
* 2        Old code.        
* Nx        Flags for AM1Par (default 2020).        
* 10        Generate standard parameters.        
* 20        Read parameters from RWF.        
* 30        Read parameters from checkpoint.        
* 40        Read parameters from checkpoint if present; otherwise generate.        
* 50        Do not produce any standard parameters.        
* 100        Read additional parameters from the input stream.        
* 200        Read additional parameters from the input stream using MOPAC format and units.        
* 300        Read additional parameters in both formats, Gaussian internal format first.        
* 1000        Save parameters on RWF.        
* 2000        Do not save parameters on RWF.        
### IOp(3/136)
Printing of semi-empirical parameters.
* 0        Default (2 or parameters read in ≤ 2 unless IPrint).        
* 1        Print parameters for elements used in this calculation.        
* 2        Do not print parameters.        
* 3        Print parameters for all elements.        
* 00        Default (10).        
* 10        Print parameters in human-readable form.        
* 20        Print parameters in input format.        
* 30        Print parameters in both formats.        
* 000        Default (100).        
* 100        Print only non-zero parameters.        
* 200        Print all parameters including zero parameters.        
### IOp(3/137)
Control of FMM for nuclear repulsion.
* 0        Default: Use for 5K or more atoms.        
* N        Use for N or more atoms.        
* -1        Always use FMM.        
* -2        Never use FMM; necessary when doing external point charges if one coincides with a (ghost) nucleus.        
### IOp(3/138)
Mid-range coefficients for split-range functionals:
* MMMMMNNNNN        NNNNN/10000 HF and MMMMM/10000 XC.        
### IOp(3/140)
Override PCM solution method.
* 0        Leave unchanged.        
* 1        Force inversion.        
* 2        Force iterative.        
* 3        Force simultaneous in L502.        
### IOp(3/141)
Override PCM FoFCou accuracy parameter.
* 0        Leave unchanged.        
* N        10^-N.        
### IOp(3/142)
Convergence for iterative PCM solution.
* 0        Default, 10^-6        
* N        10^-N.        
### IOp(3/143)
Iteration limit for PCM solution.
* 0        Default (400)        
* N        N.        
### IOp(3/144)
Threshold for discarding small surface elements.
* 0        Default (1.d-12).        
* N        10^-N.        
### IOp(3/158)
Over-ride defaults for PCM:
* 00        Normal default for model (26).        
* 1        DPCM.        
* 2        CPCM.        
* 3        Isotropic non-symmetric IEFPCM.        
* 4        Anisotropic non-symmetric IEFPCM        
* 5        Ionic non-symmetric IEFPCM        
* 6        Isotropic symmetric IEFPCM.        
* 10        Add spheres, default ofac=0.8 rmin=0.5.        
* 20        Do not add spheres.        
### IOp(3/159)
Override defaults for atomic densities:
* 00        Normal defaults.        
* NN>0        Default is NN.        
* -NN<0        Force type NN regardless of input.        
### IOp(3/160)
Operation of L316:
* 0        Default (1121).        
* 1        Print out 2e integrals.        
* 2        Do not print out 2e integrals.        
* 10        Write fortran unformatted matrix element file, using the default name ("Gau-#####.EUF", where ##### is the PID) in the scratch directory.        
* 20        Do not write matrix element file.        
* 30        Write the matrix element file, reading the file name from an input section (with terminating blank line).        
* 100        Include only active nuclei in the molecule data on the file.        
* 200        Include all centers in the molecule data on the file.        
* 1000        Use full size integers for labels of packed matrices.        
* 2000        Use Integer*4 for labels of packed matrices; ignored on machines which do not support I*4.        
* 10000        Use the same size integer labels for 4d matrices (2e integrals) as for other data.        
* 20000        Use Integer*2 labels for 4d matrices; ignored on machines which do not support 16-bit integers.        
* 100000000        Store binary data with no record marks, appropriate to reading in c/c++/perl/python.        
### IOp(3/161)
Saving/Restoring L302 results for SCF=Restart:
* 0        Default (22)        
* 1         Save the XC dimensioning and orthonormal vectors on the chk file as well as the rwf.        
* 2        Do not store on the chk file        
* 10        Restore the information from the chk file if present.        
* 20        Do not restore the information.        
### IOp(3/165)
Generate and test d/dx V = d/dx S^-1/2 for testing.
* 0        No.        
* 1        Yes.        
* Nx        Use step-size 10^-N in numerical differentiation, default 4.        
* Mxx        Use threashold 10^-M for linear dependence test, default 6.        
### IOp(3/166)
PCM point density:
* 0        Default (5 pts/A^2 for default quadrature).        
* N        N pts/A^2.        
* -N        TSAre=N, forces old quadrature.        
### IOp(3/167)
Size of core (for general basis input):
* 0        Default for internal basis sets, minimal if GBS.        
* N        N-zeta core.        
### IOp(3/168, 3/169)
Bitmap of allowed prism paths if non-zero, 0-24 in word 168, 25-49 in 169, or 168=-1/-2 for OSOnly/MDOnly
### IOp(3/172)
Damping/switching function for APF empirical dispersion.
* 0        Default (-5, see details in subroutines R6DAPF).        
### IOp(3/173)
Range for APF switching function.
* 0        Default (50).        
* NNNN        A value of NNNN/1000 of the hard cutoff.        
### IOp(3/174)
S6 scale factor in Grimme’s D2/D3/D3BJ dispersion.
* 0        Default (see subroutine R6DS6).        
* -1        Set S6 to 0.        
* NNNNNNNN        A value of NNNNNNNN/1000000.        
### IOp(3/175)
S8 scale factor in Grimme’s D2/D3/D3BJ dispersion.
* 0        Default (see subroutine R6DS8).        
* -1        Set S8 to 0.        
* NNNNNNNN        A value of NNNNNNNN/1000000.        
### IOp(3/176)
SR6 scale factor in Grimme’s D2/D3/D3BJ dispersion.
* 0        Default (see subroutine R6DSR6).        
* -1        Set SR6 to 0.        
* NNNNNNNN        A value of NNNNNNNN/1000000.        
*                 
*                 
### IOp(3/177)
A1 parameter in Becke-Johnson damping for D3BJ and XDM.
* 0        Default (see subroutine R6DABJ/XDMABJ).        
* -1        Set A1 to 0.        
* NNNNNNNN        A value of NNNNNN/1000000.        
### IOp(3/178)
A2 parameter in Becke-Johnson damping for D3BJ and XDM.
* 0        Default (see subroutine R6DABJ/XDMABJ).        
* -1        Set A2 to 0.        
* NNNNNNNN        A value of NNNNNN/1000000 Ang.        
## Overlay 4 
### IOp(4/5)
Type of guess.
* 0        Default. This uses the Harris functional except for semi-empirical, for which the modified core Hamiltonian is diagonalized.        
* -1        Skip out and leave all files as left over on the rwf from whatever was done previously.        
* 1        Read guess from the checkpoint file.        
* 2        Guessfrom model Hamiltonian, chosen via IOp(4/11).        
* 3        Huckel guess (only valid for NDDO-type methods).        
* 4        Projected ZDO guess.        
* 5        Renormalize and orthogonalize the coefficients which are on the read-write files.        
* 6        Renormalize and orthogonalize intermediate SCF results which are on the RWF.        
* 7        Read intermediate SCF results which are on the checkpoint file.        
* 8        Read the generalized density specified by IOp(4/38) from the checkpoint file and generate natural orbitals from it.        
* 9        Read the generalized density specified by IOp(4/38) from the RWF file and generate natural orbitals from it.        
* 10-14        Generated internally and correspond to 0 and 5-8 for sparse.        
* 16        Use the orthonormal set provided by L302 as MOs, avoiding any diagonalization.        
* 17        Store unit matrices for a dummy guess.        
* 18        Copy orbitals and densities that are in the chk file without checking or alteration.        
* 100        Convert Guess=Check to Guess=Restart or to generating guess depending on what if anything is on the checkpoint file.        
* 1000        Use the simultaneous optimization recipe: S^-0.5* V.        
* 00000        Default (1 for PBC without alter, otherwise 2).        
* 10000        Re-use Fock matrices instead of orbitals.        
* 20000        Re-use orbitals not Fock matrices.        
* 100000        Read the name of a checkpoint file from the input stream and read guess MOs from it, or read an option for how to generate the guess.        
Note that variable IGuess here has 4,3,2,1 corresponding to 1,2,3,4 above. IGuess values of 10-14 are generatedinternally and are the sparse versions of 0 and 5-8.
### IOp(4/6)
`L401`: Projection, orthogonalization, and checking of initial guess.
* 0        Default (1 except 3 for IOp(129)=1).        
* 1        Force projected read-in guess, even when bases are identical.        
* 2        Suppress projection.        
* 3        Project only if basis sets are different.        
* 00        Default orthogonalization (perform if Guess=Cards).        
* 10        Schmidt orthogonalize guess orbitals.        
* 20        Suppress orthogonalization.        
* 000        Default MO checking (check if Guess=Cards or Guess=Mix).        
* 100        Check MOs for othornormality.        
* 200        Don’t check MOs for othornormality.        
* 100000000         Default all 3 to on        
* 200000000         Default all 3 to off.        
### IOp(4/8)
`L401`: Alteration of configuration.
* 0        Default (3).        
* 1        Read in pairs of integers in free format indicating which pairs of MO’s are to be interchanged.  Pairs are read until a blank card is encountered.        
* 2        Read in a permutation of the orbitals.        
* 3        Do not alter configuration.        
* 10        Read alteration information from the read-write file.        
* 100        Use alpha orbitals for guess for both alpha and beta.        
* 1000        Biorthogonalize UHF MOs.        
Note: If the configuration is altered on an open shell system, two sets of data as described above will be expected, first for alpha, second for beta.
### IOp(4/9)
`L401`:  SCF symmetry control.
* 0        Default, same as 104 except 4 for IGuess=16, and 204 if C1 symmetry.        
* 1        Read groups of irreducible representations to combine in the SCF. These are read before any orbitals and before
alteration commands.        
* 2        Use no symmetry in the SCF.        
* 3        Pick up the symmetry mixing information from the alteration read-write file.        
* 4        Use the full Abelian point group, as represented by the symmetry adapted basis functions produced by link 301. Initial guess orbital symmetries are assigned.        
* 5        (Use symmetry in SCF if possible, but do not assign initial guess Abelian symmetries).        
* 10        Localize all occupied orbitals together and all virtual orbitals together.        
* 20        Localize the orbitals within the selected or defaulted symmetry.        
* 30        Localize all occupied and virtual orbitals together.        
* 40        Do not localize.        
* 100        Assign orbital symmetries for printing in full symmetry.        
* 200        Do not assign orbital symmetries in full symmetry.        
* 1000        Force the guess orbitals to have the Abelian symmetry.        
* NN0000        Use localization method NN-1 (see LocMO).        
This option can cause the symmetry adapted basis function common blocks to be modified.
### IOp(4/11)
`L401`:  Type of Guess.
For iterative ZDO Guess:
* -1        Force old path using old Huckel.        
* 0        Best available (8,4 in order of preference).        
* 1        Old Huckel.        
* 2        CNDO.        
* 3        INDO.        
* 4        New Huckel.        
* 5        Iterative extended Huckel.        
* 6        Harris, converted to IGuess=3 and IZDO=3 here.        
* 7        Harris with interpolated QEq atomic charges, converted to IGuess=3 IZDO=5 here.        
* 8        Harris with new densities.        
* 9        Iterated Harris with QEq guess, converted to IGuess=3 IZDO=7.        
* 10        Unused.        
* 11        NYI? Harris using charges from previous SCF, converted to IGuess=3 IZDO=9.        
For unprojected single diagonalization guess:
* 0        Default(1 for DFTB, 2 for AM1/PM6, 3 for ).        
* 1        Use bare core matrix.        
* 2        Dress core Hamiltonian with QEq-based density.        
* 3        Use Harris Functional with old densities.        
* 4        Neutral atom AM1/PMx guess.        
* 5        Harris functional with interpolated QEq charges.        
* 6        Harris functional with iterated charges.        
* 7        Harris functional with iterated charges starting from QEq.        
* 8        Use Harris Functional with new densities.        
* 9        Harris using charges from previous SCF        
* 000        Default, same as 2.        
* 100        Use at least SG1 in Harris guess.        
* 200        Use at least FineGrid in Harris guess.        
* 300        Use at least UltraFine in Harris guess.        
* 400        Use an unpruned (199,590) or (399,590) grid depending on the range of primitive exponents..        
* 500        Use(399,974) and 10^-12 in Harris functional.        
* 1000        Save energy in Gen(43) for Harris functional.        
* MMMM00000        Use functional MMMM.        
### IOp(4/13)
`L401`: Mixing of orbitals.
* -2        No mixing.        
* -1        Mix HOMO and LUMO (skipping beta high-spin orbitals for GHF).        
* 0        Default: Mix HOMO and LUMO to make complex guess for CRHF and CUHF if generating RUHF guess, otherwise do nothing.        
* >0        Bits request actions as follows:        
*             0: Mix HOMO and LUMO (skipping beta high-spin virtuals for GHF), done after complex/spin mixings.        
*             1: Do complex mixing, changing spin direction for GHF.        
*             2: Use real rather than imaginary coefficients.        
*             3: Flip sign of complex mixing.        
*             4: Read in a spin-vector and rotate to align spins in this direction instead of Z. GHF only.        
*             5: Read in two spin-vectors and use them for alternate orbitals.        
*             6: Reverse rotation direction applied to spin.        
*          Note that this will usually destroy both spatial and alpha/beta symmetry. The mixing is done after any alterations. Bits 1-3 are only relevant for complex wfns.        
### IOp(4/14)
`L401`: Reading of specific orbitals.
* 0        No.        
* 1        Yes. For alpha orbitals, read one card with the format for the orbitals, followed by zero or more sets of IVec (I5): vector to replace. If IVec is -1, all NBasis vectors follow.(Vector(I), I=1, NBasis): vector in the specified format. Input is terminated by IVec=0. For b orbitals, the same format as for a is used. Note that if Alter is also specified, the replacements are read before the corr. alterations (thus the order is a orbitals, a alterations, b orbitals, b alterations).        
* 2        Yes. Read using the format described in Routine RdMO2. Here a range of MOs is indicated by two integers followed by an integer giving the number of basis functions. Then a list of MO energies are given. Lastly, the MO coefficients are read in sequence. All of the reading is carried out in free format.        
* 10        Orbitals are assumed to have mixed normalization for Cartesian d and higher functions (equivalent to having AdjMO applied to them).        
* 100        Reorder d and f coefficients from the order used in NWChem (as of January, 2013) to the conventional order used in Gaussian.        
* 900        Read permutation arrays for p and higher functions for use in reordering read-in MO coefficients. (NYI)        
### IOp(4/15)
`L401`: Spin-state for initial guess.
* 0        Use multiplicity in /Mol/.        
* N        Use multiplicity N. Useful for generating guesses for open-shell singlets or unusual spin states involving orthogonal orbs by treating them as high-spin in the guess (which only does UHF).        
### IOp(4/16)
`L401`: Whether to translate basis functions of read in guess.
* 0        Default (same as 3).        
* 1        Use the basis functions as is.        
* 2        Translate to the current atomic coordinates.        
* 3        Translate to the current atomic coordinates, and determine an overall rotation to provide to the read-in orbitals.        
### IOp(4/17)
`L402`:  Number of open-shell orbitals (not electrons).
* 0        Number of open electrons.        
* N        N.        
`L405`: Number of electrons in the CAS space.
### IOp(4/18)
`L402`: Number of orbitals in CI. Default is number of open shells.
Number of orbitals in the CAS space.
### IOp(4/19)
`L402`: Spin change in CI (default based on multiplicity).
`L405`: Truncation level for excitations — default full CAS.
### IOp(4/20)
`L402`: Type of model. (This is also tested in L401 to see whether atomic numbers greater than 102 are special flags).
* 0        Default (AM1).        
* 1        CNDO.        
* 2        INDO.        
* 3        MINDO/3.        
* 4        MNDO.        
* 5        AM1.        
* 6        Unused.        
* 7        PM3.        
* 8        PM3 with mechanics correction.        
* 9        Dreiding mechanics.        
* 10        UFF mechanics.        
* 11        AMBER mechanics.        
* 12        MM2 mechanics.        
* 13        MM3 mechanics.        
* 14        Extended Huckel, Hoffmann parameters.        
* 15        Extended Huckel, Muller parameters.        
* 16        Extended Huckel, Initial guess parameters.        
* 17        External program.        
* 18        MMFF.        
* 19        QFF.        
### IOp(4/21)
`L402`: SCF type.
* 0        Default (no Pulay, no Camp-King, 3/4 point on unless Pulay or Camp-King, use pseudo-diagonalization).        
* 1        3/4.        
* 2        No 3/4.        
* 10        No Pulay (DIIS).        
* 20        Pulay.        
* 100        No Camp-King.        
* 200        Camp-King.        
* 1000        Use pseudo-diagonalization.        
* 2000        No pseudo-diagonalization.        
`L405`: Flags for MCSCF.
* 1        Read options from input stream.        
* 10        Use Slater determinants.        
* 100        Just list configurations.        
* 1000        Use determinant basis with Sz=b/2.        
* 10000        Write unformatted file (NDATA) of symbolic matrix elements.        
* 100000        Write formatted file of symbolic matrix elements.        
### IOp(4/22)
`L402`: Derivatives to do:
* 0        None.        
* 1        1st derivatives.        
* 2        2nd derivatives.        
* 12        Restart 2nd derivatives.        
* 100        Do 1st derivatives analytically if possible.        
### IOp(4/23)
`L402`: Number of iterations.
* 0        Default.        
* N        N.        
`L405`: NDiag.
### IOp(4/24)
`L402`: Whether to update orbitals, eigenvalues, /Mol/, and ILSW on the RWF.
* 0        Default (don’t update).        
* 1        Update, multiplying by S^-1/2.        
* 2        Don’t update. (For Opt=MNDOFC).        
* 3        Update, but don’t convert from Lowdin orbitals.        
* 10        Update second force array instead of first. (For Opt=MNDOFC).        
`L405`: NRow.
### IOp(4/25)
`L402`: Wavefunction.
* 0        Default (Same as 1).        
* 1        Single determinant, RHF/UHF from IOp(4/5).        
* 2        ROHF (NYI).        
* 3        Bi-radical 1/2 CI (only for MINDO3, MNDO, AM1).        
* 4        Closed-shell 1/3 CI (only for MINDO3, MNDO, AM1).        
* 5        General CI, using specified orbitals.        
* -N        General CI, with N microstates read in.        
`L405`: 10 binary switches.
### IOp(4/26)
Whether to mix orbitals in generated guess density.
* 0        No.        
* -3        Yes, mix valence occupieds with 0.05 au (according to ZDO) of the HOMO and virtuals within 0.15 au.        
* -2        Yes, mix valence orbitals and an equal number of virtuals.        
* -1        Yes, mix all equally.        
* N              Equal occupations of the lowest N virtuals and high N occupieds.        
### IOp(4/28)
`L402`: SCF Convergence (10^-N, default 10^-7).
### IOp(4/29)
`L405`: Number of core orbitals.
### IOp(4/33)
Printing of guess.
* 0        No printing.        
* 1        Print the MO coefficients.        
* 2        Print everything.        
### IOp(4/34)
Dump option.
* 0        No dump.        
* 1        Turn on all possible printing.        
### IOp(4/35)
Overlap matrix.
* 0        Default (copy on disk is used).        
* 1        Overlap assumed to be unity.        
* 2        Copy on disk is used.        
### IOp(4/36)
ZIndo reformatting.
* 0        No.        
* 1              Yes, reformat ZIndo integrals and wavefunction into RWF.        
### IOp(4/37)
`L402`: Selection of old MNDO parameters.
* 0        Defaults.        
* 1        Old Si parameters.        
* 2        Old S parameters.        
### IOp(4/38)
Generalized density to use for natural orbitals.
* 0        Default (-1, current for method on chk).        
* N        Density number N.        
### IOp(4/39)
Angle for mixing during Guess=Mix.
* 0        Default (Pi/4).        
* N        Pi/N.        
### IOp(4/43)
`L402`: Handling of background charge distribution. 
* 00        Same as 21 for MM, 22 for everything else.        
* 1              Consider external charges.        
* 2        Do not consider external charges.        
* 10        Consider self-consistent solvent charges.        
* 20        Do not consider self-consistent solvent charges.        
* `L405`: = IDiEij: = switch for direct matrix element calculation.        
* 0        For normal route, with all matrix elements calculated here and stored on disk. Configs printed as normal.        
* 1        For direct route. Eij’s calculated here and stored on disk. A flag is automatically sent to L510 to tell it to compute the remaining matrix elements directly.This type of computation can only be done in a CAS comp. Also L510 must use Lanczos.        
* 2        Like option 1, but all configurations are printed. This will be the only way to print configs in a direct matrix element calc, since there can be many thousands in a large CAS.        
### IOp(4/44)
`L405`: Prepare input for CAS-MPZ when set to 1.
### IOp(4/45)
Ipairs= number of GVB pairs in GVBCAS.
* 0              Default. No pairs, normal CAS calculation.        
* N        There are N pairs: 2*n extra orbitals and electrons will be added into the active space later. L405 performs a CAS on the inner space, and sets up L510 to compute extra matrix elements etc. implicitly. This is a normal GVBCAS calculation.        
* -N        There are N pairs: 2*n orbitals and electrons of the specified CAS are to be considered to be GVB type orbitals when generating configs/matrix elements. L510 will execute normally. This occupies as such space as a full CAS in this link, but is smaller subsequently. This is the GVBCAS test mode.        
### IOp(4/46)
CI basis in CASSCF.
* 1        Hartree-Waller functions for singlets.        
* 2        Hartree-Waller functions for triplets.        
* 3        Slater determinants.        
* 10        Write SME on disk.        
### IOp(4/47)
Convert to sparse storage after generating guess.
* -3        Save sparse storage Fock matrix for guess.        
* -2        Save full storage Fock matrix for guess.        
* -1        No, use the Lewis dot structure to generate a sparse guess directly.        
* 0              Default (-1 if sparse is turned on).        
* 1        Yes.        
### IOp(4/48)
`L402`: Whether to do (sparse) conjugate gradient methods.
* 0        No.        
* 1        Yes. Use Lewis dot structure guess density.        
* 2        Yes. Use diagonal guess density.        
### IOp(4/60)
Override standard values of IRadAn.
### IOp(4/61)
Override standard values of IRanWt.
### IOp(4/62)
Override standard values of IRanGd.
### IOp(4/63)
Flags for which terms to include in MM energy.
* 0        Default (111111).        
* 1        Turn on all terms, r^-1 Coulomb.        
* 2        Turn on all terms, r^-2 Coulomb.        
* 10        Turn on non-bonded terms.        
* 100        Turn on inversions/improper torsions.        
* 1000        Turn on torsions.        
* 10000        Turn on angle bending.        
* 100000        Turn on bond stretches.        
### IOp(4/65)
Tighten the zero thresholds as the SCF calculation proceeds.
* 0        Default: Yes, initial threshold 5×10-5.        
* 1        No variable thresholds.        
* N        Yes, initial threshold 10^-N.        
* N<-100        Yes, initial threshold 5 x 10 ^N+100.        
### IOp(4/66)
Dielectric constant to be used in MM calculations.
* 0        Eps = 1.0.        
* N        Eps = N / 1000.        
### IOp(4/67)
Whether to use QEq to assign MM charges.
* 0        Default (211 if UFF, 2 otherwise, 1⇒ 221).        
* 1        Do QEq.        
* 2        Don’t do QEq.        
* 00        Default (20).        
* 10        Do for atoms which were not explicitly typed.        
* 20        Do for all atoms regardless of typing.        
* 000        Default (200).        
* 100        Do for atoms which have charge specified or defaulted to 0.        
* 200        Do for all atoms regardless of initial charge.        
### IOp(4/68)
`L402`: Convergencecriterion for micro-iterations.
* 0        Default.        
* N        10^-N.        
### IOp(4/69)
Whether to do a new additional guess in addition to reading orbitals from the RWF.
* 0        Default (2).        
* 1        Yes if no Guess=Alter, Harris guess, and not a small geometry step.        
* 2        Do not do the extra guess.        
* 3        Do the extra guess and store as the initial Fock matrix.        
* 4        Do the extra guess regardless.        
* 5        Store the normal guess as the alternative (for SimOpt).        
* 00        Default (10 for PBC, 20 otherwise).        
* 10        Save the Harris guess as an initial Fock matrix.        
* 20        Just generate orbitals from the Harris guess.        
### IOp(4/71)
`L402`: Write out AM1 integrals.
* 0        No        
* 1        Yes        
### IOp(4/72)
Irreps to keep in MCSCF CI-wavefunction.
* 0        All        
* IJKLMNOP        List of up to 8 irreducible representation numbers to include.        
### IOp(4/80)
The maximum conjugate gradient step size (MMNN).
* 0000        No maximum step size.        
* MMNN        Step size of MM.NN.        
### IOp(4/81)
Sparse SCF Parameters.
* MM        Maximum number of SCF DIIS cycles. (MM=00 defaults to 20 cycles, MM=01 turns DIIS off).        
* NN00        F(Mu,Nu) atom–atom cutoff criterion (angstroms) Mu, Nu are basis functions on the same atom.(defaults to no F(Mu,Nu) cutoff).        
* PP0000        F(Mu,Lambda) atom–atom cutoff criterion (angstroms) Mu, Lambda are basis functions on different atoms. (defaults to 15 angstroms).        
### IOp(4/82)
Conjugate-Gradient Parameters.
* MM        Maximum number of CG cycles per SCF iteration. (defaults to 4 CG cycles).        
* NN00        Maximum number of purification cycles per CG iteration. (defaults to 3 cycles).        
* 00000        Don’t use CG DIIS.        
* 10000        Use CG DIIS.        
* 000000        Polak-Ribiere CG minimization.        
* 100000        Fletcher-Reeves CG minimization.        
* 0000000        Use diagonal preconditioning in Conjugate-Gradient.        
* 1000000        No preconditioning.        
### IOp(4/90)
`L402`: Step size in dynamics (see IOp(4/8) in L118).
* 0        Default (0.025 femtosec).        
* N        N*0.0001 femtosec.        
### IOp(4/91)
`L402`: Trajectory type and initial velocity (see IOp(4/9) in L118).
* 0        Default (same as 4).        
* 3        Read in initial Cartesian velocity.        
* 4        Read in initial mass weighted Cartesian velocity.        
### IOp(4/92)
`L402`: Maximum points in one trajectory (see IOp(4/42) in L118).
* 0        Default (100).        
* N        N points in trajectory.        
### IOp(4/93)
`L402`: Read isotopes for trajectory (see IOp(4/45) in L118).
* 0        Do not read isotopes.        
* 1        Read isotopes.        
### IOp(4/110)
`L402`: Scaling of rigid fragment steps during micro-iterations.
* 1        Scale by (# fragatoms)^-1.        
* 2        Scale by 1/SQRT (# fragatoms).        
* N        Scale by N/1000.        
### IOp(4/111)
* 0        Default (2).        
### IOp(4/112)
Compression for ONIOM.
* 4        Compressed Hessian over active atoms. For MM calculations on the real system, this converts a second derivative calculation to just forces, since the real system 2nd derivatives are computed during micro-iterations.        
* N≥4        Full storage. (default)        
### IOp(4/113)
`L402`: Which external method to use for ONIOM calculations using different external commands for 2 or more levels.
* 0        Default (First external command).        
* N        N^thexternal command (command N in file 747).        
### IOp(4/114)
Which ONIOM system is being done, which is sometimes needed by external procedures.
* 0        Default (1).        
* 1        Real system.        
* 2        Model system for 2-layer, middle for 3-layer.        
* 3        Small model system for 3-layer.        
### IOp(4/115)
Mixing of orbitals for GHF/Complex testing.
* 0        Default (No, unless generate guess for complex).        
* 1        Make MO coefficients complex.        
* 2        Don’t rotate real and imaginary components of MOs.        
* 10        Mix alpha and beta orbitals for GHF.        
* 100        Read in S vector to apply to FC perturbation.        
* 200        Read in complex-style SR, SI for GHF.        
* 0000        Default FC perturbation (1).        
* 1000        FC with MBS core orbitals blanked.        
* 2000        Full FC.        
### IOp(4/116)
Functional to use in Harris guess.
* 0        Default: PBEPBE for HSE2PBE, HSE(H)1PBE and any functional involving the kinetic energy or Laplacian, the pure version of the functional for pure and hybrid GGAs, and SVWN3 for HF.        
* N        Functional # (see values in 3/74).        
### IOp(4/117)
Set flag for BD Guess=Read.
* 0        No.        
* -1        Yes.        
### IOp(4/118)
Whether to do GHF/Complex diagonalization for Harris and Core guesses.
* 0        Default (1).        
* 1        Yes.        
* 2        No, generate UHF guess and convert.        
### IOp(4/119)
Printing MM energy contributions and force field parameters.
* 0        Default (print contributions if #p).        
* 1        Print contributions.        
* 2        Don’t print contributions.        
* 00                Default (20).        
* 10        Print all terms in the force field.        
* 20        Don’t print the force field.        
### IOp(4/120)
`L402`: Number of MM microiterations allowed.
* 0        Default, based on  Atoms but at least 5000.        
* 0        N.        
### IOp(4/121)
Convergence of iterative Harris guess.
* 0        Default (0.02).        
* N>0        N/10000.        
* N<0        10^N.        
### IOp(4/122)
Maximum number of iterations for iterated Harris:
* 0        Default, 20.        
### IOp(4/123)
Control of generation QEq charges in Harris guess. See description ICntrl in GenChg.
### IOp(4/124)
`L402`: File options for External.
### IOp(4/125)
`L402`: Options for unformatted i/o file.
### IOp(4/126)
`L402`: IDefCm for External.
### IOp(4/127)
Whether to print atomic spin vectors, etc.
* 0        Default (2).        
* 1        Yes.        
* 2        No.        
### IOp(4/128)
Whether to print analysis of projection for read-in guesses:
* 0        Default (122 if using symmetry in diagonalization, 222 otherwise).        
* 1        Yes.        
* 2        No.        
* 10        Symmetrically orthogonalize core and valence occupieds together.        
* 20        Symmetrically orthogonalize core and valence occupieds separately.        
* 100        Always project virtuals.        
* 200        Only project virtuals for CAS.        
### IOp(4/129)
Whether to read energy from chk during Guess=Read (i.e., with SCF=Skip):
* 0        Default(No).        
* 1        Yes.        
### IOp(4/130)
Store dispersion energy and derivatives as total?
* 0        Default (No).        
* 1        Yes.        
### IOp(4/131)
`L402`: Whether to include charges in MM calculations in.
* 0        Default (check ILSW for whether ONIOM or QM/MM-style).        
* 1        ONIOM-style, so include.        
* 2        Do not include.        
### IOp(4/132)
Copy MOs from chk file to reference phase file on rwf. Reference CIS/TD amplitudes are also copied, if found on the chk file.
* 0        Default(No).        
* 1        Copy.        
* 10        Flip sign of MOs.        
* 20        Flip sign of amplitudes.        
* 30        Flip sign of both MOs and amplitudes.        
## Overlay 5 
### IOp(5/5)
`L502, L508`: Direct SCF control.
* 0        Default (same as 1).        
* 1        Read the integrals off disk.        
* 2        Compute 2e integrals.        
* 3        Compute 2e integrals and store in-core.        
* 4        Compute 2e integrals and forbid in-core.        
* NNNNx        Use option NNNNN in control of 2e integral calculation.        
* 000000        Default — incremental Fock matrix formation only for direct SCF.        
* 100000        Form full Fock matrix every time.        
* 200000        Form delta-F each iteration.        
* 1000000        Clear in-core integrals for testing.        
### IOp(5/6)
Convergence (RMS density except in L506 (SQCDF), L508 (rms rotation gradient), and L510 (Energy)).
* 0        10^-8, except 10^-7 for PBC, and 10^-10 for SQCDF.        
* N        10^-N.        
### IOp(5/7)
Maximum number of iterations.
* 0        128 (except 512 in L503 and L508, and 64 in L506).        
* -1        Do CI only in L510.        
* -2        Do CI and density matrices only in L510.        
* -3        Do a single iteration in L510.        
### IOp(5/8)
`L503`: Selection of the procedure of direct minimizations.
* 0        Steepest descent with search parameters default.        
* 1        Steepest descent with search parameters read (see below).        
* 2        Classical SCF (Roothaan’s method of repeated diagonalization).        
* 4        Conjugate gradients with search parameters default.        
* 5        Conjugate gradients with search parameters read (see below).        
*          The search parameters are max. number of search points (I1).        
*          Min. number of search points (I1).        
*          Initial step size, TAU (G18.5).        
*          Scaling factor for subseq. TAU (G20.5)        
*          Q (G20.5)        
`L508`: Search method.
* 0        Default (1123).        
* 1        Steepest descent.        
* 2        Scaled steepest descent.        
* 3        Quadratic convergence (after rotation gradient is sufficiently small).        
* 4        Exit when NR point is reached, so L502 can take over.        
* 00        Default linear search (full search).        
* 10        Do a full linear search to locate a minimum.        
* 20        Do a linear search only if the energy goes up after the initial step.        
* 000        Default handling of wrong curvature (switch direction).        
* 100        Reverse direction if curvature in NR step direction is wrong.        
* 200        Take pure NR steps, even if curvature is wrong.        
* 1000        Turn on linear search and variable step logic.        
* 2000         Turn off linear search and variable step logic.        
`L510`: Flags used.
* 1        IRdF2, read damping coefficients.        
* 10        IFrzCI, freeze CI coefficients after 1st iteration.        
* 100        Read unformatted symbolic matrix elements from NDATA instead of RWF.        
* 1000        Read in damping factors from cards.        
* 10000        Use Levy damping.        
* 100000        Read Fock matrix restriction matrix.        
### IOp(5/9)
`L503 only`: Switch to classical SCF after density matrix has achieved a certain convergency.
* 0        No.        
* 1        Yes, criterion default 10^-3.        
* 2        Yes, criterion read in (Format G16.10).        
`L504, L506`: Number of pair iterations.
* -1        None; coefficients are frozen at initial values (L504 only, causes coefficients to be read in order 11 12 22).        
* 0        5.        
`L511`: IDoV in Harris functional.
### IOp(5/10)
Error: label name not recognized
### IOp(5/11)
`L502, L503 (only 4 point), L505`:  3 and 4 Point Density extrapolation control.
* 0        Both three-point and four-point extrapolation are performed when applicable.        
* 1        Three-point extrapolation is inhibited, but the program will still perform four-point extrapolation when possible.        
* 2        Both three-point and four-point extrapolation schemes are ‘locked out’ (IE. disabled).        
* 00         Default (20).        
* 10         Do Camp-King always, taking one step using if |Lpred-1| ³ Thresh.        
* 20         Do not do Camp-King.        
* 30         Do Camp-King only if the energy rises by at least Thresh.        
* 40         Same as 1, but CK also done if the energy goes up.        
* NNN00         Threshold for CK is NNN/1000 (step for 10, Hartrees for 30). Default is 0.3 for 10,0.001 for 30; with 30,999 implies 10^-10.        
### IOp(5/12)
Whether to allocate only two N^2 arrays for RHF.
* 0        Default (No).        
* 1        Yes.        
* 2        No.        
Number of GVB pairs (L506). If non-zero, the number of orbitals in each pair is read in format (30I2). Each pair consists of the highest available occupied from the guess (after high spin orbs are accounted for) and the lowest available virtuals. If <0, pair coefficients are read; otherwise standard initial values are used.
### IOp(5/13)
`L502`:  Action on convergence failure.
* 0        Default (2).        
* 1        Continue the run even on non-convergence. The ILSW flag for convergence failure is set.        
* 2        Terminate on non-convergence.        
### IOp(5/14)
`L502`:  Special functions.
* 0        None.        
* 1        Turn the current RHF run into a uhf run at the end of this link.        
* 10        Terminate after computing the 2e terms at the first iteration.        
* 20        Just recompute band structure from stored real-space Fock matrix.        
* 100        ADMP/FOSimult, later cycles:  transform the density from L103/L121 before calculating the energy and Fock matrices.        
* 200        ADMP/FOSimult, first cycle:  use initial AO densities.        
* 1000        Use Generalized energy-weighted density routines regardless.        
* 2000        Do not use GEW routines even for CP.        
* 10000        Fit the converged density even if fitting is not in use during the SCF. Also redoes the fit at the end even if using fits during SCF.        
* 0        Calculation is performed (provided of course that enough space exists in the RW-files).        
* 1        Calculation is bypassed.        
* 2        Calculation is performed, contingent on space, and the system RW-files for the appropriate density matrices are updated (useful if one wants a population analysis).        
`L503`: Reordering of the orbitals (maintaining continuity of the wavefunction along the search path).
* 0        On. Bessel criterion.        
* 1        On. Stronger individual-overlap criterion.        
* 2        Off.        
Flags for MCSCF.
* 1        Skip valence-valence Fock matrix elements.        
* 10        Skip core-valence Fock matrix elements.        
* 100        Skip valence-virtual Fock matrix elements.        
* 1000        Skip core-valence Fock matrix elements.        
* 10000        Use full diagonalization method rather than Lanczos. (Obsolete; use IOp(5/17)).        
* 100000        State average density matrices.        
### IOp(5/15)
Apply Abelian symmetry constraints on orbitals.
* 0        Default (1 for L502, 2 for L501 and L506).        
* 1        No.        
* 2        Yes, keep occupation of each irreducible representation the same as the initial guess.        
* 3        Yes, keep overall wavefunction the same as the initial guess, but doing the minimal amount of orbital switching to accomplish this.        
* 00        Default (use Abelian symmetry in diagonalization).        
* 10        Use Abelian symmetry in diagonalization.        
* 20        Do not use Abelian symmetry in diagonalization.        
`L503`: Controls the auto adjustment of TAU.
* 0        Done.        
* 1        TAU is kept fixed.        
### IOp(5/16)
`L502`: Diagonalization method.
* 0        Default (1 for full matrices HF/DFT, -30 for semi-empirical, 4 for sparse).        
* -N        Pseudo-diagonalization with real diagonalization every N^th cycle.        
* -1        Same as 3.        
* 1        DiagD.        
* 2        KyDiag.        
* 3        Pseudo-diagonalization whenever allowed by internal tests.        
* 4        CGDMS.        
* 5        PDM.        
* 6        CEM.        
* 7        Sign Matrix Method.        
* 8        SNRDMS.        
* 9        Unused.        
* 10        Jacobi diagonalization.        
* 1xx        Force formation of the Fock matrix using full storage.        
* 2xx        Force formation of the Fock matrix using sparse storage.        
* 0        No.        
* 1        Yes.        
* 0        By eigenvalue.        
* 1        By energy least change.        
* 2        By orbital least change.        
* -1        Read in eigenvector.        
* 0        C(1)= 1.0        
* N        C(N)= 1.0        
### IOp(5/17)
`L503`: Condition off-diagonal terms of the Fock matrix.
Set to zero if Abs(F(I,J)).LE.FUZZY; delete coupling terms between almost degenerate (DELTA E .LE. DEGEN) M.O. vectors.
* 0        FUZZY=1.D-10, DEGEN=2.D-5.        
* 1        FUZZY and DEGEN read in (2D20.14).        
`L506`: Selection of virtual orbitals.
* 0        Virtuals obtained by diagonalization of Hamiltonians.        
* 1        Virtuals obtained by Schmidt orthogonalization to occupieds.        
`L502, L508`: Use of symmetry.
* 0        Default (1032 for 502, 1012 for 508).        
* 1        Choose LinEq convergence based on orbital gradient.        
* 2        Always use tight convergence.        
* 3        Tighten convergence by an extra factor of 10.        
* 10        If 2E symmetry is on, symmetrize Fock matrices and require proper density matrix symmetry.        
* 20        If 2E symmetry is on, replicate integrals so that density matrices and wavefunctions need not be symmetric.        
* 30        If 2E symmetry is on, choose between replicating integrals and symmetrizing the Fock matrix based on whether the current density matrix is symmetric.        
* 40        Same as 30 in 502 but 20 in 508.        
* 100        Force the density matrix to have full symmetry at the first iteration.        
* 200        Force the density matrix to have full symmetry at every iteration.        
* 0000        Default (1000).        
* 1000        If the density matrices pass the symmetry test, symmetrize them to ensure that they are exactly symmetric.        
* 2000        Do not symmetrize the density matrices.        
* 00000        Default (20000, except if IOp(8) requests old algorithm).        
* 10000        Always pseudocanonicalize in L508.        
* 20000        Only pseudocanonicalize in L508 when doing a Newton-Raphson step.        
`L510`: MCSCF flags.
* 0        Orthogonalize C,O,V by separate Lowdin, then schmidt.        
* 1        Lowdin orthogonalize C+O and V, then schmidt.        
* 2        Just schmidt.        
* 10        Don’t use natural orbitals each iteration. Bad for 1^st order method.        
* 100        Use full 2nd order convergence.        
* 200        2nd order iteration at end, in preparation for CPMCSCF.        
* 1000        Generate data for multi-reference MP2?        
* 10000        Attempt to control root flipping in CI.        
* 100000        Read CI vector and use it every iteration.        
* 1000000        Use full diagonalization method rather than Lanczos.        
* 10000000        Use State Average density matrices (the weights 8F10.8)        
* 20000000        Do SA and prepare for SA-CPMCSCF.        
* 30000000        Do SA and prepare for Gradient of Energy difference.        
* 40000000        Do SA and prepare for SA Second Derivative Computation (terms involving 2nd order orbital rotation derivatives not included).        
### IOp(5/18)
`L502`: Mixing when doing damping.
* -3        MO damping at all iterations.        
* -2        Turn off damping.        
* -1        Dynamic selection of density damping based on band gap and DIIS error.        
* 0        Default (-1 unless re-optimizing during Stable=Opt).        
* N        N/100 new density, (100-N)/100 old density.        
`L503`: Cutoff criteria in symmetry determination of M.O.S (L503). Symmetry is determined if largest off-diagonal M.O. Fock-matrix element Abs(F(I,J))>STHRS elements Abs(F(I,J))<SPAN are considered to be 0.
* 0        STHRS=1.D-4,
SPAN=5.D-7.        
* 1        STHRS
and SPAN read in (2D20.14).        
`L506`:  Damping.
### IOp(5/19)
`L501, L502, L506, L508`: Override integral storage control.
* -1        Choose the best given amount of memory available.        
* 0        2 if possible, otherwise 1.        
* 1        Forbid in-core:  force re-reading of integrals even if they fit in 2 buffers if conventional, do not convert to in-core if direct and enough memory for in-core is available.        
* 2        Force allocation for 1 or 2 buffer case conventional case (VV¹IBuf2E).        
* 3        Force Lower-triangular in-memory storage.        
* 4        Obsolete.        
* 1x        Save generated integrals on disk (file 610).        
* 2x        Force computation of raff 1 and 2 integrals even for RHF.        
* 3x        Do not save integrals (same as 0x).        
*         
`L503`: Print F(1),T. (Read one card with start, end 2I2).
* 0        No.        
* 1        Yes.        
### IOp(5/20)
`L501, L502, L504`: Final non-DIIS iteration.
* 0        Default (only if doing pseudo-diagonalization or QNDMS).        
* 1        Yes, do a final unextrapolated diagonalization after convergence is reached.        
* 2        No, just quit when extrapolated convergence is reached.        
* 3        Do a full diagonalization at the end without recomputing a new Fock matrix.        
`L506`: Orbital rotation control.
* 0        On all the time.        
* N        Rotations are turned on when SQCDF is below 10^-N.        
### IOp(5/21)
DIIS error for density damping, maximum virtual mixing for MO damping.
For density damping.
* 0        Default (Damp if error > 0.001).        
* N        Damp if error > 10^-N.        
For MO damping:
* 0        Default, no more than 1/3 virtual component for any occupied at each iteration.        
* N        Maximum N/1000 virtual component.        
`L503`: Action if OTEST detects problems.
* 0        Abort run via LNK1E.        
* 1        Continue run.        
* 2        Check orthonormality at first iteration.        
`L506`: Extrapolation control.
MCSCFp flags.
* 2        Generate MOs using UHF natural orbitals.        
* 10        IRdNLp.        
### IOp(5/22)
`L501, L502, L504`: Use of DIIS extrapolation.
* 0        Default (1042) for calculations using diagonalization (2) for calculations using sparse diagonalization replacements.        
* 1        No.        
* 2        Yes.        
* 3        Yes, with Fermi broadening as well, deciding on the fly between the two forms.        
* 4        Yes, with "pFON" version of Fermi broadening.        
* 5        Yes, with "FON" version of Fermi broadening.        
* 10        Regular DIIS.        
* 20        Energy-based mixing.        
* 30        Energy DIIS when DIIS error has increased significantly or is above threshold.        
* 40        Energy DIIS when DIIS error has increased significantly, otherwise, mixture of energy and commutator.        
* 1xx        Use energy DIIS when commutator gives huge coefficients.        
* Nxxx        Switch from energy to commutator when error is 10^-N in method 3; use (DIIS error/10^-N) for weight of energy DIIS in method 4.        
* Mxxxx        Use print level M in DIIS.        
`L506`: Orbital mixing control.
### IOp(5/23)
`L506, L509`: Flag for later points of an optimization, so that pair and Hamiltonian information can be reused.
* 0        Read from input stream.        
* 1        Read from RWF.        
* 2        Read from checkpoint.        
### IOp(5/24)
`L506`: Orbital freezing.
* 0        Optimize all orbitals.        
* 1        Freeze all closed, high spin and first natural orbitals. Optimize only 2nd and higher naturals.        
### IOp(5/25)
`L506`: Rotation application.
* 0        Default (exponentiate rotation angles).        
* 1        Apply rotations sequentially.        
### IOp(5/26)
Number of Hamiltonians to read in (L506). If zero, the unpaired orbitals are assumed to be high spin. If -1, an open-shell singlet is assumed.
### IOp(5/28)
Root of CI to use in MCSCF.xxx
* 0        Defaults to 1.        
* N        Use N^th root.        
### IOp(5/29)
Use of Raffenetti integrals during direct SCF.
* -1        All integrals done as Raffenetti.        
* 0        Default: let FoFJK decide. It will never use Raffenetti for SCF.        
* 1        All integrals are done as regular integrals.        
* N        Integrals with degree of contraction greater than or equal to N are done at regular integrals.        
### IOp(5/30)
`L502, L505, (not needed in L506)`: Whether to symmetrize final orbitals using Abelian symmetry operations.
* 0        Default (Yes).        
* 1        Yes.        
* 2        No.        
* 3        Symmetrize even if symmetry blocking was done, and print symmetries.        
### IOp(5/31)
`L508, L509`: Number of vectors to form at a time during micro-iterations.
* 0        Default (3 in L509).        
* N        N.        
### IOp(5/32)
`L502, L510`: Sleazy SCF.
* 0        Default (No).        
* 1        Yes, use loose integral cutoffs, convergence on either energy or density and always do incremental Fock formation.        
* 2        No.        
* 3        Thresholds similar to DGauss for convergence and integrals.        
* 4        Yes, doing an inexpensive pass 0 and then full accuracy in pass 1.        
* 5        Decide between 1 and 4 based on details of the calculation.        
* 6        Do iterations with sleazy XC grid, then one iteration with next grid up. The default is CoarseGrid for iterations and SG1 for final energy.        
* 00        No longer used.        
* N00        No longer used.        
* I000        Use approximation I, 0=normal 1=Linear approximation to Xc.        
* 00000        Use general DBF logic only if the DBF RWF is present.        
* 10000        Force use of 1c instead of general DBF logic.        
* 20000        Force use of general DBF logic.        
### IOp(5/33)
Print option.
* 0        Only summary results are printed (with possible control from the ‘no-print’ option).        
* 1        The eigenvalues and the M. O. coefficients are printed at the end of the SCF.        
* 2        Same as IOp(5/33)=1, but additionally the density matrix is printed.        
* 3        Same as IOp(5/33)=2, but at the end of each iteration.        
* 4        Same as IOp(5/33)=3, but all matrix transactions are printed (Beware: Lots of output.)        
### IOp(5/34)
Dump option. Regular system defaults apply here.
### IOp(5/35)
`L501, L502`: Whether basis is orthonormal.
* 0        Default (No).        
* 1        Yes.        
* 2        No.        
### IOp(5/36)
Whether to checkpoint after every SCF cycle.
* 0        Default (checkpoint only if direct).        
* 1        Checkpoint.        
* 2        Don’t checkpoint.        
### IOp(5/37)
`L502, L508`: Frequency at which to do full Fock formation instead of incremental.
* -1        Do not do incremental Fock formation.        
* 0        Default (every 20 for direct, except 40 if Camp-King is on).        
* N        Every N^th cycle.        
### IOp(5/38)
Whether to vary integral cutoffs during direct SCF.
* 0        Default (5).        
* 1        No.        
* 2        Yes, do integrals 3 digits more accurately than current convergence.        
* 3        Yes, do integrals at same accuracy as convergence until final iteration, then 2 digits more accurately.        
* 4        Converge to 10^-5 with integrals good to 10^-6 first, then full convergence.        
* 5        VarAcc allowed, decide based on details of problems.        
* 6        VarAcc forbidden because of Guess=Read; allows different default actions for PBC.        
* 7        Full accuracy for 2e part, but do pass 0 with cheaper XC grid.        
* 8        Full grid throughout, but do pass 0 with cheaper integrals.        
### IOp(5/39)
On the fly symbolic matrix element generator.
### IOp(5/40)
Use of reaction field; only used now for Onsager and control of details of SCIPCM.
* -N        Multipoles of order N, increment field in Gen(2-4).        
* 0        No.        
* N        Multipoles of order N, store field in Gen(2-4).        
* 00000        Default (for SCIPCM, same as 10000).        
* 10000        Update surface every iteration.        
* 20000        Update surface every iteration in pass 1 only.        
* 30000        Update surface on pass 2 iterations only.        
* 40000        Same as 3, but re-use 1e matrix instead of surface terms.        
* 50000        Update surface and restart DIIS when within 10^-2 of convergence.        
### IOp(5/41)
Whether to converge on maximum density change as well or instead of RMS.
* 0        2.        
* N        Maximum allowed change is 10^N larger than RMS.        
* -1        Maximum allowed changed is same as RMS (i.e., convergence only on maximum).        
* -2        Converge only on RMS density change.        
* N0        Converge on energy to 10^N*RMS-density-accuracy.        
`L510`: Davidson options. Option xx is used also by Lanczos if IOp(5/39)=10000n or 20000n.
* xx        Maximum dimension of reduced Hamiltonian used as guess is 100*xx. Default=Min(NSec,500).        
* yy00        Maximum dimension of iterative subspace is 10*yy. Default=Max(50*NStates,200).        
* zz0000        Number of guess vectors generated:  Default= NStates*k.        
* k000000        Reduction factor between number of guess vectors provided and number of vectors wanted at the end (1 ≤ k ≤ 9). Default: 1 if reading guess vectors from prev. calc for all states, otherwise 2.        
* ll0000000        Davidson iteration after which to scale back the number of vectors. Warning: For overflow reasons, value must be 0 ≤ ll ≤ 20. Default=2.        
### IOp(5/42)
`L510`: Number of orbitals to localize.
* 1        Localize all active orbitals.        
* N        Localize first N (strongly occupied!) orbitals.        
### IOp(5/47)
`L510`.
* 1        Set up for CAS-MP2.         
* 2        Do spin-orbit calculation.        
### IOp(5/48)
Options to be passed to CalDFT.
* N        Control flag for CalDFT is N.        
`L510`: Whether to use reorthogonalization procedure in Lanczos.
### IOp(5/49)
Use of sparse storage and Conjugate Gradient optimization instead of N^2 memory and diagonalization.
* 0        Default (11, or 22 if sparse is set in ILSW).        
* 1        Diagonalization.        
* 2        Conjugate gradient.        
* 10        Square storage (only in Fock formation if CG).        
* 20        Linear storage (only in Fock formation if diagonalization).        
`L510`: Option for using Lanczos in CPMCSCF calculations.
* 0        No        
* 1        Yes        
* 2        Use Lanczos except for the last iteration.        
### IOp(5/53)
PCM input and solvent type.
* N>0        Solvent type N, default parameters.        
* N<0        Dielectric constant |N|/1000.        
### IOp(5/55)
How many HOMOs and LUMOs to solve for after CG.
* 0        None.        
* N        N of each.        
### IOp(5/56)
A0for Onsager SCRF.
* N        N/1000 Bohr.        
### IOp(5/57)
First iteration at which to level shift and do FON.
* 0        Default= 1 unless doing Stable=Opt, then start after instability searches.        
* N        Iteration N.        
### IOp(5/60)
Override standard values of IRadAn.
### IOp(5/61)
Override standard values of IRanWt
### IOp(5/62)
Override standard values of IRanGd.
### IOp(5/63)
Whether to do FMM.
* 0        Use global default.        
* 1        Turn off FMM here regardless.        
* 100        Turn off both FMM and FoFCou here.        
### IOp(5/64)
Override default value of FMFlags.
* 0        No.        
* N        Yes, use N.        
### IOp(5/65)
Override NFx parameter.
* 0        No.        
* N        Yes, use N.        
### IOp(5/66)
Override the choice of XC functional.
* 0        Use global values.        
* N        Use functional N, with the same values as for IOp(5/74) in overlay 3.        
### IOp(5/70)
Maximum initial temperature for FON (non-PBC), or temperature for broadening (PBC and IOp(5/74)=[1-4]xx).
* -2        None.        
* -1        Start at a high temperature (limited only by DIIS error).        
* 0        Default (3000K = 10 milliHartrees for non-PBC, 600K for PBC).        
* N        N degrees.        
### IOp(5/71)
`L502`:  Number of steps to apply simulated annealing.
* 0        Default — 10 steps FON / 20 steps PFON.        
* N        N steps.        
### IOp(5/72)
Whether L510 should save a state density as the SCF density and whether it should save any excited state densities as CI/TD densities. Requires that Slater determinants be used so that spin densities can be computed, and cannot be used when doing forces or frequencies.
* 0        Default (No).        
* 1        Read the pair of states to use to compute the density saved as the SCF density.  Only one number gives the total rather than transition density.        
* -1        Store the lowest state as the SCF density and the higher states, if any, as CIS/TD excited state densities.        
### IOp(5/73)
Options for ADMP.
* 0        Default (2 for ADMP, 1 for QNDMS).        
* 1        Use Lowdin basis for CP orthonormal transform.        
* 2        Use Cholesky basis for CP orthonormal transform.        
### IOp(5/74)
Type of k-point integration.
* 0        Default (911, should be 193 for metals).        
* 1        Use LT method (interpolation).        
* 2        Occupy entire points (used together with broadening).        
* 3        Full points for insulators, temperature broadening for metals.        
* 9        Occupy lowest NE at each k point regardless of the energies.        
* 10        Improved LT with quadratic corrections.        
* 20        Original LT method.        
* 90        No concern for corrections.        
* 100        Smearing Marzari method I.        
* 200        Smearing Marzari method II.        
* 300        First order Hermite-Gaussian of Paxton and Methfessel.        
* 400        Gaussian smearing.        
* 500        Classical Fermi-Dirac broadening.        
* 900        No broadening (this will be Gaussian broadening with small T).        
### IOp(5/75-78)
Number of alpha electrons, alpha orbitals, beta electrons, and beta orbitals for fractional occupation.
### IOp(5/79)
Range around Fermi level around which temperature distribution will be applied if broadening is turned on for PBC.
* 0        Default, a value will be chosen in ZInLT1.        
### IOp(5/80)
The maximum conjugate gradient step size.
* -1        No maximum step size.        
* 0        Default maximum (.8).        
* MMNN        Step size of MM.NN.        
### IOp(5/81)
Conjugate-Gradient parameters.
* MM        Maximum Number of CG cycles per SCF iteration. (defaults to 4 CG cycles).        
* NN00        Maximum Number of purification cycles per CG iteration. (defaults to 3 cycles).        
* 00000        Don’t use CG DIIS.        
* 10000        Use CG DIIS.        
* 000000        Polak-Ribiere CG minimization.        
* 100000        Fletcher-Reeves CG minimization.        
* 0000000        Use diagonal preconditioning in Conjugate-Gradient.        
* 1000000        No preconditioning.        
### IOp(5/82)
C.G. Convergence criterion.
* 0        Defaults  to 10^-7.        
* N        10^-N.        
### IOp(5/83)
Maximum SCF DIIS vectors.
* 0        Default (20, except 40 if Camp-King is on).        
* N        Use SCF DIIS with N vectors.        
### IOp(5/84)
`L509`: Restart.
`L502`: Restart using Fock matrix.
* 0        Default (Yes for PBC and sparse with guess Fock).        
* 1        Yes.        
* 2        No.        
### IOp(5/85)
Over-riding of maximum cycles for XQC.
* -1        Default for first step (32).        
* 0        No.        
* N        Limit is N cycles.        
### IOp(5/86)
`L502`:  Strategy options.
* 000000        Default (101100).        
* 0        Default (1 except during Stable=Opt, then 4).        
* 1        Just continue as usual if energy goes up.        
* 2        Reduce DIIS space when energy rises from previous cycle.        
* 3        Reduce DIIS space when energy goes above the lowest energy.        
* 4        Reduce DIIS space whenever energy is above the lowest energy.        
* 10        Turn on dynamic level shift from the beginning.        
* 20        Turn on dynamic level shift only after FON is over.        
* 100        Keep level shift after energy rises.        
* 200        Turn off level shift after energy rises.        
* 1000        Level shift to a maximum of the goal.        
* 2000        Level shift to a maximum of 2*goal.        
* 3000        Level shift as much as necessary for HOMO > LUMO.        
* 4000        Level shift only if the HOMO-LUMO gap is zero.        
* 5000        Level shift only if the HOMO-LUMO gap is zero or insignificant (> -0.1)        
* 6000        Level shift only if the gap is zero or insignificant (> -0.1), up to twice the goal.        
* N0000        No longer used.        
* 100000        Turn off 3 and 4 point extrapolation if DIIS is on.        
* 200000        Retain 3 and 4 point extrapolation if DIIS is on.        
* The energy is only checked after FON has been turned off.        
### IOp(5/87)
Accuracy criterion in Fock matrix formation.
* 0        Default, set in FoFCou/CalDSu based on accuracy part of IOp(5/5). Typically 10^-10 for molecules and 10^-12 for periodic systems.        
* N        10^-N.        
### IOp(5/88)
No longer used.
### IOp(5/89)
Linearly dependent basis control for PBC; this and ZFormV should be moved to L302.
### IOp(5/90)
Whether to generate sparse guess here.
* 0        No        
* 1        Yes, do preliminary AM1 calculation.        
* 2        Yes, do preliminary AM1 calculation and compare with guess from previous step in geometry optimization.        
### IOp(5/91)
Control option for Chebyshev sparse control.
### IOp(5/92)
How to do exact exchange.
* 0        Default (Normal processing based on FMM for non-PBC, separate Coulomb and NFx exchange for PBC).        
* 1        FoFCou for Coulomb, separate FoFCou/NFx for exchange.        
### IOp(5/93)
Number of initial iterations for which damping is allowed.
* 0        Default (10).        
* N        N iterations.        
### IOp(5/95)
`L510`: Whether to do Davidson during RFO.
* 0        No.        
* 1        Yes.        
### IOp(5/96)
`L509`: Override IRadAn for CPHF-like step.
`L502`: Override IRadAn for pass 0 grid.
* 0        Use default.        
* N        Use grid N.        
`L510`: Prepares for direct RAS method. The CAS active space is subdivided into three RAS active subspaces:  Ras1, Ras2 and Ras3. In the reference space, Ras1 orbitals are doubly occupied, and Ras3 orbitals are empty. We also need to define the maximum number of holes in the Ras1 space (i.e., the number of electrons that can be excited out of the Ras1 subspace) and the maximum number of electrons in the Ras3 space.
* ww        ww = Number of Ras1 orbitals.        
* xx00        xx = Maximum number of holes in Ras1.        
* yy0000        yy = Number of Ras3 orbitals.        
* zz000000        zz = Maximum number of electrons in Ras3.        
### IOp(5/97)
Whether to update precomputed grid data with timing information.
* 0        Default (Yes, if available).        
* 1        Yes.        
* 2        No.        
`L510`: Hopping threshold during trajectories.
### IOp(5/98)
Whether to save eigenvalues and orbitals at all k-points.
* 0        Default (Yes).        
* 1        Yes.        
* 2        No.        
`L510`: Hopping options.
### IOp(5/99)
Grid for numerical k-integration in FT-LT method.
* 0        Default: 32,12,8 for 1,2,3d.        
* N        Number of points in the grid.        
### IOp(5/100)
Tight convergence during CGDMS.
* 0        Default (No).        
* 1        Yes.        
* 2        No.        
### IOp(5/101)
SDif test on numerical accuracy of PBC diagonalization.
* 0        Default (10).        
* -1        No test.        
* N>0        Abort if SDif is larger than N.        
### IOp(5/102)
Maximum number of configurations for CAS-MP2.
* 0        Default (1000).        
* N        N.        
### IOp(5/103)
Number of occupied and virtual orbitals to print for each k-point.
* -1        Default of 5 occupieds and 5 virtuals.        
* 0        Default is 5 if printing turned up; otherwise 0.        
* N        N occupieds and N virtuals.        
### IOp(5/105)
`L510`:  Convergence for Davidson iterations.
* 0        Default (6 digits on coefficients).        
* N        10^-N on coefficients.        
### IOp(5/106)
`L510`:  Saving and restart for iterative CI.
* 0        No.        
* 1        Save CI vectors.        
* 2        Restart CI, possibly adding states.        
### IOp(5/107)
`L510`: Maximum number of Davidson iterations.
* 0        Default (huge, number of CI configurations).        
* -1        No limit.        
* N        N iterations.        
### IOp(5/108)
Minimum number of iterations at which to damp density.
* 0        Default (1 if transition metals present, otherwise 0).        
* N        N.        
### IOp(5/120)
Whether to store nuclear repulsion energy as total energy.
* 0        Default (No).        
* 1        Yes.        
### IOp(5/121)
IDoVI for HarFok in test calculations.
* xx0        Ones digit always set to 4 here.        
### IOp(5/122)
Whether to do Hirshfeld analysis of spin orientations and compute spin each iteration.
* 0        Default (yes for GHF/GKS, no otherwise).        
* 1        Yes.        
* 2        No.        
### IOp(5/123)
Number of iterations for Pseudodiagonalization.
* 0        Default (1 for semi-empirical, -1 for HF/DFT).        
* -1        Sweep until variable convergence is reached.        
* N        Do a maximum of N sweeps.        
### IOp(5/124)
Variable convergence in pseudodiagonalization:
* 0        Default (1 for ab initio, 2 for semi-empirical).        
* N        Off-diagonals larger than the initial max/10^N are swept.        
* -N        Off-diagonals larger than OVMax*10^-N are swept, with OVMax updated each iteration.        
### IOp(5/125)
Scale factor for Diag/PseudoDiag tradeoff. Roughly related to the ratio of Diag to Fock formation for large systems.
* -1        No test.        
* 0        Default (30 for ab intio, 15 for semi-empirical).        
* N        Pseudodiag must be estimated to be at least N/10 times faster than full diag to be used.        
### IOp(5/126)
`L508`: Initial step size for linear searches.
* 0        Default (300).        
* N        N/10000        
### IOp(5/127)
`L508`: Maximum rotation gradient for Newton-Raphson (above this value, scaled steepest descent is used):
* 0        Default (1.d-2).        
* N        10^-N.        
### IOp(5/128)
`L502`:  Diagonalization algorithm.
* 0        Default (GSYEVD if memory permits, otherwise GSPEV).        
* N         Algorithm N in DiagDS.        
### IOp(5/129)
Threshold for trying alternate initial guess:
* 0        Default (2).        
* -1        Same as 0.        
* -2        Ignore the alternate guess.        
* N        Try the alternate if the DIIS error &gteq; 10^-N.        
### IOp(5/131)
Whether to match phases with reference orbitals (useful during numerical differentiation).
* 0        Default (1).        
* 1        Match if file of reference orbitals exists.        
* 2        Do not match.        
### IOp(5/139)
`L510`: Large-scale CI method
* 0        Default (Shaopeng for CAS, Klene for RAS).        
* 1        Shaopeng (NYI for RAS).        
* 2        Klene.        
## Overlay 6 
### IOp(6/7)
Printing of MOs.
* 0        Default: 1 for molecules, 2 for PBC.        
* 1        Print the occupied and first 5 virtual MOs.        
* 2        Do not print any MOs.        
* 3        Print all MOs.        
* 10        Biorthogonalize unrestricted MOs.        
* 100        Save biorthogonalized MOs over canonical ones.        
### IOp(6/8)
Density matrix. Default: No-print. See below for values.
### IOp(6/9)
Full population analysis. Default: Print. See below for values.
### IOp(6/10)
Gross orbital charges. Default: Print. See below for values.
### IOp(6/11)
Gross orbital type charges. Default: No-print. See below for values.
### IOp(6/12)
Condensed to atoms. Default: Print. See below for values.
### IOp(6/8-12)
These options are print/no-print options. The possible values are:
* 0        Default.        
* 1        Print the normal amount.        
* 2        Do not print.        
* 3        Print verbosely.        
### IOp(6/13)
Whether to save computed electric field on disk for use in Tomasi RF calculations.
* 0        Default (No).        
* 1        Yes.        
* 2        No.        
### IOp(6/14)
`L602`: Specification of other properties to be calculated.
* 0        Default (1).        
* 1        Evaluate the electric potential, the electric field, and the electric field gradient at each center.        
* 2        Evaluate the potential and the electric field at each center.        
* 3        Evaluate only the potential at each center.        
* 4        Evaluate none.        
### IOp(6/15)
Specification of additional centers. If more than one of these is requested, the lists are in separate input sections in the order listed below.
* 0        No additional centers. Evaluate the properties only at each atomic center.        
* 1        Read additional centers. One card per center with the X, Y, and Z coordinates in Angstroms (free format).        
* 2        Read in coordinates as for 1. Starting at each point, located the nearest stationary point in the electric potential.        
* 4        Read in a set of cards specifying a grid of points at which the electric potential will be computed. Two forms of specifications are below.        
* 8        Do potential-derived charges.        
* 16        Constrain the dipole in fitting charges.        
* 32        Read in centers at which to evaluate the potential from the RWF.        
* 128        Read grid; do not default cube.        
Grid specifications for option 4
A. Evenly spaced rectangular grid. Three cards are required:
* KTape,XO,YO,ZO        —output unit and coordinates of one corner of grid. If KTape is 0, it defaults to 51.        
* N1,X1,Y1,Z1        —number of increments and vector.        
* N2,X2,Y2,Z2        —number of increments and vector.        
N1 records will be written to unit KTape, with N2 values in each record.
B. An arbitrary list of points. Only one card is needed: N,NEFG,LTape,KTape.
The coordinates of N points in Angstroms will be read unit LTape in format (3F20.12). The potential (NEFG=3), potential and field (NEFG=2), or potential, field, and field gradient (NEFG=1) will be computed and written along with the coordinates to unit KTape in format (4F20.12). Thus if NEFG=3 for each point there will be 4 cards written per point, containing:
* X-coord,Y-coord,Z-coord,Potential        
* X-field,Y-field,Z-field,XX-EFG        
* YY-EFG,ZZ-EFG,XY-EFG,XZ-EFG        
* YZ-EFG        
Note that either form of grid should be specified with respect to the standard orientation of the molecule.
### IOp(6/16)
`L602`: Cutoffs.
* 0        Use full accuracy in calculations at specific points, but use sleazy cutoffs in mapping a grid of points.        
* 1        Do all points to full accuracy.        
### IOp(6/17)
`L602`: Debugging control.
* 0        Compute all contributions to selected properties.        
* 1        Compute only the nuclear contribution.        
* 2        Compute only the electronic contribution.        
* -N        Compute only the contribution of shell N.        
### IOp(6/18)
Whether to update dipole RWF.
* 0        Yes.        
* 1        No.        
### IOp(6/19)
Whether to rotate exact polarizability before comparing with approximate (which will be calculated in the standard orientation). This is like IOp(6/9) in L9999.
* 0        Default, same as 1.        
* 1        Exact is still in standard orientation; use as-is.        
* 2        Exact is already in z-matrix orientation, so rotate.        
### IOp(6/20)
How to do electrostatic-potential derived charges.
* 0        Default (1).        
* -1        Read a list of points at which to fit, one per line.        
* 1        Merz-Kollman point selection.        
* 2        CHELP point selection.        
* 3        CHELPG point selection.        
* 4        MK but with 2xUFF radii.        
* 5        Hu, Lu, and Yang point selection/weighting. By default, HLY’s atomic densities are used. These are available only up to Ar.        
* 00        Default radii are those defined with the selected method.        
* 10        Force Merz-Kollman radii.        
* 15        Use Gaussian’s atomic density expansions instead of HLY’s. Gaussian’s are defined for all elements up to 112.        
* 20        Force CHELP (Francl) recommended radii.        
* 30        Force CHELPG (Breneman) recommended radii.        
* 40        Force 2xUFF Radii.        
* 100        Read in replacement radii for selected atom types as pairs (IAn,Rad) or (Symbol,Rad), terminated by a blank line.        
* 200        Read in replacement radii for selected atoms as pairs (I,Rad), terminated by a blank line.        
* 1000        Fit united atoms (heavy atoms only) rather than all atoms.        
* 00000        Default (10000).        
* 10000        Use only active atoms in the fit.        
* 20000        Use all atoms in the fit.        
* 30000        Fix the charges of all atoms with a non-zero MM charge.        
### IOp(6/22)
`L601, L602, L604`: Selection of density matrix.
* -1x        Read density matrices from .checkpoint file.        
* +1x        Read density matrices from .checkpoint file.        
* -5        All available transition densities.        
* -4        Transition density between the states given by IOp(6/29) and IOp(6/30).        
* -3        Density for the excited state given by IOp(6/29).        
* -2        Use all available density matrices.        
* -1        Use the density matrix for the current method, or the HF density if the one for the current method is not available.        
* N≥0        Use the density matrix for method N (see Link 1 for the numbering scheme).        
### IOp(6/23)
`L604`: Density values to evaluate over grid.
* 0        Default (same as 3).        
* 1        Density values.        
* 2        Density values and gradients.        
* 3        Density values, gradients and divergence.        
### IOp(6/24)
Frozen core.
* -N        Freeze N orbitals.        
* 0        Default (Yes).        
* 1        Yes.        
* 2        No.        
### IOp(6/25)
`L601`: Whether to compute Coulomb self-energy.
* 0        No.        
* 1        Yes, classically (including self terms — requires 2e integrals, O(N^4)).        
* 2        Yes, quantum mechanically (no self terms — requires 2e integrals, and only available for HF. O(N^5)).        
### IOp(6/26)
`L602, L604`: Which density to use.
* 0        Default (same as 1).        
* 1        Total.        
* 2        Alpha.        
* 3        Beta.        
* 4        Spin.        
### IOp(6/27)
Choice of population analysis.
* 0        Default (12).        
* 1        Don’t do Mulliken populations.        
* 2        Do Mulliken populations.        
* 10        Don’t do bonding Mulliken populations.        
* 20        Do bonding Mulliken populations.        
* 100        Do minimal population analysis.        
* 1000        Read in weightings for atoms pairs for unequally split Mulliken.        
### IOp(6/28)
Mark SCF density as current density.
* 0        No: save SCF density, but do not mark.        
* 1        Yes: mark as well.        
### IOp(6/29)
Excited state to use if requested by IOp(6/22).
### IOp(6/30)
2nd excited state for transition density.
* 0        Transition density between state IOp(6/29) and g.s.        
* N        Transition density between state IOp(6/29) and state N.        
### IOp(6/31)
Whether to determine natural orbitals from densities.
* 0        No.        
* 1        Yes, using total density.        
* 2        Yes, using alpha and beta separately for UHF.        
* 3        Store only alpha NOs.        
* 4        Store only beta NOs.        
* 5        Use spin density.        
### IOp(6/32)
`L609`: Control parameters for COVBON (not to be changed under most circumstances).
100000*IPrSma+10000*MItLoc+1000*ITlLoc+100*IDcInt+IPrLoc, where:
* IPrSma        When printing MOs in terms of AOIMs, include only MOs with occupancies per spin greater than 10^-IPrSma and AOIMs with squares of coefficients greater than 10^-IPrSma (1…9, the default of 0 implies printing of all MOs and AOIMs).        
* MItLoc        MItLoc*NOrb*(NOrb-1)/2 is the maximum number of iterations in localization of (spin) orbitals (1…9, default 6).        
* ITlLoc        10.^-ITlLoc is the convergence criterion for (spin)orbital localization (1…9, default 9).        
* IDcInt        Localized (spin)orbitals with atomic occupancies less than 0.01*IDcInt are interpreted as lone pair MOs rather than bond MOs (1…99, default 10).        
* IPrLoc        0: Print the atomic occupancies of localized (spin)orbitals (default).
1: Do not print the atomic occupancies.        
`L605, L606`: naming of RPAC interface file.
* 0        Make this a scratch file.        
* 1        Name this file ‘rpac.11’        
### IOp(6/35)
`L609`: What to do:
* 0        Determine attractors, attractor interaction lines, ring points, and cage points.        
* 1        Determine zero-flux surfaces (IDoZrF).        
* 2        Compute charges of AIMs (IDoAtC).        
* 4        Compute kinetic energies and multipole moments of AIMs (IDoPrp).        
* 10        Compute energies of electrostatic interactions between AIMs (IDoPot). This precludes calculations of atomic property derivatives with respect to nuclear displacements.        
* 100        Compute atomic overlap matrices (IDoAOM).        
* 200        Compute other atomic matrix elements (IDoAMa).        
* 400        Include zero-flux surface relaxation terms in all atomic matrix elements (IDoSRe).        
* 1000        Compute derivatives of atomic properties with respect to electric field (IDoSeP). Note that IDoSRe should be set to 1 in order to obtain correct results! Also note that analytical polarizabilities have to be available but force constants have to be absent!        
* 2000        Compute derivatives of atomic properties with respect to nuclear displacements as well (IDoNuD). Note that analytical force constants have to be available!        
* 10000        Compute localized orbitals and bond orders (IDoLoc).        
* 20000        Compute atomic orbitals in molecule (IDoAOs).        
* 100000        If necessary, augment valence electron densities with relativistic core contributions, which is a default anyway (IHwAug = 0).        
* 200000        If necessary, augment valence electron densities with non-relativistic core contributions (IHwAug = 1).        
* 400000        Abort if pseudo-potentials have been used (IHwAug = 3).        
* 1000000        Reduce accuracy so atomic charges can be computed more rapidly (IQuick). No other properties can be calculated. This option sets IPrNDe=5, IPrNA t= 5, and IEpsIn = 100.        
* 2000000        Use numerical instead of analytic integration.        
* 3000000        Use numerical instead of analytic integration and use reduced cutoffs.        
* 4000000        Full accuracy and analytic integration.        
### IOp(6/36)
`L609`: Control parameters for neglect of orbitals and primitives.
10000*INoZer+100*IPrNDe+IPrNAt, where…
* INoZer        0: Ignore (spin)orbitals with zero occupancies (default).
1: Do not ignore (spin)orbitals with zero occupancies.        
* IPrNDe        Neglect primitive contributions below 10.^-IPrNDe in evaluations of electron density and its derivatives (0…99, default 7).        
* IPrNAt        Neglect primitive contributions below 10.^-IPrNAt in integrations over atomic basins (0…99, default 7).        
### IOp(6/37)
`L609`: Control parameters for ATINLI, RNGPNT, and CAGPNT (not to be changed under most circumstances).
1000000*MxBpIt+100000*SBpMax+1000*NGrd+LookUp, where…
* MxBpIt        Maximum number of iterations in trial path determination (1…99, default 10).        
* SBpMax        Maximum value of the control sum (1…9, default 2).        
* NGrd        Length of Fourier expansion for the trial path (1…99, default 20).        
* LookUp        Number of grid points in critical point search (1…999, default 100).        
### IOp(6/38)
`L609`: Control parameters for ZRFLUX and OIGAPI (not to be changed under most circumstances):
100000*INStRK+10000*IHowFa+1000*IGueDi+100*IPraIn+10*IRScal+IRtFSe
* INStRK        10*INStRK is the number of steps in the Runge-Kutta integrations along gradient paths (1…9, default 2).        
* IHowFa        IHowFa is the maximum distance in the Runge-Kutta integrations along gradient paths (1…9, default 5),        
* IGueDi        10.^-IGueDi is the initial displacement from the critical point in the Runge-Kutta integrations (1v9, default 6).        
* IPraIn        10.*IPraIn is the cut-off for zero-flux surfaces (1…9, default 2).        
* IRScal        IRScal is the scaling factor in the nonlinear transformation used in the intersection search (1…9, default 2).        
* IRtFSe        10.*IRtFSe is the safety factor used in the intersection search (1…9, default 2).        
### IOp(6/39)
`L609`: More control parameters for ZRFLUX and OIGAPI (not to be changed under most circumstances):
1000000*IToler+100000*INInGr+10000*INInCh+1000*IEpsSf+10*IEpsIn+INTrig
* IToler        10.^-5-IToler is the tolerance for the intersection search (1…9, default 5).        
* INInGr        10*INInGr is the initial number of grid points in theta and phi in the adaptive integration subroutine (1…9, default 2).        
* INInCh        5+INInCh is the initial number of sampling points in the intersection search (1…9, default 2).        
* IEpsSf        IEpsSf is the safety factor used for patches with surface faults in the adaptive integration subroutine (1…9, default 6).        
* IEpsIn        0.0001*IEpsIn is the target for integration error (1…99, default 2).        
* INTrig        10*INTrig is the number of sine and cosine functions in the trial function for surface sheets (1…9, default 2).        
### IOp(6/40)
`L607`: Control.
* -2        Skip NBO analysis.        
* -1        Do only NPA.        
* 0        Default (-2).        
* 1        Default NBO analysis — don’t read input.        
* 2        Read input data to control NBO analysis.        
* 3        Delete selected elements of NBO Fock matrix and form a new density, whose energy can then be computed by one of the SCF links. This link must have been invoked with IOp(40) = 0 or 1 prior to invoking it with IOp(40) = 2.        
* 4        Read the deletion energy produced by a previous run with IOp(40) = 2 and print it.        
* 10        NBO should not delete its internal data file.        
### IOp(6/41)
Number of layers in esp charge fit.
* 0        Default (4).        
* N        N layers, must be ≤ 4.        
### IOp(6/42)
Density of points per unit area in esp fit.
* 0        Default (1).        
* N        Points per unit area.        
### IOp(6/43)
Increment between layers in MK charge fit.
* 0        Default (0.4/Sqrt(#layers)), where # layers = IOP (6/41)        
* N        0.01*N.        
### IOp(6/44)
`L604`: Type of calculation.
* 0        Default, same as 2.        
* 1        Compute the molar volume.        
* 2        Evaluate the density over a cube of points.        
* 3        Evaluate MOs over a cube of points.        
* 10        Skip header information in cube file.        
### IOp(6/45)
Number of points per Bohr^3 for Monte-Carlo calculation of molar volume.
* -1        Read from input.        
* 0        Default (20).        
* N        N points — for tight accuracy, 50 is recommended.        
### IOp(6/46)
Threshold for molecular volume integration.
* 0        Default — 10^-3        
* -1        Read from input.        
* N        N*10^-4.        
### IOp(6/47)
Scale factor to apply to van der Waals radii for the box size during volume integration.
* 0        Default.        
* N        N*0.01 — for debugging.        
### IOp(6/48)
Use of cutoffs.
* 0        Default (10^-6 accuracy for cubes, 1 digit better than desired accuracy for volumes).        
* N        10^-N.        
### IOp(6/49)
`L602, L604`: Approximate number of points per side in cube.
* 0        Default (80).        
* N        N points.        
* -1        Read from cards.        
* -2        Coarse grid, 3 points/Bohr.        
* -3        Medium grid, 6 points/Bohr.        
* -4        Fine grid, 12 points/Bohr.        
* -N>4        Grid using 1000 / N points/Bohr.        
### IOp(6/50)
Whether to write Antechamber file during ESP charge fitting.
* 0        Default (No).        
* 1        Yes.        
### IOp(6/51)
Whether to apply Extended Koopman’s Theorem (EKT).
* 0        Default (No).        
* N        Yes, on non-SCF densities, up to N IPs and EAs.        
* -1        Yes, on non-SCF densities, all possible IPs and EAs.        
* -2        No.        
### IOp(6/52)
`L609`: Number of radial integration points.
* 0        Default (100).        
* N        N.        
### IOp(6/53)
`L609`: Distribution of radial points.
* 0        Default (cubic).        
* N        Polynomial of order N.        
### IOp(6/54)
Maximum number of domains.
* 0        Default (100000).        
* N        N.        
### IOp(6/55)
`L609`: Number of inner angular points in numerical integration.
* -1        0(no inner sphere).        
* 0        302.        
* N        N point Lebedev grid (see AngQad).        
### IOp(6/56)
`L608`: Whether to read in density matrix from input stream.
* 0        No.        
* 1        Yes.        
### IOp(6/57)
Whether to generate data over a grid using the total SCF density.
* 0        No.        
* 1        Yes, read in name for output file.        
* 2        Yes, also read in name for input file with a different grid and compare.        
* 3        Output in the form of data statements.        
* 4        Fit atomic density to Gaussians.        
* 5        Fit atomic density to Gaussians, forcing positive definiteness.        
### IOp(6/58)
Grid to use in generating tables of density and potential if IOp(57) = 1–3. Must be an unpruned grid.
* 0        Default (99001).        
If IOp(57) = 4–5, whether to remove primitives which have all zero coefficients in the expansion:
* 0        Default (1).        
* 1        Yes.        
* 2        No.        
### IOp(6/59)
Approximations to Exc
* -1        Test superposition of atomic densities using L608:        
* 0        Do correct energies.        
* 1        Do correct energies and 0th order approximation.        
* 2        Do correct energies and 0th-1st order approximations.        
* 3        Do correct energies and 0th-2nd order approximations.        
### IOp(6/60–62)
Over-ride standard values of IRadAn, IRanWt, and IRanGd. The default is 3 steps smaller grid for HLY charges in L602 and the global default otherwise.
### IOp(6/63)
`L608`: Suppress number of electrons test in XC quadrature (for debugging with small grids):
* 0        Default (do test).        
* 1        Suppress test.        
* 2        Do test as usual.        
### IOp(6/64)
Natural Chemical Shielding Analysis.
* 0        No.        
* 1        Yes, of isotropic value.        
* 2        Yes, of diagonal tensor elements and isotropic value.        
* 3        Yes, of all tensor components.        
### IOp(6/65)
Threshold for printing of NCS contributions.
* -1        Zero.        
* 0        Default (1 pmm).        
* N        N/1000 ppm.        
### IOp(6/72)
`L602`: Whether to read isotopes for hyperfine interactions and do hyperfine terms.
* 0        Default (1).        
* 1        Yes, if open-shell, NMR data is available, and other terms are being computed.        
* 2        No.        
* 3        Yes, regardless of other terms.        
* 4        Yes, reading isotopes.        
### IOp(6/73)
Whether to save orbitals from NBO.
* 0        Default (No).        
* 1        Save NBOs in place of regular MOs.        
* 2        Save NLMOs in place of regular MOs.        
* 3        Save NLMO occupieds and NBO virtuals.        
* 10        Suppress re-orthogonalization.        
* 110        Suppress sorting.        
### IOp(6/74)
Whether to use Gaussian connectivity in choosing Lewis structure for NBO.
* 0        Default (use if present and choose is selected in NBO input).        
* 1        Use.        
* 2        Don’t use.        
### IOp(6/75)
`L602`: Model for CM2 charges.
### IOp(6/76)
`L607`: Threshold for linear dependence.
* 0        Default (1.D-6).        
* N        10^-N.        
### IOp(6/77)
* 0        None.        
* -1        2.d-4.        
* N        N * 10^-5.        
### IOp(6/78)
Use MOs instead of density in AtmTab.
* 0        Default (2).        
* 1        Use density.        
* 2        Use MOs.        
### IOp(6/79)
Whether to calculate Hirshfeld charges.
* 0        Default (No).        
* 1        Yes.        
* 2        No.        
* 3        Yes, do atom-atom electrostatic interactions as well.        
* 10        Do iterative charges.        
* 20        Do iterative charges and read initial values.        
* 100        Do partitioning of density by abelian irrep.        
* NNNxxx        Maximum number of iterations. Default is 50.        
### IOp(6/80)
Whether to calculate Lowdin charges and Mayer bond orders.
* 0        Default (No).        
* 1        Yes.        
* 2        No.        
### IOp(6/81)
Print kinetic energy of orbitals?
* 0        Default (yes, if doing other orbital results).        
* 1        Yes, for the top 5 occupieds and lowest 5 virtuals.        
* 2        No.        
* 3        Yes, for all orbitals.        
### IOp(6/82)
Tensors for hyperfine spectra.
* 0        Default, compute if there are 100 or fewer atoms.        
* 1        Compute QEq tensors and for open-shell systems compute isotropic and anisotropic splitting tensors.        
* 2        Do not compute tensors.        
### IOp(6/83)
Orbital angular momentum analysis.
* 0        Default (No).        
* 1        Yes, do total angular momentum contribution to each MO.        
* 10        Report the largest atomic d and f contributions to orbitals specified by IOp(6/84).        
* 20        Report the largest transition metal atomic d and f contribs. to orbitals specified by IOp(6/84).        
* 30        Read a list of atoms whose d and f contributions will be analyzed.        
* 90        Do not do atomic d and f contributions.        
* 100        Report the population of each angular momentum on each atom.        
### IOp(6/84)
Orbitals to analyze for d and f contributions.
* -1        All orbitals.        
* 0        Just occupied orbitals.        
* N        Occupieds plus lowest N virtuals.        
### IOp(6/86)
Computation of multipole moments.
* 0        Default (1, except for PBC and old semi-empirical).        
* 1        Calculate with DipInt.        
* 2        Use stored moment operators.        
### IOp(6/87)
`L608`: Accuracy criterion in Fock matrix formation
* 0        Default.        
* N        10^-N        
### IOp(6/88)
Thresholds for orbital atomic angular momentum printing.
* 0        Default (10%).        
* NN        At least NN % to print contribution from L on a particular atom.        
### IOp(6/89)
Do Natural Transition Orbital Analysis.
* 0        No.        
* 1        Yes, if ground to excited transition density requested.        
* 10        Save over canonical MOs.        
### IOp(6/90)
Whether to include p’s as valence for transition metals and actinides during NBO analysis.
* 0        Default (Yes).        
* 1        Yes.        
* 2        No.        
### IOp(6/91)
Whether to compute electron-electron spin-spin coupling.
* 0        No.        
* 1        Yes, if multiplicity >2.        
### IOp(6/92)
Thresholds for HLY charge fitting.
* 0        Default (Tiny=1.d-8, ThrGrd=1.D-8)        
* MMNN        Tiny=10^-MM, ThrGrd=10^-NN.        
### IOp(6/93)
Reference density for HLY charge fitting.
* -1        Zero.        
* 0        Exp(-9)        
* N        N/100.        
### IOp(6/94)
Sigma parameter for HLY charge fitting.
* 0        0.8.        
* N        N/1000.        
### IOp(6/95)
`L608`: Whether to diagonalize Fock matrices.
* 0        Default (No).        
* 1        Yes, with Davidson.        
* 2        Yes, with DiagDN.        
### IOp(6/96)
Analyze all orbitals by atom and angular momentum contribution.
* 0        Default (No).        
* -2        Highest 10 occupieds and lowest 10 virtuals.        
* -1        Yes, for all orbitals.        
* N        For highest N occupieds and lowest N virtuals.        
### IOp(6/113)
`L612`: Which external method to use.
* 0        Default (1).        
* N        Command N in file 747.        
### IOp(6/114)
Which ONIOM system is being done, which is sometimes needed by external procedures.
* 0        Default (1)        
* 1        Real system.        
* 2        Model system for 2-layer, middle for 3-layer.        
* 3        Small model system for 3-layer.        
### IOp(6/120)
Store nuclear repulsion energy as total energy? (Here, store only the nuclear contribution to the dipole moment).
* 0        Default (no).        
* 1        Yes.        
### IOp(6/124)
`L612`: Options for External.
### IOp(6/125)
`L612`: Options for unformatted i/o file.
### IOp(6/126)
`L612`: IDefCm for external.
* -1        Same as 0.        
* 0        Default to Gau_External.        
* 1        Default to runnbo6.        
### IOp(6/127)
Whether to compute BEBO energy corrections.
* 0        Default (1 if parameters available).        
* 1        Yes.        
* 2        No.        
* 00        Default (10).        
* 10        Use number of pairs (including core) rather than number of lone pairs.        
* 20        Use number of lone pairs.        
### IOp(6/128)
`L608`: Compute core and valence energies.
* 0        Default (01).        
* 1        Do regular calculations.        
* 10        Do core-valence.        
* 11        Do both.        
### IOp(6/129)
Whether to do DCT charge transfer analysis on the selected excited state densities:
* 1        Do the analysis if excited state densities are available, and for the relaxed excited state density if this was selected.        
* NNNx        Do a maximum of NNN matrices at a time.        
## Overlay 7 
### IOp(7/7)
Use of internal coordinates.
* 0        Yes.        
* 1        No.        
* 2        Yes, but neglect first derivatives in conversion of second derivatives to internal coordinates.        
### IOp(7/8)
Harmonic frequency calculation.
* 0        Default (10003).        
* 1        Yes, with most common isotopes.        
* 2        Yes, with read-in isotopes.        
* 3        No.        
* 10        Print higher precision normal modes.        
* 20        Print normal mode displacements in redundant internals.        
* 30        Print both HP modes and internal displacements.        
* 40        Print only intensities and not modes.        
* Nxx        Default scale factor is #N (1=HF, 1/1.12, (2=CBS4=0.91671, 3=CBSQ=0.91844).        
* Mxxx        If M=1, only harmonic thermochemistry. If M=2, do hindered rotor analysis. If M=3, Read hindered rotor parameters from input.        
* Lxxxx        L=1 diagonalize full NAt3^2 force constant matrix and print low modes, unless there are frozen atoms. L=2 do not diagonalize full FC matrix.        
* Kxxxxx        K=1 print eigenvalues of FC matrices. K=2 also read file names and dump mass-weighted FC matrices (full and projected) to disk.        
* Jxxxxxx        J=1 print normal-mode derivatives.        
### IOp(7/9)
Whether to rotate derivatives back to the z-matrix orientation.
* 0        Yes.        
* 1        No.        
Whether to rotate and process derivative properties.
* 00        Default (yes).        
* 10        Yes.        
* 20        No.        
### IOp(7/10)
First/second derivative control.
* 0        Do only first derivatives.        
* 1        Do only second derivatives.        
* 2        Do both.        
### IOp(7/11)
Control of integral derivative algorithm.
* 0        Default; use IsAlg to decide.        
* 2        Scalar Rys SPDF.        
* 3        Berny SP, Scalar Rys DF.        
* 4        Old vector Rys SPDF (obsolete).        
* 5        Berny SP, old vector Rys DF (obsolete).        
* 6        FoFJK: Rys spdf (obsolete).        
* 7        Berny SP, FoFJK Rys df (obsolete).        
* 8        FoFJK: HGP sp, Rys df (obsolete).        
* 9        Berny SP, FoFJK Rys df (same as 7).        
* 10        FoFJK: HGP spd, Rys f (obsolete).        
* 11        Berny SP, FoFJK HGP d Rys f (obsolete).        
* 12        FoFJK: HGP spdf.        
* 13        Berny SP, FoFJK HGP df (obsolete).        
* 14        FoFJK: PRISM spdf.        
* 15        FoFJK: Berny SP, PRISM df (obsolete).        
### IOp(7/12)
Selection of density matrix.
* 0        Usual SCF density.        
* N        Use generalized density number N for both the one-electron integral derivatives and the corresponding 2PDM terms.        
### IOp(7/13)
Contraction with two-particle density matrices.
* 0        Default (same as 1).        
* 1        Use HF 2PDM.        
* 2        Use external 2PDM.        
* 3        Use both HF and external 2PDM.        
* 4        Generate 2PDM from CIS/TD square 1PDM (for debugging)        
* 5        Generate 2PDM from CIS/TD square 1PDM and use HF/Z 2PDM as well.        
* 6        Contract with external 2PDM derivatives. The types of derivatives are given by IOp(7/15).        
* 7        Form derivative 2PDM from CIS and HF deriv. dens. matrices. IOp(7/15) gives types of derives.        
* 8        Do TDA/TDnon-adiabatic coupling in addition to forces. Uses 
generaized density, does not compute ground-state or T*T force terms, 
and does the half-overlap term in L701.        
* 9        Do only TDA/TD non-adiabatic coupling.        
* 1xx        Leave the external 2PDM on the disk instead of deleting it.        
2-5, 8 imply use of the generalized density in L701, while 6-7 imply use of gen. density derivatives in L701.
### IOp(7/14)
State for CIS/TD derivatives; gradients. Defaults to 1.
### IOp(7/15)
The nature of the perturbation(s).
* 0        Default (1st order nuclear and electric field).        
* IJK        Nuclear Kth order. Electric field Jth order. Magnetic field Ith order.        
* 1000        Generate simulated density derivatives.        
Only 1, 10, and 11 are valid in overlay 7 (I is used in other overlays).
### IOp(7/16)
Number of translations and rotations to remove during redundant coordinate transformations.
* -2        0.        
* -1        Normal (6 or 5 for linear molecules).        
* 0        Default, same as -1.        
* N        N.        
### IOp(7/18)
Derivative accuracy option.
* 0        Compute to 10^-8 accuracy.        
* 1        Do as accurately as possible in L702.        
* 2        Use the original ‘BERNY’ values in L702.        
* 10        Do as accurately as possible in L703.        
* 20        Use sleazier cutoffs in L703.        
* 100        Do as accurately as possible in L708.        
* 200        Use sleazier cutoffs in L708.        
### IOp(7/19)
`L703`: Sets ICntrl for DFT.
* 0        Default based on job.        
* 20000        Added to default to use DBF logic for spherical atoms.        
* N        Use N+100/200 for 2nd/1st derivatives.        
### IOp(7/25)
Type of derivatives available.
* 0        First.        
* 1        Second.        
* 2        Third.        
* 10        Read derivatives from checkpoint file (in input orientation).        
* 20        Read almost all derivatives from chk file (in the input 
orientation), except take fd tensor derivatives from the rwf in the 
standard orientation. For the second step of Raman/ROA using mixed basis
 sets.        
* 30        Same as 10, but set up for anharmonic differentiation.        
* 40        Same as 30, but after VibFrq store derivs from chk file in file 
IOCPFX and leave derivs from the current job in the standard places.        
* 100        3rd derivatives, DEDerv, D2FDPrp, DMag are Cartesian (numerical) derivatives (default).        
* 200        3rd derivatives, DEDerv, D2FDPrp, DMag are normal-mode (numerical) derivatives.        
### IOp(7/28)
`L703`: Skip option to defer integral evaluation.
* 0        Default (1).        
* 1        Compute as normal.        
* 2        Do all gradient integrals in L703.        
### IOp(7/29)
`L716`: Mode of use.
* 0        Normal, same as 2.        
* 1        Normal + Generate estimated initial force constants.        
* 2        Normal.        
* 6        Nuclear repulsion only (useful for testing).        
### IOp(7/30)
Use of symmetry in overlay 7.
* 0        Use (subject to availability).        
* 1        Don’t use.        
### IOp(7/31)
Handling of forces contributions.
* 0        Just use the forces in IRWFX.        
* 1        Compute HF forces from D2E file & incr. both FX and FXYZ (non-O11 PSCF grad & HF freq).        
* 00        Use FX in conversion of force constants to internal coordinates (HF freq, PSCF Freq=Numer).        
* 10        Use FXYZ in conversion of forces constants to internal cords (PSCF opt with HF 2nd deriv).        
### IOp(7/32)
Punch option.
* 0        None.        
* 1        Punch energy in format D24.16, forces and lower triangular force constants in format 6F12.8.        
* 2        Punch nuclear coordinate derivatives. Forces are punched in 3D20.12 
format, one card per atom. Force constants and third derivatives are 
punched in 4E20.12 format in compressed form.        
* 3        Punch energy, coordinates, and derivatives in Cartesians and redundant internals.        
* 4        Punch energy, coordinates, and derivatives in redundant internals only in compressed form.        
* 5        Punch energy, first and second derivatives in both Cartesian and internal coordinates.        
* 1x        Do punch only if second derivatives are available.        
### IOp(7/42)
1PDM.
* 0        Use SCF total density.        
* N        Use generalized density N.        
### IOp(7/44)
Handling of an applied electric field.
* -1        Do not add electric field terms to forces.        
* 0        Update forces for a uniform electric field.        
* 1        Update forces for the self-consistent reaction field (SCRF) method.        
* 2        Update forces for a uniform electric field, with forces done the usual way for CIS or MP2 2nd derivatives.        
### IOp(7/45)
Controlling the projection of the reaction path.
* 0        Do not project. The point is a stationary point.        
* 1        Project the reaction path and compute 3N-7 frequencies.        
* 2        Project using the Newton-Raphson step.        
* 3        Project using forces if the RMS force is larger than 1.d-3 atomic mass units.        
* 4        Conical intersection seam, state 2.        
* 5        Conical intersection seam, state 1.        
* 6        Conical intersection seam, final processing.        
### IOp(7/60-62)
Override standard values of IRadAn, IRanWt, and IRanGd.
### IOp(7/63)
Whether to do FMM.
* 0        Use global default.        
* 1        Turn off FMM here regardless.        
* 2        Turn on FMM here if it is on elsewhere.        
* 3        Turn on FMM here regardless.        
* 100        Turn off FoFCou as well as FMM.        
### IOp(7/64)
Type of simulated spectrum in output.
* 0        Default (1).        
* 1        Lines.        
* 2        Lorentzians.        
* 3        Both.        
### IOp(7/65)
Harmonic constraints with respect to initial structure during geometry optimization.
* -1        No.        
* 0        Default (Yes, if ref structure is present and has non-zero force constants).        
* 1        Yes.        
### IOp(7/70)
Do vibro-rotational analysis.
* 0        Default (No).        
* 1        Yes.        
* 2        No.        
### IOp(7/71)
Do vibrational 2nd order perturbation.
* 0        No.        
* 1        Yes.        
* 2        Yes, initial point.        
* 10        Do FC.        
* 20        Do FCHT.        
* 30        Do HT.        
* 100        Do emission rather than absorption.        
### IOp(7/72)
Read additional parameters for anharmonic computations.
* 0        No.        
* 1        Yes.        
* 2        Read an input section specifying the normal modes to consider in the anharmonic calculation.        
* 3        Read both.        
### IOp(7/74)
Non-equilibrium PCM gradients.
* 0        No.        
* 1        Yes.        
### IOp(7/75)
Threshold for printing redundant internal contributions to normal mode displacements.
* 0        Default (10%).        
* N        10^-N.        
* -1        Zero (all printed).        
The threshold is automatically lowered for each mode until 90% of the absolute displacements are included.
### IOp(7/76)
`L703`: Override use of FoFCou.
* -1        Same default choice as the rest of the program.        
* 0        Defaults to 1.        
* 1        Force FoFCou.        
* 2        Prohibit FoFCou.        
### IOp(7/77)
Debugging options for DBFs.
* 0        Normal processing.        
* 1        Omit subtraction and do P(Fit)*Jx*P.        
* 2        Copy fit density over real density and do P(Fit)*Jx*P(Fit).        
* 3        Turn off 1c logic for 1c DBF case.        
* 4        Clear real density and do -1/2 P(Fit)*Jx*P(Fit).        
### IOp(7/87)
Accuracy in FoFJK/CalDSu.
* 0        Default, 10^-10 for molecules, 10^-12 for PBC.        
* N        10^-N.        
### IOp(7/88)
Compression of output force constants.
* 4        Force constants are stored over active atoms only.        
* &#8800 4        All other values mean full storage here (default).        
### IOp(7/89)
IDoV for Harris gradient.
* 0        Default (1).        
### IOp(7/90)
Vibrational analysis for large systems.
* 0        Do regular vibrational analysis.        
* -1        Do full analysis, but exclude frozen atoms.        
* -2        Do full analysis, but exclude frozen atoms, and only print the non-frozen atoms.        
* N        Compute N lowest modes.        
### IOp(7/91)
Selection of particular normal modes for analysis.
* 0        Default (1).        
* 1        Show all normal modes.        
* 2        Read input specifying how to select modes.        
* 3        Show all modes, sorted by layer.        
* 4        Show all modes which are primarily on the smallest model system.        
* 5        Show all modes which are primarily on either model system in a 3-layer ONIOM.        
### IOp(7/92)
Whether to save normal modes and intensities on disk, or read them from disk.
* 0        Default (save unless reading).        
* 1        Save.        
* 2        Don’t Save.        
* 3        Save selected modes.        
* 00        Default (don’t read).        
* 10        Read.        
* 20        Don’t Read.        
### IOp(7/93)
Whether to zero out derivatives with respect to frozen atoms.
* 0        Default (1).        
* 1        Yes.        
* 2        No.        
* 3        Check ICNUse.        
### IOp(7/102)
Control of FMM for nuclear repulsion.
* 0        Default: Use for 5K or more atoms.        
* N        Use for N or more atoms.        
* -1        Always use FMM.        
* -2        Never use FMM.        
### IOp(7/120)
Store nuclear repulsion energy as total energy?
* 0        Default (No).        
* 1        Yes.        
### IOp(7/121)
Read additional parameters for FCHT calculations:
* 0        No.        
* 1        Yes.        
* 2        Read an input section specifying the normal modes to consider in the anharmonic calculation.        
* 3        Read both.        
### IOp(7/122)
Generation of G- in L716. (IAprBG in Red2BG).
### IOp(7/123)
Print partitioning of ONIOM vibrational frequencies into 
contributions from individual sub-calculations. see Vreven et al. JCTC, 
2012, DOI: 10.1021/ct300612m
* 0        Don’t do ONIOM frequency analysis.        
* 1        Do ONIOM frequency analysis.        
### IOp(7/124)
Reserved for options for VibRot.
### IOp(7/125)
Mode of operation of L717:
* 0        Default (1).        
* 1        GDV defaults.        
* 2        Pisa defaults.        
### IOp(7/126)
Type of overlay 7, for printing:
* 0        Default (1).        
* 1        Normal derivative calculation.        
* 2        Process integrated ONIOM or counterpoise derivatives.        
## Overlay 8 
### IOp(8/5)
Whether to pseudo-canonicalize ROHF orbitals.
* -2        Yes, and save over canonical MOs setting ILSW for UHF.        
* -1        Yes.        
* 0        Default (Yes if ROHF).        
* 1        No.        
### IOp(8/6)
Bucket selection.
* 0        Buckets for MP2: (IA/JB).        
* 1        Buckets for stability: (IA/JB), (IJ/AB).        
* 2        Buckets for CID or MP3: (IJ/AB), (IA/JB), (IJ/KL).        
* 3        Buckets for semi-direct MP4DQ, CISD, QCISD, BD: (IJ/AB), (IA/JB), (IK/KL), (IJ/KA).        
* 4        CISD or MP4SDQ or MP4SDTQ, but includes (IA/BC).        
* 5        The complete set of transformed integrals.        
* 6        Full transformation if this is consistent with MaxDisk, otherwise same as 3.        
* 7        Full transformation if this is consistent with MaxDisk, otherwise same as 4.        
### IOp(8/7)
SCF convergence test.
* 0        Test that SCF has converged.        
* 1        Do not test SCF convergence (mainly used for testing).        
### IOp(8/8)
`L811`: Whether to delete MO integrals.
* 0        Default (No).        
* 1        Yes.        
* 2        No.        
### IOp(8/9)
`L802`: Debug control.
* 0        Operate normally.        
* -N        Force N orbitals per pass.        
`L804`: Direct Transformation Control.
* 0        Operate normally.        
* 1        Generate and test RInt3 array (L804).        
* 2        Accumulate MP2 force constant terms in direct fashion.        
* 3        Write the MO basis first derivative ERI’s to disk.        
* 10        Force fully in-Core algorithm (L804 only).        
* 20        Force transformed integrals in Core algorithm.        
* 30        Force semi-direct transformation.        
* 100        Force output bucket in Core anti-symmetrization.        
* 200        Force sorting for output bucks.        
* 1000        Force semi-direct mode 1.        
* 2000        Force semi-direct mode 2.        
* 3000        Force semi-direct mode 3 if IOp(8/6)=3.        
* 4000        Force semi-direct mode 4 if IOp(8/6)=3.        
* 00000        Default (10000).        
* 10000        Do not symmetry compress transformed integrals.        
* 20000        Do symmetry compress transformed integrals (buckets) (This will cause windowed MOs, reordered in the order of representations like occ-rep1,occ-rep2,… virt-rep1,virt-rep2,… eigenvalues and symm. assignment vectors will be put in correspondence with vectors. VGZ).        
* 30000        Symmetry compress transformed integrals only if RHF. (Upper triangle of symmetry compressed integrals for IOp(8/6)=5 or 4 only! (VGZ)).        
* 40000        Store buckets of single-bar integrals, not symmetry compressed.        
* 100000        Reorder MOs, eigenvalues and symmetry assignment vectors according to the representations.        
### IOp(8/10)
Window is selected as follows:
* -N        Use the top N occupieds and lowest N virtuals.        
* 0        Default, same as 4.        
* N        1 ≤ N ≤ 89 selects frozen-core type N.        
* 1        The largest noble gas core is frozen.        
* 2        G2 frozen-core: the largest noble gas core and main group d orbitals are frozen, except that the outer sp electrons of 3rd row and later alkali and alkali earth elements are retained.        
* 3        The next to the largest noble gas core is frozen.        
* 4        The largest noble gas core and main group d’s are frozen.        
* 5        G3 frozen-core: the largest noble gas core is frozen, except that the outer sp electrons of 3rd row and later alkali and alkali earth elements are retained.        
* 6        G4 frozen-core: the largest noble gas core is frozen, except that the outer sp electrons of 2nd row and later alkali and alkali earth elements are retained. For basis sets with double-zeta cores, core virtuals are also frozen.        
* 7        CBS-Wes core:  noble gas except 3sp valence K-Zn, 3d valence Ga-As.        
* 90        Use all MOs.        
* 91        The window is specified by IOp(8/37-38). If IOp(8/37) is 0, a card is read in indicating the start and the end. A negative value for the end deletes the top virtuals.        
* 92        The window is recovered from RWF 569.        
* 93        The window is recovered from file 569 on the checkpoint file.        
* 94        Read a list of orbitals to freeze.        
* 000        Default (200).        
* 10x        Use orbital energies to choose core orbitals.        
* 20x        Use overlap with atomic core orbitals from Harris to choose core orbitals.        
* 30x        Use overlap with atomic core orbitals from Core Ham to choose core orbitals.        
### IOp(8/11)
MO coefficient, orbital energy, and number of electrons test.
* 0        Default, same as 2 except for during BD iterations or BD=Read.        
* 1        Just print a warning message.        
* 2        Kill the job if any MO coefficients are greater than 1000.0 or the smallest difference between occupied and virtual orbital energies is less than 0.001. Also, kill a frozen-core job if there is significant core-valence mixing in the canonical orbitals.        
* 00        Default, same as 10.        
* 10        Suppress such a test (CPHF may still be done for such a case).        
* 20        Kill the job if there is no corr. energy; e.g., if there is only 1 electron or 1 virtual spin-orbital.        
### IOp(8/16)
`L811`: Maximum number of orbitals per pass (only if integral derivative file is being written). Default is as many as fit with Max Disk.
### IOp(8/18)
`L811`: Which type of derivative transformation to do.
* 0        Default, same as 3.        
* 1        Non-canonical, Uij,x = -1/2 Sij,x.        
* 2        Canonical, Uij,x = (Fij,x – EjSij,x) / (Ei-Ej) Note that this blows up for degenerate orbitals and is intended primarily for debugging.        
* 3        Non-canonical, Uij,x = -1/2 Sij,x, except canonical in frozen-active blocks.        
* 4        Non-canonical, Uij,x = -Sij,x Uji,x = 0.        
* 5        Canonical occupieds, Uab,x = -Sab,x/2.        
* 6        Canonical virtuals, Uij,x = -Sij,x/2.        
### IOp(8/19)
`L811`: The nature of the perturbation(s).
* 0        Default (1st order nuclear and electric field).        
* IJK        Nuclear Kth order. Electric field Jth order. Magnetic field Ith order.        
### IOp(8/20)
`L811`: Which terms to include.
* 0        Default (same as 11).        
* 1        MO derivative times integral term.        
* 10        MO times integral derivative term.        
### IOp(8/23)
`L811`: Algorithm control.
* 0        Default (32).        
* 1        Unused.        
* 2        Accumulate MP2 force constant terms in direct fashion.        
* 3        Write the MO basis first derivative ERI’s to disk.        
* 20        Force fully direct.        
* 30        Force semi-direct.        
### IOp(8/24)
Whether to try to transform old amplitudes on the checkpoint file.
* 0        Default: 1 if doing BD=Read and amplitudes are present; 2 otherwise.        
* 1        Yes.        
* 2        No.        
* 10        Transform Z-amplitudes as well.        
* 20        Do not transform Z-amplitudes as well.        
* 000        Default, transform EOM amplitudes if transforming ground-state ones.        
* 100        Transform EOM amplitudes.        
* 200        Do not transform EOM amplitudes.        
### IOp(8/28)
`L921, L922`: Hack number of occupieds for full CI.
* -1        Transform all orbitals (after freezing core) as occupieds (i.e., set NOA=NOB=NROrb in transformation).        
* 0        No.        
* N        Transform N orbitals (after frozen core) as occupieds (i.e., set NOA=NOB=N for purposes of transformation).        
### IOp(8/29)
`L811`: Requested diskusage. This will determine the number of times AO integrals and derivatives are evaluated unless overridden by IOp(8/31). This only applies if the integral derivatives are not stored.
* -3        Use as much as desired, independent of MAXDISK.        
* -2        Use an amount which is similar to the maximum disk usage in other parts of the MP2 freq. code.        
* -1        Use as much as needed for maximum efficiency, subject to the limit imposed by MAXDISK.        
* 0        Default (-1).        
* N        N evaluations and hence N coarse tiled batches (1…6 are the currently implemented options).        
### IOp(8/30)
Type of window.
* 0        Default. Set up /Orb/ as indicated by IOp(8/10).        
* 1        Test window. Set up for full but zero core MOs.        
* -1        Set up /Orb/ for a full window but then blank the wavefunction coefficients in L804.        
### IOp(8/36)
Whether to update force constants with the MP2 product of MP2 integral derivatives term (only applies if integral derivative file is not written).
* 0        Default (Yes).        
* 1        Yes.        
* 2        No.        
* 00        Default on whether to make Poo and Pvv for MP2. (Yes if Ix is not stored, no otherwise).        
* 10        Yes.        
* 20        No.        
### IOp(8/37)
Integer specifying first window parameter (n).
### IOp(8/38)
Integer specifying second window parameter (m).
### IOp(8/39)
Localized orbital method adopted in SAC/SAC-CI.
* 0        Default. No localization.        
* 1        Boys method.        
* 2        Population method.        
* 3        Boys + population method.        
### IOp(8/40)
Handling of ROHF window.
* 0        Default (2).        
* 1        Use ROMP2 approach, forming pseudo-canonical alpha and beta orbitals and doing UHF transformation.        
* 2        Treat as RHF, transforming only alpha orbitals.        
### IOp(8/41)
Transformation of spin-orbitals (alpha only) within occupied and unoccupied orbital subspaces by minimum orbital-deformation (MOD) method.
* 0        Default. No.        
* 1        No, but save MOs.        
* 2        Yes. Take reference MOs from disk if available.        
* 3        No for the 1st geometry of opt, yes otherwise.        
### IOp(8/42)
Whether to reorder MOs during potential surface exploration.
* 0        No.        
* 1        Yes.        
* 2        Yes (for SAC-CI single point calculation).        
* 00        Use orbital energies in ordering.        
* 10        Don’t use orbital energies in ordering.        
* 000        Use second moments in ordering.        
* 100        Don’t use second moments in ordering.        
* 0000        Use dipole moments in ordering.        
* 1000        Don’t use dipole moments in ordering.        
### IOp(8/46)
Indicates special case of non-HF calculation.
* 0        Default – MOs are canonical HF orbitals.        
* 1        Input orbitals are not canonical HF and pseudo-canonical orbitals must be generated here for the post-SCF.        
* 10        Generate HF pseudo-canonical even if the original SCF method was not (i.e., Kohn-Sham).        
### IOp(8/47)
Whether L804/L811 should generate results compressed over active atoms.
* 0        Default (2).        
* 1        Active atoms.        
* 2        Full list.        
* 3        Full list, but blank contributions from inactive atoms (no difference from 2 for overlay 8).        
* 4        Active atoms, and store Hessian contributions over active atoms only.        
### IOp(8/60-62)
Over-ride standard values of IRadAn, IRanWt, and IRanGd. For DFTCV, IRadAn defaults to 299974 rather than the global default.
### IOp(8/68)
EOM-CCSD
* 0        No EOM.        
* 1        Do EOM with the default algorithm (right and left spaces separately).        
* 11        Do EOM doing only the transition energy (right space).        
* 21        Do EOM doing right and left eigenvectors using the same expansion space for both.        
* 31        Do EOM doing right and left eigenvectors using biorthogonal expansion spaces.        
### IOp(8/69)
EOM: Number of states per irreducible representation (largest Abelian subgroup) to do.
* 0        Default (2).        
* N        N per irreducible representation.        
* -1        Read the number for each irreducible representation, all from one line.        
The order of irreducible representations is the same as printed for symmetry-adapted basis functions by L301.
### IOp(8/87)
Accuracy of integrals.
* 0        Default (12).        
* N        10^-N.        
### IOp(8/105)
Convergence of amplitudes for EOM iterations.
* 0        Default (1.d-5).        
* N        10^-N.        
### IOp(8/106)
Number of EOM states for LR transition densities.
* 0        Default (None).        
* -1        All.        
* N        First N of each symmetry.        
### IOp(8/107)
EOM state of most interest.
* 0        Default (1st excited state).        
* N        N^thexcited state.        
### IOp(8/108)
EOM-CCSD: Total number of states to do. Guesses are taken from the checkpoint file if RdAmp was specified, with remaining states taken from the CIS guess in CIS energy order.
* 0        Default (2*NIrrep)        
### IOp(8/109)
IFact for Davidson in EOM-CC.
### IOp(8/110)
State-to-State transition dipoles in EOM-CC:
* 0        None.        
* 1        From state NRoot to higher states.        
* 2        From state NRoot to higher and lower states.        
### IOp(8/111)
MaxIt for EOM.
### IOp(8/112)
MaxMin for EOM.
### IOp(8/113)
WhenSc for EOM.
### IOp(8/114)
IRdLft for EOM.
### IOp(8/115)
IFirst for EOM.
### IOp(8/116)
Compute DFT estimate of core-core and core-valence correlation?
* 0        Default.        
* 1        Yes.        
* 2        No.        
* 10        Include empirical corrections for total energies.        
* 20        Do not include empirical corrections.        
The default is not to compute the correction, and if the correction is requested, to include the total energy terms only for CBS-Wes style frozen-core (the only case for which they have been determined). Corrections are only included for elements H-Ar.
### IOp(8/123)
Flag for SOS in EOM.
## Overlay 9 
### IOp(9/5)
Method
* 0        CISD. Configuration interaction with all single and double substitutions.        
* 1        CID. CI with all double substitutions.        
* 2        MP3. Third-order perturbation theory.        
* 3        MP4(DQ). Fourth-order perturbation theory in the space double and quadruple substitutions.        
* 4        MP4(SDQ). Fourth-order perturbation theory in the space single, double and quadruple substitutions.        
* 5        MP4(SDTQ). Full fourth-order perturbation theory in the space of single, double, triple, and quadruple substitutions.        
* 6        CCD. Coupled cluster theory with double substitutions.        
* 7        CCSD. Coupled cluster theory with single and double substitutions.        
* 8        QCISD.        
* 9        BD.        
### IOp(9/6)
`L913`: Criteria for termination of the iteration.
* 0        Default convergence criterion and maxcycle.        
* -2        Use regular default maxcycles even for BD.        
* -1        Read in maxcycles and convergence criterion (I2,D18.13).        
* N        Max N cycles.        
### IOp(9/7)
Update the energy in Common/GEN/.
* 0        Yes, with the correlation energy, ECID in CID, ECISD in CISD EUMP3 in MP3, and EUMP4 in MP4 calculations.        
* 1        Yes, with EUMP3.        
* 2        Yes, with EMP4(SDQ) or EMP4(DQ) If singles are not available.        
* 7        No.        
### IOp(9/8)
`L902`: Constraint on output wavefunction for stability calculations (see link 902).
`L907, L919`: Number of roots (default 1 in 907 and 10 in 919).
`L906`: Term and method selection for debugging.
* 0        Default — all terms, L using AOs if frozen-core, using MOs if full.        
* 1        Do AA only (semidirect only).        
* 2        Do AB only (semidirect only).        
* 3        Do BB only (semidirect only).        
* 4        Do BA only (semidirect only).        
* 10        Force out-of-core semidirect method.        
* 20        Force out-of-core and quartic I/O method for L.        
* 30        Force out-of-core and qintic I/O method for L.        
* 100        Do L using AO integrals rather than <ia||bc>.        
* 200        Do L using <ia||bc>.        
* 300        Do 2nd order sigmas instead of L.        
* 400        Do 2nd order sigmas for ionization of active occupieds only, including contributions from all orbitals including inactive ones.        
* NN000        Permute occupieds as for NN processors, regardless of actual number.        
`L913`: Whether to use fast routines.
* 0        Default (Slava, fast and R where possible).        
* 1        Original code (DD1,2,3, UMP41,2,3,4) for first iteration.        
* 2        Use DD[1-3]R and UMP4xR (closed-shell) on 1st iteration.        
* 10        Original code for 2nd and later iterations.        
* 20        Use DD[1-3]R and UMP4xR (closed-shell).        
* 30        Use DD1, UMp41U, UMP42, UMP43, DD4UQ.        
* 40        Use DD1R, UMP41R, UMP42, UMP43, DD4RQ (closed-shell).        
* 000        Default, same as 1.        
* 100        Original routines.        
* 200        Slava routines.        
The defaults are 22 for RCI, 11 for UCI, 42 for RQCI, and 31 for UQCI.
`L914`: State of interest.
* -3        Repeating stable=opt. End diag. as soon as we have a vector with a negative diagonal element.        
* -2        Do a stable=opt calculation.        
* -1        Do a stability calculation.        
* 0        We are not doing gradients, FP or CIS-MP2        
* N        We are interested in the N^th excited state.        
### IOp(9/9)
Convergence criterion (on energy for L913, wavefunction for L914).
* 0        Default:        
*          L913 single point: 10^-7 energy, 10^-5 wfn.        
*          L913 gradient or EOM-CCSD: 10^-8 energy, 10^-6 wfn.        
*          L914 single point: 10^-4 wfn.        
*          L914 gradient: 10^-6 wfn.        
* N        10^-N.        
### IOp(9/10)
`L914`: Whether to do "fake" frozen-core (i.e., with a full transformation).
* 0        No; follow /Orb/.        
* 1        For AO usage (unused here).        
* 2        Yes, note number of frozen core and virtual and reset /Orb/ for full.        
* 3        Yes, and store full /Orb/ back on disk.        
`L902`: Test flag.
### IOp(9/11)
`L908`: Flags for Green’s function calculations.
* 0        Normal use of MO integrals.        
* 1        Force direct computation of <ab||cd> contributions.        
* 2        Force direct computation of <ia||bc> contributions.        
* 00        Normal production of intermediates (in-core if possible).        
* 10        Force use of sort for intermediates.        
* 100        Read window of MOs to refine in the same format as 801, but with two ranges on the same line for open-shell.        
* 1000        Force N^3 algorithm in GFSCMA.        
* 00000        Default (2).        
* 10000        P3 for ionizations and affinities.        
* 20000        OVGF.        
* 30000        OVGF + P3 for ionization (+ P3 for affinities, if <ia||bc> present)        
* 40000        2nd order only.        
* 50000        P3 + PPH3 (ionization) , or HHP3 (affinities).        
* 60000        Truncation of virtual space.        
* 70000        Make OVGF but remove (C1+D1). i.e. PPH3r.        
* 80000        Default (P3 for ionizations).        
* 100000        Read EMin, EMax, and pole strength warning level on one line. Link 909 only.        
* 1000000        Save Dyson orbitals over the canonical MOs.        
`L902`: Test flag.
`L913`: Spin projection control.
* 0        Default (1).        
* 1        Do basic projection.        
* 2        Include triples.        
### IOp(9/12)
`L902`: Test flag.
`L908`: Debug flag.
### IOp(9/13)
`L902`: Symmetry constraint of output wavefunction from Stable=Opt.
* 0        Yes.        
* 1        No.        
`L909`: 1 for Test mode.
### IOp(9/14)
Non-iterative corrections.
ICNonI
* 0        No.        
* 1        Fourth-order triples.        
* 2        Fourth- and fifth-order singles and triples –QCISD(T), BD(T).        
* 3        Same as 2, but save the amplitudes.        
* 4        Same as 2, but do E4T as well.        
### IOp(9/15)
Type of derivative information generated.
* 0        None.        
* 1        Do Lagrangian in L906, L913, L914, L916.        
* 2        Do AO 1st derivative terms as well in L906 and L914.        
* 3        Set up for second derivatives in L906 and L914, doing the non-separable AO 2nd derivative terms in L906.        
* 4        Do L and GIAO L(x) in L906.        
* 5        Set up for second derivatives without AO terms. Same as 3 for L914; skips AO derivatives in L906.        
### IOp(9/16)
`L906`: Control of (Semi-) Direct MP2.
* -N        Do a maximum of (-N-6) occupieds per pass, using the fully out-of-core algorithm.        
* -6        Force the fully in-core algorithm.        
* -5        Try to minimize integral evaluations as for -3, but also force use of the fully out-of-core algorithm in Tran4D.        
* -4        Force a single integral evaluation as for -2, but also force use of the fully out-of-core algorithm in Tran4D.        
* -3        Try to minimize integral evals, using fully direct methods if possible, otherwise spill to disk.        
* -2        Force a single integral evaluation (two for UMP2) using disk-based algorithm.        
* -1        Force in-memory algorithm (fully direct MP2, requires 2OVN words of memory for E2, 2N^3 words for derivatives).        
* 0        Default (same as -3).        
* M        Use disk storage for partially transformed integrals handling M occupieds at once.        
`L913, L914`: Control of in-core integrals for W(Tilde).
* -6        Force in-core storage.        
* -3        Suppress in-core storage.        
* 0        Default: in-core if possible.        
* 1        Use AO integral algorithm (L914 only).        
### IOp(9/17)
`L914`: Functional to use.
`L918`: Auto-adjustment of TAU.
### IOp(9/18)
Iteration scheme: DE = (in A(S) = W(S)/(DE-DELTA(S))) I.E. in the formation of a new wavefunction.
* 0        Use DE depending on the method used. (IOp(9/5)). For method = 0,1 DE = W(0)/A0. For method GT.1 DE = 0. Note that for perturbation methods (Method=2,3,4,5) DE is not really needed since the wavefunction formed never gets used.        
* 1        W(0)/A0. Always.        
* 2        0. Always.        
### IOp(9/19)
Extrapolation.
* 0        Default: CI using old extrapolation, CC/QCI using RLE.        
* 1        Do not extrapolate.        
* 2        Use BFGS.        
* 3        Use DIIS.        
* 4        Use old extrapolation for CI.        
* 5        Use RLE.        
* 00        Use A as guess for Z.        
* 10        Use scaled A as guess for Z.        
* 100        Reset RLE for Z iterations.        
### IOp(9/20)
`L901`: Whether to update the total energy with the MP2 energy.
* 0        Yes.        
* 1        No (used in HF second derivative calculations).        
### IOp(9/21)
`L902`: Guess for eigenvector of y-matrix.
### IOp(9/22)
`L919`: Conversion factor.
* -1        Read in factor in format D20.10.        
* 0        Default of 10^-8.        
* N        10^-N.        
### IOp(9/23)
`L919`: Localization of orbitals.
* 0        None.        
* 1        Localize occupieds.        
* 2        Localize virtuals.        
* 3        Localize both.        
* 00        Default (same as 10).        
* 10        Choose configurations by simple truncation.        
* 20        Read in configurations.        
* 000        Rettrup-Davidson RPA.        
* 100        Jorgensen-Linderberg Hermetian RPA.        
* 0000        Out-of-core method.        
* 1000        In-core method.        
* 00000        Singlet states.        
* 10000        Triplet states.        
`L921, L922`: Maximum order of perturbation theory.
`L914`: Correction to CIS.
* 0        No.        
* -2        Do primitive CIS-DFT.        
* -1        Yes (in primitive in-core program).        
* 1        Yes (in MO Basis disk routine).        
* 2        Do CIS-DFT instead.        
* 3        Do CIS(D) with old N^6 algorithm.        
* 4        Do CIS(D) with N^5 algorithm.        
The functional is given by IOp(17).
### IOp(9/25)
Print pair contribution and weight to correlation energy.
* 0        No.        
* 1        Yes, at the end of CI.        
* 2        Yes, at each cycle.        
* 3        Yes, at one cycle given by input (I3).        
* 4        Yes, at first cycle and at end.        
### IOp(9/26)
Normalization of the wavefunction.
* 0        Normalized to A(0) = 1.        
* 1        SUM(S) A(S)^2 = 1 (ALL S).        
NOTE: Perturbation theoretical results are valid with NORM=0 ONLY.
### IOp(9/28)
Printing of dominant configurations.
* 0        Default (print coefficients 0.1 and above).        
* -3        Do not print coefficients.        
* -2        Print all coefficients every iteration.        
* -1        Scan the ‘A’ vector and print all coefficients.        
* N        Scan the ‘A’ vector and print all coefficients having coefficients greater than 0.0001*N.        
### IOp(9/30)
Calculation of the one-particle density matrices:
* 00        Default (21 for CI, 22 otherwise).        
* 1        Compute the CI one-particle density matrix.        
* 2        Do not form the CI one-particle density matrix.        
* 10        Compute the density correct to second order (NOT the same as the density corresponding to the MP2 energy).        
* 20        Do not compute the density correct to second order.        
### IOp(9/31)
`L902, L918`: Print vectors and matrices.
* 0        No.        
* 1        Yes.        
### IOp(9/36)
Compute the T1 Diagnostic of T.J. Lee.
* 0        No.        
* 1        Yes.        
### IOp(9/37)
The Maximum dimension for the coupled cluster extrapolation. The default is 5 for RLE, and 10 for BFGS.
### IOp(9/38)
Minimum dimension for the BFGS coupled cluster. The default is 3. Not meaningful for DIIS extrapolation.
### IOp(9/39)
`L914`: Pick out guesses from restart file or orthogonalize guesses to the states already on restart file (IOp(49) must be set to 1 or 2 for this option to be valid)
* 0        Just take guess from restart file.        
* N        Make N additional orthogonal guesses to those present.        
* -1        Read which N states to use (free format integers).        
Warning: The states on the restart file MUST be orthogonal to the convergence requested (ie; the previous job indicates wavefunction not just expansion vectors has converged).
### IOp(9/40)
`L906`: Reference wavefunction for MP2.
* 0        Default (HF).        
* 1        CASSCF.        
* 2        HF.        
`L913, L914`: Threshold for printing eigenvector components.
* 0        ITHR = 1        
* N        ITHR = N        
Where threshold = GFLOAT(10)^-ITHR
### IOp(9/41)
`L914`: Number of states to seek when using Davidson or number of states to print out information for when using DODIAG.
* 0        Default to 2 lowest.        
* N        N states.        
* -N        Read in principle component of N guesses (DAVIDSON) format I5 on last card before EOF.        
### IOp(9/42)
Method and matrix blocks to work on in L914 (See below)
* -NNN        Mapped directly to NNN below.        
* 1        AO basis.        
* 2        In-core. Mapped to 2, 222, or 20 as appropriate.        
* 3        MO Mapped to 3, 333, or 30 as appropriate.        
* 0        DEFAULT IS: 3 (RHF reference state)        
* 333        (UHF reference state)        
Bits Matrix Method
* 1        AA,BB }        
* 10        AB (NYI) }–> Force DAVIDSON in A.O. basis.        
* 100        BA (NYI) }        
* 2        AA,BB }        
* 20        AB }–> Force DODIAG to find all roots.        
* 200        BA }        
* 3        AA,BB }        
* 30        AB }–> Force DAVIDSON in M.O. basis.        
* 300        BA }        
### IOp(9/43)
`L914`: How to handle subsequent Davidson iterations.
* -N        Reduce after iteration N but also include states skipped due to energy criteria at the first iteration only.        
* -1        Do only the requested number of states from the beginning.        
* 0        Default: (0 if restart, 1 for TD, 2 for TDA).        
* N        Davidson reduces the number of states after iteration N.        
The number of extra states to do initially is set by IOp(117).
### IOp(9/44)
`L914`: Density matrix control for filling RWF 633.
* 0        Same as 2.        
* 1        Do densities of each excited state.        
* 2        Do densities and transition densities from ground.        
* 3        Do densities, transition densities from ground, and transitions densities among all excited states.        
* 1x        Do DCT analysis of charge-transfer character for each state.        
### IOp(9/45)
`L914`: Debug option for comparing previous results.
* 0        Use Phycon to convert to eV’s.        
* 1        Use old conversion to eV’s.        
### IOp(9/46)
`L914`: Control of Davidson convergence.
* <0        Use Ortvec convergence only.        
* 0        Converge on the number of roots – IOp(41).        
* N        Converge on Ci Amplitudes for N lowest states.        
### IOp(9/47)
`L914`: Control of Davidson iterations.
* 0        Usual.        
* 1        Don’t do any iterations (Guess=Print).        
* 2        Stop after first iteration.        
### IOp(9/48)
Restriction on types of roots (Davidson RHF only).
* 0        Guess only singlets.        
* 1        Same as 0.        
* 2        Guess both singlets and triplets.        
* 3        Guess only triplets.        
* 4        Same as 2        
Note: A singlet guess may result in a triplet root in extreme cases (small number of roots sought).
### IOp(9/49)
`L914`: Initial guess vectors.
* 0        Make a guess based on diagonal elements.        
* 1        Use guess vectors already on RWF.        
* 2        Use guess vectors already on CHK.        
* 3        Generate guesses from CIS densities on CHK.        
* 4        Generate guesses from CIS densities on RWF.        
* 5        Same as 0.        
* 00        Default (20 for CIS and TDHF, 10 for TDDFT).        
* 10        Use SCF virtuals        
* 20        Use IVOs.        
* 30        Do IVOs without scaling densities (for debugging).        
* 100        Do HF IVOs even if doing TD-KS.        
* 1000        Force recomputation of integrals during IVO.        
### IOp(9/50)
Frozen-core handling for BD.
* 0        Default (2 if "fake" frozen-core transformation done).        
* 1        Old method: core orbitals are not updated from their initial values.        
* 2        Update core orbitals according to BD criteria.        
* 3        Update core orbitals acc. to BD criteria, compressing MO integrals for use during CC iterations.        
### IOp(9/60)
Override standard values of IRadAn.
### IOp(9/61)
Override standard values of IRanWt.
### IOp(9/62)
Override standard values of IRanGd.
### IOp(9/67)
`L913 and L916`: Type of convergence test.
* 0        Default: energy and gradient.        
* 1        Converge on energy only.        
* 2        Converge on energy and gradient.        
* 3        Converge on gradient only.        
Convergence on gradient is for extrapolated CI and QCISD procedures.
### IOp(9/68)
`L914`: IEOM (guess for EOM-CC)
* 0        No.        
* 1        Yes. Default the number of states to do based on number requested for EOM, and convert reading densities if requested into reading amplitudes.        
### IOp(9/70)
`L913`: CIS/TDA or TD.
* 0        Default (CIS for HF, 1 for TD-HF and TD-KS with hybrid functionals, 2 for TD-KS with pure functionals).        
* 1        RPA using general, non-Hermitean algorithm.        
* 2        RPA using Hermitean scheme for pure DFT, converted here to 1 for hybrid functionals and HF.        
* 3        CIS/TDA.        
### IOp(9/71)
`L914`: Whether to do an extra iteration after Davidson convergence.
* 0        Default (No).        
* 1        Yes.        
* 2        No.        
### IOp(9/72)
`L914`: Whether to compute frequency-dependant polarizabilities.
* 0        No.        
* 1        Yes.        
### IOp(9/73)
`L914`: Whether to do non-equilibrium solvation.
* 0        Default (Yes, if doing excited state energy without gradient, or cLR absorption or VEM, no for stability or cLR noneq=write).        
* 1        Yes.        
* 2        No, use equilibrium.        
* 00        Default (same as 1).        
* 10        Linear response.        
* 20        Corrected linear response.        
* 30        Vertical excitation model (NYI).        
### IOp(9/74)
`L914`: Override default choice of frequency dependence of the XC functional.
* 0        Use default value.        
* N        Use form N (see IOp(9/88) in overlay 5).        
### IOp(9/75)
`L906`: Whether to save amplitudes and <IJ||AB> integrals.
* 0        Save only if doing second derivatives (SqS12 set).        
* 1        Save amplitudes.        
* 2        Save amplitudes and integrals.        
### IOp(9/76)
`L914`: Maximum number of vectors during Davidson.
* 0        200.        
* N        N.        
### IOp(9/77)
Whether to save converged amplitudes on checkpoint file.
* 0        Default (No).        
* 1        Yes.        
* 2        No.        
* 0x        Default (check ILSW).        
* 1x        Ground-state amplitudes were read in. Set initial SAvail, etc. accordingly.        
* 2x        Act as though amplitudes were not read in.        
* 0xx        Default (check ILSW).        
* 0xxx        Check ILSW to see if Z-amplitudes are available.        
* 1xxx        Z-amplitudes were read in.        
* 2xxx        Do not read Z-amplitudes.        
### IOp(9/81)
`L904`: Minimum number of Pair Natural Orbitals (PNO) to start the extrapolations from, NStart.
* 0        Default — 5 (assuming CBS-4 calculations, i.e. 6-31+G(d’,p’)).        
* -N        Calculate the extrapolated value at N only.        
* N        Get the lowest energy value between CBS(N) and CBS(NVirt).        
### IOp(9/82)
`L904`: Convergence tolerance for CBS localization.
* 0        Use the default.        
* N        Use 10^-N        
### IOp(9/83)
`L904`: Localization method.
* -1        No localization.        
* 0        Default (4).        
* 1        Boys.        
* 2        Population.        
* 3        Boys+Population.        
* 4        Minimal population.        
* 5        No localization.        
* 10        Do 2nd order.        
* 100        Localize core even if not needed.        
### IOp(9/84)
`L904`: Save CBS localized orbitals to RWF (this will overwrite the SCF orbitals, intended for visualization).
* 0        No, don’t save (default).        
* 1        Yes, save them.        
### IOp(9/85)
Flags for SAC-CI.
### IOp(9/86)
`L906`: Whether to generate data compressed to active atoms during mp2 frequencies with ONIOM.
* 0        Default (2).        
* 1        Yes.        
* 2        No.        
* 3        Yes, and also store Hessian contributions over only active atoms.        
### IOp(9/87)
AO Integral threshold.
* 0        Default, N=10.        
* N        Discard contributions expected to be smaller than 10^-N.        
### IOp(9/101)
`L914, L926`: Raffenetti in DD1Dir.
### IOp(9/104)
Number of states in CIS guess for EOM-CC.
* 0        Same as regular NState (IOp(9/41).        
* N        N.        
### IOp(9/105)
Maximum batch size in CISAX:
* 0        Default, unlimited.        
* N        No more than N density/Fock matrices at a time        
### IOp(9/108)
`L906`: Whether to use matrix multiplication instead of PTrnI1 to transform the first (or back-transform the last) index.
* -1        Default. Decide on the fly looking at the ratio of NBas2p and NTT. Turned off for now.        
* 0        Default (2).        
* 1        Yes.        
* 2        No.        
* NNN0        Use matrix multiplication if the ratio NBas2p/NTT is larger than 0.NNN.        
### IOp(9/114)
`L914`: Number of EOM states per irreducible representation, used to decide on number of CIS states to do for guesses.
### IOp(9/115)
Abelian symmetry in CIS/TD:
* 0        Default, 1 for direct, 2 for in-core.        
* 1        Use the petite list.        
* 2        Replicate integrals.        
* 3        No integral symmetry used.        
* 00        Default, 10 for petite list, 20 otherwise.        
* 10        Symmetrize update vectors in DiskD.        
* 20        Do not symmetrize vectors.        
### IOp(9/116)
PCM options:
* 0        Default. PTE model: PCM only in the reference.        
* 1        Activate PTED model for CCSD and BD. This method couples the T and Z equations.        
* 2        PTE-S (ground or excited state).        
* 3        PTES (ground or excited state).        
* 4        EOM-PTE model: PTE method for ground state, but state-specific solvent response based on the L-T-R part of the EOM 1PDM for the excited state.        
* 10        Linear Response.        
### IOp(9/117)
`L914`: IFact (number of extra vectors for initial iterations):
* -N        N.        
* 0        Default – Max(4,NOp2), unless IOp(43) turns this off.        
* N        Max(4,NOp2,N).        
### IOp(9/118)
`L914`: First occupied orbital to include in guesses.
* 0        First non-frozen orbital.        
* N        Active orbital number N.        
### IOp(9/119)
`L914`: Last occupied orbital to include in guesses.
* -M        All but the highest M active occupieds.        
* 0        Last non-frozen occupied orbital.        
* N        Active occupied orbital number N.        
### IOp(9/120)
`L914`: Minimum energy threshold for initial guesses.
* -2        Read threshold in Hartrees.        
* -1        No minimum.        
* 0        Default, same as threshold for converged states.        
* N        N/1000 eV.        
### IOp(9/121)
`L914`: Minimum energy threshold for converged states.
* -2        Read threshold in Hartrees.        
* -1        No minimum.        
* 0        Default, -1.        
* N        N/1000 eV.        
### IOp(9/122)
Linear response CCSD:
* 1        Polarizability.        
* 2        Specific rotation (modified velocity gauge).        
* 3        Specific rotation (length gauge).        
* 4        Specific rotation (both MVG and LG).        
* 10        Frequency dependent LR.        
### IOp(9/124)
Epsilon-infinity for SOS with EOM.
### IOp(9/125)
Whether to make permuted copies of integral buckets.
* 0        Default (1).        
* 1        Yes.        
* 2        No.        
### IOp(9/126)
Maximum number of matrices to handle at a time in DD1Dir.
* 0        Default (-1).        
* -1        No limit.        
* N>0        At most N matrices at a time.        
### IOp(9/127)
Whether to discard MO integrals at the end of this link.
* 0        Default (21).        
* 1        Yes.        
* 2        No.        
* 10        Save IW{1,2,3}Sav if doing derivatives (for old deriv algs).        
* 20        Do not save IW{1,2,3}Sav.        
### IOp(9/128)
Approximate CC/EOM.
* 0        Default.        
* 1        EOM-MBPT2.        
* 2        P-EOM-MBPT2.        
### IOp(9/130)
Algorithm control in CISGrd.
* 0        Default (1 for CIS, 3 for TDA/TD-HF/TD-DFT).        
* 1        Single pass doing AX.        
* 2        Two passes doing (A+B)(X+Y) and (A-B)(X-Y).        
* 3        Single pass doing AX + BY.        
* 0x        Default (1).        
* 1x        Store XC overlap contributions in W.        
* 2x        Store XC overlap contributions in S1.        
### IOp(9/131)
In-Core Code.
* 0        Default (1).        
* 1        Use if possible.        
* 2        Off.        
* 3        On, error if things don’t fit.        
### IOp(9/132)
Test kill and restart.
* 0        Off.        
* 1        On.        
## Overlay 10 
### IOp(10/5)
Calculation of first derivatives of post-SCF energies. Only implemented for closed-shell and UHF.
* 0        No.        
* 1        Calc. D E(MP2) / D R        
* 2        Calc. D E(CID) / D R        
* 3        Calc. D E(CISD) / D R        
* 4        Calc. D E(CIS/TD) / D R        
* 5        Calc. D E(CCD) / D R        
* 6        Calc. D E(CCSD/QCISD) / D R        
* 7        Calc. D E(BD) / D R        
* 8        Calc. D E(MP3) / D R        
* 9        Calc. D E(MP4) /D R        
* 00        Default CPHF usage (Z-vector unless HF D2E).        
* 10        Full 3*NAtoms CPHF.        
* 20        Z-Vector method.        
* 30        Test Z-Vector using full CPHF.        
* 000        Default derivative processing — just set up here unless doing HF 2nd derivatives simultaneously.        
* 100        Compute F1 and S1 derivative terms here.        
* 200        Don’t process any derivative terms here. Setup for external processing of W and Z.        
* 0xxx        Default (1).        
* 1xxx        Compute forces.        
* 2xxx        Do nonadiabatic coupling in addition to forces, skipping CPHF. Only implemented for TD.        
* 3xxx        Do nonadiabatic coupling in addition to forces, doing CPHF. Only implemented for CIS and TD.        
* 4xxx        Do nonadiabatic coupling instead of forces, skipping CPHF. Only implemented for TD.        
* 5xxx        Do nonadiabatic coupling instead of forces, doing CPHF. Only implemented for CIS and TD.        
### IOp(10/6)
Calculation of the second derivatives of the SCF energy. Available for RHF and UHF only. Partially coded but NYI for high-spin ROHF.
* 0        No.        
* 1        Yes, do D2 E(SCF) / D R(I) D R(J).        
* 2        Setup for MP2 2nd derivatives (i.e. No contributions to the force constants are done here).        
* 3        Same as 1, but do not do any 3rd order properties.        
* 4        Same as 0 if doing post-SCF gradients or same as 2 otherwise. This makes possible to run L1014 with in the old way, i.e. using IRwP1 and IRwW1.        
* 00        Default: use new Px/Wx digestion code if possible, save as little data as possible.        
* 10        Use old Px/Wx digestion code.        
* 20        Use new Px/Wx code but save both S1 and F1 over MOs.        
* 30        Use new Px/Wx code and don’t save S1 but do save F1.        
* 100        Compute dipole derivatives using only electric field CPHF and F(x) matrices.        
* 200        Compute dipole-dipole, dipole-quadrupole, and OR tensors.        
* 300        Combination of 100 and 200        
* 1000        Set up for GIAO MP2 calculation.        
* 10000        Do DFT 3rd derivatives.        
* 20000        Do hyperpolarizabilities for second-harmonic generation.        
* 000000        Default (don’t do magnetic susceptibility).        
* 100000        Do magnetic susceptibility.        
* 200000        Don’t do magnetic susceptibility.        
### IOp(10/7)
RMS convergence on C1(I,A) contributions. The max element is tested against 10* this value.
* 0        Default: 1.D-8, except 1.D-10 for Z-Vector CPHF or SSC including Fermi Contact.        
* N        1.D-N.        
`L1003`: Accuracy of CPMCSCF convergence. Only used for Direct CPMCSCF. Convergence = 10^-K. For default value, see IOp(50).
### IOp(10/8)
Selection of linear equation solution method.
* 0        Default (same as 2, except for ZDO non-ONIOM-EE).        
* -1        Solve CPHF for each variable in a separate call to LinEq1.        
* 1        Expand each variable in a separate expansion space. This is the default and necessary for frequency-dependent perturbations at multiple frequencies, and is the default if there is only 1 perturbation or if the convergence is set to less 10.d-10.        
* 2        Solve all equations together, possibly reverting to the old (one variable at a time) method in the secondary solution. This is the default for multiple perturbations at the same or zero frequency with the default convergence.        
* 3        Invert the A matrix directly.        
* 0x        Default:  2 if memory permits, or 3 if the number of right-hand sides is significantly larger than N0 (the number after orthogonalization). If memory does not permit direct solution, then 4 if there is sufficient memory to form the inverse and the reduced dimension is still below that specified by IOp(11), or 1 if all others are rejected.        
* 1x        Use recursive DIIS with simultaneous solution.        
* 2x        Solve linear equations for all N RHS in reduced space.        
* 3x        Solve linear equations for N0 RHS in reduced space.        
* 4x        Invert the reduced A-matrix.        
* 0xx        Default NormTp in LinEq2 (3, except for 2nd order CPHF for Raman/ROA, where it depends on IOp(92)).        
* 1xx        Full normalization        
* 2xx        Normalize input vectors with norm > 1.        
* 3xx        No normalization.        
### IOp(10/10)
Control of CPMCSCF during avoided crossing/conical intersection searches.
`L1003`: The most useful options for IOp(10) are as follows (assumes L510 is run with IOp(14)=310000 or 300000):
* 600006        Optimize lowest energy point on a conical intersection (or n-1)hyperline IOp(10)=600006. This takes one state to be IOp(28) and the other IOp(28)-1.        
* 600005        As for IOp(10)=600006 but solves CP-MCSCF equation. Usually a very small correction but you must check. Needs IOp(17)=200 in l510 (Orbital Hessian).        
* 300006 or 300005        Optimize (e2-e1)^2. Not meaningful alone; can be used to start a diff. crossing search.        
* 700007        Computes the SA-CPMCSCF corrected gradient for the Ivec state, and writes it for use in other links. Also computes the SA second derivatives. (The only approximation is the neglect of the second order orbital rotation derivatives.)        
* 700006        Computes the SA-CPMCSCF corrected gradient for the Ivec state, and writes it for use in other links.        
* 000 00X        Extras at CP-MCSCF, where X=:        
*          1: Non-optimum orbitals (obsolete).        
*          2: Non-optimum vector (obsolete).        
*          3: Non-optimum orbitals without Z-vector trick (obsolete).        
*          4: Calculate Ha contribution to Der Cp via <Ci|H|Cj> disactivated.        
*          5: Conical intersection information.        
*          6: Conical intersection information without solving CP equations (approx. values).        
*          7: Compute approximation of the SA second derivatives.        
*          8: Conical intersection information using Z-vector trick. This option should be set if solving the cpmcscf equations for either a SA gradient or conical intersection optimization only compatible with IOp(50=2 or 3 or with Hessian inversion IOp(17=0).        
* 000 QL0        Reserved for future use.        
* 00N 000        Other state in grdiff/dercpl.        
*          N: Calculate the derivative couplings of the Nth state. Defaults to IOp(28)-1 so not required.        
* 0M0 000        Contribution to be included at derivative coupling, where M=:        
*          0: Both CI and orbs are included. DC=Ea+Ex+Ey.        
*          1: Only CI contribution. DC= Ea.        
*          2: CI and ortho contributions will be included. DC= Ea+Ey.        
*          3: Only orbital contribution will be here DC=Ex.        
*          4: Orbital and ortho contributions. DC=Ex+Ey.        
* K00 000        Which gradient to use at the optimization links, where K=:        
*          0: (Scaled gradient difference or Fxyz).        
*          1: Derivative coupling(without division by energy diff.)        
*          2: -//- -//- (after -//- -//- -//-)        
*          3: Unscaled gradient difference * E2-E1.        
*          4: Projection of ivec gradient.        
*          5: Read forces from the input stream (test purposes).        
*          6: Normalized gradient difference * E2-E1 + projected ivec gradient (conical intersection searches).        
*          7: iVec gradient.        
*          8: force (n-1) intersection search (to be used if GD is small).        
### IOp(10/11)
Largest matrix for direct inversion in LinEq2.
* 0        Default (10000).        
* -1        Always use DIIS, never invert directly.        
* N        Use DIIS recursively if the O(N^3) work (N*N*NSolve) is at least N^3. Rounded to an even multiple of 1000.        
### IOp(10/13)
The nature of the perturbation(s).
* 0        Default (1st order nuclear and electric field).        
* IJKL        Nuclear Lth order. Electric field Kth order. Magnetic field Jth order. Nuclear magnetic moment Ith order.        
### IOp(10/14)
Whether to update dipole and polarizability derivatives.
* 0        Default (yes if IOp(5) = 0).        
* 1        Update dipole.        
* 2        Don’t update dipole        
* 10        Update polarizability.        
* 20        Don’t update polarizability.        
* 100        Force 2nd order cphf for polarizability derivatives.        
### IOp(10/15)
What to do with expansion vectors from the linear equations.
* 0        Default (2).        
* 1        Save vectors at end.        
* 2        Delete vectors at end of each CPHF.        
* 3        Pass vectors from 1st to 2nd order CPHF, but delete at end of link (off given defaults in CPHF).        
* 4        Save only static electric field solutions.        
* 00        Default (use old vectors if available).        
* 10        Use old vectors if available.        
* 20        Ignore old vectors.        
### IOp(10/16)
Convergence in secondary linear equations (only for simultaneous solution).
* 0        Use standard machine tolerance (MDCutO) on maximum and rms.        
* N        Convergence is 10^-N for max and rms.        
### IOp(10/17)
Frozen-core.
* 0        Default (use AO 2PDM for Lagrangian only if orbitals are frozen in /Orb/).        
* 1        Do C1, C2, S1, and S2 off the AO 2PDM.        
* 2        Convert /Orb/ to full, for debugging frozen-core with integrals over the full window.        
* 3        Save as 2, but leave the full version of /Orb/ on the disk.        
`L1003`: Controls direct or in-core version of CPMCSCF.
* 000        In-core version. Must be used with IOp(5/17=200).        
* 400        Direct solution of CPMCSCF equations. Must be used with IOp(5/17=400).        
### IOp(10/18)
Whether to do correct or approximate CPHF.
* 0        CPHF is done correctly.        
* 1        The A-matrix is neglected, and hence the U-matrices are set equal to the B-matrices (i.e., uncoupled Hartree-Fock is used).        
* 2        The U-matrices are set to zero.        
* 3        Only a single set of products AX are computed, independent of convergence criteria. Simultaneous solution is implied.        
### IOp(10/19)
Whether overlap (S1) terms must be included.
* 0        Default (yes, unless ZDO).        
* 1        Yes.        
* 2        No.        
Note that the appropriate RWF (588) must be present in any case.
### IOp(10/20)
How to handle 2e integral contributions.
* 0        Default (decide on the fly).        
* 1        Read the 2e integral files, MO if possible.        
* 2        Compute the 2e integrals when needed.        
* 3        Force use of AO integrals, even if MO ones are available, i.e. force AO or direct.        
* 4        Don’t use <IA||BC> integrals, even if present.        
* MNx        Use option MN in control of 2e integral calculation.        
### IOp(10/21)
Whether to store Uai, Spq, and full MO Fock matrix derivatives in permanent RWFs.
* 0        Default (No).        
* 1        Yes. Disables use of symmetry to reduce the size of the CPHF problem here.        
* 2        No.        
* 10        Save magnetic MO derivatives.        
### IOp(10/22)
Which multipole (electric field) perturbations to include? Only used if J part of IOp(10/13) is non-zero.
* 0        Default. Uniform electric field (dipole) only.        
* 1        Dipole (uniform electric field).        
* 2        Quadrupole (electric field gradient, all 6 Cartesian components).        
* 3        Octupole.        
* 4        Hexadecapole.        
### IOp(10/28)
State for CPCIS/CPTD, CPMCSCF, and NAC.
* 0        Default (1).        
* N        Nth excited state.        
### IOp(10/29)
Use of Raffenetti integrals during direct SCF.
* -N        All integrals done as Raffenetti if there are N or more matrices; all as regular if there are < N.        
* 0        Default: let FoFJK decide.        
* 1        All integrals are done as regular integrals.        
* N        Integrals with degree of contraction greater than or equal to N are done are regular integrals.        
### IOp(10/30)
In-core storage of 2e integrals.
* 0        Default — do if possible in direct calculation.        
* 1        Force in-core storage; recover ints if available on RWF 610.        
* 2        Force recomputation.        
### IOp(10/31)
Whether to use symmetry to reduce the number of CPHF equations.
* 0        Default (yes).        
* 1        No.        
* 2        Yes.        
* 3        Yes, Override check of density matrix symmetry.        
* 00        2e integral symmetry in CPHF (default 2, except 3 for nuclear derivatives).        
* 10        No.        
* 20        Yes, via petite list if possible, integral replication if not.        
* 30        Yes, via integral replication.        
### IOp(10/32)
`L1014`: Whether to apply interchange.
* 0        Default (Yes).        
* 1        Yes.        
* 2        No.        
`L1003`: Whether to read D2E file.
* 0        Default (No).        
* 1        Yes.        
* 2        No.        
### IOp(10/45)
Type of gauge transformations to perform to calculate the current distribution within the molecule, and hence the molecule’s other magnetic properties.
* -1        None.        
* 0        Default (16 if doing magnetic CPHF).        
* 1        Use single gauge origin – the gauge used to calculate the angular momentum perturbed wavefunctions.        
* 2        Use IGAIM method – gauge origin coincident with the nucleus of the integrated atomic regions.        
* 4        Use CSGT method.        
* 8        Use single gauge origin – the coordinates of which are read in (in Angstroms).        
* 16        Use GIAOs.        
### IOp(10/46)
Whether to calculate dipole and rotational strengths (VCD).
* 0        No (Default).        
* 1        Yes.        
* 2        No.        
* 3        Do only optical rotational using GIAOs.        
* 4        Do velocity optical rotation (CPHF for r x Del perturbation).        
* 5        Do velocity optical rotation (CPHF for Del perturbation).        
* 6        Do velocity optical rotation (CPHF for both Del and r x Del).        
* 7        Do length optical rotation with GIAOs (electric field CPHF).        
* 8        Do length optical rotation with GIAOs (magnetic field CPHF).        
### IOp(10/47)
Whether to do spin-spin coupling constants.
* 0        Default (No).        
* 1        Yes.        
* 2        No.        
* 3        Just do the Fermi-contact contribution.        
* 4        Yes, but do not print/store the Fermi-Contact contribution. (This assumes that the FC term was done in a previous job step).        
### IOp(10/48)
Whether to operate only over perturbations involving active atoms.
* 0        Default (for nuclear, compress if overlay 11 did).        
* 1        Compress.        
* 2        Don’t compress. For SSC or frequencies with frozen atoms, do CPHF for all atoms, even frozen ones.        
* 3        Don’t compress, but blank contributions for inactive atoms.        
* 4        Compress and store force constants only over active atoms (for ONIOM(MO:MM) Opt=CalcFC with micro-iterations).        
* 5        Permute the order of permutations here in order to put QM atoms ahead of electronic embedding atoms.        
* 10        Read a list of atoms to include in perturbations.        
* 000        Default (100).        
* 100        All ONIOM-active, non-frozen nuclei are included in nuclear perturbations.        
* 200        Atoms which are not used in the redundant internal coordinate set are not included in the list of perturbations. Saves time for ONIOM-EE non-quadratic Opt=CalcFC.        
* 0000        Default (do not include frozen atom coordinates in perturbations unless saving Fock-derivatives).        
* 1000        Keep frozen atoms in the perturbation list.        
* 2000        Keep frozen atoms in the perturbation list, but zero their B matrices.        
When Fermi-contact spin-spin couplings are read from a previous job step, the same atoms are selected when computing the other terms.
### IOp(10/49)
Flag for doing FD polarizability derivatives.
* 0        Default (No).        
* 1        Yes, do nuclear coord CPHF for Ux and use interchange (production). Default if same basis used to compute both FD polar derivatives and force field.        
* 2        Yes, do (static) 2nd order cphf wrt applied field, compute contribution from F(x)/Bx here and use interchange (production). Default if only computing FD polar derivative using this basis.        
* 3        Yes, like 2, except use L1110 to produce F(x) and MakeAB for Bx (debugging option).        
* 4        Yes, like 1, except use partial interchange (debugging option).        
* 5        Yes, do 2nd order CPHF with respect to field and nuclear coord. (debugging option).        
* 10        Also do dipole-quadrupole polarizability derivatives.        
* 100        Also do dipole-magnetic dipole polarizability derivatives.        
### IOp(10/50)
`L1003`: This controls mode of action of the CPMCSCF. The 3*(Natom-1) linear equations are either solved in turn or an iterative tridiagonal solution of the inverse of Hessian is developed. The first method is very expensive because it scales as 3*(Natom-1)*Nbasis^2 whereas the second scales as Nbasis^2.
* 0        Default, same as 3.        
* 1        Solve each atom in turn. This is the most accurate approach but it is much more expensive. The recommended value of IOp(7) is 7 (10^-7).        
* 2        DIIS method with multiple rhs.        
* 3        DIIS method with multiple rhs. Forces scalar multiplications.        
* 4        Tridiagonal solution of inverse of Hessian. (Default). The recommended value of IOp(7) is 12 (10^-12).        
### IOp(10/55)
Options for trajectory surface hopping calculations.
See mcscf.F for descriptions.
### IOp(10/60-62)
Override standard values of IRadAn, IRanWt, and IRanGd. The default for IOp(60) here is -3, two steps down from default, unless post-SCF gradients or spin-spin couplings are being computed, in which case the same grid is used as in the rest of the calculation.
`L1002, L1014`: Special values for IOp(60):
* 0        Default (-1 for post-SCF gradients and spin-spin coupling, otherwise -3).        
* N>1        Use the specified grid.        
* -1        Use the same grid as the rest of the calculation.        
* -2        Use a grid one step smaller than the general calculation (finegrid for int=ultrafine, sg1 for int=finegrid, etc.).        
* -3        Use a grid two steps smaller than the general calculation.        
* -NN0        A number with two bits for the default in each nuclear case:
N = 10(0/1/2/3) + (0/4/8/12) + (0/16/32/48) where the four choices are:
    0 = default (same as 3 and global default).
    1 = two steps smaller grid for GGAs, one for tau functionals.
    2 = one step smaller grid.
    3 = full grid.
and the 3 terms are for a) CPKS during ground state frequencies, b) CPKS during ground state part of TD and double hybrid frequencies and c) CPTD during TD frequencies.        
* -640        Sets all flags 3 to zero so default of two steps everywhere.        
The values ≤-10 are primarily useful in setting alternate defaults in `Default.Route` or on the command line.
### IOp(10/63)
Change FMM defaults.
* 0        Default: Use FMM if turned on globally, use more aggressive cutoffs in Xc integration, use more aggressive cutoffs in integrals and FMM unless doing NFx.        
* 1        Turn off FMM here regardless.        
* 2        Use FMM if turned on globally.        
* 3        Turn FMM on here regardless.        
* 10        Use global cutoffs.        
* 20        Use local, lower cutoffs suitable only for CPHF/CPKS.        
* 100        Turn off FoFCou as well as FMM.        
### IOp(10/70)
`L1003`: Memory estimation scheme:
* 0 or 1        Better memory estimation for ¾ integral transformation (Default).        
* 2        Old memory estimation.        
### IOp(10/72)
Whether to do frequency-dependant properties.
* 0        Default (No, unless both electric and magnetic properties are requested).        
* 1        No.        
* 2        Yes.        
* 3        Also Yes.        
* 4        Yes, with formalism for frequency-dependent XC response.        
* 00        Update frequency-dependent property file if frequency-dep. calculation is performed.        
* 10        Update regardless.        
* 20        Do not update.        
### IOp(10/73)
Maximum number of CPHF cycles.
* 0        Default (1000).        
* N        N.        
* N<0        N cycles but return to default if restarting.        
### IOp(10/74)
Whether to do non-equilibrium solvation.
* 0        Default: Only if frequency-dependant.        
* 1        Yes.        
* 2        No.        
* 00        Default: Not doing state-specific iterations.        
* 10        Doing state-specific with non-equilibrium solvation.        
* 20        Doing state-specific with equilibrium solvation        
### IOp(10/75)
Print during NMR.
* 0        Default (1).        
* 1        Print tensors and eigenvalues.        
* 2        Print eigenvectors as well.        
### IOp(10/76)
Override general choice of exchange-correlation frequency dependence.
* 0        Use global value for this job step.        
* N        Use type N (see IOp(10/88) in overlay 5).        
### IOp(10/77)
Test CPHF results by checking the CPHF equations using the complete MO Fock and density derivatives.
* 0        Default (No).        
* 1        Yes.        
* 2        No.        
### IOp(10/79)
Stop L1002 at selected points for testing restarts.
* MNN        Stop at pass M (default 1), restart point NN.        
### IOp(10/80)
Options for trajectory surface hopping calculations. See mcscf.F for descriptions.
### IOp(10/81)
Control of number of passes in AXAO.
* 0        Default: at most 96 matrices at a time if doing FMM, otherwise no limit.        
* -1        As few passes (as many matrices) as possible.        
* N>0        Do at most N densities per pass.        
* N<-1        Do at least -N passes.        
### IOp(10/82)
* 1        Force recalculation of MO integrals for MOCPHF. Debugging option.        
### IOp(10/87)
Accuracy of 2e integrals.
* 0        Default.        
* N        10^-N.        
### IOp(10/90)
Whether to do correct or approximate CPCIS.
* 0        CPCIS is done correctly.        
* 1        The A-matrix is neglected, and hence the U-matrices are set equal to the B-matrices (i.e., uncoupled Hartree-Fock is used).        
* 2        The U-matrices are set to zero.        
* 3        Only a single set of products AX are computed, independent of convergence criteria. Simultaneous solution is implied.        
### IOp(10/91)
`L1002`: Limit IDoFFX.
* 0        Default: use the best possible.        
* N        Limit IDoFFX<=N, N=9=>IDoFFX=0.        
* -N        Force IDoFFX=N.        
### IOp(10/92)
Normalization to speed up Raman/ROA:
* 0        Default (1).        
* 1        Yes.        
* 2        No.        
### IOp(10/93)
Generate file for AICD. Only works with NMR=CSGT.
* 0        Default (No).        
* 1        Yes, all orbitals.        
* 2        Yes, read in orbitals to include.        
* 3        No.        
* 00        Default (20).        
* 10        Write small elements in matrices.        
* 20        Do not write small elements in matrices.        
### IOp(10/94)
`L1014`: Threshold for testing Tx.T.
* 0        Default, 5.d-6, continue if test fails.        
* N>0        1.d-N, die if test fails.        
* N<0        1.d+N, continue test fails.        
* -99        Default report but but do not die if test fails.        
### IOp(10/95)
`L1014`: Limit IDoFFX.
* 0        Default:  use the best possible, currently 0.        
* N        Limit IDoFFX≤N, N=9=>IDoFFX=0.        
* -N        Force IDoFFX=N.        
* 0x        Default (3 for IDoFFX=6, 1 otherwise).        
* 1x        Do not optimize the XC matrices update.        
* 2x        Optimize XC matrices update involving T/Tx, but not G/Gx (this is mostly a debugging option).        
* 3x        Optimize XC matrices update as much as possible.        
### IOp(10/96)
`L1014`: Whether to compute transition dipole derivatives.
* 0        Default (No).        
* 1        Yes (results in minor deviations from optimal IDoFFX).        
* 2        No.        
### IOp(10/100)
`L1014`: Solution method for CPCIS/CPTD.
* 0        Default, same as IOp(10/8) except that separate is done if the convergence is less than the default of 1.d-8.        
* -1        CPHF for each variable in a separate call to LinEq1.        
* 1        Expand each variable in a separate expansion space.        
* 2        Solve all equations together, possibly reverting to the old (one variable at a time) method in the secondary solution.        
* 3        Invert the A matrix directly.        
### IOp(10/101)
`L1014`: Solution method (no interchange).
### IOp(10/102)
Diagonal shift preconditioning in CPHF:
* -1        Same as 0.        
* 0        No.        
* 1        Shift Ea-Ei up to a minimum given by IOp(103).        
* 2        Shift all diagonals by the amount given by IOp(103).        
* 0x        Default (1x).        
* 1x        Flip the sign of Y shifts.        
* 2x        Same sign for X and Y.        
### IOp(10/103)
Value/threshold for shift during CPHF:
* 0        Default (0.1 Hartree).        
* N        N/1000 Hartree.        
### IOp(10/105)
Shift for predconditioning during CPCIS/CPTD.
* -1        Same as 0.        
* 0        No.        
* 1        Shift Ea-Ei up to a minimum given by IOp(103).        
* 2        Shift all diagonals by the amount given by IOp(103).        
* 0x        Default (1x).        
* 1x        Flip the sign of Y shifts.        
* 2x        Same sign for X and Y.        
### IOp(10/106)
Override of IRadAn for just L1014, taking precedence over IOp(60).
### IOp(10/107)
Override of IRadAn for just XC2E part of L1014, taking precedence over IOp(60) and IOp(107).
### IOp(10/108)
`L1014`: Stop at selected points for testing restarts.
* 0        Default (no stopping).        
* BBBNNNN        Stop at restart point N, in batch BBB if applicable.        
### IOp(10/109)
`L1014`: Max number of iterations, overriding IOp(73).
### IOp(10/109)
`L1014`: Max number of iterations, overriding IOp(73).
## Overlay 11 
### IOp(11/5)
IFWRT: derivative integral write option.
* 0        Do not produce a D2E file.        
* 1        Produce a D2E file.        
### IOp(11/6)
IFHFFX: Whether or not to contract integral derivatives with Hartree-Fock density matrix terms to produce Hartree-Fock two-electron contribution to the forces.
* 0        No.        
* 1        Yes.        
* 2        Yes, also contracted electric field density matrix derivatives to form thetwo-electron integral derivative contribution to the pol. derivatives, but ignore frequency-dependent density derivs.        
* 3        Yes, do polarizability derivatives using frequency-dependent density derivatives if the FD density derivatives are available.        
### IOp(11/7)
IFTPDM: whether or not to contract integral derivatives with a ‘read-in’ two-particle density-matrix.
* 0        No.        
* 1        Yes.        
* 2        Yes, but generate and write out the HF 2PDM here for debugging purposes.        
* -N        Generate and use the 2PDM for CIS state N.        
### IOp(11/8)
IFF1: whether or not to compute F1 over AO’s.
* 0        No.        
* 1        Yes.        
* 2        Yes, then compress to active atoms.        
* 3        Generate active list.        
### IOp(11/9)
IDOUT: First-derivative output option.Contains I2*100+I1*10+I0.
* I0        Whether or not to use the contents of IRWFX.        
* 0        No.        
* 1        Yes, if not there, merely set the array to zeroes.        
* I1        Processing of two-electron Hartree-Fock contributions.        
* 0        None.        
* 1        Take HF contributions from FX1 (A LA IFHFFX).        
* 2        Take HF contributions from F1 (A LA IFF1). (forms the 1/2(F-H) term in link 1110).        
* 3        Form 1/2(F+H) term in link 1110.        
* I2        Processing of TPDM contributions.        
* 0        None.        
* 1        Add in contents of FX2.        
### IOp(11/10)
`L1110`: Whether to compute Fock matrices, Lagrangian, and SCF energy.
* 0        No.        
* 1        Yes.        
* 2        Yes, and in addition, compute other pieces necessary for second-order simultaneous optimization.        
### IOp(11/11)
Control of integral derivative algorithm.
* 0        Default: use IsAlg to decide.        
* 2        Scalar Rys SPDF.        
* 3        Illegal here.        
* 4        Illegal here.        
* 5        Illegal here.        
* 6        Illegal here.        
* 7        Illegal here.        
* 8        Illegal here.        
* 9        Illegal here.        
* 10        Illegal here.        
* 11        Illegal here.        
* 12        FoFJK: Prism spdf.        
* 13        Illegal here.        
### IOp(11/12)
`L1102, L1110`: Selection of 1PDM.
* 0        Usual SCF density.        
* N        Use generalized density number N for both the one-electron integral derivatives and the corresponding 2PDM terms.        
* -N        Contract with HF density, CI density for state N, and CIS 1PDM for state N.        
### IOp(11/13)
`L1112`: Flags.
* 0        Default for IxÞSx (same as 1).        
* 1        Use Ix.        
* 2        Use L(x) and Ux*I.        
* 00        Formation of Ux*I*T terms, default, same as 1.        
* 10        N^4 I/O algorithm.        
* 20        Old gOV3 I/O algorithm.        
* 000        Formation of Fx*T*T terms: default is to choose based on available memory.        
* 100        Force O2V2 method.        
* 200        Use(2g+O)V2 memory algorithm even if O2V2 memory is available.        
* 300        Force old N^5 I/O algorithm.        
* 0000        Default Ix*T algorithm (1)        
* 1000        Force new algorithm.        
* 2000        Force old algorithm.        
* 00000        Default availability of MO basis Ix — use if avail.        
* 10000        Ix file is not available (omit OO/VV blocks of Px,Wx).        
* 20000        Ix file is available (i.e. do OO/VV blocks of Px,Wx).        
* 000000        Default non-zero Delta(ij+ab) processing: if Full and some Delta’s are non-zero.        
* 100000        Force addition of these terms.        
* 200000        Suppress addition of Delta terms.        
### IOp(11/14)
The nature of the perturbation(s).
* 0        Default (1st order nuclear and electric field).        
* IJK        Nuclear Kth order. Electric field Jth order. Magnetic field Ith order.        
### IOp(11/15)
Controls output of derivatives to rw-files.
* 1        Load fxyz from rw-files if it exists.        
* 10        Calculate nuclear contribution.        
* 100        Calculate one-electroon contribution.        
* 1000        Output of ‘old’ format.        
* 10000        Forces out-of-core algorithm.        
### IOp(11/16)
`L1102`: Mode of operation.
* 0        Default: compute dipole derivative matrices only.        
* 1        Also compute dipole derivative integral contribution to the HF dipole derivatives.        
* 10        Also compute HF contribution to the dipole moment.        
### IOp(11/17)
`L1111`: Frozen-core.
* 0        Default (use AO 2PDM for Lagrangian only if orbitals are frozen in /Orb/).        
* 1        Do C1, C2, S1, and S2 off the AO 2PDM.        
* 2        Convert /Orb/ to full, for debugging frozen-core with integrals over the full window.        
* 3        Save as 2, but leave the full version of /Orb/ on the disk.        
* 10        Form the derivative integral contribution to the Lagrangian as well. This is stored on disk as RL(NBasis,NBasis,NAt3,IOpCl+1) in RWF 1001.        
### IOp(11/18)
`L1111`: Save AO 2PDM?
* 0        No.        
* N        Save the AO 2PDM on RWF N. It is (NTT,NTT) and includes factors (2-Delta(ij))(2-Delta(kl)). It doesn’t include any normalization factor.        
### IOp(11/19)
`L1112`: Whether to delete MO integrals after.
* 0        Default (Yes).        
* 1        Yes.        
* 2        No.        
### IOp(11/20)
`L1112`: How to handle 2e integral contributions.
* 0        Default (same as 1).        
* 1        Read the 2e integral files, MO if possible.        
* 2        Compute the 2e integrals when needed.        
* 3        Force use of AO integrals, even if MO ones are available.        
* MNx        Use option MN in control of 2e integral calculation.        
### IOp(11/21)
Size of buffers for integral derivative file.
* 0        Default (Machine dependent; see DSet2E).        
* N        N integer words.        
### IOp(11/22)
`L1112`: In-core option for W(Tilde) term.
* -6        Force in-core storage.        
* -3        Suppress in-core storage.        
* 0        Default: in-core if possible.        
### IOp(11/23)
`L1112`: Use of Raffenetti integrals during direct term.
* -N        All integrals done as Raffenetti if there are N or more matrices; all as regular if there are less than N.        
* 0        Default: let FoFJK decide.        
* 1        All integrals are done as regular integrals.        
* N        Integrals with degree of contraction greater than or equal to N are done at regular integrals.        
### IOp(11/24)
`L1102`: Output.
* 00        Default (01).        
* 1        Contract with density matrix to form dipole derivative contributions.        
* 10        Store dipole derivative matrices on disk.        
### IOp(11/26)
Program accuracy option.
* 0        Do integrals economically to 10^-10 accuracy.        
* 1        ‘Test’ option bypass cutoffs.        
### IOp(11/27)
`L1110`: Integral retention parameter if writing d2e file.
* 0        Retain integrals GE 10^-10 in the D2E file (if selected) and/or 10^-10 in the integral heap if IFF1=1 and MODE=2.        
* N        Retain integrals GE 10^-N.        
`L1111`: Save unsymmetrized S1 and S2.
* 0        No.        
* 1        Yes.        
### IOp(11/28)
`L1111`: Location or generation of MO 1 and 2 PDMs.
* -16        Compute EOM-CCSD 2PDM.        
* -15        Compute Direct SAC-CI 2PDM.        
* -14        Compute SAC-CI General-R 2PDM.        
* -13        Compute SAC-CI 2PDM.        
* -12        Compute MP4SDQ 2PDM.        
* -11        Compute MP4DQ 2PDM.        
* -10        Compute MP3 2PDM.        
* -9        Compute BD 2PDM.        
* -8        Compute CCSD 2PDM.        
* -7        Compute QCISD 2PDM.        
* -6        Compute CCD 2PDM.        
* -5        Compute CIS 2PDM.        
* -4        Compute CISD 2PDM.        
* -3        Compute CID 2PDM.        
* -2        Compute MP2 2PDM.        
* -1        Compute HF DMs.        
* 0        Default (RWFs 626, 627, and 628).        
* N        RWFS N (1PDM), N+1 (W), and N+2 (2PDM).        
### IOp(11/29)
What to do:
* 0        Nothing.        
* 1        Transform 1PDM and Lagrangian from MO to AO.        
* 10        Transform 2PDM from MO to AO.        
* 100        Sort AO 2PDM into shell order. If back transformation has not been requested, the double-length AO 2PDM is expected in file 1001. The sorted 2PDM is left in file 602.        
* 200        Form the contribution of the 2PDM to the forces right here. Note that if the 2PDM is also to be left behind, it will be over 6d/10f and have the HGP d and f scale factors in it.        
* 1000        Suppress writing alpha, beta, and spin density RWFs.        
* 10000        Form and sort the 2PDM derivatives rather than the 2PDM.        
* 20000        Generate replicated 2PDM copies for testing.        
### IOp(11/30)
What to compute using integrals or D2E file.
* 0        Nothing.        
* 1        Energy.        
* 10        Gradient.        
### IOp(11/31)
`L1110`: Whether to use symmetry in Rys integral derivatives.
* 0        Yes.        
* 1        No.        
* 2        Yes.        
* 3        Yes, skip check of density symmetry in L1110.        
### IOp(11/32)
`L1111`: Whether to do 2PDM or just Lagrangian.
* 0        Compute full gradient        
* 1        Compute full gradient (same as default).        
* 2        Compute density only.        
* 3        Compute density and W only.        
* 4        Compute 2PDM only, no density or W.        
* 5        Compute non-separable terms only.        
* 6        Testing (no lag currently).        
* 7        T-relaxed MO-unrelaxed 1PDM for (EOM-)CCSD (no need for 2PDM. 1PDM stored in IODens).        
### IOp(11/33)
IPRINT print option.
* 0        No printing.        
* 1        Print computed first-derivatives.        
* 2        Print F1 matrices.        
### IOp(11/39)
Compression of derivative matrices.
* 0        Default (2 if expanded matrices, otherwise 4 or 5).        
* 1        Compute over active atoms only.        
* 2        Compute over the full list of atoms.        
* 3        Compute over the full list of atoms, but blank contributions for inactive atoms.        
* 4        Compute over active atoms only, and store second deriv. contributions over only active atoms.        
* 5        Store only matrices for QM atoms, but include the contribution of EE centers in the matrices.        
### IOp(11/42)
Compressed file formats.
* 0        Default: compressed.        
* 1        Force expanded form.        
* 2        Force compressed form.        
* 3        Compressed Sx but separate H1 and F1.        
### IOp(11/43)
Batching in overlay 11.
* 0        Default, smallest possible number of passes.        
* 1        Do at least one pass, but using the out-of-core algorithms.        
* N        Do at least N passes.        
* For        Rys in L1110, N is 0/1/2 for default/in-core/out-of-core.        
### IOp(11/45)
Force NAt3 instead of NAt3+3 storage of matrices (for debugging).
* 0        No.        
* 1        Yes.        
### IOp(11/46)
Whether to include orbital rotation gradient terms for SAC-CI.
* 0        No.        
* 1        Convert 1PDM to canonical representation.        
* 2        Save gradients to disk, needed for non-canonical methods.        
### IOp(11/53)
Convert forces over shells to field-dependent dipole and forces over atoms (for debugging).
* 0        No.        
* 1        Yes.        
### IOp(11/60)
Override standard values of IRadAn.
### IOp(11/61)
Override standard values of IRanWt.
### IOp(11/62)
Override standard values of IRanGd.
### IOp(11/63)
Whether to do FMM.
* 0        Use global default.        
* 1        Turn off FMM here regardless.        
### IOp(11/75)
Print during NMR.
* 0        Default (1).        
* 1        Print tensors and eigenvalues.        
* 2        Print eigenvectors as well.        
### IOp(11/76)
`L1102`: Force DoH1 logic for debugging.
* 0        Default (No).        
* 1        Yes.        
* 2        No.        
### IOp(11/77)
Debugging option for DBF derivatives.
* 0        Normal processing.        
* 1        Ignore fitting density and just process real density in L1110.        
* 4        Skip increment of Fx with J(Z^-1*Jx(P-Pfit)).        
* 6        Compute only Pfit and not P terms involving 2e integral derivatives.        
* 7        Clear both Pfit and P before FoFJK.        
* 1x        Do polarizability derivative contribution separately; only works with density fitting.        
* 11x        Do polarizability derivatives for density fitting separately and keep only dbf-ao terms.        
* 21x        Do polarizability derivatives for density fitting separately and keep only dbf-dbf terms.        
* 31x        Do polarizability derivatives for density fitting separately via 2PDM in one call to FoFCou.        
### IOp(11/81)
Control of number of passes in GXX.
* 0        Default: at most 96 matrices at a time if doing FMM, otherwise no limit.        
* -1        As few passes (as many matrices) as possible.        
* N>0        Do at most N densities per pass.        
* N<-1        Do at least -N passes.        
### IOp(11/87)
`L1110`: Accuracy of 2e integrals.
* 0        Default.        
* N        10^-N.        
### IOp(11/101)
Raffenetti in DD1Dir.
### IOp(11/102)
Control of FMM for nuclear repulsion.
* 0        Default: Use for 5K or more atoms.        
* N        Use for N or more atoms.        
* -1        Always use FMM.        
* 2        Never use FMM.        
### IOp(11/103)
Flag for PTED with CCSD and BD.
* 0        Normal solvation.        
* 1        PTED.        
* 2        PTE-S.        
* 3        PTES.        
### IOp(11/126)
Maximum number of matrices to handle at a time in DD1Dir.
* 0        Default (-1).        
* -1        No limit.        
* N>0        At most N matrices at a time.        
## Overlay 99 
### IOp(99/5)
Controls handling of the checkpoint file.
* 0        The run is an optimization or frequency run, so both the permanent and restart files are in the checkpoint file. Delete the restart information if the run is finishing normally (I.E. if the error termination ILSW bit is not set).        
* 1        The run is not an optimization. Save the permanent information (MOS, basis set info etc.) on the checkpoint file.        
* 2        Do not write anything to the checkpoint file.        
* 3        Archive data from the checkpoint file.        
* 4        Restart a multi-step job, recovering data from the checkpoint file and figuring out which job step to run next and whether it needs restart if an optimization or numerical frequency.        
* 5        Save data on the checkpoint file, but don’t remove extra data (i.e., if a new version was not generated in this step).        
* 0x        Defaults to 1.        
* 1x        Remove Cartesian force constants from chk file if this is not a frequency job.        
* 2x        Leave Cartesian force constants on the chk file even if this is not a frequency job.        
### IOp(99/6)
Controls output of data files for other programs.
* 0        No PolyAtom output.        
* 1        PolyAtom output in working precision to Fortran unit 8.        
* 00        No GVB2P5 trans file.        
* 10        GVB2P5 trans file to unit 14.        
* 100        WFN file output.        
* 200        WFNX file output.        
* 1000        Use natural orbitals in WFN file.        
* 10000        Regular WFN/WFNX file.        
* 20000        WFN/WFNX file should include magnetic orbital derivatives.        
* 30000        WFN/WFNX file should include GIAO magnetic orbital derivatives.        
* 100000        Write generate matrix element file.        
### IOp(99/7)
Controls whether MOs are written to the polyatom integral tape in LANL style.
* 0        No.        
* 1        Yes.        
### IOp(99/8)
Reading temperature, pressure, and isotopes during multi-step energy calculations.
* 0        Default (same as 1).        
* 1        No, use defaults.        
* 2        Yes.        
### IOp(99/9)
Controls archiving of dipole moment and other electric field
derivatives, except for archiving from the checkpoint file.
* 0        Archive all as is.        
* 1        Archive all, but rotates to z-matrix orientation first.        
* 2        Don’t archive.        
### IOp(99/10)
Controls punching of assorted information (i.e., formatted output to unit 7).
* 0        Nothing.        
* 1        Title.        
* 2        Atomic numbers and coordinates in format (I3,3D20.12).        
* 4        Derivatives (forces and force constants) in format (2X,3D20.12). These are in the Z-matrix orientation.        
* 8        The archive entry. This is independent of normal archiving to the main file.        
* 16        An input deck for HONDO.        
* 32        The molecular orbitals, in format suitable for Guess=Cards, in the standard orientation.        
* 64        A GAMESS input deck.        
* 128        The natural orbitals generated by link 601.        
* 256        A WFN file for PROAIMS.        
* 512        Use natural orbitals in WFN file.        
* 1024        Output hyperfine tensors as input to Pickett’s program (sent to the output file).        
* 2048        Read a list of atoms to use in the Pickett input.        
### IOp(99/11)
Which type of database to update.
* 0        Default (3).        
* 1        Old format.        
* 2        New format.        
* 3        Both.        
### IOp(99/12)
Flag for coordinate optimization.
* 0        No.        
* 1        Yes; remove /ZMat/ and /ZSubst/ from the RWF and checkpoint files.        
### IOp(99/13)
Whether this is the end of the job step.
* 0        Default (Yes).        
* 1        Yes.        
* 2        No.        
* 3        Go back to Link 1.        
### IOp(99/14)
Whether to attempt to express the final optimized structure in terms of the input z-matrix.
* 0        Yes if there are 20 or fewer atoms.        
* 1        Yes.        
* 2        No.        
* 3        Yes, and update RWFs.        
### IOp(99/15)
Act as though in multi-step job type IOp(15).
### IOp(99/16)
Treat the job as type (Info(7)) given by IOp(16).
### IOp(99/17)
Override multi-step job defaults.
* NNN        Treat as MSJDon = IOp(17) step in a multi-step job.        
* Mxxx        MSJOpt M from L1. If M=2, do not abort if no force constants are found. If M≥2, skip any later optimization steps.        
### IOp(99/18)
How many virtual orbitals to include in the WFN file.
* 0        Default (None).        
* -1        Include all virtual orbitals.        
* N        Include N virtual orbitals.        
### IOp(99/19)
Generation of archive entry.
* 0        Default, generate archive entry unless the job is flagged for error termination or the job was marked by l1 as not archivable.        
* 1        Generate the entry ignoring the l1 flag.        
* 2        Do not generate the entry.        
### IOp(99/20)
Saving atomic charges as MM charges.
* 0        Default (No).        
* N        Save charge type N-1 as MM charges.        
### IOp(99/22)
Compress files.
* 0        Default (3).        
* 1        Compress chk.        
* 2        Compress all files.        
* 3        Do not compress.        
### IOp(99/23)
MinPSp for compression.
### IOp(99/24)
MaxPCp for compression.
### IOp(99/33)
Controls debug print.
* 0        No debug print.        
* 1        Debug print.        
### IOp(99/125)
Options for matrix element file; see WrtUnF.
