# Offline Gaussian IOps 
## Overlay 1 
### IOp(1/5)
`L103`: Mode of optimization.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Find&nbsp;local&nbsp;minimum.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Find&nbsp;a&nbsp;saddle&nbsp;point.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Find&nbsp;stationary&nbsp;point&nbsp;on&nbsp;the&nbsp;energy&nbsp;surface&nbsp;with&nbsp;N&nbsp;negative&nbsp;eigenvalues&nbsp;of&nbsp;the&nbsp;2nd&nbsp;deriv.&nbsp;matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L107`: Mode of search.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Locate&nbsp;the&nbsp;maximum&nbsp;in&nbsp;the&nbsp;LST&nbsp;path.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scan&nbsp;the&nbsp;LST&nbsp;path.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Which&nbsp;approximation&nbsp;to&nbsp;make.&nbsp;Default&nbsp;is&nbsp;III&nbsp;for&nbsp;Tomasi&nbsp;(interlocking&nbsp;spheres)&nbsp;and&nbsp;IV&nbsp;for&nbsp;general&nbsp;surface.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Apprx.   I:&nbsp;&nbsp;Don’t&nbsp;Do&nbsp;Self-Polarization&nbsp;or&nbsp;“Compensation”&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Apprx.  II:&nbsp;&nbsp;Do&nbsp;Self-Polarization,&nbsp;But&nbsp;No&nbsp;Compensation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Apprx. III:&nbsp;&nbsp;Do&nbsp;Self-Polarization&nbsp;and&nbsp;Compensation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Apprx.  IV:&nbsp;&nbsp;Do&nbsp;III,&nbsp;and&nbsp;Allow&nbsp;Surface&nbsp;To&nbsp;“Relax”&nbsp;in&nbsp;Solution&nbsp;if&nbsp;no&nbsp;spheres…&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N0000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Whether&nbsp;to&nbsp;evaluate&nbsp;densities&nbsp;using&nbsp;orbitals&nbsp;or&nbsp;density&nbsp;matrix.&nbsp;Default&nbsp;is&nbsp;to&nbsp;use&nbsp;density.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;MOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;density.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L121`: Time step, N*0.0001 fs, default 0.1.




### IOp(1/6)
`L102, L103, L105, L107, L109, L113, L114`: Maximum number of steps (or number of steps for an LST scan).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NSTEP&nbsp;=&nbsp;Max(20,NVAR+10)&nbsp;(L103)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;Min(20,NVAR+10)&nbsp;(L102,&nbsp;L105,&nbsp;L109)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;Min(40,NVAR+20)&nbsp;(L113,&nbsp;L114)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NSTEP&nbsp;=&nbsp;N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/7)
`L103, L105, L109, L112, L113, L114`: Convergence on the first derivative and estimated displacement for the optimization, RMS first derivative < ConvF, RMS Est. Displacement < ConvX = 4*ConvF. For L123, similar convergence control for the GS integrator.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ConvF&nbsp;=&nbsp;1/600&nbsp;Hartree/Bohr&nbsp;or&nbsp;Radian&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ConvF&nbsp;=&nbsp;0.0003&nbsp;Hartree/Bohr&nbsp;or&nbsp;Radian&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ConvF&nbsp;=&nbsp;N*10^-6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L116, L117`: Convergence on electric field/charges.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;value&nbsp;for&nbsp;optimizations:&nbsp;10^-7.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;value&nbsp;for&nbsp;single-points:&nbsp;10^-5&nbsp;in&nbsp;L116,&nbsp;10^-7&nbsp;in&nbsp;L117.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;


`L123`: Regular force/displacement convergence for GS2. For EulerPC, N/1000000 displacement conv.




### IOp(1/8)
`L103, L109, L112`: Maximum step size allowed during Opt.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DXMAXT&nbsp;=&nbsp;0.1&nbsp;Bohr&nbsp;or&nbsp;Radian&nbsp;(L103,&nbsp;Estm&nbsp;or&nbsp;UnitFC).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;0.3&nbsp;Bohr&nbsp;or&nbsp;Radian&nbsp;(L103,&nbsp;Read&nbsp;or&nbsp;CalcFC).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;0.2&nbsp;Bohr&nbsp;or&nbsp;Radian&nbsp;(L105).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;0.3&nbsp;Bohr&nbsp;or&nbsp;Radian(L113,&nbsp;L114).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DXMAXT&nbsp;=&nbsp;0.01&nbsp;*&nbsp;N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L117`: General control.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Which&nbsp;type&nbsp;of&nbsp;basin&nbsp;to&nbsp;use&nbsp;to&nbsp;partition&nbsp;the&nbsp;density&nbsp;isosurface.&nbsp;Default&nbsp;is&nbsp;4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GradVne.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GradRho.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;Use&nbsp;Basins,&nbsp;Use&nbsp;only&nbsp;the&nbsp;Center&nbsp;of&nbsp;Nuclear&nbsp;Charge.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Interlocking&nbsp;Spheres.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Order&nbsp;of&nbsp;Adam’s-Bashforth-Moulton&nbsp;(ABM)&nbsp;predictor-corrector&nbsp;method&nbsp;to&nbsp;use&nbsp;in&nbsp;solving&nbsp;diff.&nbsp;eqns.&nbsp;for&nbsp;the&nbsp;grad&nbsp;RHO&nbsp;or&nbsp;Vne&nbsp;trajectories.&nbsp;Default&nbsp;is&nbsp;4;&nbsp;max&nbsp;is&nbsp;9.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number&nbsp;of&nbsp;small&nbsp;steps&nbsp;per&nbsp;ABM&nbsp;step&nbsp;to&nbsp;be&nbsp;used&nbsp;in&nbsp;starting&nbsp;ABM&nbsp;and&nbsp;when&nbsp;“slow&nbsp;down”&nbsp;is&nbsp;needed&nbsp;in&nbsp;ABM.&nbsp;Default&nbsp;is&nbsp;5.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Which&nbsp;approximation&nbsp;to&nbsp;make.&nbsp;Default&nbsp;is&nbsp;III&nbsp;for&nbsp;Tomasi&nbsp;(interlocking&nbsp;spheres)&nbsp;and&nbsp;IV&nbsp;for&nbsp;general&nbsp;surface.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Apprx.&nbsp;I&nbsp;–&nbsp;Don’t&nbsp;Do&nbsp;Self-Polarization&nbsp;or&nbsp;“Compensation”&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Apprx.&nbsp;II&nbsp;–&nbsp;Do&nbsp;Self-Polarization,&nbsp;But&nbsp;No&nbsp;Compensation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Apprx.&nbsp;III&nbsp;–&nbsp;Do&nbsp;Self-Polarization&nbsp;and&nbsp;Compensation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Apprx.&nbsp;IV&nbsp;–&nbsp;Do&nbsp;III,&nbsp;and&nbsp;Allow&nbsp;Surface&nbsp;To&nbsp;“Relax”&nbsp;in&nbsp;Solution&nbsp;if&nbsp;no&nbsp;spheres…&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N0000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Whether&nbsp;to&nbsp;evaluate&nbsp;densities&nbsp;using&nbsp;orbitals&nbsp;or&nbsp;density&nbsp;matrix.&nbsp;Default&nbsp;is&nbsp;to&nbsp;use&nbsp;density.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;MOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;density.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L121`: Time step, N*0.0001 fs, if N>0, -N*0.0001 au if N<0.




### IOp(1/9)
`L103`: Use of Trust radius.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Whether&nbsp;to&nbsp;update&nbsp;trust&nbsp;radius&nbsp;(DXMaxT,&nbsp;default&nbsp;Yes).&nbsp;Default&nbsp;is&nbsp;Yes&nbsp;for&nbsp;minima,&nbsp;no&nbsp;for&nbsp;TS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Whether&nbsp;to&nbsp;scale&nbsp;or&nbsp;search&nbsp;the&nbsp;sphere&nbsp;when&nbsp;reducing&nbsp;the&nbsp;step&nbsp;size&nbsp;to&nbsp;the&nbsp;trust&nbsp;radius.&nbsp;Default&nbsp;search&nbsp;for&nbsp;minima,&nbsp;scale&nbsp;for&nbsp;transition&nbsp;states.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scale.&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Search.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L106`: Whether to use symmetry to reduce the number of L110 displacements.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;use&nbsp;symmetry&nbsp;to&nbsp;skip&nbsp;steps&nbsp;back.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;use&nbsp;symmetry&nbsp;to&nbsp;skip&nbsp;equivalent&nbsp;atoms&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L107`: Whether to maintain symmetry along the search path.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L117`: Whether to delete points which are too close together and how close to get to the iso surface in search.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No;&nbsp;Approx.&nbsp;1.0&nbsp;D-6&nbsp;(N=20)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;using&nbsp;a&nbsp;default&nbsp;criterion&nbsp;(0.05&nbsp;Angstroms).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;using&nbsp;a&nbsp;(10^-N&nbsp;Angstroms)&nbsp;criteria:&nbsp;2.0^-N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.0^-N&nbsp;&nbsp;&nbsp;&nbsp;


`L121`: Whether to read in initial velocities.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;random&nbsp;initial&nbsp;velocity.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;initial&nbsp;Cartesian&nbsp;velocity&nbsp;(Bohr/sec).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;initial&nbsp;MW&nbsp;Cartesian&nbsp;velocity&nbsp;(sqrt(amu)*Bohr/sec).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/10)
`L103, L105, L109, L112, L113, L114`: Input of initial Hessian. All values must be in atomic units (Hartree, Bohr, and radians).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;defaults&nbsp;(not&nbsp;valid&nbsp;for&nbsp;L109).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;((FC(I,J),J=1,I),I=1,NVAR)&nbsp;(8F10.6)&nbsp;(L103&nbsp;only).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;I,J,FC(I,J)&nbsp;(5I3,F20.0)&nbsp;(L103&nbsp;only).&nbsp;End&nbsp;with&nbsp;a&nbsp;blank&nbsp;card.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;from&nbsp;checkpoint&nbsp;file&nbsp;in&nbsp;internal&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Second&nbsp;derivative&nbsp;matrix&nbsp;calculated&nbsp;analytically.&nbsp;(Not&nbsp;valid&nbsp;for&nbsp;L109).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;Cartesian&nbsp;forces&nbsp;and&nbsp;force&nbsp;constants&nbsp;from&nbsp;the&nbsp;checkpoint&nbsp;file&nbsp;are&nbsp;converted&nbsp;to&nbsp;internal&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;Cartesian&nbsp;forces&nbsp;followed&nbsp;by&nbsp;Cartesian&nbsp;force&nbsp;constants&nbsp;(both&nbsp;in&nbsp;format&nbsp;6F12.8)&nbsp;from&nbsp;input&nbsp;stream,&nbsp;followed&nbsp;by&nbsp;a&nbsp;blank&nbsp;line.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;semi-empirical&nbsp;force&nbsp;constants.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;unit&nbsp;matrix&nbsp;(default&nbsp;for&nbsp;L105;&nbsp;only&nbsp;recognized&nbsp;by&nbsp;103).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Estimate&nbsp;force&nbsp;constants&nbsp;using&nbsp;valence&nbsp;force&nbsp;field.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;unit&nbsp;matrix&nbsp;throughout.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/11)
`L103`: Test of curvature. Bomb the job if the second derivative matrix has the wrong # of negative eigenvalues.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Test&nbsp;for&nbsp;z-matrix&nbsp;or&nbsp;Cartesian&nbsp;TS&nbsp;but&nbsp;not&nbsp;for&nbsp;LST/QST&nbsp;or&nbsp;for&nbsp;minimum).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;test.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Test.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L117`: Step size for ABM method in Trudge for isodensity method.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.05&nbsp;(N=2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.1/N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/12)
`L103`: Optimization control parameters.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;default&nbsp;values.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;new&nbsp;values&nbsp;for&nbsp;all&nbsp;parameters&nbsp;(see&nbsp;INITBS).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/13)
`L103, L113, L114, L115, L123`: Type of Hessian Update.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(9&nbsp;for&nbsp;L103&nbsp;minimization,&nbsp;7&nbsp;for&nbsp;L103&nbsp;TS,&nbsp;D2Corr&nbsp;and&nbsp;L115,&nbsp;Powell&nbsp;for&nbsp;L113&nbsp;and&nbsp;L114,&nbsp;Bofill&nbsp;in&nbsp;L123).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Powell&nbsp;(not&nbsp;in&nbsp;L103).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BFGS&nbsp;(not&nbsp;in&nbsp;L103).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BFGS,&nbsp;safeguarding&nbsp;positive&nbsp;definiteness&nbsp;(not&nbsp;in&nbsp;L103&nbsp;or&nbsp;L115).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D2Corr&nbsp;(New,&nbsp;only&nbsp;in&nbsp;L103&nbsp;and&nbsp;L115).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D2Corr&nbsp;(Old,&nbsp;only&nbsp;in&nbsp;L103&nbsp;and&nbsp;L115).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D2Corr&nbsp;(BFGS).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D2Corr&nbsp;(Bofill&nbsp;Powell+MS&nbsp;for&nbsp;transition&nbsp;states).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D2Corr&nbsp;(No&nbsp;update,&nbsp;use&nbsp;initial&nbsp;Hessian).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D2Corr&nbsp;(New&nbsp;if&nbsp;energy&nbsp;rises,&nbsp;otherwise&nbsp;BFGS).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L118`: Integration method.


`L121`: Multi-time step parameter (NDtrC,NDtrP).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;multi-time&nbsp;stepping.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Iterate&nbsp;density&nbsp;constraints&nbsp;NN&nbsp;times&nbsp;per&nbsp;step.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MM00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;gradient&nbsp;once&nbsp;every&nbsp;MM&nbsp;steps.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L123`: Hessian update.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Bofill).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Murtagh-Sargent&nbsp;(SR1)&nbsp;update.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Powell-symmetric-Broyden&nbsp;(PSB)&nbsp;update.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bofill’s&nbsp;update.&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sqrt(Bofill)&nbsp;update.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;update&nbsp;(keep&nbsp;old&nbsp;Hessian).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/14)
`L103`: Maximum number of bad steps to allow before doing a linear minimization (i.e., no quadratic step).


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(0&nbsp;for&nbsp;TS,&nbsp;1&nbsp;for&nbsp;minima).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Allow&nbsp;N&nbsp;—&nbsp;linear&nbsp;only&nbsp;starts&nbsp;with&nbsp;the&nbsp;N+1st.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/15)
`L103, L109`: Abort if derivatives too large.


* -1&nbsp;or&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;force&nbsp;test&nbsp;at&nbsp;all.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FMAXT&nbsp;=&nbsp;0.1&nbsp;*&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/16)
`L103, L113, L114`: Maximum allowable magnitude of the eigenvalues of the second derivative matrix. If the limit is exceeded, the size of the eigenvalue is reduced to the maximum, and processing continues.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EIGMAX&nbsp;=&nbsp;25.0&nbsp;Hartree&nbsp;/&nbsp;Bohr^2&nbsp;or&nbsp;Radian^2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EIGMAX&nbsp;=&nbsp;0.1&nbsp;*&nbsp;N&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/17)
`L103, L113, L114`: Minimum allowable magnitude of the eigenvalues of the second derivative matrix. Similar to IOp(16).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EIGMIN&nbsp;=&nbsp;0.0001.&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EIGMIN&nbsp;=&nbsp;1.&nbsp;/&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/18)
`L103`: Coordinate system.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Proceed&nbsp;normally.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Second&nbsp;derivatives&nbsp;will&nbsp;be&nbsp;computed&nbsp;as&nbsp;directed&nbsp;on&nbsp;the&nbsp;variable&nbsp;definition&nbsp;cards.&nbsp;No&nbsp;optimization&nbsp;will&nbsp;occur.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;optimization&nbsp;in&nbsp;Cartesian&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;full&nbsp;optimization&nbsp;in&nbsp;redundant&nbsp;internal&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;full&nbsp;optimization&nbsp;in&nbsp;pruned&nbsp;distance&nbsp;matrix&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;optimization&nbsp;in&nbsp;z-matrix&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 50&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;full&nbsp;optimization&nbsp;in&nbsp;redundant&nbsp;internal&nbsp;coordinates&nbsp;with&nbsp;large&nbsp;molecular&nbsp;tools.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;the&nbsp;AddRedundant&nbsp;input&nbsp;section&nbsp;for&nbsp;each&nbsp;structure.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;define&nbsp;H-bonds&nbsp;(default).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Define&nbsp;H-bonds&nbsp;with&nbsp;no&nbsp;related&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Define&nbsp;H-bonds&nbsp;and&nbsp;related&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reduce&nbsp;the&nbsp;number&nbsp;of&nbsp;redundant&nbsp;internals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Define&nbsp;all&nbsp;redundant&nbsp;internals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Old&nbsp;definition&nbsp;of&nbsp;redundant&nbsp;internals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2000000).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Skip&nbsp;MM&nbsp;atoms&nbsp;in&nbsp;internal&nbsp;coordinate&nbsp;definitions&nbsp;and&nbsp;do&nbsp;microiterations&nbsp;the&nbsp;old&nbsp;way,&nbsp;in&nbsp;L103.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Include&nbsp;MM&nbsp;atoms&nbsp;in&nbsp;internal&nbsp;coordinate&nbsp;definitions&nbsp;(no&nbsp;microiterations).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Skip&nbsp;MM&nbsp;atoms&nbsp;in&nbsp;internal&nbsp;coordinate&nbsp;definitions&nbsp;and&nbsp;do&nbsp;microiterations&nbsp;the&nbsp;new&nbsp;way,&nbsp;in&nbsp;L120.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Microiterations&nbsp;for&nbsp;pure&nbsp;MM,&nbsp;done&nbsp;in&nbsp;L402.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/19)
`L103`: Search selection.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;6).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Linear&nbsp;and&nbsp;steepest&nbsp;descent.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Steepest&nbsp;descent&nbsp;and&nbsp;linear&nbsp;only&nbsp;when&nbsp;essential.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Quadratic&nbsp;if&nbsp;curvature&nbsp;is&nbsp;correct;&nbsp;RFO&nbsp;if&nbsp;not.&nbsp;Linear&nbsp;as&nbsp;usual.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Quadratic&nbsp;if&nbsp;curvature&nbsp;is&nbsp;correct;&nbsp;RFO&nbsp;if&nbsp;not.&nbsp;No&nbsp;linear&nbsp;search.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RFO&nbsp;and&nbsp;linear.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RFO&nbsp;without&nbsp;linear.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Newton-Raphson&nbsp;and&nbsp;linear.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Newton-Raphson&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GDIIS&nbsp;and&nbsp;linear.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GDIIS&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 15&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GEDIIS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L113, L114`: Search Selection.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;P-RFO&nbsp;or&nbsp;RFO&nbsp;step&nbsp;only&nbsp;(Default).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;P-RFO&nbsp;or&nbsp;RFO&nbsp;step&nbsp;for&nbsp;“wrong”&nbsp;Hessian&nbsp;otherwise&nbsp;Newton&nbsp;Raphson.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/20)
`L101, L106, L108, L109, L110`: Input units.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Angstroms&nbsp;degrees.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bohrs&nbsp;degrees.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Angstroms&nbsp;Radians.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bohrs&nbsp;Radians.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/21)
`L103, L113, L114`: Expert switch.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal&nbsp;mode.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Expert&nbsp;mode.&nbsp;Certain&nbsp;cutoffs&nbsp;used&nbsp;to&nbsp;control&nbsp;the&nbsp;optimization&nbsp;will&nbsp;be&nbsp;relaxed.&nbsp;These&nbsp;include&nbsp;FMAXT,&nbsp;DXMAXT,&nbsp;EIGMAX&nbsp;and&nbsp;EIGMIN.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/22)
`L107`: Whether to reorder coordinates for maximum coincidence.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Assume&nbsp;reactant&nbsp;order&nbsp;equals&nbsp;product&nbsp;order.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;a&nbsp;re-ordering&nbsp;vector&nbsp;from&nbsp;the&nbsp;input.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L115/L123`: Kind of search.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Both&nbsp;directions&nbsp;and&nbsp;generate&nbsp;search&nbsp;vector.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Forward&nbsp;direction&nbsp;and&nbsp;generates&nbsp;vector.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Backward&nbsp;direction&nbsp;and&nbsp;generates&nbsp;vector.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Both&nbsp;directions&nbsp;and&nbsp;generates&nbsp;vector.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Forward&nbsp;direction&nbsp;and&nbsp;reads&nbsp;vector&nbsp;8F10.6.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Forward&nbsp;direction&nbsp;and&nbsp;reads&nbsp;vector&nbsp;8F10.6.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Backward&nbsp;direction&nbsp;and&nbsp;reads&nbsp;vector&nbsp;8F10.6.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Both&nbsp;directions&nbsp;and&nbsp;reads&nbsp;vector&nbsp;8F10.6.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/23)
No longer used.




### IOp(1/24)
Whether to round tetrahedral angles.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Yes).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;round&nbsp;angles&nbsp;within&nbsp;0.001&nbsp;degree.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/25)
Whether SCRF is used with numerical polarizability.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;the&nbsp;field&nbsp;in&nbsp;/Gen/&nbsp;must&nbsp;be&nbsp;cleared&nbsp;each&nbsp;time.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/26)
Accuracy of function being optimized:


* -NNMM&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Energy&nbsp;10^-NN,&nbsp;Gradient&nbsp;10^-MM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;values.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal&nbsp;accuracy&nbsp;for&nbsp;HF&nbsp;(energy&nbsp;and&nbsp;gradient&nbsp;both&nbsp;1.d-7).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Accuracy&nbsp;for&nbsp;DFT&nbsp;with&nbsp;SG1&nbsp;grid&nbsp;(Energy&nbsp;1.d-5,&nbsp;gradient&nbsp;1.d-4).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fine&nbsp;grid&nbsp;accuracy&nbsp;for&nbsp;DFT&nbsp;(Energy&nbsp;1.d-7,&nbsp;gradient&nbsp;1.d-6).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ultrafine&nbsp;accuracy&nbsp;(E&nbsp;1.d-7,&nbsp;G&nbsp;1.d-6).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Superfine&nbsp;accuracy&nbsp;(E&nbsp;1.d-7,&nbsp;G&nbsp;1.d-7).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UltraFine+PCM&nbsp;accuracy&nbsp;(E&nbsp;5.d-5,&nbsp;G&nbsp;5.d-6)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/27)
= IJKL (i.e. 1000*I+100*J+10*K+L).


Transition state searching using QST and redundant internal coordinates


* L&nbsp;=&nbsp;0,1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input&nbsp;one&nbsp;structure,&nbsp;either&nbsp;initial&nbsp;guess&nbsp;of&nbsp;the&nbsp;minimizing&nbsp;structure&nbsp;or&nbsp;transition&nbsp;structure&nbsp;without&nbsp;QST.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* L&nbsp;=&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input&nbsp;2&nbsp;structures.&nbsp;The&nbsp;first&nbsp;one&nbsp;is&nbsp;the&nbsp;reactant,&nbsp;the&nbsp;second&nbsp;one&nbsp;is&nbsp;the&nbsp;product.&nbsp;The&nbsp;union&nbsp;of&nbsp;the&nbsp;two&nbsp;redundant&nbsp;coordinates&nbsp;is&nbsp;taken&nbsp;as&nbsp;the&nbsp;redundant&nbsp;coordinates&nbsp;for&nbsp;the&nbsp;TS.&nbsp;The&nbsp;values&nbsp;of&nbsp;the&nbsp;TS&nbsp;coordinate&nbsp;are&nbsp;estimated&nbsp;by&nbsp;interpolating&nbsp;the&nbsp;structure&nbsp;of&nbsp;R&nbsp;and&nbsp;P.&nbsp;R&nbsp;and&nbsp;Pare&nbsp;used&nbsp;to&nbsp;guide&nbsp;the&nbsp;QST&nbsp;optimization&nbsp;of&nbsp;the&nbsp;TS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* L&nbsp;=&nbsp;3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input&nbsp;3&nbsp;structures.&nbsp;The&nbsp;first&nbsp;one&nbsp;is&nbsp;the&nbsp;reactant&nbsp;the&nbsp;second&nbsp;one&nbsp;is&nbsp;the&nbsp;product.&nbsp;The&nbsp;third&nbsp;one&nbsp;is&nbsp;the&nbsp;initial&nbsp;guess&nbsp;of&nbsp;the&nbsp;transition&nbsp;structure.&nbsp;R&nbsp;and&nbsp;P&nbsp;are&nbsp;used&nbsp;to&nbsp;guide&nbsp;the&nbsp;QST&nbsp;optimization&nbsp;of&nbsp;the&nbsp;TS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* K&nbsp;=&nbsp;1-9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Interpolation&nbsp;of&nbsp;initial&nbsp;guess&nbsp;of&nbsp;TS&nbsp;between&nbsp;R&nbsp;and&nbsp;P&nbsp;(TS&nbsp;=&nbsp;0.1*J*R&nbsp;+&nbsp;0.1*(10-J)*P,&nbsp;default&nbsp;J=5).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* J&nbsp;=&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LST&nbsp;constraint&nbsp;in&nbsp;internals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* J&nbsp;=&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QST&nbsp;constraint&nbsp;in&nbsp;internals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* J&nbsp;=&nbsp;3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LST&nbsp;constraint&nbsp;in&nbsp;distance&nbsp;matrix&nbsp;space.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* J&nbsp;=&nbsp;4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QST&nbsp;constraint&nbsp;in&nbsp;distance&nbsp;matrix&nbsp;space.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* I&nbsp;=&nbsp;0-9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Control&nbsp;parameters&nbsp;for&nbsp;climbing&nbsp;phase&nbsp;of&nbsp;QST&nbsp;(e.g.&nbsp;QSTRad&nbsp;=&nbsp;0.01*I,&nbsp;default&nbsp;QSTrad&nbsp;=&nbsp;0.05).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/28)
`L103`: Number of translations and rotations to remove during redundant coordinate transformations.


* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal&nbsp;(6&nbsp;or&nbsp;5&nbsp;for&nbsp;linear&nbsp;molecules).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;same&nbsp;as&nbsp;-1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/29)
`L101`: Specification of nuclear centers.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;By&nbsp;z-matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;By&nbsp;direct&nbsp;coordinate&nbsp;input&nbsp;(must&nbsp;set&nbsp;IOp(29)&nbsp;in&nbsp;L202).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Get&nbsp;z-matrix&nbsp;and&nbsp;variables&nbsp;from&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Get&nbsp;Cartesian&nbsp;coordinates&nbsp;only&nbsp;from&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;By&nbsp;model&nbsp;builder,&nbsp;model&nbsp;A.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;By&nbsp;model&nbsp;builder,&nbsp;model&nbsp;B.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Get&nbsp;z-matrix&nbsp;from&nbsp;the&nbsp;checkpoint&nbsp;file,&nbsp;but&nbsp;read&nbsp;new&nbsp;values&nbsp;for&nbsp;some&nbsp;variables&nbsp;from&nbsp;the&nbsp;input&nbsp;stream.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Get&nbsp;all&nbsp;input&nbsp;(title,&nbsp;charge&nbsp;and&nbsp;multiplicity,&nbsp;structure)&nbsp;from&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;details&nbsp;of&nbsp;the&nbsp;model-building&nbsp;process.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;100).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;abort&nbsp;job&nbsp;if&nbsp;model&nbsp;builder&nbsp;generates&nbsp;a&nbsp;z-matrix&nbsp;with&nbsp;too&nbsp;many&nbsp;variables.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Abort&nbsp;job&nbsp;if&nbsp;model&nbsp;builder&nbsp;generates&nbsp;a&nbsp;z-matrix&nbsp;with&nbsp;too&nbsp;many&nbsp;variables.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;optimization&nbsp;flags&nbsp;in&nbsp;format&nbsp;50L1&nbsp;after&nbsp;the&nbsp;z-matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;all&nbsp;optimization&nbsp;flags&nbsp;to&nbsp;optimize.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Purge&nbsp;flags&nbsp;except&nbsp;the&nbsp;frozen&nbsp;variables.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rebuild&nbsp;the&nbsp;coordinate&nbsp;system.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(2+3)&nbsp;Purge&nbsp;all&nbsp;flags&nbsp;but&nbsp;keep&nbsp;the&nbsp;coordinate&nbsp;definition.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;new&nbsp;redundant&nbsp;coordinates,&nbsp;reading&nbsp;an&nbsp;input&nbsp;section&nbsp;selecting&nbsp;frozen&nbsp;and&nbsp;optimized&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mark&nbsp;all&nbsp;internal&nbsp;coordinates&nbsp;as&nbsp;frozen&nbsp;before&nbsp;handling&nbsp;ModRed&nbsp;input&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;same&nbsp;as&nbsp;10000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mark&nbsp;z-matrix&nbsp;constants&nbsp;as&nbsp;frozen&nbsp;variables&nbsp;rather&nbsp;than&nbsp;wired-in&nbsp;constants.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;retain&nbsp;symbolic&nbsp;constants.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;a&nbsp;symbolic&nbsp;z-matrix&nbsp;using&nbsp;all&nbsp;Cartesians&nbsp;if&nbsp;none&nbsp;is&nbsp;present&nbsp;on&nbsp;the&nbsp;checkpoint&nbsp;file&nbsp;(a&nbsp;hack&nbsp;to&nbsp;make&nbsp;IRCs&nbsp;work&nbsp;with&nbsp;Cartesian&nbsp;input).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200000&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;1,&nbsp;but&nbsp;retain&nbsp;the&nbsp;redundant&nbsp;internal&nbsp;coordinate&nbsp;definitions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Get&nbsp;input&nbsp;type&nbsp;or&nbsp;chk&nbsp;file&nbsp;name&nbsp;to&nbsp;read&nbsp;from&nbsp;input&nbsp;stream;&nbsp;title&nbsp;and&nbsp;charge/multiplicity&nbsp;for&nbsp;each&nbsp;structure&nbsp;read&nbsp;from&nbsp;input.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;input&nbsp;type&nbsp;for&nbsp;each&nbsp;structure&nbsp;from&nbsp;input&nbsp;stream;&nbsp;title&nbsp;and&nbsp;charge/multiplicity&nbsp;are&nbsp;those&nbsp;of&nbsp;last&nbsp;chk&nbsp;file&nbsp;read.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;0000000.&nbsp;&nbsp;&nbsp;&nbsp;
* 00000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(read&nbsp;one&nbsp;set&nbsp;of&nbsp;charge/multiplicity
pairs&nbsp;unless&nbsp;both&nbsp;NFrag&nbsp;and&nbsp;ONIOM&nbsp;are&nbsp;set).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;ONIOM&nbsp;charge/multiplicity&nbsp;pairs&nbsp;if&nbsp;reading
any.&nbsp;Fragment&nbsp;values&nbsp;will&nbsp;be&nbsp;defaulted&nbsp;from&nbsp;the&nbsp;supermolecule.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;fragment&nbsp;charge/multiplicity&nbsp;pairs&nbsp;if&nbsp;reading&nbsp;any.&nbsp;ONIOM&nbsp;model&nbsp;system&nbsp;values&nbsp;will&nbsp;be&nbsp;defaulted&nbsp;from&nbsp;the&nbsp;real&nbsp;system.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;two&nbsp;lines,&nbsp;with&nbsp;ONIOM&nbsp;followed&nbsp;by&nbsp;fragment&nbsp;values.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/30)
`L103`: Are the read-write files to be updated? This option is set for the last call to 103 in frequency calculations in order to preserve the values of the variables for archiving. It also suppresses error termination on large gradients.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No,&nbsp;print&nbsp;internal&nbsp;coordinate&nbsp;step&nbsp;but&nbsp;don’t&nbsp;set&nbsp;up&nbsp;for&nbsp;microiterations&nbsp;and&nbsp;don’t&nbsp;update&nbsp;the&nbsp;RWF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;up&nbsp;for&nbsp;step&nbsp;but&nbsp;don’t&nbsp;update&nbsp;coordinates;&nbsp;for&nbsp;QM/MM&nbsp;iterative&nbsp;frequencies.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(1/32)
Title card punch control.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;punch.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Punch.&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(1/33)
`L101, L102, L103, L106, L109, L110, L113, L114`: Debug print.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Off.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;On.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/34)
`L101, L102, L103`: Debug + Dump print.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Off.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;On.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/35)
`L102-L112`: Restart.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal&nbsp;optimization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;First&nbsp;point&nbsp;of&nbsp;a&nbsp;restart.&nbsp;Get&nbsp;geometry,&nbsp;wavefunction,&nbsp;etc.&nbsp;from&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/36)
Checkpoint.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal&nbsp;checkpoint&nbsp;of&nbsp;optimization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Suppress&nbsp;checkpointing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/38)
`L103, L106, L107, L108, L109, L110, L111, and L112`: Entry control option (Not by L102 and L105).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Continuation&nbsp;of&nbsp;run.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initial&nbsp;entry.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N>1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In&nbsp;L103:&nbsp; Initial&nbsp;entry&nbsp;of&nbsp;guided&nbsp;optimization&nbsp;using&nbsp;N&nbsp;levels.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In&nbsp;L106:&nbsp; differentiate&nbsp;N^th&nbsp;derivatives&nbsp;once.&nbsp;In&nbsp;L110&nbsp;and&nbsp;L111:&nbsp;differentiate&nbsp;energy&nbsp;N&nbsp;times.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In&nbsp;L106:&nbsp;differentiate&nbsp;with&nbsp;respect&nbsp;to&nbsp;nuclear&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In&nbsp;L106:&nbsp;differentiate&nbsp;with&nbsp;respect&nbsp;to&nbsp;electric&nbsp;field.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In&nbsp;L106:&nbsp;differentiate&nbsp;with&nbsp;respect&nbsp;to&nbsp;field&nbsp;and&nbsp;nuclear.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In&nbsp;L106:&nbsp;Save&nbsp;original&nbsp;forces&nbsp;and&nbsp;force&nbsp;constants.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In&nbsp;L106:&nbsp;Assume&nbsp;all&nbsp;quantities&nbsp;available&nbsp;at&nbsp;the&nbsp;central&nbsp;point&nbsp;will&nbsp;also&nbsp;be&nbsp;computed&nbsp;at&nbsp;displaced&nbsp;points.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In&nbsp;L106:&nbsp;No&nbsp;analytic&nbsp;nuclear&nbsp;coordinate&nbsp;derivatives&nbsp;will&nbsp;be&nbsp;done&nbsp;at&nbsp;displaced&nbsp;points,&nbsp;even&nbsp;though&nbsp;they&nbsp;were&nbsp;done&nbsp;at&nbsp;the&nbsp;central&nbsp;point.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000000&nbsp;&nbsp;&nbsp;&nbsp;L106&nbsp;control&nbsp;of&nbsp;number&nbsp;of&nbsp;diff.&nbsp;steps.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;2-point&nbsp;differentiation&nbsp;(one&nbsp;step&nbsp;each&nbsp;way).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200000&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;4-point&nbsp;differentiation&nbsp;(two&nbsp;steps&nbsp;each&nbsp;way).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Differentiate&nbsp;with&nbsp;respect&nbsp;to&nbsp;translation&nbsp;vectors&nbsp;for&nbsp;PBC&nbsp;for&nbsp;elasticity.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;differentiate&nbsp;with&nbsp;respect&nbsp;to&nbsp;translation&nbsp;vectors.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/39)
`L106, L109, L110, L111`: Step size control for numerical differentiation.


`L115`: Path step size.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;internal&nbsp;default&nbsp;(0.001&nbsp;Angstroms&nbsp;and&nbsp;0.001/3&nbsp;au&nbsp;E-field&nbsp;in&nbsp;L106,&nbsp;0.005&nbsp;Å&nbsp;in&nbsp;L109,&nbsp;0.01&nbsp;Angstrom&nbsp;in&nbsp;L110,&nbsp;0.001&nbsp;au&nbsp;in&nbsp;L111).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;step-size&nbsp;of&nbsp;0.0001*N&nbsp;(angstroms&nbsp;in&nbsp;L106,&nbsp;L109,&nbsp;L110,&nbsp;electric&nbsp;field&nbsp;au&nbsp;in&nbsp;L111).&nbsp;In&nbsp;L106,&nbsp;the&nbsp;electric&nbsp;field&nbsp;step&nbsp;will&nbsp;be&nbsp;3x&nbsp;smaller.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;step&nbsp;size&nbsp;(up&nbsp;to&nbsp;2&nbsp;for&nbsp;L106,&nbsp;1&nbsp;for&nbsp;others),&nbsp;free-format.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N>1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;step-size&nbsp;of&nbsp;0.0001*N&nbsp;atomic&nbsp;units&nbsp;everywhere.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L123`: Step-size.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(0.1&nbsp;Bohr,&nbsp;except&nbsp;0.075&nbsp;Bohr&nbsp;for&nbsp;EulerPC,&nbsp;or&nbsp;original&nbsp;value&nbsp;if&nbsp;restart.&nbsp;DVV&nbsp;default&nbsp;is&nbsp;0.25&nbsp;fs).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N<0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Supplied&nbsp;step&nbsp;size&nbsp;is&nbsp;in&nbsp;units&nbsp;of&nbsp;sqrt(amu)*Bohr.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Supplied&nbsp;step&nbsp;size&nbsp;is&nbsp;in&nbsp;units&nbsp;of&nbsp;Bohr.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/40)
`L113, L114`: Hessian recalculation.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pick&nbsp;up&nbsp;analytic&nbsp;second&nbsp;derivatives&nbsp;every&nbsp;time.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Just&nbsp;update.&nbsp;The&nbsp;default,&nbsp;except&nbsp;for&nbsp;CalcAll.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Recalculate&nbsp;the&nbsp;Hessian&nbsp;every&nbsp;N&nbsp;steps.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L116`:  Whether to read initial E-field.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Start&nbsp;with&nbsp;0.0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;from&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;from&nbsp;input&nbsp;stream.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L123`: Truncation error threshold for the modified BS integration routine (EPS).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10^-8&nbsp;Bohr).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N&nbsp;Bohr.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/41)
Take previous geometry from checkpoint file:


* N&nbsp;>&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N^th&nbsp;point&nbsp;of&nbsp;geometry&nbsp;optimization&nbsp;(z-matrix&nbsp;only).&nbsp;Converted&nbsp;to&nbsp;-(N+1)&nbsp;if&nbsp;no&nbsp;z-matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;<&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N^th&nbsp;geometry&nbsp;on&nbsp;trajectory&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/42)
`L103, L115, L118, L123`: Number of points along the reaction path in each direction, or maximum number of points in one trajectory. Default 10 for IRC, 100 for trajectory.


`L117`: Cutoff to be used in evaluating densities.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.0D-10.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.0D-N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/43)
`L116`: Extent of Reaction Field.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dipole.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Quadrupole.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Octapole.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hexadecapole.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L117`: How to define Radii.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;is&nbsp;11.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;internally&nbsp;stored&nbsp;Radii,&nbsp;centers&nbsp;will&nbsp;be&nbsp;on&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read-in&nbsp;centers&nbsp;and&nbsp;radii&nbsp;on&nbsp;cards.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;Merz-Kollman&nbsp;radii&nbsp;(Default).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;CHELP&nbsp;(Francl)&nbsp;recommended&nbsp;radii.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;CHELPG&nbsp;(Breneman)&nbsp;recommended&nbsp;radii.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;replacement&nbsp;radii&nbsp;for&nbsp;selected&nbsp;atom&nbsp;types&nbsp;as&nbsp;pairs&nbsp;(IAn,Rad)&nbsp;or&nbsp;(Symbol,Rad),&nbsp;terminated&nbsp;by&nbsp;a&nbsp;blank&nbsp;line.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;replacement&nbsp;radii&nbsp;for&nbsp;selected&nbsp;atoms&nbsp;as&nbsp;pairs&nbsp;(I,Rad),&nbsp;terminated&nbsp;by&nbsp;a&nbsp;blank&nbsp;line.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


Initial radius of spheres to be placed around attractors to “capture” the gradient trajectories. The final radius is then automatically optimized separately for each atom.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NM&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.M=NM/10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/44)
`L115, L123,` and `L125`: IRC Type.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Optimization&nbsp;coordinates&nbsp;(Default&nbsp;3&nbsp;in&nbsp;L15&nbsp;and&nbsp;L123,&nbsp;2&nbsp;in&nbsp;L125).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Cartesian.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Internal&nbsp;(NYI&nbsp;in&nbsp;L123).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mass-weighted&nbsp;Cartesian&nbsp;(NYI&nbsp;in&nbsp;L125).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* M0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initial&nbsp;interpolation&nbsp;in&nbsp;L125&nbsp;(default&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L117`: Maximum distance between a nucleus and its portion of the isosurface – used in Trudge only to eliminate, from the outset, points which clearly lie in another basin. This parameter should be chosen with the parameter Cont in mind:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10.0&nbsp;au.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NM&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.M&nbsp;au&nbsp;=&nbsp;NM/10.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L121`: Seed for random number generator (ISeed).


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;system&nbsp;time&nbsp;initialize&nbsp;iseed&nbsp;(Note&nbsp;each&nbsp;run&nbsp;will&nbsp;give&nbsp;different&nbsp;results).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;default&nbsp;seed&nbsp;value&nbsp;(ISeed&nbsp;=&nbsp;398465).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;random&nbsp;number&nbsp;seed&nbsp;to&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/45)
`L123`: Options.


* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Which&nbsp;IRC&nbsp;integrator&nbsp;to&nbsp;use.&nbsp;Default&nbsp;=&nbsp;3,&nbsp;except&nbsp;6&nbsp;for&nbsp;ONIOM&nbsp;QuadMac/Micro&nbsp;or&nbsp;1&nbsp;for&nbsp;GradientOnly.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 01&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Euler.&nbsp;&nbsp;&nbsp;&nbsp;
* 02&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LQA.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 03&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HPC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 04&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GS2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 05&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DVV.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 06&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Euler-based&nbsp;PC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Coordinate&nbsp;driving&nbsp;schemes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is&nbsp;the&nbsp;integration&nbsp;being&nbsp;done&nbsp;on&nbsp;an&nbsp;empirical&nbsp;surface?&nbsp;Default=2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;this&nbsp;is&nbsp;an&nbsp;empirical&nbsp;surface.&nbsp;The&nbsp;energies&nbsp;and&nbsp;derivatives&nbsp;required&nbsp;for&nbsp;the&nbsp;IRC&nbsp;integration&nbsp;are&nbsp;NOT&nbsp;evaluated&nbsp;in&nbsp;this&nbsp;link.&nbsp;Instead&nbsp;it&nbsp;is&nbsp;assumed&nbsp;that&nbsp;an&nbsp;external&nbsp;program&nbsp;communicates&nbsp;the&nbsp;appropriate&nbsp;values&nbsp;with&nbsp;Link&nbsp;402,&nbsp;etc.&nbsp;Also,&nbsp;the&nbsp;force&nbsp;constant&nbsp;matrix,&nbsp;when&nbsp;needed,&nbsp;is&nbsp;simply&nbsp;diagonalized,&nbsp;i.e.&nbsp;translation&nbsp;and&nbsp;rotation&nbsp;projections&nbsp;are&nbsp;NOT&nbsp;used.&nbsp;Also,&nbsp;all&nbsp;atomic&nbsp;masses&nbsp;are&nbsp;set&nbsp;to&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Order&nbsp;of&nbsp;magnitude&nbsp;for&nbsp;the&nbsp;step&nbsp;size&nbsp;relative&nbsp;to&nbsp;the&nbsp;integer&nbsp;value&nbsp;given&nbsp;with&nbsp;the&nbsp;StepSize=N&nbsp;option&nbsp;on&nbsp;the&nbsp;route&nbsp;line&nbsp;—&nbsp;IOp(1/39).&nbsp;Default=2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Nxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Integration&nbsp;step&nbsp;size&nbsp;is&nbsp;taken&nbsp;as&nbsp;IOp(1/39)*10^-N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Whether&nbsp;or&nbsp;not&nbsp;energies&nbsp;reported&nbsp;in&nbsp;the&nbsp;final&nbsp;summary&nbsp;table&nbsp;should&nbsp;be&nbsp;given&nbsp;relative&nbsp;to&nbsp;the&nbsp;TS&nbsp;energy.&nbsp;Default=1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xxxxx&nbsp;&nbsp;&nbsp;&nbsp;Whether&nbsp;or&nbsp;not&nbsp;statistics&nbsp;over&nbsp;coordinates&nbsp;should&nbsp;be&nbsp;converted&nbsp;to&nbsp;Angstoms/Degrees&nbsp;when&nbsp;reported&nbsp;in&nbsp;the&nbsp;summary&nbsp;table.&nbsp;Default=1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xxxxx&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xxxxx&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Should&nbsp;a&nbsp;URVA&nbsp;input&nbsp;file&nbsp;be&nbsp;written?&nbsp;Default=2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xxxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Should&nbsp;IRC&nbsp;data&nbsp;besaved&nbsp;to&nbsp;the&nbsp;PES&nbsp;data&nbsp;structure&nbsp;file?&nbsp;Default=1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xxxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xxxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xxxxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;When&nbsp;second-order&nbsp;methods&nbsp;are&nbsp;employed,&nbsp;should&nbsp;the&nbsp;Newton-Raphson&nbsp;step&nbsp;test&nbsp;be&nbsp;carried&nbsp;out?&nbsp;Default=1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xxxxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xxxxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/46)
Order of multipoles in numerical SCRF.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dipole.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Quadrupole.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Octapole.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hexadecapole.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/47)
Number of redundant internal coordinates to allow for.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;Max(50000,MCV/(100*NStruc))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/48)
IRCMax control.


* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;IRCMax.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Include&nbsp;zero-point&nbsp;energy.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/49)
Options to IRC path relaxation (IJKL).


* L&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2/1&nbsp;don’t/do&nbsp;optimize&nbsp;reactant&nbsp;structure.&nbsp;Default:&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* K&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2/1&nbsp;don’t/do&nbsp;optimize&nbsp;product&nbsp;structure.&nbsp;Default:&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* J&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3/2/1&nbsp;don’t/QST3/QST2&nbsp;optimize&nbsp;TS&nbsp;structure&nbsp;(for&nbsp;QST&nbsp;input).&nbsp;Default:&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* I&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2/1&nbsp;unimolecular/bimolecular&nbsp;reaction.&nbsp;Default:&nbsp;unimolecular.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/52)
`L101 and L120`: Type of ONIOM calculation.


* 0/1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;One&nbsp;layer,&nbsp;normal&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Two&nbsp;layers.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Three&nbsp;layers.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(20).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Include&nbsp;electrostatics&nbsp;in&nbsp;model&nbsp;systems&nbsp;using&nbsp;MM&nbsp;charges&nbsp;(in&nbsp;case&nbsp;of&nbsp;three-layer&nbsp;ONIOM,&nbsp;this&nbsp;includes&nbsp;the&nbsp;charges&nbsp;in&nbsp;both&nbsp;the&nbsp;small&nbsp;model&nbsp;and&nbsp;the&nbsp;intermediate&nbsp;model&nbsp;system).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;electrostatics&nbsp;included&nbsp;in&nbsp;the&nbsp;model&nbsp;systems.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As&nbsp;10,&nbsp;but&nbsp;exclude&nbsp;the&nbsp;MM&nbsp;charges&nbsp;in&nbsp;the&nbsp;calculations&nbsp;on&nbsp;the&nbsp;smallest&nbsp;model&nbsp;system&nbsp;in&nbsp;case&nbsp;of&nbsp;a&nbsp;three-layer&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As&nbsp;10,&nbsp;but&nbsp;exclude&nbsp;the&nbsp;MM&nbsp;charges&nbsp;in&nbsp;the&nbsp;calculations&nbsp;on&nbsp;the&nbsp;intermediate&nbsp;model&nbsp;system&nbsp;in&nbsp;case&nbsp;of&nbsp;a&nbsp;three-layer&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;full&nbsp;square&nbsp;for&nbsp;testing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;atomic&nbsp;charge&nbsp;type&nbsp;N-1&nbsp;during&nbsp;microiterations.&nbsp;The&nbsp;default&nbsp;is&nbsp;MK&nbsp;charges.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* M0000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type&nbsp;of&nbsp;link&nbsp;atoms&nbsp;for&nbsp;the&nbsp;MM&nbsp;calculation&nbsp;in&nbsp;QM/MM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Conventional&nbsp;(Maseras)&nbsp;style.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ONIOM&nbsp;style.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* L00000&nbsp;&nbsp;&nbsp;&nbsp;Whether&nbsp;to&nbsp;read&nbsp;additional&nbsp;charges&nbsp;with&nbsp;electronic&nbsp;embedding.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* K000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Whether&nbsp;to&nbsp;create&nbsp;new&nbsp;entries&nbsp;in&nbsp;Common/Mol&nbsp;for&nbsp;the&nbsp;link&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/53)
`L120`: Action of each invocation of L120.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;nothing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;up&nbsp;point&nbsp;MM&nbsp;on&nbsp;RWF&nbsp;from&nbsp;initial&nbsp;data.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;up&nbsp;point&nbsp;MM&nbsp;on&nbsp;RWF&nbsp;from&nbsp;initial&nbsp;data&nbsp;and&nbsp;restore&nbsp;point&nbsp;MM&nbsp;on&nbsp;checkpoint&nbsp;file&nbsp;if&nbsp;ONIOM&nbsp;data&nbsp;is&nbsp;present&nbsp;there.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Restore&nbsp;point&nbsp;M&nbsp;from&nbsp;data&nbsp;on&nbsp;the&nbsp;RWF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Integrate&nbsp;energy.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Integrate&nbsp;energy&nbsp;and&nbsp;gradient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Integrate&nbsp;energy,&nbsp;gradient,&nbsp;and&nbsp;Hessian.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Restore&nbsp;point&nbsp;MM&nbsp;from&nbsp;RWF&nbsp;but&nbsp;do&nbsp;not&nbsp;create&nbsp;a&nbsp;new&nbsp;model&nbsp;system.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NN0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;necessary&nbsp;information&nbsp;(some&nbsp;RWF’s,&nbsp;energy,&nbsp;gradients,&nbsp;Hessian)&nbsp;of&nbsp;point&nbsp;NN&nbsp;of&nbsp;the&nbsp;ONIOM&nbsp;grid.&nbsp;NN&nbsp;=&nbsp;MaxLev^2&nbsp;+&nbsp;1&nbsp;(currently&nbsp;17)&nbsp;to&nbsp;restore&nbsp;real&nbsp;system.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MM000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Next&nbsp;point&nbsp;to&nbsp;do&nbsp;is&nbsp;MM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + Calc&nbsp;Level&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + High&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4—7—9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|    |   |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + Mid&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2—5—8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|    |   |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + Low&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1—3—6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    +  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;S  M  L&nbsp;system&nbsp;size&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/54)
Whether to recover initial energy during IRCMax from checkpoint file.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/55)
`L103`: Options for GDIIS. ICos*1000+IChkC*100+IMix*10+Method form.


`L115`: IRC optimization.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;use&nbsp;gradients&nbsp;to&nbsp;find&nbsp;the&nbsp;next&nbsp;geometry.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;displacements&nbsp;to&nbsp;find&nbsp;the&nbsp;next&nbsp;geometry.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/56)
Set of atom type names to parse.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Accept&nbsp;any.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dreiding/UFF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Amber.&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Amber&nbsp;allowing&nbsp;any&nbsp;symbol,&nbsp;for&nbsp;use&nbsp;with&nbsp;parameters&nbsp;in&nbsp;input&nbsp;stream.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/57)
Whether to produce connectivity.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(4&nbsp;if&nbsp;reading&nbsp;geometry&nbsp;from&nbsp;checkpoint&nbsp;file&nbsp;and&nbsp;connectivity&nbsp;is&nbsp;there,&nbsp;otherwise&nbsp;3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;read&nbsp;from&nbsp;input&nbsp;stream.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;generate&nbsp;connectivity.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;read&nbsp;from&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;read&nbsp;from&nbsp;RWF&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;modifications.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Connectivity&nbsp;input&nbsp;is&nbsp;in&nbsp;terms&nbsp;of&nbsp;z-matrix&nbsp;entries,&nbsp;including&nbsp;dummy&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/58)
`L115`: IRCMax control.


* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;IRC&nbsp;rather&nbsp;than&nbsp;IRCMax.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store&nbsp;compound&nbsp;energy;&nbsp;default&nbsp;for&nbsp;IRCMax.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Zero-point&nbsp;energies&nbsp;are&nbsp;available&nbsp;during&nbsp;IRCMax.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/59)
`L103`: Update of coordinates.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;New&nbsp;versions&nbsp;(RedCar/RedQ2X);&nbsp;fall&nbsp;back&nbsp;to&nbsp;ORedCr/RedQX1&nbsp;if&nbsp;RedCar&nbsp;fails.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Old&nbsp;version&nbsp;(ORedCr/RedQX).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Old&nbsp;version&nbsp;(ORedCr/RedQX1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;New&nbsp;version&nbsp;(ORedCr/RedQ2X)&nbsp;but&nbsp;fall&nbsp;back&nbsp;to&nbsp;ORedCr/RedQX&nbsp;if&nbsp;RedCar&nbsp;fails.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMMM0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IAprBG&nbsp;in&nbsp;Red2BG.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Re-use&nbsp;eigenvectors&nbsp;of&nbsp;G&nbsp;only&nbsp;if&nbsp;exact.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Re-use&nbsp;eigenvectors&nbsp;of&nbsp;G&nbsp;if&nbsp;they&nbsp;are&nbsp;linearly&nbsp;independent.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Test&nbsp;old&nbsp;eigenvectors&nbsp;of&nbsp;G&nbsp;but&nbsp;don’t&nbsp;re-use&nbsp;them.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;look&nbsp;at&nbsp;old&nbsp;eigenvectors.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 50&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Re-use&nbsp;eigenvectors&nbsp;of&nbsp;G&nbsp;if&nbsp;the&nbsp;RMS&nbsp;of&nbsp;the&nbsp;elements&nbsp;of&nbsp;the&nbsp;new&nbsp;G&nbsp;in&nbsp;the&nbsp;old&nbsp;null&nbsp;space&nbsp;is&nbsp;less&nbsp;than&nbsp;the&nbsp;threshold.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NN00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RMS&nbsp;<&nbsp;10^-N,&nbsp;default&nbsp;4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* M0000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Form&nbsp;G-inverse&nbsp;from&nbsp;the&nbsp;B&nbsp;eigen-values/vectors.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Form&nbsp;G-inverse&nbsp;directly&nbsp;from&nbsp;G.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;G-&nbsp;via&nbsp;diagonalization&nbsp;of&nbsp;G&nbsp;(NYI).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;G-&nbsp;via&nbsp;SVD&nbsp;on&nbsp;B,&nbsp;returning&nbsp;only&nbsp;the&nbsp;eigenvectors&nbsp;with&nbsp;nontrivial&nbsp;eigenvalues.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/60)
Interpret extra integer and fp values in z-matrix as scan information.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/61)
How ONIOM should leave the RWF at the end of each geometry.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal:&nbsp;leave&nbsp;the&nbsp;RWF&nbsp;set&nbsp;up&nbsp;for&nbsp;the&nbsp;low-level&nbsp;calculation&nbsp;on&nbsp;the&nbsp;real&nbsp;system.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MOMM:&nbsp;leave&nbsp;the&nbsp;RWF&nbsp;set&nbsp;up&nbsp;for&nbsp;the&nbsp;real&nbsp;system,&nbsp;but&nbsp;with&nbsp;NBasis&nbsp;and&nbsp;NBsUse&nbsp;for&nbsp;the&nbsp;high-level&nbsp;calculation&nbsp;on&nbsp;the&nbsp;model&nbsp;system.&nbsp;Useful&nbsp;for&nbsp;treating&nbsp;the&nbsp;full&nbsp;system&nbsp;as&nbsp;having&nbsp;electrons&nbsp;only&nbsp;on&nbsp;the&nbsp;QM&nbsp;atoms.&nbsp;This&nbsp;is&nbsp;really&nbsp;a&nbsp;hack&nbsp;for&nbsp;two&nbsp;layer&nbsp;QM:MM&nbsp;ONIOM&nbsp;ADMP&nbsp;and&nbsp;should&nbsp;probably&nbsp;be&nbsp;generalized&nbsp;to&nbsp;behave&nbsp;like&nbsp;an&nbsp;ONIOM-PCM-A&nbsp;case.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Lowest&nbsp;level&nbsp;is&nbsp;MO,&nbsp;but&nbsp;normal&nbsp;setup&nbsp;at&nbsp;end.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10,&nbsp;but&nbsp;20&nbsp;if&nbsp;doing&nbsp;EE&nbsp;microiterations).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Leave&nbsp;the&nbsp;charges&nbsp;file&nbsp;(605)&nbsp;from&nbsp;the&nbsp;best&nbsp;calculation&nbsp;that&nbsp;produced&nbsp;one.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Leave&nbsp;605&nbsp;in&nbsp;its&nbsp;normal&nbsp;state&nbsp;(present&nbsp;if&nbsp;from&nbsp;real,&nbsp;low-level).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/62)
Counterpoise control.


* NN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NN&nbsp;fragments.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1NN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;use&nbsp;of&nbsp;new&nbsp;ghost&nbsp;atoms&nbsp;(default).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2NN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;use&nbsp;of&nbsp;old&nbsp;ghost&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Counterpoise&nbsp;(default).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fragment&nbsp;guess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(1/63)
Step in counterpoise calculation.


* LMM&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;L:&nbsp;order&nbsp;of&nbsp;derivatives:&nbsp;1&nbsp;=&nbsp;Energy,&nbsp;2&nbsp;=&nbsp;Gradient,…&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MM:&nbsp;0&nbsp;=&nbsp;Supermolecule,&nbsp;1-NFrag&nbsp;=&nbsp;Fragments&nbsp;with&nbsp;ghost&nbsp;atoms,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NFrag+1-2*NFrag&nbsp;=&nbsp;lone&nbsp;fragments.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/64)
Molecular mechanics force field selection.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dreiding.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UFF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AMBER.&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;only&nbsp;hard-wired.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;soft&nbsp;and&nbsp;hard-wired,&nbsp;hard-wired&nbsp;has&nbsp;priority.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;soft&nbsp;and&nbsp;hard-wired,&nbsp;soft&nbsp;has&nbsp;priority.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;only&nbsp;soft.&nbsp;Lowest&nbsp;2&nbsp;digits&nbsp;then&nbsp;have&nbsp;no&nbsp;meaning.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;read&nbsp;modifications&nbsp;to&nbsp;parameter&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;modifications&nbsp;to&nbsp;parameter&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;With&nbsp;soft&nbsp;parameters,&nbsp;abort&nbsp;when&nbsp;different&nbsp;parameters&nbsp;match&nbsp;to&nbsp;the&nbsp;same&nbsp;degree.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;first&nbsp;when&nbsp;there&nbsp;are&nbsp;equivalent&nbsp;matches.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;last&nbsp;when&nbsp;there&nbsp;are&nbsp;equivalent&nbsp;matches.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


If IOp(67) = 3, then the default is to apply soft parameters with higher priority.




### IOp(1/65)
Control of which terms are included in MM, corresponding to the ‘classes’ in FncInf.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;all&nbsp;(default).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Non-bonded.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stretching.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bending.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Torsion.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Out-of-plane.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Stretch-bend.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/66)
Whether to generate QEQ charges, over-write the values in AtChMM, or to use the values already there.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2,&nbsp;1&nbsp;⇒&nbsp;221).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;QEq&nbsp;here&nbsp;in&nbsp;GenChg.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;do&nbsp;QEq.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;charges&nbsp;here&nbsp;using&nbsp;QEqN.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(20).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;for&nbsp;atoms&nbsp;which&nbsp;were&nbsp;not&nbsp;explicitly&nbsp;typed.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;for&nbsp;all&nbsp;atoms&nbsp;regardless&nbsp;of&nbsp;typing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(200).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;for&nbsp;atoms&nbsp;which&nbsp;have&nbsp;charge&nbsp;specified&nbsp;or&nbsp;defaulted&nbsp;to&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;for&nbsp;all&nbsp;atoms&nbsp;regardless&nbsp;of&nbsp;initial&nbsp;charge.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* `MMMMM000`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IType&nbsp;passed&nbsp;to&nbsp;QEq.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/67)
Source of MM parameters.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;2&nbsp;if&nbsp;reading&nbsp;geometry&nbsp;from&nbsp;checkpoint&nbsp;file,&nbsp;else&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;here,&nbsp;reading&nbsp;from&nbsp;input&nbsp;if&nbsp;requested&nbsp;by&nbsp;IOp(64).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Copy&nbsp;from&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pick&nbsp;up&nbsp;non-standard&nbsp;parameters&nbsp;from&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/70)
`L118`: Type of sampling (Nact).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Orthant&nbsp;sampling.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Classical&nbsp;microcanonical&nbsp;normal&nbsp;mode&nbsp;sampling.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fixed&nbsp;normal&nbsp;mode&nbsp;energy.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Local&nbsp;mode&nbsp;sampling&nbsp;(thermal&nbsp;sampling&nbsp;based&nbsp;on&nbsp;RTemp).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Currently&nbsp;0,&nbsp;2,&nbsp;3&nbsp;and&nbsp;4&nbsp;are&nbsp;working.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;Hessian&nbsp;from&nbsp;checkpoint&nbsp;for&nbsp;initial&nbsp;sampling.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L124`: SCRF flag.


* IJKLLMM&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;See&nbsp;comments&nbsp;in&nbsp;overlay&nbsp;3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;the&nbsp;1st&nbsp;iteration&nbsp;in&nbsp;gas-phase.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;the&nbsp;1st&nbsp;iteration&nbsp;in&nbsp;solution.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/71)
`L103`: How often to calculate analyic 2nd derivatives.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(every&nbsp;cycle&nbsp;if&nbsp;IOp(10)=4).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Every&nbsp;Nth&nbsp;geometry,&nbsp;starting&nbsp;with&nbsp;the&nbsp;initial&nbsp;one.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L115`: Whether to print out input files for each structure along an IRC.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L118`: Hessian update.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gradient&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gradient+Hessian,&nbsp;but&nbsp;never&nbsp;calculate&nbsp;full&nbsp;H&nbsp;(only&nbsp;updates).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Full&nbsp;Hessian&nbsp;at&nbsp;every&nbsp;step.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Try&nbsp;to&nbsp;do&nbsp;NN&nbsp;updates&nbsp;between&nbsp;full&nbsp;Hessians.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;updating&nbsp;(same&nbsp;as&nbsp;300).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SR1&nbsp;Hessian&nbsp;updating&nbsp;algorithm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PSB&nbsp;Hessian&nbsp;updating&nbsp;algorithm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bofill’s&nbsp;Hessian&nbsp;updating&nbsp;algorithm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 400&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sqrt(Bofill)&nbsp;Hessian&nbsp;updating&nbsp;algorithm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 500&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;update.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;1000).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reintegrated&nbsp;updated&nbsp;steps.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Suppress&nbsp;reintegration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L123`: Hessian calculation.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gradient&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Either&nbsp;only&nbsp;update&nbsp;or&nbsp;CalcAll&nbsp;as&nbsp;determined&nbsp;by&nbsp;IOp(10).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Recalculate&nbsp;analytic&nbsp;Hessian&nbsp;every&nbsp;N^th&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/72)
`L121`: Lagrangian constrain method for ADMP (ICType).


* Half*Gamma*Tr[(P*P-P)^2]&nbsp;+&nbsp;Lambda*[Tr(P)-Ne]&nbsp;+&nbsp;Eta*Tr(P*P-P)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;same&nbsp;as&nbsp;7&nbsp;if&nbsp;no&nbsp;mass-weighting&nbsp;(IOp(76)&nbsp;<&nbsp;0).&nbsp;Same&nbsp;as&nbsp;10&nbsp;if&nbsp;mass-weighting&nbsp;(IOp(76)&nbsp;>&nbsp;0).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Lambda&nbsp;and&nbsp;Eta&nbsp;only.&nbsp;(Gamma=0).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Lambda,&nbsp;Eta,&nbsp;Gamma.&nbsp;Gamma&nbsp;=&nbsp;.2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Lambda,&nbsp;Eta,&nbsp;Gamma.&nbsp;Gamma&nbsp;=&nbsp;1.&nbsp;Constraints&nbsp;for&nbsp;scalar&nbsp;mass&nbsp;case.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;exact&nbsp;constraint&nbsp;Sum(ij)[Vij*(P^2-P)ij].&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5-7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Iterative&nbsp;Scheme&nbsp;same&nbsp;as&nbsp;4.&nbsp;Different&nbsp;initial&nbsp;guesses.&nbsp;7&nbsp;is&nbsp;default&nbsp;for&nbsp;scalar&nbsp;mass&nbsp;case.&nbsp;Constraints&nbsp;for&nbsp;tensorial&nbsp;mass.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8-11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mass-weighting&nbsp;constraints.&nbsp;Documentation&nbsp;may&nbsp;be&nbsp;found&nbsp;in&nbsp;DVelV1.&nbsp;10&nbsp;is&nbsp;default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L124`: Solvent type for external iteration PCM. (ISolv).




### IOp(1/73)
`L123`: Whether to compute projected frequencies: 0/1/2 Default (No)/No/Yes.


`L118` and `L121`: Initial Kinetic energy of the Nuclei (EStrtC).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(.1&nbsp;Hartree).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N*micro-Hartree.&nbsp;&nbsp;&nbsp;&nbsp;
* N<0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.0&nbsp;Hartree&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/74)
Charge scaling for charge embedding in ONIOM. IJKLMN 6th through 1st nearest neighbors of current layer scaled by I*0.2, J*0.2, etc. 0 Þ 5³ IAtTyp=6 (no scaling); all layers are scaled by at least as much as ones farther out. The default is 500.


* M&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Factor&nbsp;for&nbsp;charges&nbsp;one&nbsp;bond&nbsp;away&nbsp;from&nbsp;link&nbsp;atom.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* K00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Factor&nbsp;for&nbsp;charges&nbsp;three&nbsp;bonds&nbsp;away&nbsp;from&nbsp;link&nbsp;atom.&nbsp;IJ&nbsp;etc.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;actual&nbsp;factors&nbsp;used&nbsp;for&nbsp;each&nbsp;value&nbsp;of&nbsp;IAtTyp&nbsp;are:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + 1:&nbsp;0.0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2:&nbsp;0.2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + 3:&nbsp;0.4 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4:&nbsp;0.6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + 5:&nbsp;0.8 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 6:&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/75)
ADMP control flag (ICntrl).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard&nbsp;ADMP.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;converged&nbsp;density&nbsp;at&nbsp;every&nbsp;step.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fix&nbsp;the&nbsp;nuclear&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Test&nbsp;time&nbsp;reversibility&nbsp;(MaxStp&nbsp;must&nbsp;be&nbsp;even).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(20).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;stopping&nbsp;parameters&nbsp;from&nbsp;input.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;read&nbsp;stopping&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/76)
Fictitious electron mass (EMass). Format of input: +/- XXXXZYYYY.


* YYYY&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1000)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IOp(1/76)&nbsp;>&nbsp;0  YYYY*.0001&nbsp;amu.&nbsp;MW&nbsp;core&nbsp;functions&nbsp;more&nbsp;than&nbsp;valence&nbsp;functions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IOp(1/76)&nbsp;<&nbsp;0  YYYY*.0001&nbsp;amu.&nbsp;Use&nbsp;uniform&nbsp;scaling&nbsp;for&nbsp;all&nbsp;basis&nbsp;functions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Note&nbsp;YYYY&nbsp;>&nbsp;9999&nbsp;makes&nbsp;no&nbsp;sense).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Z&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mass-weighting&nbsp;option.&nbsp;If&nbsp;IOp(76)&nbsp;<&nbsp;0,&nbsp;Z&nbsp;is&nbsp;meaningless.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* XXXX&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If&nbsp;PBC:&nbsp;Mass&nbsp;of&nbsp;Box&nbsp;Coordinates&nbsp;(BoxMas)&nbsp;=&nbsp;XXXX*.0001&nbsp;AMU&nbsp;BoxMas=0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Box&nbsp;coordinates&nbsp;not&nbsp;propagated&nbsp;(default).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/77)
Initial Kinetic energy of the density matrix (EStrtP) (For UHF, Alpha and Beta each get half this energy) and Option Number to compute initial kinetic energy. Format of Input: XXYYYY (six digits).


IWType = XX
N = YYYY


(For UHF, Alpha and Beta each get half this energy).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(0.0&nbsp;Hartree).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N*micro-Hartree&nbsp;IWType&nbsp;is&nbsp;used&nbsp;to&nbsp;figure&nbsp;out&nbsp;how&nbsp;the&nbsp;initial&nbsp;velocity&nbsp;is&nbsp;computed&nbsp;(in&nbsp;gnvelp).
If&nbsp;XXYYYY&nbsp;<&nbsp;0:&nbsp;Initial&nbsp;velocity&nbsp;=&nbsp;0.0&nbsp;Hartree&nbsp;(i.e.,&nbsp;currently&nbsp;same&nbsp;as&nbsp;N=0&nbsp;above).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/78)
`L121`: Sparse.


* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sparse&nbsp;here&nbsp;with&nbsp;cutoff&nbsp;10^-N,&nbsp;full&nbsp;elsewhere.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;full&nbsp;matrices&nbsp;or&nbsp;sparse&nbsp;based&nbsp;on&nbsp;standard&nbsp;settings.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;sparse&nbsp;fixed&nbsp;form.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/79)
`L115`:  IRCMax convergence.


`L118, L121`: Stopping Criteria.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;do&nbsp;not&nbsp;analyze&nbsp;pure&nbsp;rotation&nbsp;and&nbsp;vibration&nbsp;for&nbsp;polyatomic&nbsp;molecules.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;pure&nbsp;rotational&nbsp;and&nbsp;harmonic&nbsp;normal&nbsp;mode&nbsp;analysis&nbsp;for&nbsp;polyatomic&nbsp;molecule;&nbsp;EBK&nbsp;theory&nbsp;for&nbsp;diatomic&nbsp;vibrational&nbsp;analysis&nbsp;(require&nbsp;equilibrium&nbsp;information&nbsp;for&nbsp;each&nbsp;of&nbsp;the&nbsp;polyatomic&nbsp;molecules&nbsp;from&nbsp;saved&nbsp;checkpoint&nbsp;files&nbsp;and&nbsp;Morse&nbsp;parameters&nbsp;for&nbsp;diatomic&nbsp;molecule).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;pure&nbsp;rotational&nbsp;and&nbsp;harmonic&nbsp;normal&nbsp;mode&nbsp;analysis&nbsp;for&nbsp;polyatomic&nbsp;molecule;&nbsp;local&nbsp;harmonic&nbsp;vibrational&nbsp;analysis&nbsp;for&nbsp;diatomic&nbsp;molecule&nbsp;(require&nbsp;equilibrium&nbsp;information&nbsp;for&nbsp;each&nbsp;of&nbsp;the&nbsp;fragments&nbsp;from&nbsp;saved&nbsp;checkpoint&nbsp;files).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;pure&nbsp;rotational&nbsp;analysis&nbsp;and&nbsp;select&nbsp;the&nbsp;best&nbsp;normal&nbsp;mode&nbsp;analysis&nbsp;methods&nbsp;(harmonic&nbsp;and&nbsp;anharmonic)&nbsp;for&nbsp;polyatomic&nbsp;molecule;&nbsp;local&nbsp;harmonic&nbsp;vibrational&nbsp;analysis&nbsp;for&nbsp;diatomic&nbsp;molecule&nbsp;(require&nbsp;equilibrium&nbsp;information&nbsp;for&nbsp;each&nbsp;of&nbsp;the&nbsp;fragments&nbsp;from&nbsp;saved&nbsp;checkpoint&nbsp;files).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;use&nbsp;default&nbsp;stopping&nbsp;criteria.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;user&nbsp;specified&nbsp;stopping&nbsp;criteria.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/80)
`L106`: 0/1 Cartesian/Normal mode/ Internal coordinate differentiation. 2 is NYI.


`L118`: = 1 to suppress the 5th order correction after surface hop has been made in Trajectory Surface Hopping calculations. Needs also IOp(10/80 = 1)


`L121`: Nuclear Kinetic Energy Thermostat Option (currently only velocity scaling is implemented).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;Thermostat.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 11XXXXX&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Velocity&nbsp;scaling,&nbsp;but&nbsp;only&nbsp;for&nbsp;the&nbsp;first&nbsp;XXXXX&nbsp;simulation&nbsp;steps.&nbsp;(This&nbsp;option&nbsp;is&nbsp;useful,&nbsp;if&nbsp;thermostating&nbsp;is&nbsp;only&nbsp;required&nbsp;during&nbsp;equilibration.)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Velocity&nbsp;scaling,&nbsp;all&nbsp;the&nbsp;way&nbsp;through&nbsp;the&nbsp;simulation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/81)
Nuclear KE thermostat in ADMP — temperature is checked and scaled every IOp(81) steps.




### IOp(1/82)
`L121`: Temperature for nuclear KE thermostat.




### IOp(1/83)
Whether to read in frequencies for electric and magnetic perturbations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes&nbsp;unless&nbsp;geom=allcheck.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;even&nbsp;if&nbsp;geom=allcheck.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ensure&nbsp;that&nbsp;the&nbsp;static&nbsp;case&nbsp;is&nbsp;done,&nbsp;by&nbsp;putting&nbsp;a&nbsp;zero&nbsp;frequency&nbsp;at&nbsp;the&nbsp;beginning.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;put&nbsp;a&nbsp;zero&nbsp;frequency&nbsp;at&nbsp;the&nbsp;beginning.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(100).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sort&nbsp;the&nbsp;frequencies&nbsp;into&nbsp;increasing&nbsp;order.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;sort&nbsp;the&nbsp;frequencies&nbsp;(for&nbsp;debugging).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/84)
Differentiation of frequency-dependent properties.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mask&nbsp;for&nbsp;which&nbsp;properties&nbsp;on&nbsp;file&nbsp;721&nbsp;will&nbsp;be&nbsp;differentiated.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/85)
Band gap calculation in PBC ADMP.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Diagonalize&nbsp;Fock&nbsp;matrix&nbsp;to&nbsp;get&nbsp;band&nbsp;gap,&nbsp;evolution,&nbsp;etc.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/86)
Printing for NMR for ONIOM.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;tensors&nbsp;and&nbsp;eigenvalues.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;eigenvectors&nbsp;as&nbsp;well.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(1/87)
ONIOM integration of density.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;integrate.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Integrate&nbsp;current&nbsp;densities.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Integrate&nbsp;densities&nbsp;specified&nbsp;by&nbsp;following&nbsp;digits:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* K0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Density&nbsp;to&nbsp;use&nbsp;from&nbsp;gridpoint&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* L00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Density&nbsp;to&nbsp;use&nbsp;from&nbsp;gridpoint&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* M000&nbsp;etc.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Values&nbsp;for&nbsp;K,&nbsp;L,&nbsp;M,&nbsp;etc.:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0:&nbsp;SCF&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1:&nbsp;MP&nbsp;first&nbsp;order&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2:&nbsp;MP2&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3:&nbsp;MP3&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4:&nbsp;MP4&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5:&nbsp;CI&nbsp;one-particle&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6:&nbsp;CI&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7:&nbsp;QCI/CC&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8:&nbsp;Correct&nbsp;to&nbsp;second&nbsp;order&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/88)
Whether to read in atomic masses (isotopes).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1&nbsp;if&nbsp;geometry&nbsp;read&nbsp;from&nbsp;input,&nbsp;4&nbsp;if&nbsp;geometry&nbsp;read&nbsp;from&nbsp;checkpoint)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;most&nbsp;abundant&nbsp;isotopes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;isotopes&nbsp;from&nbsp;input.&nbsp;The&nbsp;temperature&nbsp;and&nbsp;pressure&nbsp;are&nbsp;read&nbsp;first,&nbsp;for&nbsp;backwards&nbsp;compatibility.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;isotopes&nbsp;from&nbsp;RWF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;isotopes&nbsp;from&nbsp;checkpoint.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Generated&nbsp;internally)&nbsp;Isotopes&nbsp;were&nbsp;read&nbsp;from&nbsp;chk&nbsp;file&nbsp;during&nbsp;Guess=Input.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




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


* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(112)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Retrieve&nbsp;from&nbsp;checkpoint&nbsp;file&nbsp;if&nbsp;available,&nbsp;otherwise&nbsp;diagonalize&nbsp;QM&nbsp;Hessian&nbsp;or&nbsp;read&nbsp;from&nbsp;input.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;try&nbsp;to&nbsp;retrieve&nbsp;from&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Diagonalize&nbsp;QM&nbsp;contribution&nbsp;to&nbsp;Hessian.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;from&nbsp;input.&nbsp;&nbsp;&nbsp;&nbsp;
* N00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How&nbsp;to&nbsp;deal&nbsp;with&nbsp;‘suspicious&nbsp;RFO&nbsp;solutions’&nbsp;(default&nbsp;is&nbsp;1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.&nbsp;Just&nbsp;take&nbsp;the&nbsp;step.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.&nbsp;Check&nbsp;if&nbsp;there&nbsp;is&nbsp;an&nbsp;eigenvector&nbsp;with&nbsp;wrong&nbsp;curvature.&nbsp;If&nbsp;there&nbsp;is,&nbsp;flip&nbsp;its&nbsp;eigenvalue.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.&nbsp;Check&nbsp;if&nbsp;there&nbsp;is&nbsp;an&nbsp;eigenvector&nbsp;with&nbsp;wrong&nbsp;curvature.&nbsp;If&nbsp;there&nbsp;is,&nbsp;take&nbsp;a&nbsp;small&nbsp;step&nbsp;into&nbsp;this&nbsp;direction,&nbsp;followed&nbsp;by&nbsp;a&nbsp;linear&nbsp;search.&nbsp;This&nbsp;should&nbsp;step&nbsp;out&nbsp;(or&nbsp;stay&nbsp;in)&nbsp;the&nbsp;wrong&nbsp;region,&nbsp;and&nbsp;fix&nbsp;the&nbsp;eigenvalue.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/94)
Davidson control for quadratic micro-iterations.


* OP&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number&nbsp;of&nbsp;initial&nbsp;guess&nbsp;vectors&nbsp;(4).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MN00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Iteration&nbsp;to&nbsp;scale&nbsp;down&nbsp;number&nbsp;of&nbsp;vectors&nbsp;(5).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* KL0000&nbsp;&nbsp;&nbsp;&nbsp;Factor&nbsp;to&nbsp;scale&nbsp;down&nbsp;with;&nbsp;1&nbsp;for&nbsp;no&nbsp;scaling&nbsp;(2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* J000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Whether&nbsp;to&nbsp;do&nbsp;geometry&nbsp;steps&nbsp;when&nbsp;the&nbsp;CG&nbsp;is&nbsp;done&nbsp;(2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Make&nbsp;the&nbsp;CG&nbsp;steps.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;displacements.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Only&nbsp;do&nbsp;displacements&nbsp;at&nbsp;first&nbsp;guess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* I0000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Whether&nbsp;to&nbsp;re-use&nbsp;previous&nbsp;RFO&nbsp;solution&nbsp;or&nbsp;to&nbsp;regenerate&nbsp;guess&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;After&nbsp;first&nbsp;step,&nbsp;use&nbsp;previous&nbsp;solution&nbsp;as&nbsp;guess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Regenerate&nbsp;guess&nbsp;each&nbsp;time.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;previous&nbsp;lowest&nbsp;root,&nbsp;and&nbsp;regenerate&nbsp;remainder.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* H00000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Whether&nbsp;(1,&nbsp;default)&nbsp;or&nbsp;not&nbsp;(2)&nbsp;to&nbsp;add&nbsp;0,…,0,1&nbsp;guess&nbsp;vector.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(1/95)
RFO/Davidson control for quadratic micro-iterations.


* MM&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Convergence&nbsp;(7).&nbsp;&nbsp;&nbsp;&nbsp;
* LLL00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<0:&nbsp;Regular&nbsp;Davidson.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0:&nbsp;Only&nbsp;check&nbsp;convergence&nbsp;on&nbsp;first&nbsp;vector,&nbsp;and&nbsp;iterate&nbsp;the&nbsp;lowest&nbsp;root&nbsp;only.&nbsp;Use&nbsp;all&nbsp;the&nbsp;intermediate&nbsp;vectors.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;>0:&nbsp;Only&nbsp;check&nbsp;convergence&nbsp;on&nbsp;first&nbsp;vector,&nbsp;and&nbsp;iterate&nbsp;the&nbsp;new&nbsp;vectors&nbsp;LLL&nbsp;times&nbsp;with&nbsp;the&nbsp;explicit&nbsp;last&nbsp;row/column.&nbsp;This&nbsp;is&nbsp;specifically&nbsp;appropriate&nbsp;for&nbsp;RFO.&nbsp;The&nbsp;last&nbsp;row/column&nbsp;of&nbsp;the&nbsp;Hessian&nbsp;comes&nbsp;after&nbsp;the&nbsp;diagonal&nbsp;elements.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/96)
Options for generating initial guess vectors for RFO/Davidson diagonalization in coupled QM/MM macro steps. Note that other RFO/Davidson diagonalization controls for coupled QM/MM macro steps are available in IOp(97). Format of input: GHIJKLLMM.


* MM&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number&nbsp;of&nbsp;initial&nbsp;guess&nbsp;vectors&nbsp;to&nbsp;get&nbsp;from&nbsp;CG&nbsp;steps.&nbsp;The&nbsp;default&nbsp;is&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* LL&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number&nbsp;of&nbsp;initial&nbsp;guess&nbsp;vectors&nbsp;from&nbsp;the&nbsp;diagonal&nbsp;of&nbsp;the&nbsp;QM&nbsp;block&nbsp;(4).&nbsp;The&nbsp;default&nbsp;is&nbsp;4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* K&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add&nbsp;0,…,0,1&nbsp;guess&nbsp;vector?&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;K&nbsp;=&nbsp;1;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* J&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add&nbsp;the&nbsp;gradient&nbsp;vector&nbsp;to&nbsp;the&nbsp;guesses?&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;J&nbsp;=&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* I&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pre-diagonalize&nbsp;a&nbsp;Hessian/RFO&nbsp;matrix&nbsp;without&nbsp;non-bonding&nbsp;contributions?&nbsp;Note&nbsp;that&nbsp;this&nbsp;control&nbsp;is&nbsp;only&nbsp;valid&nbsp;for&nbsp;IOp(98)&nbsp;>&nbsp;3;&nbsp;otherwise,&nbsp;I&nbsp;is&nbsp;ignored.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;I&nbsp;=&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* H&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scale&nbsp;factor&nbsp;for&nbsp;the&nbsp;size&nbsp;of&nbsp;the&nbsp;Davidson&nbsp;sub-space&nbsp;in&nbsp;early&nbsp;iterations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;H&nbsp;=&nbsp;4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;no&nbsp;scaling.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + H&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;a&nbsp;sub-space&nbsp;in&nbsp;early&nbsp;iterations&nbsp;that&nbsp;is&nbsp;H&nbsp;times&nbsp;the&nbsp;number&nbsp;of&nbsp;requested&nbsp;vectors.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* G&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number&nbsp;of&nbsp;vectors&nbsp;to&nbsp;solve&nbsp;using&nbsp;Davidson&nbsp;diagonization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;G&nbsp;=&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    + G&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Solve&nbsp;for&nbsp;G&nbsp;vectors.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/97)
RFO/Davidson control for coupled QM/MM macro step. Note that other RFO/Davidson diagonalization conrols for coupled QM/MM macro steps are available in IOp(96). Format of input: GHIJKLMM.


* MM&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Convergence&nbsp;in&nbsp;Davidson&nbsp;iterations.&nbsp;Convergence&nbsp;is&nbsp;set&nbsp;to&nbsp;10^-MM.&nbsp;The&nbsp;default&nbsp;value&nbsp;is&nbsp;MM=5.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* L&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What&nbsp;is&nbsp;being&nbsp;diagonalized?&nbsp;This&nbsp;option&nbsp;is&nbsp;set&nbsp;explicitly&nbsp;in&nbsp;subroutines&nbsp;before&nbsp;calling&nbsp;the&nbsp;Davidson&nbsp;diagonalization&nbsp;code.&nbsp;Therefore,&nbsp;the&nbsp;value&nbsp;set&nbsp;in&nbsp;this&nbsp;IOp&nbsp;is&nbsp;ignored&nbsp;and&nbsp;serves&nbsp;only&nbsp;as&nbsp;a&nbsp;place&nbsp;holder.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the&nbsp;Hessian&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the&nbsp;augmented-Hessian/RFO&nbsp;matrix&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* K&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check&nbsp;convergence&nbsp;on&nbsp;which&nbsp;roots?&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;For&nbsp;L=0,&nbsp;K=2;&nbsp;For&nbsp;L=1,&nbsp;K=1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check&nbsp;convergence&nbsp;on&nbsp;lowest&nbsp;root&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check&nbsp;convergence&nbsp;on&nbsp;all&nbsp;roots.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* J&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Appears&nbsp;to&nbsp;be&nbsp;unused.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* I&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number&nbsp;of&nbsp;Davidson&nbsp;iterations&nbsp;to&nbsp;store.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;Keep&nbsp;all&nbsp;iterations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Keep&nbsp;only&nbsp;the&nbsp;last&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* H&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number&nbsp;of&nbsp;new&nbsp;vectors&nbsp;to&nbsp;create&nbsp;in&nbsp;each&nbsp;Davidson&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;For&nbsp;L=0,&nbsp;H=1;&nbsp;For&nbsp;L=1,&nbsp;H=2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Iterate&nbsp;all&nbsp;roots/vectors.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Iterate&nbsp;lowest&nbsp;root/vector&nbsp;only&nbsp;up&nbsp;to&nbsp;the&nbsp;maximum&nbsp;number&nbsp;of&nbsp;iterations&nbsp;that&nbsp;are&nbsp;default&nbsp;in&nbsp;the&nbsp;Davidson&nbsp;code&nbsp;(ignores&nbsp;J&nbsp;above)&nbsp;and&nbsp;keeping&nbsp;vectors&nbsp;from&nbsp;all&nbsp;iteratations&nbsp;(ignores&nbsp;I&nbsp;above).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Iterate&nbsp;lowest&nbsp;root/vector&nbsp;only.&nbsp;Note&nbsp;that&nbsp;this&nbsp;option&nbsp;is&nbsp;essentially&nbsp;the&nbsp;same&nbsp;as&nbsp;H=2,&nbsp;though&nbsp;J&nbsp;and&nbsp;I&nbsp;option&nbsp;settings&nbsp;are&nbsp;honored.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* G&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initial&nbsp;approximation&nbsp;to&nbsp;use&nbsp;for&nbsp;Davidson&nbsp;diagonization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;G=2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;a&nbsp;diagonal&nbsp;Hessian&nbsp;approximation&nbsp;together&nbsp;with&nbsp;the&nbsp;gradient&nbsp;vector.&nbsp;This&nbsp;is&nbsp;best&nbsp;used&nbsp;in&nbsp;RFO&nbsp;applications&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;inverted&nbsp;Hessian&nbsp;for&nbsp;the&nbsp;QM&nbsp;block&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;a&nbsp;diagonal&nbsp;Hessian&nbsp;approximation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/98)
Control of quadratic micro-iterations and coupled QM/MM quadratic macro step.


* <0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;use&nbsp;dynamic&nbsp;convergence&nbsp;criteria&nbsp;for&nbsp;the&nbsp;micro-iterations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(11).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Regular&nbsp;non-coupled&nbsp;macro&nbsp;step.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Coupled&nbsp;macro&nbsp;step,&nbsp;full&nbsp;diagonalization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Coupled&nbsp;macro&nbsp;step,&nbsp;direct&nbsp;/w&nbsp;full&nbsp;Hessian&nbsp;in&nbsp;core.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Coupled&nbsp;macro&nbsp;step,&nbsp;direct&nbsp;/w&nbsp;MM&nbsp;Hessian&nbsp;in&nbsp;core.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Coupled&nbsp;macro&nbsp;step,&nbsp;fully&nbsp;direct.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Go&nbsp;through&nbsp;the&nbsp;QuadMac&nbsp;machinery,&nbsp;but&nbsp;use&nbsp;the&nbsp;fully&nbsp;integrated&nbsp;ONIOM&nbsp;Hessian&nbsp;to&nbsp;calculate&nbsp;the&nbsp;Hessian-vector&nbsp;products.&nbsp;Switch&nbsp;to&nbsp;regular&nbsp;micro-iterations&nbsp;at&nbsp;points&nbsp;without&nbsp;analytic&nbsp;second&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fully&nbsp;quadratic&nbsp;at&nbsp;2nd&nbsp;derivative&nbsp;points&nbsp;(1st&nbsp;in&nbsp;CalcFC,&nbsp;all&nbsp;in&nbsp;CalcAll),&nbsp;QuadMac&nbsp;with&nbsp;integrated&nbsp;Hessian&nbsp;at&nbsp;non-2nd&nbsp;derivative&nbsp;points.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Regular&nbsp;micro-iterations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Quadratic&nbsp;micro-iterations,&nbsp;full&nbsp;diagonalization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Quadratic&nbsp;micro-iterations,&nbsp;direct&nbsp;with&nbsp;prepared&nbsp;Hessian&nbsp;in&nbsp;core.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Quadratic&nbsp;micro-iterations,&nbsp;direct&nbsp;with&nbsp;raw&nbsp;MM&nbsp;Hessian&nbsp;in&nbsp;core.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 50&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Quadratic&nbsp;micro-iterations,&nbsp;fully&nbsp;direct.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 60&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;micro-iterations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/99)
Accuracy used for the non-bonded interactions in the Hessian-vector product calculations in the fully direct algorithms. Setting this IOp does not affect the MM energy and gradient calculations; only the direct evaluation in the QuadMac optimization step. When IOp(99) < 0, the full accuracy is used.


* MM&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum&nbsp;multipole&nbsp;level&nbsp;(8)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* LLL00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Box&nbsp;size&nbsp;in&nbsp;FMM&nbsp;(12)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* KKK00000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Cutoff&nbsp;in&nbsp;van&nbsp;der&nbsp;Waals&nbsp;(30)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/101-104)
`L115, L118`: Phase control in N1, N2, N3, N4.




### IOp(1/105)
Reaction direction.


* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Same&nbsp;as&nbsp;10).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Forward&nbsp;direction.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reverse&nbsp;direction&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Same&nbsp;as&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;DVV.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;use&nbsp;DVV.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Same&nbsp;as&nbsp;10).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Follow&nbsp;the&nbsp;rxn&nbsp;path&nbsp;in&nbsp;the&nbsp;forward&nbsp;direction&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Follow&nbsp;the&nbsp;rxn&nbsp;path&nbsp;in&nbsp;the&nbsp;reverse&nbsp;direction.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Same&nbsp;as&nbsp;200).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Time&nbsp;step&nbsp;correction&nbsp;not&nbsp;used.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Time&nbsp;step&nbsp;correction&nbsp;used&nbsp;but&nbsp;not&nbsp;to&nbsp;recalculate&nbsp;current&nbsp;DVV&nbsp;step.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Time&nbsp;step&nbsp;correction&nbsp;used&nbsp;and&nbsp;current&nbsp;DVV&nbsp;step&nbsp;recalculated.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Same&nbsp;as&nbsp;1000).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;DVV&nbsp;stopping&nbsp;criteria.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;NOT&nbsp;use&nbsp;DVV&nbsp;stopping&nbsp;criteria&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/106)
Damping constant for DVV Dynamic Reaction Path following (v0).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;v0&nbsp;=&nbsp;0.04&nbsp;(N=400).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;v0&nbsp;is&nbsp;set&nbsp;to&nbsp;N*0.0001.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/107)
Error tolerance for DVV time step correction (Error).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;Error&nbsp;=&nbsp;0.003&nbsp;(N=30).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Error&nbsp;=&nbsp;N*0.0001.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/108)
Gradient magnitude for DVV stopping criteria (Crit1).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(N&nbsp;=&nbsp;15).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* <0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;this&nbsp;test.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N*0.0001&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/109)
Force-velocity angle for DVV stopping criteria (Crit2).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(90&nbsp;Degrees).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* <0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;this&nbsp;test.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;N&nbsp;Degrees.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/110)
Scaling of rigid fragment steps during microiterations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;scale.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scale&nbsp;with&nbsp;1/NRA&nbsp;(NRA&nbsp;=&nbsp;number&nbsp;of&nbsp;atoms&nbsp;in&nbsp;fragment).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scale&nbsp;with&nbsp;1/Sqrt(NRA).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scale&nbsp;with&nbsp;1/n.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/111)
`L103`: Step-size to use with steepest descent when L103 is having trouble.


* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scale&nbsp;up&nbsp;to&nbsp;RMS&nbsp;step&nbsp;of&nbsp;N/1000&nbsp;if&nbsp;DXRMS&nbsp;is&nbsp;less.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Effectively&nbsp;disables&nbsp;the&nbsp;scaling.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(50).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scale&nbsp;up&nbsp;or&nbsp;down&nbsp;to&nbsp;maximum&nbsp;change&nbsp;in&nbsp;a&nbsp;variable&nbsp;of&nbsp;N/1000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/112)
`L101`: Temperature for thermochemistry.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(standard&nbsp;temperature,&nbsp;unless&nbsp;read&nbsp;in).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/1000&nbsp;degrees.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N<1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/1000000&nbsp;degrees.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/1000000&nbsp;degrees.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/113)
Pressure for thermochemistry.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1&nbsp;atmosphere,&nbsp;unless&nbsp;read&nbsp;in).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/1000&nbsp;atmospheres.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N<1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/1000000&nbsp;atmospheres.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/114)
Scale factor for harmonic frequencies for use in thermochemistry and harmonic vibration-rotation analysis.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1&nbsp;unless&nbsp;specified&nbsp;by&nbsp;IOp&nbsp;in&nbsp;overlay&nbsp;7&nbsp;or&nbsp;read&nbsp;in).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;to&nbsp;0&nbsp;(default).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/1000000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/115)
Compression for MOMM quadratic steps.


* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Second&nbsp;derivatives&nbsp;generated&nbsp;over&nbsp;active&nbsp;atoms,&nbsp;with&nbsp;real&nbsp;system&nbsp;terms&nbsp;done&nbsp;iteratively&nbsp;during&nbsp;micro-iterations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N¹4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Full&nbsp;second&nbsp;derivative&nbsp;matrices&nbsp;are&nbsp;used.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/116)
Options for ONIOM Conical intersections: which calculations have adiabatic couplings done.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(111&nbsp;all&nbsp;component&nbsp;calculations).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/118)
Dump structures for each ONIOM system formatted as input.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(1/119)
Control Initial Lanczos Vector (ILzVec).


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;guess&nbsp;by&nbsp;card&nbsp;in&nbsp;input&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;largest&nbsp;elements&nbsp;of&nbsp;H&nbsp;as&nbsp;a&nbsp;guess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;five&nbsp;largest&nbsp;contributions&nbsp;of&nbsp;H&nbsp;as&nbsp;a&nbsp;guess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For&nbsp;Opt,&nbsp;IRC,&nbsp;dynamics&nbsp;read&nbsp;guess&nbsp;from&nbsp;previous&nbsp;cycle.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For&nbsp;Opt,&nbsp;IRC,&nbsp;dynamics&nbsp;generate&nbsp;a&nbsp;fresh&nbsp;guess&nbsp;for&nbsp;each&nbsp;cycle&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/120)
Flags for QM:QM embedding. NOTE: The standard embedding flags must also be set in the same way as necessary for QM:MM embedding calculations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;–&nbsp;Same&nbsp;as&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Mulliken&nbsp;charges.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;nuclear&nbsp;charge&nbsp;stored&nbsp;in&nbsp;array&nbsp;AtmChg.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;the&nbsp;charges&nbsp;to&nbsp;zero.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Same&nbsp;as&nbsp;20).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Just&nbsp;use&nbsp;the&nbsp;charges&nbsp;that&nbsp;already&nbsp;reside&nbsp;in&nbsp;AtChMM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update&nbsp;AtChMM&nbsp;using&nbsp;current&nbsp;atomic&nbsp;charges&nbsp;on&nbsp;the&nbsp;RWF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


This option is only employed immediately following low-level real-system sub-calculations.




### IOp(1/121)
`L106`: Extra items to differentiate.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;none.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Differentiate&nbsp;AO&nbsp;density&nbsp;and&nbsp;Fock&nbsp;matrices.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NYI.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/122)
Read secondary structure information.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(4&nbsp;or&nbsp;3&nbsp;if&nbsp;reading&nbsp;geometry&nbsp;from&nbsp;checkpoint&nbsp;or&nbsp;RWF&nbsp;file,&nbsp;otherwise&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;read&nbsp;from&nbsp;input&nbsp;stream&nbsp;if&nbsp;any&nbsp;residue&nbsp;information&nbsp;was&nbsp;provided&nbsp;on&nbsp;the&nbsp;atom&nbsp;definition&nbsp;lines.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;read&nbsp;from&nbsp;RWF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;read&nbsp;from&nbsp;checkpoint.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(1/123)
Version of /Mol/ to save on disk.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(current,&nbsp;version&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Version&nbsp;1&nbsp;(flag&nbsp;-12345).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Version&nbsp;2&nbsp;(flag&nbsp;-12346).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N<0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Flag&nbsp;value&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/124)
Flavor of ONIOM-PCM to use.


* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“A,”&nbsp;reaction&nbsp;field&nbsp;from&nbsp;the&nbsp;ONIOM&nbsp;integrated&nbsp;density;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“B,”&nbsp;reaction&nbsp;field&nbsp;from&nbsp;the&nbsp;real&nbsp;system&nbsp;low&nbsp;level;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“C,”&nbsp;reaction&nbsp;field&nbsp;in&nbsp;the&nbsp;real&nbsp;system&nbsp;low&nbsp;level&nbsp;only;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;“X,”&nbsp;reaction&nbsp;field&nbsp;in&nbsp;all&nbsp;subcalculations&nbsp;using&nbsp;the&nbsp;real&nbsp;system&nbsp;cavity.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;1&nbsp;unless&nbsp;a&nbsp;semiempirical&nbsp;method&nbsp;is&nbsp;involved);&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Integrate&nbsp;the&nbsp;density&nbsp;for&nbsp;ONIOM-PCM-A;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Integrate&nbsp;the&nbsp;potential&nbsp;for&nbsp;ONIOM-PCM-A;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Flag&nbsp;to&nbsp;indicate&nbsp;ONIOM-PCM-X&nbsp;as&nbsp;first&nbsp;iteration&nbsp;of&nbsp;ONIOM-PCM-A.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/125)
Solvent charge distribution to add to Hamiltonian.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;charges&nbsp;and&nbsp;DBFs&nbsp;from&nbsp;input&nbsp;stream&nbsp;in&nbsp;input&nbsp;orientation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;from&nbsp;RWF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;from&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;charges&nbsp;and&nbsp;DBFs&nbsp;from&nbsp;input&nbsp;stream&nbsp;in&nbsp;standard&nbsp;orientation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;units&nbsp;of&nbsp;Angstroms&nbsp;for&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;units&nbsp;of&nbsp;Bohr&nbsp;for&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/126)
Whether to read an input section with atom opt/freeze information.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/127)
Use of MM coordinates and forces in GEDIIS:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(-3&nbsp;for&nbsp;ME,&nbsp;-3&nbsp;for&nbsp;EE).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;pass&nbsp;MM&nbsp;info.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Zero&nbsp;MM&nbsp;forces&nbsp;and&nbsp;MM&nbsp;part&nbsp;of&nbsp;step,&nbsp;equivalent&nbsp;to&nbsp;not&nbsp;passing&nbsp;MM&nbsp;info.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Zero&nbsp;MM&nbsp;forces&nbsp;but&nbsp;interpolate&nbsp;step&nbsp;in&nbsp;MM&nbsp;coords.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;MM&nbsp;forces&nbsp;scaled&nbsp;by&nbsp;1/N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/128)
Initial micro-iterations in L120 before first QM step, and micro-iterations in L120 during numerical differentiation in L103.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/129)
`L123`: Whether or not the final statistics printed in the job summary should include coordinate values at each IRC step.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(none).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;user-defined&nbsp;stats&nbsp;from&nbsp;the&nbsp;input&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(do&nbsp;not&nbsp;report&nbsp;all&nbsp;Cartesian&nbsp;coordinates).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Report&nbsp;all&nbsp;Cartesian&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Unused.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(do&nbsp;not&nbsp;report&nbsp;bond&nbsp;coordinates).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If&nbsp;redundant&nbsp;internals&nbsp;are&nbsp;on&nbsp;the&nbsp;RWF,&nbsp;then&nbsp;report&nbsp;values&nbsp;for&nbsp;bond&nbsp;coordinates&nbsp;along&nbsp;the&nbsp;IRC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(do&nbsp;not&nbsp;report&nbsp;angle&nbsp;coordinates).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If&nbsp;redundant&nbsp;internals&nbsp;are&nbsp;on&nbsp;the&nbsp;RWF,&nbsp;then&nbsp;report&nbsp;values&nbsp;for&nbsp;angle&nbsp;coordinates&nbsp;along&nbsp;the&nbsp;IRC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xxxxx&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(do&nbsp;not&nbsp;report&nbsp;dihedral&nbsp;coordinates).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xxxxx&nbsp;&nbsp;&nbsp;&nbsp;If&nbsp;redundant&nbsp;internals&nbsp;are&nbsp;on&nbsp;the&nbsp;RWF,&nbsp;then&nbsp;report&nbsp;values&nbsp;for&nbsp;dihedral&nbsp;coordinates&nbsp;along&nbsp;the&nbsp;IRC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/130)
Eigenvector number to be followed during coordinate driving jobs (IOp(1/19 = 10)).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Follow&nbsp;input&nbsp;structure&nbsp;Hessian&nbsp;eigenvector&nbsp;number&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/131)
Options for corrector integration in predictor-corrector IRC calulcations (Link 123).


* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Should&nbsp;the&nbsp;corrector&nbsp;integration&nbsp;scheme&nbsp;be&nbsp;run&nbsp;in&nbsp;an&nbsp;(macro-cycle)&nbsp;iterative&nbsp;fashion?&nbsp;Default&nbsp;=&nbsp;2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -01&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;After&nbsp;each&nbsp;corrector&nbsp;integration,&nbsp;evaluate&nbsp;the&nbsp;actual&nbsp;energy&nbsp;and&nbsp;derivatives,&nbsp;but&nbsp;do&nbsp;not&nbsp;actually&nbsp;use
these.&nbsp;The&nbsp;final&nbsp;IRC&nbsp;will&nbsp;be&nbsp;the&nbsp;same&nbsp;as&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 01&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Never&nbsp;check&nbsp;convergence&nbsp;of&nbsp;the&nbsp;corrector&nbsp;integration.&nbsp;Always&nbsp;do&nbsp;one&nbsp;corrector&nbsp;integration&nbsp;for&nbsp;each&nbsp;predictor&nbsp;integration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 02&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Always&nbsp;check&nbsp;for&nbsp;convergence&nbsp;of&nbsp;the&nbsp;corrector&nbsp;integration&nbsp;end&nbsp;point.&nbsp;Convergence&nbsp;is&nbsp;acheived&nbsp;when&nbsp;the&nbsp;change&nbsp;in&nbsp;corrector&nbsp;integration&nbsp;end&nbsp;point&nbsp;geometry&nbsp;is&nbsp;less&nbsp;than&nbsp;the&nbsp;convergence&nbsp;criteria&nbsp;indicated&nbsp;by&nbsp;IOp(7).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 03&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;2,&nbsp;but&nbsp;never&nbsp;accept&nbsp;convergence&nbsp;after&nbsp;the&nbsp;first&nbsp;corrector&nbsp;integration&nbsp;at&nbsp;a&nbsp;point.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This&nbsp;flag&nbsp;iteratively&nbsp;refines&nbsp;the&nbsp;DWI&nbsp;fitted&nbsp;surface&nbsp;if&nbsp;multiple&nbsp;corrector&nbsp;integration&nbsp;macro-cycles&nbsp;are&nbsp;taken&nbsp;by&nbsp;adding&nbsp;the&nbsp;largest&nbsp;standard&nbsp;deviation&nbsp;point&nbsp;from&nbsp;the&nbsp;previous&nbsp;BS&nbsp;cycle.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This&nbsp;flag&nbsp;forces&nbsp;a&nbsp;PES&nbsp;evaluation&nbsp;step&nbsp;after&nbsp;each&nbsp;corrector&nbsp;integration.&nbsp;This&nbsp;is&nbsp;similar&nbsp;option&nbsp;-1,&nbsp;except&nbsp;that&nbsp;the&nbsp;actual&nbsp;energy&nbsp;and&nbsp;derivatives&nbsp;are&nbsp;used&nbsp;for&nbsp;the&nbsp;next&nbsp;predictor&nbsp;step&nbsp;rather&nbsp;than&nbsp;the&nbsp;values&nbsp;on&nbsp;the&nbsp;DWI&nbsp;fitted&nbsp;surface&nbsp;at&nbsp;the&nbsp;corrector&nbsp;end-point.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Should&nbsp;DWI&nbsp;surfaces&nbsp;employ&nbsp;numerical&nbsp;thrid-order&nbsp;terms&nbsp;in&nbsp;Taylor&nbsp;series?&nbsp;Default&nbsp;=&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;DWI&nbsp;surface&nbsp;with&nbsp;Taylor&nbsp;series&nbsp;expansions&nbsp;truncated&nbsp;at&nbsp;second-order.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;DWI&nbsp;surface&nbsp;with&nbsp;Taylor&nbsp;series&nbsp;expansions&nbsp;truncated&nbsp;at&nbsp;third-order&nbsp;using&nbsp;numerical&nbsp;third-derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Nxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What&nbsp;power&nbsp;should&nbsp;be&nbsp;used&nbsp;for&nbsp;DWI&nbsp;weights&nbsp;that&nbsp;include&nbsp;delta-x&nbsp;raised&nbsp;to&nbsp;an&nbsp;even&nbsp;power.&nbsp;The&nbsp;value&nbsp;of&nbsp;this&nbsp;option&nbsp;setsthat&nbsp;power&nbsp;to&nbsp;2*N.&nbsp;Default&nbsp;=&nbsp;N&nbsp;=&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;How&nbsp;should&nbsp;the&nbsp;first&nbsp;step&nbsp;off&nbsp;of&nbsp;the&nbsp;transition&nbsp;structure&nbsp;point&nbsp;be&nbsp;handled&nbsp;in&nbsp;corrector&nbsp;integration&nbsp;cycles?&nbsp;Note,&nbsp;in&nbsp;all&nbsp;cases,&nbsp;the&nbsp;transition&nbsp;vector&nbsp;is&nbsp;used&nbsp;to&nbsp;define&nbsp;the&nbsp;tangent&nbsp;at&nbsp;the&nbsp;transition&nbsp;structure.&nbsp;Default&nbsp;=&nbsp;2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run&nbsp;the&nbsp;requested&nbsp;number&nbsp;of&nbsp;Euler&nbsp;steps&nbsp;in&nbsp;the&nbsp;standard&nbsp;way.&nbsp;Only&nbsp;the&nbsp;first&nbsp;Euler&nbsp;step&nbsp;taken&nbsp;uses&nbsp;the&nbsp;transition&nbsp;vector.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Take&nbsp;a&nbsp;large&nbsp;step&nbsp;off&nbsp;of&nbsp;the&nbsp;transition&nbsp;structure&nbsp;point&nbsp;along&nbsp;the&nbsp;transition&nbsp;vector.&nbsp;This&nbsp;step&nbsp;is&nbsp;taken&nbsp;to&nbsp;be&nbsp;half&nbsp;of&nbsp;the&nbsp;total&nbsp;requested&nbsp;step&nbsp;size&nbsp;given&nbsp;by&nbsp;TotStp.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3xxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This&nbsp;the&nbsp;same&nbsp;as&nbsp;option&nbsp;2&nbsp;in&nbsp;concept.&nbsp;The&nbsp;only&nbsp;difference&nbsp;is&nbsp;that&nbsp;the&nbsp;first&nbsp;step&nbsp;off&nbsp;of&nbsp;the&nbsp;transition&nbsp;structure&nbsp;is&nbsp;taken&nbsp;as&nbsp;one-third&nbsp;the&nbsp;total&nbsp;requested&nbsp;step&nbsp;size&nbsp;given&nbsp;by&nbsp;TotStp.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4xxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This&nbsp;the&nbsp;same&nbsp;as&nbsp;option&nbsp;2&nbsp;in&nbsp;concept.&nbsp;The&nbsp;only&nbsp;difference&nbsp;is&nbsp;that&nbsp;the&nbsp;first&nbsp;step&nbsp;off&nbsp;of&nbsp;the&nbsp;transition&nbsp;structure&nbsp;is&nbsp;taken&nbsp;as&nbsp;one-fourth&nbsp;the&nbsp;total&nbsp;requested&nbsp;step&nbsp;size&nbsp;given&nbsp;by&nbsp;TotStp.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xxxxx&nbsp;&nbsp;&nbsp;&nbsp;Should&nbsp;update&nbsp;vectors&nbsp;be&nbsp;used&nbsp;in&nbsp;DWI&nbsp;fits&nbsp;if&nbsp;possible?&nbsp;Default&nbsp;=&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xxxxx&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;when&nbsp;possible.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xxxxx&nbsp;&nbsp;&nbsp;&nbsp;Never.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/132)
Whether to check for divalent link atoms in ONIOM input:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(yes).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/133)
Suppress integration/restore of quantities for Polar=Raman and Polar=ROA ONIOM jobs:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;restore&nbsp;or&nbsp;integrate&nbsp;forces,&nbsp;force&nbsp;constants,&nbsp;static&nbsp;electric&nbsp;or&nbsp;magnetic&nbsp;field&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Restore&nbsp;all&nbsp;files.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




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


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;based&nbsp;on&nbsp;NAtoms&nbsp;but&nbsp;at&nbsp;least&nbsp;5000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/140)
Whether to restore the real system from chk file:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(yes&nbsp;if&nbsp;ONIOM).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/141)
Control of error choice during GEDIIS:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;RFO&nbsp;steps&nbsp;as&nbsp;error&nbsp;vectors,&nbsp;using&nbsp;the&nbsp;NR&nbsp;step&nbsp;at&nbsp;a&nbsp;point&nbsp;if&nbsp;the&nbsp;RFO&nbsp;fails&nbsp;or&nbsp;gives&nbsp;a&nbsp;Hessian&nbsp;eigenvector.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If&nbsp;RFO&nbsp;fails&nbsp;for&nbsp;any&nbsp;point,&nbsp;use&nbsp;the&nbsp;gradient&nbsp;for&nbsp;all&nbsp;points.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Always&nbsp;use&nbsp;the&nbsp;gradients&nbsp;as&nbsp;the&nbsp;errors.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;RFO&nbsp;steps&nbsp;as&nbsp;error&nbsp;vectors&nbsp;unless&nbsp;any&nbsp;RFO&nbsp;fails&nbsp;and&nbsp;unless&nbsp;Hessian&nbsp;is&nbsp;marked&nbsp;as&nbsp;untrustworthy;&nbsp;then&nbsp;use&nbsp;gradients&nbsp;instead.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Drop&nbsp;back&nbsp;to&nbsp;RFO&nbsp;(no&nbsp;DIIS)&nbsp;if&nbsp;Hessian&nbsp;is&nbsp;untrustworthy.&nbsp;NR&nbsp;steps&nbsp;are&nbsp;used&nbsp;if&nbsp;RFO&nbsp;fails&nbsp;during&nbsp;DIIS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(1/142)
Whether to copy MM charges to link atoms:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(3&nbsp;if&nbsp;QEq&nbsp;is&nbsp;done;&nbsp;otherwise&nbsp;1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Copy&nbsp;if&nbsp;link&nbsp;atom&nbsp;charge&nbsp;is&nbsp;zero.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;copy.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Always&nbsp;copy.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/143)
Hessian during IRC restarts.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;change&nbsp;in&nbsp;when&nbsp;Hessian&nbsp;is&nbsp;done.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;Hessian&nbsp;at&nbsp;first&nbsp;new&nbsp;point&nbsp;in&nbsp;each&nbsp;direction.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/144)
Whether to analyze residue geometry.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Yes,&nbsp;if&nbsp;secondary&nbsp;structure&nbsp;present&nbsp;and&nbsp;N&nbsp;Atoms&nbsp;≤&nbsp;10000).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/145)
Controls for the new internal coordinate data structure.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Should&nbsp;the&nbsp;new&nbsp;internal&nbsp;coordinate&nbsp;data&nbsp;structure&nbsp;be&nbsp;set-up&nbsp;for&nbsp;use?&nbsp;(Default&nbsp;=&nbsp;1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;The&nbsp;coordinates&nbsp;are&nbsp;either&nbsp;generated&nbsp;by&nbsp;default&nbsp;(e.g.,&nbsp;Option&nbsp;9×2)&nbsp;or&nbsp;obtained&nbsp;from&nbsp;the&nbsp;user-provided&nbsp;input&nbsp;(e.g.,&nbsp;Option&nbsp;6×2).&nbsp;Alternatively,&nbsp;they&nbsp;can&nbsp;be&nbsp;taken&nbsp;from&nbsp;a&nbsp;chk&nbsp;file&nbsp;if&nbsp;they&nbsp;exist&nbsp;there&nbsp;and&nbsp;if&nbsp;geom=check&nbsp;without&nbsp;any&nbsp;GIC&nbsp;keyword&nbsp;(i.e.,&nbsp;IOp(1/145=0)&nbsp;is&nbsp;used.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;but&nbsp;do&nbsp;two&nbsp;calls&nbsp;to&nbsp;CrdDef&nbsp;when&nbsp;building&nbsp;the&nbsp;coordinate&nbsp;definitions.&nbsp;The&nbsp;first&nbsp;call&nbsp;adds&nbsp;the&nbsp;coordinates&nbsp;in&nbsp;the&nbsp;same&nbsp;way&nbsp;that&nbsp;Option&nbsp;2&nbsp;does.&nbsp;The&nbsp;second&nbsp;call&nbsp;adds&nbsp;coordinates&nbsp;from&nbsp;a&nbsp;list&nbsp;of&nbsp;user-provided&nbsp;input&nbsp;coordinates&nbsp;in&nbsp;the&nbsp;same&nbsp;way&nbsp;as&nbsp;Option&nbsp;6×2&nbsp;does.&nbsp;In&nbsp;other&nbsp;words,&nbsp;there&nbsp;will&nbsp;be&nbsp;two&nbsp;sets&nbsp;of&nbsp;coordinates&nbsp;to&nbsp;be&nbsp;merged.&nbsp;The&nbsp;first&nbsp;set&nbsp;is&nbsp;generated&nbsp;by&nbsp;default&nbsp;(e.g.,&nbsp;in&nbsp;the&nbsp;case&nbsp;of&nbsp;Option&nbsp;9×3&nbsp;without&nbsp;geom=check)&nbsp;or&nbsp;it&nbsp;comes&nbsp;from&nbsp;a&nbsp;chk&nbsp;file&nbsp;(Option&nbsp;9×3&nbsp;with&nbsp;geom=check).&nbsp;The&nbsp;second&nbsp;set&nbsp;is&nbsp;provided&nbsp;by&nbsp;the&nbsp;user&nbsp;as&nbsp;a&nbsp;separate&nbsp;input&nbsp;section,&nbsp;and&nbsp;it&nbsp;contains&nbsp;some&nbsp;additional&nbsp;coordinates&nbsp;or&nbsp;modifications&nbsp;to&nbsp;the&nbsp;first&nbsp;set.&nbsp;A&nbsp;blank&nbsp;line&nbsp;can&nbsp;be&nbsp;used&nbsp;instead&nbsp;of&nbsp;the&nbsp;second&nbsp;set’s&nbsp;input&nbsp;section.&nbsp;It&nbsp;is&nbsp;also&nbsp;possible&nbsp;to&nbsp;make&nbsp;the&nbsp;user-provided&nbsp;input’s&nbsp;reading&nbsp;to&nbsp;be&nbsp;the&nbsp;first&nbsp;step&nbsp;and&nbsp;the&nbsp;construction&nbsp;of&nbsp;complementary&nbsp;coordinates&nbsp;by&nbsp;CrdCon&nbsp;to&nbsp;be&nbsp;the&nbsp;second&nbsp;step.&nbsp;The&nbsp;latter&nbsp;is&nbsp;Option&nbsp;6×3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Which&nbsp;coordinate&nbsp;derivative&nbsp;terms&nbsp;should&nbsp;be&nbsp;included&nbsp;in&nbsp;the&nbsp;data&nbsp;structure?&nbsp;(Default&nbsp;=&nbsp;3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Include&nbsp;only&nbsp;values&nbsp;in&nbsp;the&nbsp;definitions&nbsp;list.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;the&nbsp;coordinate&nbsp;definitions&nbsp;from&nbsp;the&nbsp;input&nbsp;file&nbsp;using&nbsp;the&nbsp;symbolic&nbsp;form,&nbsp;(See&nbsp;Routine&nbsp;CrInp1),&nbsp;and&nbsp;then&nbsp;automatically&nbsp;differentiate&nbsp;the&nbsp;active&nbsp;coordinate&nbsp;derivatives&nbsp;as&nbsp;needed.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Define&nbsp;(the&nbsp;full&nbsp;set&nbsp;of)&nbsp;distance&nbsp;matrix&nbsp;coordinates.&nbsp;This&nbsp;option&nbsp;can&nbsp;be&nbsp;combined&nbsp;with&nbsp;2xxx&nbsp;to&nbsp;use&nbsp;inverse&nbsp;distance&nbsp;matrix&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;the&nbsp;coordinate&nbsp;definitions&nbsp;from&nbsp;the&nbsp;input&nbsp;file&nbsp;using&nbsp;the&nbsp;OLD&nbsp;symbolic&nbsp;form&nbsp;(See&nbsp;Routine&nbsp;CrDfSy),&nbsp;and&nbsp;then&nbsp;automatically&nbsp;differentiate&nbsp;the&nbsp;active&nbsp;coordinate&nbsp;derivatives&nbsp;as&nbsp;needed.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;new&nbsp;coordinate&nbsp;generation&nbsp;code&nbsp;to&nbsp;create&nbsp;an&nbsp;intermediate&nbsp;RP&nbsp;structure&nbsp;based&nbsp;on&nbsp;the&nbsp;molecular&nbsp;connectivity&nbsp;(See&nbsp;Routine&nbsp;CrdCon),&nbsp;then&nbsp;have&nbsp;CrdDef&nbsp;build&nbsp;the&nbsp;data&nbsp;structure&nbsp;using&nbsp;the&nbsp;intermediate&nbsp;RP&nbsp;data&nbsp;from&nbsp;CrdCon&nbsp;and&nbsp;build&nbsp;derivatives&nbsp;wrt&nbsp;Cartesian&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;When&nbsp;building&nbsp;the&nbsp;internal&nbsp;coordinate&nbsp;definitions,&nbsp;should&nbsp;any&nbsp;systematic&nbsp;modifications&nbsp;be&nbsp;done?&nbsp;(Default&nbsp;=&nbsp;1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;Simply&nbsp;define&nbsp;the&nbsp;coordinates&nbsp;to&nbsp;be&nbsp;the&nbsp;same&nbsp;as&nbsp;they&nbsp;would&nbsp;have&nbsp;been&nbsp;using&nbsp;the&nbsp;old&nbsp;coordinate&nbsp;code.&nbsp;2xxx&nbsp;…&nbsp;Invert&nbsp;all&nbsp;bond&nbsp;stretch&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Invert&nbsp;all&nbsp;bond&nbsp;stretch&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;for&nbsp;default&nbsp;is&nbsp;1&nbsp;(GIC).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;to&nbsp;1&nbsp;if&nbsp;not&nbsp;specified.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;to&nbsp;2&nbsp;if&nbsp;not&nbsp;specified.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/146)
Control of SCVS:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(03045011).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Include&nbsp;forces&nbsp;in&nbsp;virial&nbsp;ratio.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;include&nbsp;forces&nbsp;in&nbsp;virial&nbsp;ratio.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Murdoch’s&nbsp;extrapolation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;use&nbsp;Murdoch’s&nbsp;extrapolation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Nxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Apply&nbsp;SCVS&nbsp;when&nbsp;max&nbsp;force&nbsp;on&nbsp;nuclei&nbsp;is&nbsp;below&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Mxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;convergence&nbsp;on&nbsp;the&nbsp;virial&nbsp;Eta.&nbsp;Default&nbsp;is&nbsp;5.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Lxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;convergence&nbsp;threshhold&nbsp;on&nbsp;|E|&nbsp;*&nbsp;(2*Eta&nbsp;–&nbsp;2),&nbsp;where&nbsp;|E|&nbsp;is&nbsp;the&nbsp;magnitude&nbsp;of&nbsp;the&nbsp;kinetic&nbsp;energy&nbsp;is&nbsp;10^-M.&nbsp;Default&nbsp;is&nbsp;3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Kxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;initial&nbsp;order&nbsp;of&nbsp;extrapolation&nbsp;is&nbsp;10^L&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* JJJxxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum&nbsp;of&nbsp;KKK&nbsp;SCVS&nbsp;iterations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/148)
`L106`: Storage of derivatives.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(221).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal&nbsp;storage&nbsp;of&nbsp;numerical&nbsp;first&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store&nbsp;numerical&nbsp;first&nbsp;and&nbsp;diagonal&nbsp;second&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;differences&nbsp;between&nbsp;numerical&nbsp;and&nbsp;analytic&nbsp;quantities.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;print&nbsp;differences.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Threshold&nbsp;for&nbsp;printing&nbsp;differences&nbsp;is&nbsp;-6-N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/150)
`L112`: Initial scale factor. 


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1.0)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;+&nbsp;N/100000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/151)
How many vectors with negative curvature to use in downhill step during minimization:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(3)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None,&nbsp;do&nbsp;regular&nbsp;RFO&nbsp;step.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Up&nbsp;to&nbsp;N&nbsp;vectors.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/152)
`L103`: Control of MaxStp (allocated max number of steps in L103).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;compute&nbsp;based&nbsp;on&nbsp;number&nbsp;of&nbsp;variables,&nbsp;NStep,&nbsp;etc.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Make&nbsp;MaxStp&nbsp;at&nbsp;least&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N<0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Make&nbsp;MaxStp&nbsp;at&nbsp;least&nbsp;-N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/153)
`L103`: Whether to fill OT file.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;do&nbsp;so&nbsp;for&nbsp;Cartesian&nbsp;and&nbsp;redundant&nbsp;internal&nbsp;coordinate&nbsp;optimizations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/154)
Linear angle test during internal coordinate generation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(15&nbsp;degrees,&nbsp;applied&nbsp;to&nbsp;all&nbsp;3&nbsp;tests).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Threshold&nbsp;N&nbsp;degrees,&nbsp;applied&nbsp;to&nbsp;the&nbsp;angle&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Threshold&nbsp;N&nbsp;degrees,&nbsp;applied&nbsp;to&nbsp;all&nbsp;3&nbsp;tests.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/155)
Number of steps to take in guessing a TS during QST2:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Divide&nbsp;the&nbsp;overall&nbsp;step&nbsp;into&nbsp;N&nbsp;increments.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/156)
Automatic generation of internal coordinates.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;bonds,&nbsp;angles,&nbsp;and&nbsp;dihedrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;bonds&nbsp;and&nbsp;angles&nbsp;but&nbsp;no&nbsp;dihedrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;bonds&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;no&nbsp;coordinates&nbsp;automatically.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(1/157)
Maximum step when going down an eigenvector:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(0.6)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/1000&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/158)
`L124`: PCM defaults; `L301`: Details.




### IOp(1/159)
Default maximum step in Cartesians during redundant coordinate optimizations.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Unlimited&nbsp;(10^6&nbsp;Bohr).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(3&nbsp;Bohr).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/10&nbsp;Bohr.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(1/160)
Type of fragment calculation:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(11).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;use&nbsp;of&nbsp;new&nbsp;ghost&nbsp;atoms&nbsp;in&nbsp;counterpoise.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;use&nbsp;of&nbsp;old&nbsp;ghost&nbsp;atoms&nbsp;in&nbsp;counterpoise.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Counterpoise.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fragment&nbsp;guess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 80&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Excitation&nbsp;energy&nbsp;transfer.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;full-system&nbsp;PCM&nbsp;cavity&nbsp;for&nbsp;fragments.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;fragment&nbsp;PCM&nbsp;cavity&nbsp;for&nbsp;fragments.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/161)
`L123`: Hack to save results at each IRC point.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/162)
Frequency of analytic Hessians during IRC corrector cycles.




### IOp(1/163)
Copy of external input section from chk file:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default;&nbsp;copy&nbsp;if&nbsp;Geom=AllCheck.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Copy&nbsp;regardless.&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;copy.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/164)
Read of atomic pair potential.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default;&nbsp;copy&nbsp;from&nbsp;chk&nbsp;if&nbsp;Geom=AllCheck.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;from&nbsp;input.&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;read.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;from&nbsp;chk.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(1/165)
Convergence of MM microiterations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10x&nbsp;tighter&nbsp;than&nbsp;macro,&nbsp;except&nbsp;&nbsp;10x&nbsp;for&nbsp;FOSimult&nbsp;with&nbsp;MM&nbsp;included).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nx&nbsp;tighter.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/166)
`L103`: Maximum number of vectors in DIIS. Format of input: MMNN.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;N&nbsp;vectors&nbsp;(default&nbsp;10&nbsp;for&nbsp;GEDIIS,&nbsp;10&nbsp;for&nbsp;SimOpt).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mix&nbsp;up&nbsp;to&nbsp;MM&nbsp;<&nbsp;NN&nbsp;vectors&nbsp;in&nbsp;DIIS&nbsp;when&nbsp;mixing&nbsp;RFO&nbsp;steps.&nbsp;(Default&nbsp;NN).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


A negative value requests uses of the Hessian eigenvector basis for the step. This is the default and only choice for GEDIIS TS optimizations.


### IOp(1/167)
Version of GEDIIS.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Old.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;New.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/168)
GEDIIS switches.


* NN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Switch&nbsp;from&nbsp;RFO&nbsp;to&nbsp;DIIS&nbsp;on&nbsp;RMS&nbsp;force&nbsp;(10^-NN,&nbsp;default&nbsp;1.d-3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MM00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Switch&nbsp;toEn-DIIS&nbsp;from&nbsp;RFO-DIIS&nbsp;on&nbsp;RMS&nbsp;step&nbsp;(10^-MM,&nbsp;default&nbsp;2.5d-3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* LLL0000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum&nbsp;coefficient&nbsp;allowed&nbsp;in&nbsp;RFO-DIIS&nbsp;before&nbsp;space&nbsp;is&nbsp;reduced&nbsp;(LLL/10,&nbsp;default&nbsp;10.0).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* `KKK0000000`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum&nbsp;coefficient&nbsp;allowed&nbsp;in&nbsp;RFO-DIIS&nbsp;before&nbsp;coefficients&nbsp;are&nbsp;adjusted&nbsp;(KKK/10;&nbsp;default&nbsp;3.0).&nbsp;The&nbsp;minimum&nbsp;value&nbsp;is&nbsp;-KKK/10&nbsp;+&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/170)
Control for selecting the initial conditions.


* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initial&nbsp;Cartesian&nbsp;coordinates&nbsp;and&nbsp;velocities&nbsp;are&nbsp;read-in&nbsp;from&nbsp;the&nbsp;input&nbsp;file.&nbsp;This&nbsp;data&nbsp;is&nbsp;read&nbsp;in&nbsp;a&nbsp;free-format&nbsp;fashion.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initial&nbsp;Cartesian&nbsp;coordinates&nbsp;and&nbsp;mass-weighted&nbsp;velocities&nbsp;are&nbsp;read-in&nbsp;from&nbsp;the&nbsp;input&nbsp;file.&nbsp;This&nbsp;data&nbsp;is&nbsp;read&nbsp;in&nbsp;a&nbsp;free-format&nbsp;fashion.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initial&nbsp;coordinates&nbsp;are&nbsp;given&nbsp;by&nbsp;the&nbsp;user-input&nbsp;geometry;&nbsp;initial&nbsp;velocities&nbsp;are&nbsp;determined&nbsp;by&nbsp;selecting&nbsp;a&nbsp;random&nbsp;velocity&nbsp;which&nbsp;gives&nbsp;an&nbsp;kinetic&nbsp;energy&nbsp;equal&nbsp;to&nbsp;the&nbsp;value&nbsp;set&nbsp;in&nbsp;IOp(73).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/172)
`L101`: Whether to print internal coordinates in L101.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;if&nbsp;present.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/173)
`L106`: Extra files to differentiate.


* -11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Differentiate&nbsp;the&nbsp;files&nbsp;related&nbsp;to&nbsp;ground-state&nbsp;post-SCF&nbsp;2nd&nbsp;derivatives&nbsp;(Lagrangian,&nbsp;P,&nbsp;and&nbsp;W).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Differentiate&nbsp;the&nbsp;files&nbsp;related&nbsp;to&nbsp;CIS/TD&nbsp;second&nbsp;derivatives&nbsp;(Lagrangian,&nbsp;P,&nbsp;W,&nbsp;and&nbsp;T).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;two&nbsp;lists,&nbsp;each&nbsp;terminated&nbsp;by&nbsp;a&nbsp;blank&nbsp;line,&nbsp;the&nbsp;first&nbsp;the&nbsp;files&nbsp;to&nbsp;differentiate&nbsp;and&nbsp;the&nbsp;second&nbsp;the&nbsp;files&nbsp;where&nbsp;the&nbsp;numerical&nbsp;derivatives&nbsp;will&nbsp;be&nbsp;stored&nbsp;(0&nbsp;for&nbsp;items&nbsp;which&nbsp;will&nbsp;not&nbsp;be&nbsp;saved).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;a&nbsp;list&nbsp;from&nbsp;an&nbsp;input&nbsp;section,&nbsp;terminated&nbsp;by&nbsp;a&nbsp;blank&nbsp;link.&nbsp;The&nbsp;numerical&nbsp;derivatives&nbsp;will&nbsp;be&nbsp;printed&nbsp;but&nbsp;not&nbsp;stored&nbsp;on&nbsp;disk.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;file&nbsp;number&nbsp;N,&nbsp;storing&nbsp;derivatives&nbsp;in&nbsp;file&nbsp;795.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/174)
Reading parameters for classical electrostatics and dispersion.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;3&nbsp;if&nbsp;Geom=AllCheck&nbsp;else&nbsp;2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;selected&nbsp;parameters&nbsp;for&nbsp;elements&nbsp;from&nbsp;input.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;default&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;user-specified&nbsp;parameters&nbsp;from&nbsp;chk&nbsp;file&nbsp;if&nbsp;present.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;both&nbsp;user-specified&nbsp;and&nbsp;default&nbsp;parameters&nbsp;from&nbsp;chk&nbsp;file&nbsp;if&nbsp;present.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/175)
Electronic embedding type:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ONIOM&nbsp;style.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QM/MM&nbsp;style.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/176)
Box size used for generating connectivity.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(8&nbsp;Bohr).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;Bohr.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(1/179)
Use of subprocesses for energy+derivatives, for debugging:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1002).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;using&nbsp;loop&nbsp;over&nbsp;steps&nbsp;in&nbsp;L106.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;using&nbsp;loop&nbsp;over&nbsp;calls&nbsp;to&nbsp;utility&nbsp;in&nbsp;L106.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;using&nbsp;Linda.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Debug&nbsp;output&nbsp;and&nbsp;save&nbsp;of&nbsp;subprocess&nbsp;files.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Full&nbsp;copy&nbsp;of&nbsp;rwf&nbsp;back&nbsp;and&nbsp;forth.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Iterate&nbsp;purturbations&nbsp;forward.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Iterate&nbsp;purturbations&nbsp;backward.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(1/180)
Stopping during subprocess execution, for debugging.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;stop.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stop&nbsp;after&nbsp;running&nbsp;N&nbsp;subprocesses.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(1/181)
Maximum number of middle iterations during ONIOM-EE:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(40).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




## Overlay 2 
### IOp(2/9)
Printing of distance and angle matrices.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;print&nbsp;if&nbsp;≤50&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;print&nbsp;the&nbsp;distance&nbsp;matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;distance&nbsp;matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;do&nbsp;not&nbsp;print.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;print&nbsp;the&nbsp;angle&nbsp;matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;the&nbsp;angle&nbsp;matrix,&nbsp;using&nbsp;z-matrix&nbsp;connectivity&nbsp;if&nbsp;possible.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;cutoffs&nbsp;instead&nbsp;of&nbsp;the&nbsp;z-matrix&nbsp;for&nbsp;determining&nbsp;which&nbsp;angles&nbsp;to&nbsp;print.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;same&nbsp;as&nbsp;100.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;print&nbsp;dihedral&nbsp;angles.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;dihedral&nbsp;angles,&nbsp;using&nbsp;the&nbsp;z-matrix&nbsp;for&nbsp;connectivity&nbsp;info.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;dihedral&nbsp;angles,&nbsp;using&nbsp;a&nbsp;distance&nbsp;cutoff&nbsp;for&nbsp;connectivity&nbsp;info.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;print&nbsp;only&nbsp;for&nbsp;small&nbsp;cases.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;print&nbsp;the&nbsp;Cartesian&nbsp;coordinates&nbsp;in&nbsp;the&nbsp;input&nbsp;orientation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;print&nbsp;the&nbsp;Cartesian&nbsp;coordinates&nbsp;in&nbsp;the&nbsp;input&nbsp;orientation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(2/10)
Tetrahedral angle fixing


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(don’t&nbsp;test).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Angles&nbsp;within&nbsp;0.001&nbsp;degree&nbsp;of&nbsp;109.471&nbsp;will&nbsp;be&nbsp;set&nbsp;to&nbsp;ACOS(-1/3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;test&nbsp;for&nbsp;such&nbsp;angles.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(2/11)
Printing of z-matrix and resultant coordinates.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(print&nbsp;if&nbsp;50&nbsp;atoms&nbsp;or&nbsp;less).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print.&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;print.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(2/12)
Crowding abort control.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Abort&nbsp;the&nbsp;run&nbsp;for&nbsp;zero&nbsp;atomic&nbsp;distances&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Abort&nbsp;the&nbsp;run&nbsp;if&nbsp;any&nbsp;atoms&nbsp;are&nbsp;within&nbsp;0.5&nbsp;Å.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;abort&nbsp;the&nbsp;run&nbsp;regardless&nbsp;of&nbsp;0&nbsp;distances.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(2/13)
Punch coordinates.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;in&nbsp;‘atoms’&nbsp;format&nbsp;(3E20.12).&nbsp;Note:&nbsp;atoms&nbsp;will&nbsp;not&nbsp;take&nbsp;the&nbsp;atomic&nbsp;numbers,&nbsp;so&nbsp;they&nbsp;are&nbsp;not&nbsp;punched.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;in&nbsp;format&nbsp;suitable&nbsp;for&nbsp;coord.&nbsp;input&nbsp;to&nbsp;Gaussian.&nbsp;The&nbsp;atomic&nbsp;numbers&nbsp;and&nbsp;coordinates&nbsp;are&nbsp;punched&nbsp;in&nbsp;(I2,3E20.12).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(2/14)
Internal coordinate linear independence.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Perform&nbsp;the&nbsp;test,&nbsp;but&nbsp;do&nbsp;not&nbsp;abort&nbsp;the&nbsp;job.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;perform&nbsp;the&nbsp;test.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If&nbsp;internal&nbsp;cords.&nbsp;are&nbsp;in&nbsp;use,&nbsp;test&nbsp;the&nbsp;variables&nbsp;for&nbsp;linear&nbsp;indep,&nbsp;and&nbsp;abort&nbsp;the&nbsp;job&nbsp;if&nbsp;they’re&nbsp;dep.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;nuclear&nbsp;forces&nbsp;as&nbsp;well&nbsp;as&nbsp;second&nbsp;derivatives&nbsp;for&nbsp;the&nbsp;test.&nbsp;&nbsp;This&nbsp;is&nbsp;not&nbsp;correct&nbsp;for&nbsp;the&nbsp;linear&nbsp;independence&nbsp;check,&nbsp;but&nbsp;is&nbsp;useful&nbsp;for&nbsp;debugging&nbsp;the&nbsp;derivative&nbsp;transformation&nbsp;routines.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Abort&nbsp;the&nbsp;job&nbsp;if&nbsp;the&nbsp;number&nbsp;of&nbsp;z-matrix&nbsp;variables&nbsp;is&nbsp;not&nbsp;exactly&nbsp;the&nbsp;number&nbsp;of&nbsp;degrees&nbsp;of&nbsp;freedom&nbsp;(i.e.,&nbsp;this&nbsp;is&nbsp;not&nbsp;a&nbsp;full&nbsp;optimization).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(2/15)
Symmetry control.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turns&nbsp;on&nbsp;symmetry;&nbsp;same&nbsp;as&nbsp;0&nbsp;for&nbsp;molecules&nbsp;but&nbsp;turns&nbsp;on&nbsp;assignment&nbsp;of&nbsp;space&nbsp;group&nbsp;operations&nbsp;for&nbsp;PBC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Leave&nbsp;symmetry&nbsp;in&nbsp;whatever&nbsp;state&nbsp;it&nbsp;is&nbsp;presently&nbsp;in.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Unconditionally&nbsp;turn&nbsp;symmetry&nbsp;off.&nbsp;Note&nbsp;that&nbsp;symmetry&nbsp;is&nbsp;still&nbsp;called,&nbsp;and&nbsp;will&nbsp;determine&nbsp;the&nbsp;framework&nbsp;group.&nbsp;However,&nbsp;the&nbsp;molecule&nbsp;is&nbsp;not&nbsp;oriented.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bring&nbsp;the&nbsp;molecule&nbsp;to&nbsp;a&nbsp;symmetry&nbsp;orientation,&nbsp;but&nbsp;then&nbsp;disable&nbsp;further&nbsp;use&nbsp;of&nbsp;symmetry.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;even&nbsp;call&nbsp;Symm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Call&nbsp;Symm&nbsp;once&nbsp;with&nbsp;loose&nbsp;cutoffs,&nbsp;symmetrize&nbsp;the&nbsp;resulting&nbsp;coordinates&nbsp;then&nbsp;confirm&nbsp;symmetry&nbsp;with&nbsp;tight&nbsp;cutoffs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Recover&nbsp;the&nbsp;previous&nbsp;symmetry&nbsp;operations&nbsp;from&nbsp;the&nbsp;RWF,&nbsp;and&nbsp;confirm&nbsp;that&nbsp;the&nbsp;new&nbsp;structure&nbsp;has&nbsp;the&nbsp;same&nbsp;symmetry.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;5,&nbsp;but&nbsp;get&nbsp;symmetry&nbsp;info&nbsp;from&nbsp;the&nbsp;checkpoint.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;re-orientation&nbsp;for&nbsp;PBC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Suppress&nbsp;re-orientation&nbsp;for&nbsp;PBC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;on&nbsp;symmetry&nbsp;operations&nbsp;for&nbsp;PBC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(2/16)
Action taken if the point group changes during an optimization.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Keep&nbsp;going.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Keep&nbsp;going,&nbsp;and&nbsp;leave&nbsp;symmetry&nbsp;on,&nbsp;using&nbsp;the&nbsp;old&nbsp;symmetry.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Keep&nbsp;going,&nbsp;and&nbsp;leave&nbsp;symmetry&nbsp;on,&nbsp;using&nbsp;the&nbsp;new&nbsp;symmetry.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Abort&nbsp;the&nbsp;job.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(2/17)
Tolerance for distance comparisons in symmetry determination.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(determined&nbsp;in&nbsp;the&nbsp;symmetry&nbsp;package,&nbsp;currently&nbsp;1.d-8).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;
* N<0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^N,&nbsp;use&nbsp;same&nbsp;tolerance&nbsp;for&nbsp;orientation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(2/18)
Tolerance for non-distance comparisons in symmetry determination.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(determined&nbsp;in&nbsp;the&nbsp;symmetry&nbsp;package,&nbsp;currently&nbsp;1.d-7).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;
* N<0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^N,&nbsp;use&nbsp;same&nbsp;tolerance&nbsp;for&nbsp;orientation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(2/19)
Largest allowed point group, as Hollerith string.




### IOp(2/20)
Number (1-3 for X-Z) of axis to help specify which subgroup of the type specified in IOp(2/19) to use.




### IOp(2/21)
Atomic values to use in symmetry assignment/orientation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(221).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Atomic&nbsp;numbers.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Atomic&nbsp;masses.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;symmetry&nbsp;coordinates&nbsp;to&nbsp;high&nbsp;precision.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;print&nbsp;symmetry&nbsp;coordinates&nbsp;to&nbsp;high&nbsp;precision.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;standard&nbsp;orientation&nbsp;as&nbsp;input&nbsp;orientation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;save&nbsp;standard&nbsp;orientation&nbsp;as&nbsp;input&nbsp;orientation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(2/29)
Update of coordinates from current z-matrix.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;but&nbsp;remove&nbsp;z-matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(2/30)
Read in vector of atom types (for debugging).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;format&nbsp;(50I2)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(2/40)
Save (initial) structure and possible constraints in RWF 698.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pick&nbsp;up&nbsp;structure&nbsp;from&nbsp;RWF&nbsp;698&nbsp;on&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;structure&nbsp;from&nbsp;input&nbsp;stream.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(2/41)
Force constants for harmonic constraints.


* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;force&nbsp;constants&nbsp;for&nbsp;each&nbsp;Cartesian&nbsp;coordinate.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;constraints.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(no&nbsp;constraint&nbsp;unless&nbsp;reading&nbsp;constraint&nbsp;from&nbsp;checkpoint&nbsp;file).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/10^6&nbsp;Hartree/Bohr^2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(2/42)
Count nearest neighbor interactions.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Count&nbsp;atoms&nbsp;within&nbsp;N/100&nbsp;Å&nbsp;as&nbsp;neighbors.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(2/43)
Print standard orientation to high precision.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(2/44)
Control for symmetry package.


* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(12,&nbsp;unless&nbsp;COM&nbsp;was&nbsp;specified,&nbsp;in&nbsp;which&nbsp;case&nbsp;21).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initially.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;rotate&nbsp;to&nbsp;principal&nbsp;axes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rotate&nbsp;to&nbsp;old&nbsp;axes&nbsp;for&nbsp;C1,&nbsp;Cs,&nbsp;and&nbsp;Ci.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;principal&nbsp;axes&nbsp;for&nbsp;C1,&nbsp;Cs,&nbsp;and&nbsp;Ci.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




## Overlay 3 
### IOp(3/5)
Type of basis set. The same numbers are used for all basis sets, whether intended for use in expanding AOs (IOp(5)) or in expanding the density (IOp(82)).


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Minimal&nbsp;STO-2G&nbsp;to&nbsp;STO-6G&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Extended&nbsp;4-31G,5-31G,6-31G&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Minimal&nbsp;STO-NG&nbsp;(valence&nbsp;functions&nbsp;only)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Extended&nbsp;LP-N1G&nbsp;(valence&nbsp;basis&nbsp;for&nbsp;coreless&nbsp;Hartree-Fock&nbsp;pseudo-potentials)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Extended&nbsp;6-311G&nbsp;(UMP2&nbsp;frozen&nbsp;core&nbsp;optimized)&nbsp;basis&nbsp;for&nbsp;first&nbsp;row,&nbsp;MacLean-Chandler&nbsp;(12s,9p)–>(631111,52111)&nbsp;for&nbsp;second&nbsp;row.&nbsp;Use&nbsp;IOp(8)&nbsp;to&nbsp;select&nbsp;5D/6D.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Split&nbsp;valence&nbsp;N-21G&nbsp;(or&nbsp;NN-21G)&nbsp;basis&nbsp;for&nbsp;first&nbsp;or&nbsp;second&nbsp;row&nbsp;atoms.&nbsp;(Various&nbsp;implementations&nbsp;may&nbsp;omit&nbsp;second&nbsp;row&nbsp;atoms.)&nbsp;See&nbsp;IOp(6)&nbsp;for&nbsp;determination&nbsp;of&nbsp;the&nbsp;number&nbsp;of&nbsp;Gaussians&nbsp;in&nbsp;the&nbsp;inner&nbsp;shell.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LANL&nbsp;ECP&nbsp;basis&nbsp;sets.&nbsp;IOp(3/6)&nbsp;selects&nbsp;options.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;General;&nbsp;see&nbsp;routine&nbsp;GenBas&nbsp;for&nbsp;input&nbsp;instructions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dunning/Caltech&nbsp;basis&nbsp;sets.&nbsp;Type&nbsp;selected&nbsp;by&nbsp;IOp(3/6).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stevens/Basch/Krauss/Jasien/Cundari&nbsp;ECP&nbsp;basis&nbsp;sets&nbsp;for&nbsp;H-Lu.&nbsp;Type&nbsp;selected&nbsp;by&nbsp;IOp(3/6)&nbsp;for&nbsp;H-Ar.&nbsp;Literature&nbsp;citations&nbsp;in&nbsp;CEPPot.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CBS&nbsp;basis&nbsp;#1&nbsp;–6-31+g(d,p)&nbsp;on&nbsp;H,&nbsp;He,&nbsp;6-311+G(2df)&nbsp;on&nbsp;Li&nbsp;–&nbsp;Ne,&nbsp;6-311+g(3d2f)&nbsp;on&nbsp;Na&nbsp;–&nbsp;Ar.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CBS&nbsp;basis&nbsp;#2&nbsp;–6-31G,&nbsp;use&nbsp;daggers&nbsp;if&nbsp;any&nbsp;polarization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 12&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CBS&nbsp;basis&nbsp;#3&nbsp;–&nbsp;6-311++G(2df,2p)&nbsp;on&nbsp;H&nbsp;–&nbsp;Ne,&nbsp;6-311++g(3d2f)&nbsp;on&nbsp;Na&nbsp;–&nbsp;Ar&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 13&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CBS&nbsp;basis&nbsp;#4&nbsp;–6-31+G(d,p)&nbsp;on&nbsp;H&nbsp;–&nbsp;Si,&nbsp;6-31+G(df,p)&nbsp;on&nbsp;P,&nbsp;S,&nbsp;Cl&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 14&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CBS&nbsp;basis&nbsp;#5&nbsp;–Large&nbsp;APNO&nbsp;basis&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 15&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CBS&nbsp;basis&nbsp;#6&nbsp;–Core&nbsp;correlation&nbsp;basis&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 16&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dunning&nbsp;cc&nbsp;basis&nbsp;sets,&nbsp;type&nbsp;selected&nbsp;by&nbsp;IOp(3/6)&nbsp;(=0-4&nbsp;for&nbsp;V{D,T,Q,5,6}Z)&nbsp;and&nbsp;augmented&nbsp;if&nbsp;IOp(7)=10.&nbsp;IOp(6)=5&nbsp;for&nbsp;MTsmall&nbsp;basis&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 17&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stuttgart/Dresden&nbsp;ECP&nbsp;basis&nbsp;sets.&nbsp;IOp(3/6)&nbsp;specifies&nbsp;type.&nbsp;Literature&nbsp;citations&nbsp;in&nbsp;SDDPot.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 18&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ahlrichs&nbsp;SV&nbsp;basis&nbsp;sets.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 19&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ahlrichs&nbsp;TZV&nbsp;basis&nbsp;sets.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MIDI!&nbsp;basis&nbsp;sets.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 21&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EPR-II&nbsp;basis&nbsp;sets.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 22&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EPR-III&nbsp;basis&nbsp;sets.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 23&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UGBS&nbsp;basis&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 24&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G3large&nbsp;basis&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 25&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G3MP2large&nbsp;basis&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 26&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Coreless:&nbsp;Li,Be&nbsp;2SDF,&nbsp;B-Ne&nbsp;2MWB,&nbsp;rest&nbsp;LANL1MB.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 27&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DGauss&nbsp;basis&nbsp;sets,&nbsp;selected&nbsp;by&nbsp;IOp(3/6).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 28&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Auto-generated,&nbsp;useful&nbsp;only&nbsp;for&nbsp;density&nbsp;basis&nbsp;sets.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 29&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Spherical&nbsp;atomic&nbsp;densities:&nbsp;&nbsp;a&nbsp;single&nbsp;highly&nbsp;contracted&nbsp;s-Gaussian&nbsp;for&nbsp;each&nbsp;atom.&nbsp;Only&nbsp;useful&nbsp;for&nbsp;fitting&nbsp;sets.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;One&nbsp;s-Gaussian&nbsp;per&nbsp;atom;&nbsp;dummy&nbsp;basis&nbsp;used&nbsp;for&nbsp;MM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 31&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G3largeXP&nbsp;basis&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G3MP2largeXP&nbsp;basis&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 33&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G3&nbsp;basis&nbsp;1&nbsp;–&nbsp;"6-31G(d)"&nbsp;basis&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 34&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G3&nbsp;basis&nbsp;2&nbsp;–&nbsp;"6-31+G(d)"&nbsp;basis&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 35&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G3&nbsp;basis&nbsp;3&nbsp;–&nbsp;"6-31G(2df,d)"&nbsp;basis&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 36&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G4&nbsp;QZ&nbsp;HF&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 37&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G4&nbsp;5Z&nbsp;HF&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 38&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G4MP2&nbsp;TZ&nbsp;HF&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 39&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G4MP2&nbsp;QZ&nbsp;HF&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Weigand&nbsp;Coulomb&nbsp;fitting&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 41&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ahlrichs&nbsp;SVP&nbsp;Coulomb&nbsp;fitting&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 42&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ahlrichs&nbsp;TZVP&nbsp;Coulomb&nbsp;fitting&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 43&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ahlrichs/Weigand&nbsp;def2-SV&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 44&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ahlrichs/Weigand&nbsp;def2-TZV&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 45&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ahlrichs/Weigand&nbsp;QZV&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 46&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fitting&nbsp;set&nbsp;matched&nbsp;to&nbsp;AO&nbsp;basis,&nbsp;or&nbsp;error&nbsp;if&nbsp;there&nbsp;is&nbsp;none.&nbsp;Converted&nbsp;here&nbsp;to&nbsp;matched&nbsp;value.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 47&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fitting&nbsp;set&nbsp;matched&nbsp;to&nbsp;AO&nbsp;basis,&nbsp;or&nbsp;/Auto&nbsp;if&nbsp;there&nbsp;is&nbsp;none.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/6)
Number of Gaussian functions.


* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;STO-NG,N-31G,LP-N1G,STO-NG-VALENCE,&nbsp;N-21G.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


Note if IOp(3/5)=3 and IOp(3/6)=8: LP-31G for Li,Be,B,Na,Mg,Al; LP-41G for other row 1 and 2 atoms.


Default options IOp(6)=0


* If&nbsp;IOp(3/5)=0&nbsp;N=3   STO-3G&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* If&nbsp;IOp(3/5)=1&nbsp;N=4   4-31G&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* If&nbsp;IOp(3/5)=2&nbsp;N=3   STO-3G&nbsp;(valence)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* If&nbsp;IOp(3/5)=3&nbsp;N=3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* If&nbsp;IOp(3/5)=5&nbsp;N=3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


When IOp(5)=7 (general basis), this option is used to control where the basis is taken from.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;general&nbsp;basis&nbsp;from&nbsp;the&nbsp;input&nbsp;stream.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;the&nbsp;general&nbsp;basis&nbsp;from&nbsp;the&nbsp;RW-files&nbsp;and&nbsp;merge&nbsp;with&nbsp;the&nbsp;coordinates&nbsp;in&nbsp;blank&nbsp;common&nbsp;to&nbsp;produce&nbsp;the&nbsp;current&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;the&nbsp;general&nbsp;basis&nbsp;from&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;1,&nbsp;for&nbsp;density&nbsp;basis&nbsp;(generated&nbsp;here&nbsp;from&nbsp;1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;2,&nbsp;for&nbsp;density&nbsp;basis&nbsp;(generated&nbsp;here&nbsp;from&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;from&nbsp;the&nbsp;alternate&nbsp;file&nbsp;and&nbsp;remove&nbsp;functions/ECPs&nbsp;for&nbsp;inactive&nbsp;atoms.&nbsp;Used&nbsp;for&nbsp;counterpoise&nbsp;calculations,&nbsp;where&nbsp;one&nbsp;wants&nbsp;to&nbsp;modify&nbsp;the&nbsp;basis&nbsp;differently&nbsp;during&nbsp;different&nbsp;steps.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;from&nbsp;the&nbsp;other&nbsp;alternate&nbsp;file,&nbsp;saved&nbsp;before&nbsp;the&nbsp;basis&nbsp;is&nbsp;massaged,&nbsp;uncontracted,&nbsp;etc.&nbsp;This&nbsp;option&nbsp;is&nbsp;useful&nbsp;when&nbsp;doing&nbsp;general&nbsp;basis&nbsp;geometry&nbsp;optimizations&nbsp;or&nbsp;properties&nbsp;using&nbsp;a&nbsp;wavefunction&nbsp;on&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;If&nbsp;non-standard&nbsp;ECPs&nbsp;are&nbsp;in&nbsp;use,&nbsp;they&nbsp;are&nbsp;read&nbsp;along&nbsp;with&nbsp;the&nbsp;basis&nbsp;set&nbsp;information.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


When IOp(3/5)=6 (LANL basis and potentials) this selects the type.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LANL1&nbsp;ECP,&nbsp;MBS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LANL1&nbsp;ECP,&nbsp;DZ.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LANL2&nbsp;ECP&nbsp;(where&nbsp;available,&nbsp;otherwise&nbsp;LANL1),&nbsp;MBS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LANL2&nbsp;ECP&nbsp;(where&nbsp;available,&nbsp;otherwise&nbsp;LANL1),&nbsp;DZ.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


When IOp(3/5)=8 (Dunning bases) this option selects the type.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dunning&nbsp;full&nbsp;double-zeta.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dunning&nbsp;valence&nbsp;double-zeta.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WAG&nbsp;basis&nbsp;(Dunning&nbsp;VDZ&nbsp;on&nbsp;first&nbsp;row,&nbsp;SHC&nbsp;ECP&nbsp;on&nbsp;second&nbsp;row).&nbsp;See&nbsp;Rappe,&nbsp;Smedley,&nbsp;and&nbsp;Goddard,&nbsp;J.&nbsp;Phys.&nbsp;Chem.&nbsp;85,&nbsp;1662&nbsp;(1981)&nbsp;and&nbsp;J.&nbsp;Phys.&nbsp;Chem.&nbsp;85,&nbsp;3546&nbsp;(1981).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


When IOp(3/5)=9 (CEP basis) this option selects the type (H-Ar only).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CEP-4G.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CEP-31G.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CEP-121G.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


When IOp(3/5)=17 (Stuttgart/Dresden ECP bases) this option selects the type according to:


* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SDDAll:&nbsp;SDD&nbsp;for&nbsp;Z&nbsp;>&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SDD&nbsp;for&nbsp;Z&nbsp;>&nbsp;18&nbsp;with&nbsp;SEG&nbsp;basis&nbsp;for&nbsp;Lanthanides&nbsp;&&nbsp;Actinides,&nbsp;D95&nbsp;or&nbsp;6-31G&nbsp;and&nbsp;no&nbsp;ECP&nbsp;otherwise.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SDDOld:&nbsp;same&nbsp;as&nbsp;SDD&nbsp;with&nbsp;old&nbsp;Lanthanide&nbsp;&&nbsp;Actinide&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


When IOp(3/5)=26 (Coreless basis) this selects the choice of basis (the same ECPs are used regardless).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(3)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Primitives&nbsp;which&nbsp;match&nbsp;the&nbsp;ECPs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Functions&nbsp;from&nbsp;extended&nbsp;Huckel&nbsp;theory.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VSTO-4G&nbsp;basis&nbsp;for&nbsp;1st&nbsp;row,&nbsp;along&nbsp;with&nbsp;LP-31G&nbsp;potential.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N>3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Huckel&nbsp;basis&nbsp;for&nbsp;method&nbsp;N-1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


When IOp(3/5)=27 (DGauss basis sets).


* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DGDZVP.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DZVP2.&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DGTZVP.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DGA1&nbsp;(fitting&nbsp;basis).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DGA2&nbsp;(fitting&nbsp;basis).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/7)
Diffuse and polarization functions.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D-functions&nbsp;on&nbsp;heavy&nbsp;atoms&nbsp;(2nd&nbsp;row&nbsp;only&nbsp;for&nbsp;3-21G).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2d-functions&nbsp;on&nbsp;heavy&nbsp;atoms&nbsp;(Scaled&nbsp;up&nbsp;and&nbsp;down&nbsp;by&nbsp;a&nbsp;factor&nbsp;of&nbsp;2&nbsp;from&nbsp;the&nbsp;standard&nbsp;single-d&nbsp;values).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;One&nbsp;set&nbsp;of&nbsp;d-functions&nbsp;and&nbsp;one&nbsp;set&nbsp;of&nbsp;f-functions&nbsp;on&nbsp;heavy&nbsp;atoms.&nbsp;(indicates&nbsp;an&nbsp;extra&nbsp;tight&nbsp;2df&nbsp;with&nbsp;ccp&nbsp;basis&nbsp;sets.)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Two&nbsp;sets&nbsp;of&nbsp;d-functions&nbsp;and&nbsp;one&nbsp;set&nbsp;of&nbsp;f-functions&nbsp;on&nbsp;heavy&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Three&nbsp;sets&nbsp;of&nbsp;d-functions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Three&nbsp;sets&nbsp;of&nbsp;d-functions&nbsp;and&nbsp;one&nbsp;set&nbsp;of&nbsp;f-functions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Three&nbsp;sets&nbsp;of&nbsp;d-functions&nbsp;and&nbsp;two&nbsp;sets&nbsp;of&nbsp;f-functions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CBS-Q&nbsp;d(f),d,p&nbsp;polarization&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tight&nbsp;d&nbsp;for&nbsp;VnZ+1&nbsp;(W1&nbsp;theory).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A&nbsp;set&nbsp;of&nbsp;diffuse&nbsp;sp-functions&nbsp;on&nbsp;heavy&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Augment&nbsp;non-hydrogens&nbsp;only&nbsp;(cc&nbsp;basis&nbsp;sets&nbsp;only).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maug-:&nbsp;Main&nbsp;group(SP),&nbsp;TM(SP).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;H(SP),&nbsp;Main&nbsp;group(SP),&nbsp;TM(SP).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 50&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Jul-&nbsp;aug:&nbsp;up&nbsp;to&nbsp;LVal&nbsp;on&nbsp;non-H,He.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 60&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Jun-&nbsp;aug:&nbsp;up&nbsp;to&nbsp;LVal-1&nbsp;on&nbsp;non-H,He.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 70&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;May-&nbsp;aug:&nbsp;up&nbsp;to&nbsp;LVal-2&nbsp;on&nbsp;non-H,He.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 80&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Apr-&nbsp;aug:&nbsp;up&nbsp;to&nbsp;LVal-3&nbsp;on&nbsp;non-H,He.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;P-functions&nbsp;on&nbsp;hydrogens;&nbsp;interpret&nbsp;first&nbsp;digit&nbsp;as&nbsp;pol&nbsp;level&nbsp;for&nbsp;ugbs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;sets&nbsp;of&nbsp;p-functions&nbsp;on&nbsp;hydrogens.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;One&nbsp;set&nbsp;of&nbsp;p-functions&nbsp;and&nbsp;one&nbsp;set&nbsp;of&nbsp;d-functions&nbsp;on&nbsp;hydrogens.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 400&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Two&nbsp;sets&nbsp;of&nbsp;p-functions&nbsp;and&nbsp;one&nbsp;set&nbsp;of&nbsp;d-functions&nbsp;on&nbsp;hydrogens.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 500&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Three&nbsp;sets&nbsp;of&nbsp;p-functions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 600&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Three&nbsp;sets&nbsp;of&nbsp;p-functions&nbsp;and&nbsp;one&nbsp;set&nbsp;of&nbsp;d-functions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 700&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(2d,d,p)&nbsp;—&nbsp;2d&nbsp;on&nbsp;2nd&nbsp;and&nbsp;later&nbsp;atoms,&nbsp;1d&nbsp;on&nbsp;1st&nbsp;row&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pople-style&nbsp;basis&nbsp;sets:&nbsp;&nbsp;a&nbsp;diffuse&nbsp;function&nbsp;on&nbsp;hydrogens.&nbsp;Truhlar-style&nbsp;calendar&nbsp;basis&nbsp;sets:&nbsp;inconsistent&nbsp;s&nbsp;and&nbsp;p&nbsp;diffuse&nbsp;functions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number&nbsp;of&nbsp;times&nbsp;to&nbsp;augment&nbsp;(cc-pvxz&nbsp;basis&nbsp;sets).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* M0000      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum&nbsp;L&nbsp;for&nbsp;diffuse&nbsp;functions&nbsp;is&nbsp;L(valence)-M.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/8)
Selection of pure/Cartesian functions.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Selection&nbsp;determined&nbsp;by&nbsp;the&nbsp;basis&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N-31G&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6D/7F&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N-311G&nbsp;&nbsp;&nbsp;&nbsp;5D/7F&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N-21G*&nbsp;&nbsp;&nbsp;&nbsp;5D&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;STO-NG*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5D&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LP-N1G*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5D&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LP-NIG**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5D&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;General&nbsp;basis&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5D/7F&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5D&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6DF&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7F&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10F&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(3/9)
`L308`: Where to store dipole velocity integrals.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Usual&nbsp;place&nbsp;(572).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Write&nbsp;over&nbsp;the&nbsp;dipole&nbsp;length&nbsp;integrals&nbsp;(518).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store&nbsp;in&nbsp;RWF&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/10)
Modification of internally stored bases (default 12000).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;general&nbsp;basis&nbsp;data&nbsp;in&nbsp;addition&nbsp;to&nbsp;setting&nbsp;up&nbsp;a&nbsp;standard&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Massage&nbsp;the&nbsp;data&nbsp;in&nbsp;Common&nbsp;/B/&nbsp;and&nbsp;Common&nbsp;/Mol/.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Massage&nbsp;the&nbsp;data&nbsp;in&nbsp;Common&nbsp;/B/&nbsp;and&nbsp;Common&nbsp;/Mol/,&nbsp;but&nbsp;don’t&nbsp;change&nbsp;ian&nbsp;if&nbsp;nuc&nbsp;charge&nbsp;changed.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add&nbsp;ghost&nbsp;atoms&nbsp;to&nbsp;/B/&nbsp;so&nbsp;that&nbsp;every&nbsp;shell&nbsp;is&nbsp;on&nbsp;a&nbsp;separate&nbsp;center.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Split&nbsp;S=P&nbsp;AO&nbsp;basis&nbsp;shells&nbsp;into&nbsp;separate&nbsp;S&nbsp;and&nbsp;P&nbsp;shells.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;split&nbsp;S=P&nbsp;AO&nbsp;shells.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Split&nbsp;S=P=D=…&nbsp;AO&nbsp;shells&nbsp;into&nbsp;S=P,&nbsp;D,&nbsp;F,&nbsp;…&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;split&nbsp;AO&nbsp;S=P=D…&nbsp;shells.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Uncontract&nbsp;the&nbsp;AO&nbsp;basis&nbsp;and&nbsp;removes&nbsp;duplicate&nbsp;primitives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200000&nbsp;&nbsp;&nbsp;&nbsp;Uncontract&nbsp;the&nbsp;density&nbsp;basis&nbsp;and&nbsp;removes&nbsp;duplicate&nbsp;primitives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 300000&nbsp;&nbsp;&nbsp;&nbsp;Uncontract&nbsp;both&nbsp;basis&nbsp;sets&nbsp;and&nbsp;removes&nbsp;duplicate&nbsp;primitives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 400000&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;1&nbsp;but&nbsp;don’t&nbsp;remove&nbsp;the&nbsp;duplicates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 500000&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;2&nbsp;but&nbsp;don’t&nbsp;remove&nbsp;the&nbsp;duplicates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 600000&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;3&nbsp;but&nbsp;don’t&nbsp;remove&nbsp;the&nbsp;duplicates&nbsp;from&nbsp;the&nbsp;AO&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 700000&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;3&nbsp;but&nbsp;don’t&nbsp;remove&nbsp;the&nbsp;duplicates&nbsp;from&nbsp;the&nbsp;density&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 800000&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;3&nbsp;but&nbsp;don’t&nbsp;remove&nbsp;the&nbsp;duplicates&nbsp;from&nbsp;both&nbsp;bases.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Modification&nbsp;1&nbsp;for&nbsp;Fermi-contact&nbsp;spin-spin&nbsp;coupling.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Modification&nbsp;2&nbsp;for&nbsp;Fermi-contact&nbsp;spin-spin&nbsp;coupling.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/11)
Control of two-electron integral storage format.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Regular&nbsp;integral&nbsp;format&nbsp;is&nbsp;used.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Raffenetti&nbsp;‘1’&nbsp;integral&nbsp;format&nbsp;is&nbsp;used.&nbsp;Can&nbsp;only&nbsp;be&nbsp;used&nbsp;with&nbsp;the&nbsp;closed&nbsp;shell&nbsp;SCF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Raffenetti&nbsp;‘2’&nbsp;integral&nbsp;format.&nbsp;Suitable&nbsp;for&nbsp;use&nbsp;with&nbsp;the&nbsp;open&nbsp;shell&nbsp;(UHF)&nbsp;SCF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Raffenetti&nbsp;‘3’&nbsp;integral&nbsp;format.&nbsp;Suitable&nbsp;for&nbsp;use&nbsp;with&nbsp;open&nbsp;shell&nbsp;RHF&nbsp;SCF&nbsp;and&nbsp;the&nbsp;post-SCF&nbsp;procedures,&nbsp;but&nbsp;not&nbsp;yet&nbsp;accepted&nbsp;by&nbsp;them.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;ILSW&nbsp;to&nbsp;decide&nbsp;between&nbsp;Raffenetti&nbsp;1&nbsp;and&nbsp;2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/12)
Flag for semi-empirical runs, to account for sparkles, translation vectors and d functions properly.


* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CNDO&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;INDO&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ZINDO/1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ZINDO/S&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MINDO3&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MNDO&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AM1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PM3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DFTB&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PM6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PDDG&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/13)
Nuclear center whose Fermi contact terms are to be added to the core Hamiltonian. The magnitude is specified by IOp(3/15).




### IOp(3/14)
Addition of electrostatic integrals to core Hamiltonian.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SCRF&nbsp;calculation&nbsp;—&nbsp;multiply&nbsp;moments&nbsp;by&nbsp;fudge&nbsp;factor&nbsp;for&nbsp;charged&nbsp;species.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;coefficients&nbsp;of&nbsp;field,&nbsp;starting&nbsp;with&nbsp;electric&nbsp;field,&nbsp;up&nbsp;through&nbsp;34&nbsp;elements&nbsp;(hexadecapoles)&nbsp;in&nbsp;free&nbsp;format,&nbsp;blank&nbsp;terminated.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;components&nbsp;of&nbsp;electric&nbsp;field&nbsp;only&nbsp;from&nbsp;/Gen/&nbsp;on&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;components&nbsp;of&nbsp;moments&nbsp;off&nbsp;RWF&nbsp;521&nbsp;on&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;components&nbsp;of&nbsp;electric&nbsp;field&nbsp;only&nbsp;from&nbsp;/Gen/.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;components&nbsp;of&nbsp;moments&nbsp;off&nbsp;RWF&nbsp;521.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;read&nbsp;12&nbsp;cards&nbsp;with&nbsp;x,y,z&nbsp;components&nbsp;of&nbsp;electric&nbsp;field,&nbsp;followed&nbsp;by&nbsp;xx,yy,zz,xy,xz,yz&nbsp;electric&nbsp;field&nbsp;gradient,&nbsp;xxx,&nbsp;yyy,&nbsp;zzz,&nbsp;xyy,&nbsp;xxy,&nbsp;xxz,&nbsp;xzz,&nbsp;yzz,&nbsp;yyz,&nbsp;xyz&nbsp;field&nbsp;second&nbsp;derivatives,&nbsp;and&nbsp;xxxx,&nbsp;yyyy,&nbsp;zzzz,&nbsp;xxxy,&nbsp;xxxz,&nbsp;yyyx,&nbsp;yyyz,&nbsp;zzzx,&nbsp;zzzy,&nbsp;xxyy,&nbsp;xxzz,&nbsp;yyzz,&nbsp;xxyz,&nbsp;yyxz,&nbsp;zzxy&nbsp;field&nbsp;third&nbsp;derivatives&nbsp;in&nbsp;format&nbsp;(3D20.10).&nbsp;(These&nbsp;correspond&nbsp;to&nbsp;dipole,&nbsp;quadrupole,&nbsp;octupole,&nbsp;and&nbsp;hexadecapole&nbsp;perturbations).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1-34&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Just&nbsp;component&nbsp;number&nbsp;n&nbsp;in&nbsp;the&nbsp;above&nbsp;order&nbsp;with&nbsp;magnitude&nbsp;given&nbsp;by&nbsp;IOp(3/15).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


The nuclear repulsion energy is also modified appropriately,
and the electric field is stored in Gen(2-4).




### IOp(3/15)
Magnitude of electric field.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;*&nbsp;0.0001.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/16)
Pseudopotential option


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;ECPs&nbsp;if&nbsp;defined&nbsp;with&nbsp;the&nbsp;basis&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;read&nbsp;if&nbsp;general&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;ECPs&nbsp;for&nbsp;QM&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;ECPs&nbsp;for&nbsp;EE&nbsp;charge&nbsp;centers&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;two&nbsp;input&nbsp;sections,&nbsp;for&nbsp;QM&nbsp;then&nbsp;EE&nbsp;charge&nbsp;centers.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(100).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Spin-orbit&nbsp;ECP&nbsp;coefficients&nbsp;are&nbsp;used&nbsp;as-is,&nbsp;appropriate&nbsp;for&nbsp;published&nbsp;Stuttgart&nbsp;potentials.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Spin-orbit&nbsp;ECP&nbsp;coefficients&nbsp;are&nbsp;scaled&nbsp;by&nbsp;2/(2l+1),&nbsp;appropriate&nbsp;for&nbsp;CRENBL&nbsp;potentials.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/17)
Specification of pseudo-potentials


* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;potential&nbsp;in&nbsp;old&nbsp;format.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;based&nbsp;on&nbsp;IOp(3/5).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;internally&nbsp;stored&nbsp;‘coreless&nbsp;Hartree-Fock’.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Goddard/Smedley&nbsp;SECE/SHC&nbsp;potentials.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stevens/Basch/Krauss&nbsp;CEP&nbsp;potentials.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LANL1&nbsp;potentials.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LANL2&nbsp;potentials.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6-7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Unused.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;from&nbsp;cards&nbsp;(see&nbsp;pinput&nbsp;for&nbsp;details).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dresden/Stuttgart&nbsp;potentials&nbsp;–&nbsp;SDD&nbsp;combination.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dresden/Stuttgart&nbsp;potentials&nbsp;–&nbsp;SDD&nbsp;for&nbsp;Z&nbsp;>&nbsp;18,&nbsp;D95V,&nbsp;no&nbsp;ECP&nbsp;otherwise.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dresden/Stuttgart&nbsp;potentials&nbsp;–SDF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 12&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dresden/Stuttgart&nbsp;potentials&nbsp;–SHF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 13&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dresden/Stuttgart&nbsp;potentials&nbsp;–MDF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 14&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dresden/Stuttgart&nbsp;potentials&nbsp;–&nbsp;MHF&nbsp;(first&nbsp;set).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 15&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dresden/Stuttgart&nbsp;potentials&nbsp;–&nbsp;MHF&nbsp;(second&nbsp;set).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 16&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dresden/Stuttgart&nbsp;potentials&nbsp;–&nbsp;MWB&nbsp;(first&nbsp;set).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 17&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dresden/Stuttgart&nbsp;potentials&nbsp;–&nbsp;MWB&nbsp;(second&nbsp;set).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 18&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dresden/Stuttgart&nbsp;potentials&nbsp;–&nbsp;MWB&nbsp;(third&nbsp;set).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 19&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pseudopotentials&nbsp;for&nbsp;all&nbsp;coreless&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Alternative&nbsp;potentials&nbsp;for&nbsp;coreless&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 21&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Psuedopotentials&nbsp;for&nbsp;the&nbsp;def2SV,&nbsp;def2TZV,&nbsp;and&nbsp;QZV&nbsp;basis&nbsp;sets.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/18)
Printing of pseudo-potentials


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;only&nbsp;when&nbsp;input&nbsp;is&nbsp;from&nbsp;cards&nbsp;or&nbsp;if&nbsp;GFPrint&nbsp;was&nbsp;specified.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print.&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;print.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(3/19)
Specification of substitution potential types.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;use&nbsp;any&nbsp;substitution&nbsp;potentials.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Replace&nbsp;the&nbsp;standard&nbsp;potential&nbsp;of&nbsp;this&nbsp;run&nbsp;(EG.CHF),&nbsp;with&nbsp;a&nbsp;substitution&nbsp;potential&nbsp;of&nbsp;type&nbsp;n&nbsp;wherever&nbsp;such&nbsp;substitution&nbsp;potential&nbsp;exists.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/20)
Size of buffers for integral file.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Machine&nbsp;dependant;&nbsp;16384&nbsp;integer&nbsp;words&nbsp;on&nbsp;VAX,&nbsp;55296&nbsp;words&nbsp;on&nbsp;Cray).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;integer&nbsp;words.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/21)
Size of buffers for integral derivative file. No longer used.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(3200&nbsp;integer&nbsp;words).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;integer&nbsp;words.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/22)
`L312`: Control of the pre-cutoff in the two-electron d-integral program.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;pre-cutoff.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pre-cutoffs&nbsp;designed&nbsp;for&nbsp;the&nbsp;6-31G*&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/23)
Disable use of certain basis functions.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;all&nbsp;basis&nbsp;functions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;a&nbsp;list&nbsp;of&nbsp;basis&nbsp;function&nbsp;numbers&nbsp;in&nbsp;Format&nbsp;(10I5),&nbsp;terminated&nbsp;by&nbsp;a&nbsp;blank&nbsp;line,&nbsp;and&nbsp;set&nbsp;their&nbsp;diagonal&nbsp;core&nbsp;Hamiltonian&nbsp;elements&nbsp;to&nbsp;+100.0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/24)
Printing of Gaussian function table.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(don’t&nbsp;print).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;old-fashioned&nbsp;table.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;as&nbsp;GenBas&nbsp;input.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;in&nbsp;more&nbsp;readable&nbsp;format.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;shell&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;AO&nbsp;basis&nbsp;using&nbsp;default&nbsp;primitive&nbsp;normalization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;AO&nbsp;basis&nbsp;using&nbsp;coefficients&nbsp;of&nbsp;raw&nbsp;primitives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;AO&nbsp;basis&nbsp;using&nbsp;coefficients&nbsp;of&nbsp;AO&nbsp;normalized&nbsp;primitives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;AO&nbsp;basis&nbsp;using&nbsp;coefficients&nbsp;of&nbsp;J&nbsp;normalized&nbsp;primitives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000000&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;density&nbsp;basis&nbsp;using&nbsp;default&nbsp;primitive&nbsp;normalization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;density&nbsp;using&nbsp;coefficients&nbsp;of&nbsp;raw&nbsp;primitives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200000&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;density&nbsp;using&nbsp;coefficients&nbsp;of&nbsp;AO&nbsp;normalized&nbsp;primitives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 300000&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;density&nbsp;using&nbsp;coefficients&nbsp;of&nbsp;J&nbsp;normalized&nbsp;primitives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/25)
Number of last two electron integral links.


* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;integrals&nbsp;from&nbsp;a&nbsp;previous&nbsp;job&nbsp;read&nbsp;/IBF/&nbsp;from&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We&nbsp;are&nbsp;re-using&nbsp;integrals&nbsp;produced&nbsp;earlier&nbsp;in&nbsp;the&nbsp;current&nbsp;calculation;&nbsp;use&nbsp;the&nbsp;/IBF/&nbsp;already&nbsp;on&nbsp;the&nbsp;RWF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We&nbsp;are&nbsp;not&nbsp;using&nbsp;two-electron&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Direct&nbsp;SCF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* >0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;number.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/26)
Accuracy option.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;Integrals&nbsp;are&nbsp;computed&nbsp;to&nbsp;10^-10&nbsp;accuracy.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Test.&nbsp;Do&nbsp;all&nbsp;integrals&nbsp;as&nbsp;well&nbsp;as&nbsp;possible&nbsp;in&nbsp;L311.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;STO-3G.&nbsp;Use&nbsp;old&nbsp;very&nbsp;inaccurate&nbsp;cutoffs&nbsp;in&nbsp;link&nbsp;311.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Test.&nbsp;Do&nbsp;all&nbsp;integrals&nbsp;as&nbsp;well&nbsp;as&nbsp;possible&nbsp;in&nbsp;L314.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sleazy.&nbsp;Use&nbsp;looser&nbsp;cutoffs&nbsp;in&nbsp;L314.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/27)
Computing and storing of small two-electron integrals.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Discard&nbsp;integrals&nbsp;with&nbsp;magnitude&nbsp;less&nbsp;than&nbsp;10^-12.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Discard&nbsp;integrals&nbsp;with&nbsp;magnitude&nbsp;less&nbsp;than&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(3/28)
Special SP code control.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;use&nbsp;IsAlg.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All&nbsp;integrals&nbsp;with&nbsp;d’s&nbsp;—&nbsp;L311&nbsp;does&nbsp;nothing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SP&nbsp;integrals&nbsp;in&nbsp;link&nbsp;311,&nbsp;d&nbsp;and&nbsp;higher&nbsp;elsewhere.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All&nbsp;integrals&nbsp;done&nbsp;in&nbsp;L314&nbsp;using&nbsp;Prism.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/29)
`L302`: Accuracy.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10^-13).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/30)
Control of two-electron integral symmetry.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Two-electron&nbsp;integral&nbsp;symmetry&nbsp;is&nbsp;turned&nbsp;off.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Two-electron&nbsp;integral&nbsp;symmetry&nbsp;is&nbsp;turned&nbsp;on.&nbsp;Note,&nbsp;however,&nbsp;the&nbsp;SET2E&nbsp;will&nbsp;interrogate&nbsp;ILSW&nbsp;to&nbsp;see&nbsp;if&nbsp;the&nbsp;symmetry&nbsp;RW-files&nbsp;exist.&nbsp;If&nbsp;they&nbsp;don’t,&nbsp;symmetry&nbsp;has&nbsp;been&nbsp;turned&nbsp;off&nbsp;elsewhere,&nbsp;and&nbsp;SET2E&nbsp;will&nbsp;also&nbsp;turn&nbsp;it&nbsp;off&nbsp;here.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/31)
Use of symmetry in computing gradient (Obsolete).




### IOp(3/32)
Whether to check the eigenvalues of the overlap matrix.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(205).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;and&nbsp;reduce&nbsp;expansion&nbsp;space&nbsp;if&nbsp;linear&nbsp;dependence&nbsp;is&nbsp;found&nbsp;(NYI).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;and&nbsp;use&nbsp;Schmidt&nbsp;orthogonalization&nbsp;to&nbsp;reduce&nbsp;expansion&nbsp;space.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;using&nbsp;SVD&nbsp;to&nbsp;reduce&nbsp;expansion&nbsp;space.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;up&nbsp;SAOs&nbsp;as&nbsp;with&nbsp;5&nbsp;but&nbsp;using&nbsp;diagonalization&nbsp;instead&nbsp;of&nbsp;SVD.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;up&nbsp;a&nbsp;unit&nbsp;matrix&nbsp;for&nbsp;the&nbsp;transformation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Try&nbsp;to&nbsp;make&nbsp;the&nbsp;new&nbsp;set&nbsp;of&nbsp;vectors&nbsp;as&nbsp;much&nbsp;like&nbsp;the&nbsp;previous&nbsp;set,&nbsp;if&nbsp;any.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;SVD&nbsp;ignoring&nbsp;the&nbsp;previous&nbsp;orthonormal&nbsp;set,&nbsp;if&nbsp;any.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;schmidt&nbsp;orthogonalized&nbsp;to&nbsp;match&nbsp;to&nbsp;previous&nbsp;o.n.&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;symmetric&nbsp;orthogonalization&nbsp;with&nbsp;Jacobi&nbsp;diagonalization&nbsp;to&nbsp;match&nbsp;to&nbsp;previous&nbsp;o.n.&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check&nbsp;orthonormality&nbsp;of&nbsp;generated&nbsp;set&nbsp;in&nbsp;RAOMat.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;check&nbsp;orthonormality&nbsp;of&nbsp;generated&nbsp;set&nbsp;in&nbsp;RAOMat.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/33)
Integral package printing.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;integrals&nbsp;are&nbsp;printed.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;one-electron&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;two-electron&nbsp;integrals&nbsp;in&nbsp;standard&nbsp;format.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;two-electron&nbsp;integrals&nbsp;in&nbsp;debug&nbsp;format.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Combination&nbsp;of&nbsp;1&nbsp;and&nbsp;3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Combination&nbsp;of&nbsp;1&nbsp;and&nbsp;4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/34)
Dump option.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;dump.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Control&nbsp;words&nbsp;printed&nbsp;(as&nbsp;usual).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Additionally,&nbsp;Common/B/&nbsp;is&nbsp;dumped&nbsp;at&nbsp;the&nbsp;beginning&nbsp;of&nbsp;each&nbsp;integral&nbsp;link.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Additionally,&nbsp;the&nbsp;integrals&nbsp;are&nbsp;printed&nbsp;(standard&nbsp;format).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/36)
`L303, L308`: Matrices to compute.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(dipole).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dipole.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Quadrupole.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Octupole.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hexadecapole.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;20).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;compute&nbsp;absolute&nbsp;overlaps.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;absolute&nbsp;overlap&nbsp;over&nbsp;contracted&nbsp;functions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;absolute&nbsp;overlap&nbsp;over&nbsp;both&nbsp;contracted&nbsp;and&nbsp;over&nbsp;primitive&nbsp;functions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;same&nbsp;as&nbsp;100.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;L308&nbsp;should&nbsp;compute&nbsp;(del&nbsp;r&nbsp;+&nbsp;r&nbsp;del)&nbsp;in&nbsp;addition&nbsp;to&nbsp;Del&nbsp;and&nbsp;r&nbsp;x&nbsp;Del.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;L308&nbsp;should&nbsp;just&nbsp;Del&nbsp;and&nbsp;r&nbsp;x&nbsp;Del.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/37)
`L320`: Whether to sort integrals.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;no&nbsp;longer&nbsp;functional.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/38)
Algorithm for 1e integrals.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;in&nbsp;302,&nbsp;same&nbsp;as&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Prism.&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rys.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;in&nbsp;308,&nbsp;same&nbsp;as&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Prism.&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Explicit&nbsp;spdf&nbsp;code.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/39)
Initialization of force and force constant RWFs.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initialize.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Leave&nbsp;alone.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/41)
Various semi-empirical methods.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;NDDO&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NDDO&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;use&nbsp;of&nbsp;NDDO&nbsp;beta&nbsp;parameters&nbsp;(arithmetic&nbsp;mean&nbsp;for&nbsp;indo&nbsp;parameters,&nbsp;geometric&nbsp;mean&nbsp;for&nbsp;NDDO/1&nbsp;or&nbsp;read-in&nbsp;parameters).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Arithmetic&nbsp;mean&nbsp;in&nbsp;NDDO.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Geometric&nbsp;mean&nbsp;in&nbsp;NDDO.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;parameters&nbsp;(same&nbsp;as&nbsp;5).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;parameters&nbsp;for&nbsp;atomic&nbsp;numbers&nbsp;1-18&nbsp;in&nbsp;the&nbsp;order:&nbsp;Scale&nbsp;(D20.12),&nbsp;followed&nbsp;by&nbsp;((HDiag(J,I),J=1,3),I=1,18)&nbsp;(Format&nbsp;3D20.12),&nbsp;followed&nbsp;by&nbsp;((Beta(J,I),J=1,3),I=1,18)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;parameters&nbsp;from&nbsp;rwf.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;parameters&nbsp;from&nbsp;chk.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 400&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Original&nbsp;INDO/2&nbsp;Beta&nbsp;and&nbsp;HDiag&nbsp;Parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 500&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GNDDO/1&nbsp;parametrization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;STO-3G&nbsp;scale&nbsp;factors.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Slater’s&nbsp;rules&nbsp;scale&nbsp;factors.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(unit&nbsp;overlap&nbsp;matrix).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;unit&nbsp;matrix&nbsp;for&nbsp;the&nbsp;overlap.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;real&nbsp;overlap&nbsp;matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;CNDO/2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200000&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;INDO/2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 300000&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;ZINDO/1&nbsp;(NYI).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 400000&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;ZINDO/S.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 500000&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;MINDO/3&nbsp;(NYI).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 600000&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;MNDO.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 700000&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;AM1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 800000&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;PM3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 900000&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;PM3MM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;Harris&nbsp;functionaL&nbsp;through&nbsp;L511.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1100000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;Harris&nbsp;functional&nbsp;scaling&nbsp;atomic&nbsp;densities&nbsp;for&nbsp;current&nbsp;charge&nbsp;and&nbsp;multiplicity.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1200000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Harris&nbsp;XC&nbsp;but&nbsp;regular&nbsp;Coulomb&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1300000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Harris&nbsp;(XC&nbsp;and&nbsp;atomic&nbsp;densities)&nbsp;through&nbsp;regular&nbsp;code.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1400000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Regular&nbsp;SCF&nbsp;with&nbsp;separate&nbsp;K,&nbsp;for&nbsp;testing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1500000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;J&nbsp;as&nbsp;usual&nbsp;but&nbsp;NDDO&nbsp;for&nbsp;K.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1600000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Used&nbsp;internally&nbsp;as&nbsp;part&nbsp;of&nbsp;15.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1700000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DFT-SCTB&nbsp;with&nbsp;tabulated&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1800000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DFT-SCTB&nbsp;with&nbsp;analytic&nbsp;expressions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1900000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EHT-SC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;2e&nbsp;terms&nbsp;to&nbsp;zero.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2100000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Harris&nbsp;XC&nbsp;and&nbsp;DFTB-style&nbsp;charge&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2200000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Harris&nbsp;XC&nbsp;and&nbsp;improved&nbsp;DFTB-style&nbsp;charge&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2300000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PM6PFD&nbsp;with&nbsp;overlap.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2400000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PM6PFD&nbsp;with&nbsp;overlap&nbsp;and&nbsp;Harris&nbsp;XC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2500000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PM6PFD&nbsp;with&nbsp;overlap&nbsp;and&nbsp;approximate&nbsp;XC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2600000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NDDO&nbsp;with&nbsp;Mayer&nbsp;Bond&nbsp;Order&nbsp;correlation&nbsp;corrections.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 27-38&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Prefix&nbsp;reserved&nbsp;for&nbsp;other&nbsp;methods&nbsp;with&nbsp;2e&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3900000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PM6.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PMDDG.&nbsp;&nbsp;&nbsp;&nbsp;
* 41&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PM6E.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 42&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PM7.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 43&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PM6&nbsp;with&nbsp;T&nbsp;transformed&nbsp;to&nbsp;OAO.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 44&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PM7TS.&nbsp;&nbsp;&nbsp;&nbsp;
* 45&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PM7MOPAC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 46-98&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Prefix&nbsp;assumed&nbsp;to&nbsp;be&nbsp;ZDO&nbsp;methods.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9900000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;External&nbsp;program&nbsp;&nbsp;&nbsp;&nbsp;
* 100-&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Prefix&nbsp;assumed&nbsp;to&nbsp;be&nbsp;MM&nbsp;methods.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/42)
`L317`: How to form NDDO core hamiltonian.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;the&nbsp;integrals&nbsp;sequentially.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Load&nbsp;all&nbsp;the&nbsp;integrals&nbsp;into&nbsp;memory.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/43)
Handling of background charge distribution.


* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;11.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Consider&nbsp;external&nbsp;charges.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;consider&nbsp;external&nbsp;charges.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Consider&nbsp;self-consistent&nbsp;solvent&nbsp;charges.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;consider&nbsp;self-consistent&nbsp;solvent&nbsp;charges.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/44)
`L318`: Using Integral rejection.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Keep&nbsp;all&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neglect&nbsp;four&nbsp;center&nbsp;transformed&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neglect&nbsp;four&nbsp;center&nbsp;and&nbsp;3&nbsp;center&nbsp;(ab|ac)&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neglect&nbsp;four&nbsp;center&nbsp;and&nbsp;three&nbsp;center&nbsp;(0,0)&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NDDO&nbsp;approximation&nbsp;—&nbsp;no&nbsp;(ab|xx)&nbsp;and&nbsp;no&nbsp;<a|X|b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NDDO&nbsp;on&nbsp;2e&nbsp;and&nbsp;V&nbsp;ints&nbsp;only&nbsp;—&nbsp;T&nbsp;and&nbsp;S&nbsp;unchanged.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;transform&nbsp;2e&nbsp;integrals,&nbsp;only&nbsp;1e.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/45)
`L318`: Transformation matrix.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;S^-1/2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Just&nbsp;orthogonalize&nbsp;functions&nbsp;on&nbsp;the&nbsp;same&nbsp;center.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;unit&nbsp;matrix&nbsp;(for&nbsp;debugging).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


Order of multipoles in SCRF for L303.




### IOp(3/46)
Whether to abort the job if badbas detects an error.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(yes).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/47)
Flags for use in Prism and CalDFT throughout the program.


* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;use&nbsp;of&nbsp;only&nbsp;the&nbsp;MD&nbsp;paths&nbsp;for&nbsp;all&nbsp;calculations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;use&nbsp;of&nbsp;only&nbsp;the&nbsp;OS&nbsp;path&nbsp;for&nbsp;all&nbsp;calculations.&nbsp;Bit&nbsp;flags.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If&nbsp;bit&nbsp;0&nbsp;is&nbsp;set&nbsp;(use&nbsp;AllowP&nbsp;array)&nbsp;then&nbsp;read&nbsp;in&nbsp;a&nbsp;list&nbsp;of&nbsp;allowed&nbsp;paths.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;expanded&nbsp;matrix&nbsp;logic&nbsp;for&nbsp;PBC&nbsp;exact&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reverse&nbsp;choice&nbsp;of&nbsp;whether&nbsp;to&nbsp;precompute&nbsp;distance&nbsp;matrix&nbsp;during&nbsp;numerical&nbsp;quadrature.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Skip&nbsp;consistency&nbsp;checks&nbsp;for&nbsp;XC&nbsp;quadrature.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;do&nbsp;extra&nbsp;work&nbsp;to&nbsp;use&nbsp;cutoffs&nbsp;better,&nbsp;currently&nbsp;only&nbsp;affects&nbsp;CalDFT.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reverse&nbsp;normal&nbsp;choice&nbsp;of&nbsp;diagonal/canonical&nbsp;sampling&nbsp;in&nbsp;Prism&nbsp;and&nbsp;PrmRaf.&nbsp;The&nbsp;default&nbsp;is&nbsp;diagonal&nbsp;only&nbsp;on&nbsp;vector&nbsp;machines.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Trace&nbsp;input&nbsp;and&nbsp;output&nbsp;using&nbsp;Linda/subprocess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;single&nbsp;matrix&nbsp;code&nbsp;in&nbsp;CPKS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;all&nbsp;near&nbsp;field&nbsp;in&nbsp;FMM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;dynamic&nbsp;allocation&nbsp;of&nbsp;parallel&nbsp;work&nbsp;in&nbsp;CalDSu,&nbsp;CoulSu,&nbsp;and&nbsp;FMMEnt.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;square&nbsp;loops,&nbsp;currently&nbsp;only&nbsp;in&nbsp;PrismC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;dynamic&nbsp;work&nbsp;allocation&nbsp;among&nbsp;Linda&nbsp;workers.&nbsp;(Currently&nbsp;turned&nbsp;off&nbsp;anyway).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 12&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reverse&nbsp;normal&nbsp;choice&nbsp;of&nbsp;Scat20&nbsp;vs.&nbsp;replicated&nbsp;Fock&nbsp;matrices.&nbsp;Default&nbsp;is&nbsp;to&nbsp;use&nbsp;replicated&nbsp;matrices&nbsp;only&nbsp;on&nbsp;Fujitsu&nbsp;and&nbsp;NEC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 13&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;on&nbsp;Schwartz&nbsp;screening&nbsp;only&nbsp;in&nbsp;FoFCou,&nbsp;turning&nbsp;&nbsp;off&nbsp;heuristic&nbsp;screening.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 14&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;separate&nbsp;evaluation&nbsp;of&nbsp;J&nbsp;and&nbsp;K&nbsp;terms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 15&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Forbid&nbsp;use&nbsp;of&nbsp;gather/scatter&nbsp;digestion&nbsp;even&nbsp;for&nbsp;small&nbsp;numbers&nbsp;of&nbsp;density&nbsp;matrices.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 16&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Insist&nbsp;on&nbsp;gather/scatter&nbsp;digestion&nbsp;even&nbsp;for&nbsp;large&nbsp;numbers&nbsp;of&nbsp;matrices.&nbsp;Does&nbsp;not&nbsp;affect&nbsp;FoFRaf,&nbsp;which&nbsp;only&nbsp;does&nbsp;inner&nbsp;loops&nbsp;over&nbsp;matrices.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 17&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Forbid&nbsp;use&nbsp;of&nbsp;Schwartz&nbsp;screening&nbsp;in&nbsp;FoFCou.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 18&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;compute&nbsp;on&nbsp;Linda&nbsp;master.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 19&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;nuclear&nbsp;contribution&nbsp;in&nbsp;FoFCou&nbsp;even&nbsp;for&nbsp;non-PBC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;use&nbsp;special&nbsp;Coulomb&nbsp;algorithm&nbsp;in&nbsp;FoFCou.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 21&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;dynamic&nbsp;parallel&nbsp;work&nbsp;logic&nbsp;even&nbsp;for&nbsp;single&nbsp;processor&nbsp;tasks.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 22&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;use&nbsp;of&nbsp;Sqrt(P)&nbsp;in&nbsp;density-based&nbsp;cutoffs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 23&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;tabulated&nbsp;numerical&nbsp;values&nbsp;for&nbsp;atomic&nbsp;densities&nbsp;instead&nbsp;of&nbsp;Gaussian&nbsp;expansions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 24&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;allocation&nbsp;for&nbsp;parallel&nbsp;2e&nbsp;integrals&nbsp;but&nbsp;run&nbsp;sequentially.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 25&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do
allocation&nbsp;for&nbsp;parallel&nbsp;XC&nbsp;but&nbsp;run&nbsp;sequentially.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 26&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Make&nbsp;all&nbsp;atoms&nbsp;large&nbsp;in&nbsp;XC&nbsp;quadrature.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 27&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Make&nbsp;all&nbsp;shells&nbsp;large&nbsp;in&nbsp;XC&nbsp;quadrature.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 28&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;symmetry&nbsp;reduce&nbsp;grid&nbsp;points&nbsp;on&nbsp;unique&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 29&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;on&nbsp;use&nbsp;of&nbsp;pre-computed&nbsp;XC&nbsp;weights.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Make&nbsp;Linda&nbsp;workers&nbsp;run&nbsp;sequentially.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 31&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reserved&nbsp;for&nbsp;flag&nbsp;for&nbsp;calls&nbsp;to&nbsp;OneElI,&nbsp;etc.&nbsp;in&nbsp;parallel&nbsp;regions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/48)
Options for FMM.


RRLLNNTTWW


* RR:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Range&nbsp;(default&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* LL:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LMax&nbsp;(default&nbsp;from&nbsp;tolerance).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NN:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number&nbsp;of&nbsp;levels&nbsp;(default&nbsp;8).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* TT:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tolerance&nbsp;(default&nbsp;18).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* WW:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IWS&nbsp;(default&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/49)
More bitwise options for FMM and 2e integrals. The bits are:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Indicates&nbsp;whether&nbsp;FMM&nbsp;can&nbsp;be&nbsp;used&nbsp;by&nbsp;FoFCou.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Uncontract&nbsp;all&nbsp;shell&nbsp;pairs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Apply&nbsp;symmetry&nbsp;to&nbsp;derivative&nbsp;distributions&nbsp;(NYI).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;save&nbsp;as&nbsp;many&nbsp;multipole&nbsp;expansions&nbsp;as&nbsp;possible&nbsp;in&nbsp;memory.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;on&nbsp;FMM&nbsp;print.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Convert
to&nbsp;sparse&nbsp;storage&nbsp;under&nbsp;FoFCou&nbsp;for&nbsp;testing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Split&nbsp;primitives&nbsp;for&nbsp;better&nbsp;boxification.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;UseUAB/Use&nbsp;256.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UseUAB,&nbsp;if&nbsp;128&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;parallelism&nbsp;in&nbsp;FMM&nbsp;(does&nbsp;not&nbsp;use&nbsp;parallel&nbsp;logic).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;up&nbsp;for&nbsp;parallel&nbsp;FMM&nbsp;but&nbsp;run&nbsp;loops&nbsp;sequentially.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;default&nbsp;to&nbsp;FMM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 12&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;FMM&nbsp;on.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 13&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;by&nbsp;PsmSet&nbsp;to&nbsp;indicate&nbsp;whether&nbsp;the&nbsp;NAtoms&nbsp;test&nbsp;for&nbsp;defaulting&nbsp;FMM&nbsp;was&nbsp;passed.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 14&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;on&nbsp;parallelism&nbsp;in&nbsp;FMM&nbsp;during&nbsp;CPHF.&nbsp;Default&nbsp;is&nbsp;off.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 15&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;use&nbsp;of&nbsp;old&nbsp;box-box&nbsp;screening.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 16&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;Include&nbsp;1/R&nbsp;or&nbsp;Erf(R)/R&nbsp;in&nbsp;box-box&nbsp;screening.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 17&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;use&nbsp;of&nbsp;non-cubic&nbsp;logic.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 18&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;box-box&nbsp;screening.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 19&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Skip&nbsp;FF&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20–22&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pure&nbsp;functional&nbsp;control:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0  Default,&nbsp;same&nbsp;as&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1  Convert&nbsp;densities,&nbsp;etc.&nbsp;to&nbsp;Cartesian.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2  Transform&nbsp;2e&nbsp;integrals&nbsp;to&nbsp;pure&nbsp;before&nbsp;digestion.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3  Generate&nbsp;2e&nbsp;integrals&nbsp;over&nbsp;real&nbsp;spherical&nbsp;harmonics.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4  Generate&nbsp;2e&nbsp;integrals&nbsp;over&nbsp;complex&nbsp;spherical&nbsp;harmonics.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5  Generate&nbsp;2e&nbsp;integrals&nbsp;over&nbsp;spinors.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6  Generate&nbsp;2e&nbsp;integrals&nbsp;over&nbsp;large&nbsp;and&nbsp;small&nbsp;components.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/51)
Parameters for FMM box length (MMMMMNNNN):


* MMMMM&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Box&nbsp;length&nbsp;when&nbsp;doing&nbsp;Coulomb&nbsp;will&nbsp;be&nbsp;MMMMM/1000&nbsp;Bohr.&nbsp;The&nbsp;default&nbsp;is&nbsp;2.5&nbsp;Bohr.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Box&nbsp;length&nbsp;when&nbsp;doing&nbsp;Exchange&nbsp;will&nbsp;be&nbsp;NNNN/1000&nbsp;Bohr.&nbsp;The&nbsp;default&nbsp;is&nbsp;0.75&nbsp;Bohr.&nbsp;If&nbsp;doing&nbsp;both&nbsp;Coulomb&nbsp;and&nbsp;exchange&nbsp;at&nbsp;the&nbsp;same&nbsp;time,&nbsp;the&nbsp;max.&nbsp;of&nbsp;the&nbsp;two&nbsp;values&nbsp;is&nbsp;used.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(3/52)
Turn off normal evaluation of ECP integrals.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;if&nbsp;needed,&nbsp;ECP&nbsp;integrals&nbsp;are&nbsp;evaluated&nbsp;in&nbsp;L302.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Old&nbsp;routines&nbsp;will&nbsp;be&nbsp;used,&nbsp;so&nbsp;L302&nbsp;does&nbsp;not&nbsp;do&nbsp;ECP&nbsp;ints.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/53)
Accuracy in ECP integral evaluation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;Cutoffs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/55)
Use of sparse storage.


* -100&nbsp;<&nbsp;N<&nbsp;-4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Cutoff&nbsp;10^(N+5)&nbsp;for&nbsp;testing&nbsp;new&nbsp;code.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reserved&nbsp;(used&nbsp;for&nbsp;nosparse&nbsp;in&nbsp;parsing).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;intermediate&nbsp;accuracy&nbsp;(10^-6).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;crude&nbsp;accuracy&nbsp;(10^-6).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;default&nbsp;accuracy&nbsp;(10^-8).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;cutoff&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/56)
Cutoff for intermediate matrices during sparse operations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100&nbsp;times&nbsp;smaller&nbsp;than&nbsp;storage&nbsp;cutoff.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/57)
Number of core electrons for Stuttgart/Dresden ECP’s.




### IOp(3/58)
Cholesky control options.




### IOp(3/59)
Threshold for throwing away eigenvectors of S.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10^-6).&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/60)
Control of orthogonalization and simplification of generalized contraction basis sets.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;orthogonalization&nbsp;and&nbsp;simplification.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Orthogonalize&nbsp;and&nbsp;remove&nbsp;primitives&nbsp;with&nbsp;0&nbsp;coefficients&nbsp;(exact&nbsp;transformation).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Orthogonalize&nbsp;and&nbsp;remove&nbsp;primitives&nbsp;with&nbsp;0&nbsp;or&nbsp;small&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Orthogonalize&nbsp;and&nbsp;remove&nbsp;primitives&nbsp;with&nbsp;coefficients&nbsp;less&nbsp;than&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/61)
`L302`: Sparse semi-empirical Hamiltonian cutoffs.


* XX&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F(Mu,Lambda)&nbsp;atom–atom&nbsp;cutoff&nbsp;criterion&nbsp;(angstroms)&nbsp;Mu,&nbsp;Lambda&nbsp;are&nbsp;basis&nbsp;functions&nbsp;on&nbsp;different&nbsp;atoms.&nbsp;(defaults&nbsp;to&nbsp;15&nbsp;angstroms).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* XX00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F(Mu,Nu)&nbsp;atom–atom&nbsp;cutoff&nbsp;criterion&nbsp;(angstroms)&nbsp;Mu,&nbsp;Nu&nbsp;are&nbsp;basis&nbsp;functions&nbsp;on&nbsp;the&nbsp;same&nbsp;atom.&nbsp;(defaults&nbsp;to&nbsp;no&nbsp;F(Mu,Nu)&nbsp;cutoff).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/62)
Maximum allowed error in S over orthogonalized basis functions.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10^-9.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/63)
Debug option to test point charge FMM.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;read&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Also&nbsp;do&nbsp;forces.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(3/64)
Set value for ILSW derivative flag. Only active if IOp(3/39)=0.


* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;to&nbsp;zero.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;to&nbsp;-1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Leave&nbsp;alone.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;to&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/65)
Number of k-points.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Just&nbsp;Gamma&nbsp;point.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;About&nbsp;N&nbsp;points.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Old&nbsp;logic&nbsp;for&nbsp;NRecip=N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/66)
Override setting of NThInc in lineary dependence cutoff.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;change.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;to&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/67)
Electric-field dependent functions.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(on&nbsp;if&nbsp;already&nbsp;present&nbsp;in&nbsp;basis&nbsp;read&nbsp;from&nbsp;RWF&nbsp;or&nbsp;checkpoint,&nbsp;otherwise&nbsp;off).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;with&nbsp;standard&nbsp;values.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;with&nbsp;read-in&nbsp;values.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/70)
SCRF flag.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;defaults.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;setting&nbsp;from&nbsp;checkpoint.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;setting&nbsp;from&nbsp;the&nbsp;input&nbsp;stream.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;setting&nbsp;from&nbsp;checkpoint&nbsp;and&nbsp;modify&nbsp;them&nbsp;by&nbsp;reading&nbsp;from&nbsp;the&nbsp;input&nbsp;stream.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;from&nbsp;RWF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Flag&nbsp;for&nbsp;macro-iterations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SCI-PCM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;D-PCM.&nbsp;&nbsp;&nbsp;&nbsp;
* 2100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C-PCM.&nbsp;&nbsp;&nbsp;&nbsp;
* 2200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IEF-PCM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IVC-PCM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Onsager.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate
COSMOTHERMO&nbsp;output.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;COSMO&nbsp;style&nbsp;CPCM:&nbsp;Klamt&nbsp;radii,&nbsp;iterative&nbsp;(implies&nbsp;g03defaults)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;SMD&nbsp;parametrization&nbsp;of&nbsp;non-electrostatic&nbsp;terms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* x00000&nbsp;&nbsp;&nbsp;&nbsp;Flag&nbsp;for&nbsp;PCM&nbsp;family&nbsp;options:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;=&nbsp;include&nbsp;cavity-field&nbsp;effects.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;=&nbsp;setting&nbsp;for&nbsp;accurate&nbsp;DeltaG&nbsp;of&nbsp;salvation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3&nbsp;=&nbsp;setting&nbsp;to&nbsp;reproduce&nbsp;G03&nbsp;behavior.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Flag&nbsp;to&nbsp;skip&nbsp;PCMInp&nbsp;as&nbsp;L124&nbsp;already&nbsp;did&nbsp;it&nbsp;or&nbsp;we’re&nbsp;doing&nbsp;flavor&nbsp;X&nbsp;of&nbsp;ONIOM-PCM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Write&nbsp;the&nbsp;PCM&nbsp;charges&nbsp;on&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;the&nbsp;PCM&nbsp;charges&nbsp;from&nbsp;the&nbsp;checkpoint.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;and&nbsp;write&nbsp;the&nbsp;PCM&nbsp;charges&nbsp;from&nbsp;and&nbsp;to&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Write&nbsp;the&nbsp;non-equilibrium&nbsp;PCM&nbsp;charges&nbsp;on&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;the&nbsp;non-equilibrium&nbsp;PCM&nbsp;charges&nbsp;from&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Write&nbsp;the&nbsp;CC&nbsp;non-equilibrium&nbsp;PCM&nbsp;charges&nbsp;on&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;the&nbsp;CC&nbsp;non-equilibrium&nbsp;PCM&nbsp;charges&nbsp;from&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Write&nbsp;the&nbsp;cLR&nbsp;non-equilibrium&nbsp;PCM&nbsp;charges&nbsp;on&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;same&nbsp;as&nbsp;30000000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;the&nbsp;PCM&nbsp;electrostatic&nbsp;cavity.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;the&nbsp;PCM&nbsp;non-electrostatic&nbsp;cavity.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;both&nbsp;the&nbsp;PCM&nbsp;electrostatic&nbsp;and&nbsp;non-electrostatic&nbsp;cavities.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;neither&nbsp;the&nbsp;PCM&nbsp;electrostatic&nbsp;nor&nbsp;non-electrostatic&nbsp;cavities.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/71)
IDeriv level flag (for SCRF setup): 0, 1, 2 for none, 1^st or 2^nd nuclear coordinate derivatives.




### IOp(3/72)
Solvent type flag (for SCRF setup).




### IOp(3/73)
Old ONIOM-PCM flag (currently unused).




### IOp(3/74)
Type of exchange and correlation potentials.


* -79&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PBE-QIDH.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -78&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PBE0-DH.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -77&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DSD-PBEP86&nbsp;(double&nbsp;hybrid,&nbsp;DFT-D3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -76&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PW6B95-D3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -75&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PW6B95.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -74&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M08-HX.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -73&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MN15.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -72&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MN15-L.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -71&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LC-wHPBE.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -70&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MN12-SX.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -69&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N12-SX.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -68&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MN12-L.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -67&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N12.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -66&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M11L.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -65&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SOGGA11X.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -64&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M11.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -63&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SOGGA11.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -62&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HISSaPBE.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -61&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HISSbPBE.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -60&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B2PLYP-D3&nbsp;(double&nbsp;hybrid,&nbsp;DFT-D3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -59&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B97-D&nbsp;(DFT-D3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -58&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wB97X-D.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -57&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wB97X.&nbsp;&nbsp;&nbsp;&nbsp;
* -56&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wB97.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -55&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M06-2X.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -54&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M06.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -53&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M06-L.&nbsp;&nbsp;&nbsp;&nbsp;
* -52&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M06-HF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -51&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HSEH1PBE.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -50&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mPW2PLYP-D&nbsp;(double&nbsp;hybrid).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -49&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B2PLYP-D&nbsp;(double&nbsp;hybrid).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -48&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mPW2PLYP&nbsp;(double&nbsp;hybrid).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -47&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B2PLYP&nbsp;(double&nbsp;hybrid).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -46&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PAPF-D.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -45&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PAPF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -44&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;APF-D.&nbsp;&nbsp;&nbsp;&nbsp;
* -43&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;APF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -42&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B97-D.&nbsp;&nbsp;&nbsp;&nbsp;
* -41&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LC-wPBE.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -40&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CAM-B3LYP.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -39&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OAPF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -38&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M052X.&nbsp;&nbsp;&nbsp;&nbsp;
* -37&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M05.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -36&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HSE1PBE.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -35&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TPSSh.&nbsp;&nbsp;&nbsp;&nbsp;
* -34&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BMK.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -33&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;X3LYP.&nbsp;&nbsp;&nbsp;&nbsp;
* -32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t-HCTH&nbsp;hybrid.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -31&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t-HCTH.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OmPW3PBE.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -29&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OmPW1PBE.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -28&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OmPW1LYP.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -27&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OmPW1PW91.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -26&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PBEH1PBE.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -25&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HSE2PBE.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -24&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O3LYP.&nbsp;&nbsp;&nbsp;&nbsp;
* -23&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HCTH407.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -22&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HCTH147.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -21&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B97-2.&nbsp;&nbsp;&nbsp;&nbsp;
* -20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B97-1.&nbsp;&nbsp;&nbsp;&nbsp;
* -19&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HCTH93.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -18&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B98.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -17&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B1B95.&nbsp;&nbsp;&nbsp;&nbsp;
* -16&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BA3PBE.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -15&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BA1PBE.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -14&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PBE3PBE.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -13&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PBE1PBE.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -12&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mPW3PBE.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mPW1PBE.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mPW1LYP.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LG1LYP.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B1LYP.&nbsp;&nbsp;&nbsp;&nbsp;
* -7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mPW91PW91.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Becke3&nbsp;with&nbsp;Perdew&nbsp;91&nbsp;correlation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Becke3&nbsp;using&nbsp;VWN/LYP&nbsp;for&nbsp;correlation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Becke3&nbsp;with&nbsp;Perdew&nbsp;86&nbsp;correlation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Becke&nbsp;"Half&nbsp;and&nbsp;Half"&nbsp;with&nbsp;LYP/VWN&nbsp;correlation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Becke&nbsp;"Half&nbsp;and&nbsp;Half":&nbsp;0.5&nbsp;HF&nbsp;+&nbsp;0.5&nbsp;LSD.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;only&nbsp;Coulomb&nbsp;part;&nbsp;skip&nbsp;exchange-correlation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;same&nbsp;as&nbsp;100.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 01&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Vosko-Wilk-Nusair&nbsp;method&nbsp;5&nbsp;correlation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 02&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Lee-Yang-Parr&nbsp;correlation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 03&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Perdew&nbsp;81&nbsp;correlation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 04&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Perdew&nbsp;81&nbsp;+&nbsp;Perdew&nbsp;86&nbsp;correlation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 05&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VWN&nbsp;80&nbsp;(LSD)&nbsp;correlation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 06&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VWN&nbsp;80&nbsp;(LSD)&nbsp;+&nbsp;Perdew&nbsp;86&nbsp;correlation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 07&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[unused]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 08&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PW91.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 09&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PBE.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VSXC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bc96.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 18&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VWN5+P86.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 19&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LYP+VWN5&nbsp;for&nbsp;scaling.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;KCIS&nbsp;correlation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 21&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Becke-Roussel&nbsp;correlation&nbsp;(NYI).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 22&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PKZB&nbsp;correlation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 23&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TPSSc&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 24&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t-HCTH&nbsp;(JCP&nbsp;116,&nbsp;9559&nbsp;(2002))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 25&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t-HCTH&nbsp;hybrid&nbsp;(JCP&nbsp;116,&nbsp;9559&nbsp;(2002))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 26&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BMK&nbsp;(Boese&nbsp;and&nbsp;Martin,&nbsp;JCP&nbsp;121,&nbsp;3405&nbsp;(2004))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 27&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M05&nbsp;(Zhao,Schultz,Truhlar,&nbsp;JCP&nbsp;123&nbsp;(2005)&nbsp;161103)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 28&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M05-2X&nbsp;(Zhao,Schultz,Truhlar,&nbsp;JCTC&nbsp;2006&nbsp;in&nbsp;press)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 29&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OAPF&nbsp;(Austin,&nbsp;Petersson,&nbsp;Frisch,&nbsp;…)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B97-D&nbsp;(Grimme,&nbsp;JCC&nbsp;2006,&nbsp;27,&nbsp;1787)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 31&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;APF&nbsp;(Austin,&nbsp;Petersson,&nbsp;Frisch,&nbsp;…)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PAPF&nbsp;(Austin,&nbsp;Petersson,&nbsp;Frisch,&nbsp;…)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 33&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M06-HF&nbsp;(Zhao,Truhlar,&nbsp;JPC&nbsp;A&nbsp;2006,&nbsp;110,&nbsp;13126)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 34&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M06-L&nbsp;(Zhao,Truhlar,&nbsp;JCP&nbsp;2006,&nbsp;125,&nbsp;194101)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 35&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M06&nbsp;(Zhao,Truhlar,&nbsp;Theo&nbsp;Chem&nbsp;Acc&nbsp;2008,&nbsp;120,&nbsp;215)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 36&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M06-2X&nbsp;(Zhao,Truhlar,&nbsp;Theo&nbsp;Chem&nbsp;Acc&nbsp;2008,&nbsp;120,&nbsp;215)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 37&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wB97&nbsp;(J.-D.&nbsp;Chai,&nbsp;M.&nbsp;Head-Gordon,&nbsp;JCP&nbsp;128,&nbsp;084106&nbsp;(2008))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 38&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wB97X&nbsp;(J.-D.&nbsp;Chai,&nbsp;M.&nbsp;Head-Gordon,&nbsp;JCP&nbsp;128,&nbsp;084106&nbsp;(2008))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 39&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wB97X-D&nbsp;(J.-D.&nbsp;Chai,&nbsp;M.&nbsp;Head-Gordon,&nbsp;PCCP&nbsp;10,&nbsp;6615&nbsp;(2008))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;revTPSSc&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 41&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SOGGA11&nbsp;(Peverati,&nbsp;Zhao,&nbsp;Truhlar,&nbsp;JPCL&nbsp;2,&nbsp;1991&nbsp;(2011))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 42&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M11&nbsp;(Peverati,&nbsp;Truhlar,&nbsp;JPCL&nbsp;2,&nbsp;2810&nbsp;(2011))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 43&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SOGGA11-X&nbsp;(Peverati,&nbsp;Truhlar,&nbsp;JCP&nbsp;135,&nbsp;191102&nbsp;(2011))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 44&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M11-L&nbsp;(Peverati,&nbsp;Truhlar,&nbsp;JPCL&nbsp;3,&nbsp;117&nbsp;(2012))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 45&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N12&nbsp;(Peverati,&nbsp;Truhlar,&nbsp;JCTC&nbsp;8,&nbsp;2310&nbsp;(2012))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 46&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MN12-L&nbsp;(Peverati,&nbsp;Truhlar,&nbsp;PCCP&nbsp;DOI:&nbsp;10.1030/c2cp42025b)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 47&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N12-SX&nbsp;(Peverati,&nbsp;Truhlar,&nbsp;PCCP&nbsp;submitted)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 48&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MN12-SX&nbsp;(Peverati,&nbsp;Truhlar,&nbsp;PCCP&nbsp;submitted)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 49&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CVDFT&nbsp;correlation&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 50&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCDFT&nbsp;correlation&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hartree-Fock&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hartree-Fock-Slater&nbsp;exchange&nbsp;(Alpha&nbsp;=&nbsp;2/3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;X-alpha&nbsp;exchange&nbsp;(alpha=&nbsp;0.7).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 400&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Becke&nbsp;1988&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 500&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LG&nbsp;exchange&nbsp;(depreciated)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 600&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PW91&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 700&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gill&nbsp;96&nbsp;exchange&nbsp;(depreciated)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 800&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PW86&nbsp;exchange&nbsp;(depreciated)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 900&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mPW&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PBE&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Reserved&nbsp;to&nbsp;map&nbsp;300]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VSXC&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1400&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B98&nbsp;(JCP&nbsp;108,9624(1998)&nbsp;eq.2c&nbsp;)&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1500&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HCTH&nbsp;(JCP&nbsp;109,6264&nbsp;(1998)&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1600&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B97-1&nbsp;(CPL&nbsp;316,160(2000))&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1700&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B97-2&nbsp;(JCP&nbsp;115,9233(2001))&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1800&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HCTH147&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1900&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HCTH407&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OPTX&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OPTX&nbsp;exchange&nbsp;as&nbsp;in&nbsp;O3LYP.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;XVa&nbsp;exchange&nbsp;(NYI).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Becke-Roussel&nbsp;’88&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2400&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PKZB&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2500&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TPSSX&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2600&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HSE03&nbsp;(JCP&nbsp;118,8207(2003))&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2700&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PBEHole&nbsp;(JCP&nbsp;109,3313(1998))&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2800&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Old&nbsp;mPW&nbsp;exchange&nbsp;(local&nbsp;scaling&nbsp;in&nbsp;non-local&nbsp;term).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2900&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t-HCTH&nbsp;(JCP&nbsp;116,&nbsp;9559&nbsp;(2002))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t-HCTH&nbsp;hybrid&nbsp;(JCP&nbsp;116,&nbsp;9559&nbsp;(2002))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;X&nbsp;(0.765*B88+0.235*PW91)&nbsp;(PNAS&nbsp;101(2004)&nbsp;2673)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BMK&nbsp;(Boese&nbsp;and&nbsp;Martin,&nbsp;JCP&nbsp;121,&nbsp;3405&nbsp;(2004))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M05&nbsp;(Zhao,Schultz,Truhlar,&nbsp;JCP&nbsp;123&nbsp;(2005)&nbsp;161103)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3400&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M05-2X&nbsp;(Zhao,Schultz,Truhlar,&nbsp;JCTC&nbsp;2006&nbsp;in&nbsp;press)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3500&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OAPF&nbsp;(Austin,&nbsp;Petersson,&nbsp;Frisch,&nbsp;…)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3600&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B97-D&nbsp;(Grimme,&nbsp;JCC&nbsp;2006,&nbsp;27,&nbsp;1787)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3700&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;APF&nbsp;(Austin,&nbsp;Petersson,&nbsp;Frisch,&nbsp;…)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3800&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PAPF&nbsp;(Austin,&nbsp;Petersson,&nbsp;Frisch,&nbsp;…)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3900&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HSE&nbsp;+&nbsp;Henderson&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M06-HF&nbsp;(Zhao,Truhlar,&nbsp;JPC&nbsp;A&nbsp;2006,&nbsp;110,&nbsp;13126)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M06-L&nbsp;(Zhao,Truhlar,&nbsp;JCP&nbsp;2006,&nbsp;125,&nbsp;194101)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M06&nbsp;(Zhao,Truhlar,&nbsp;Theo&nbsp;Chem&nbsp;Acc&nbsp;2008,&nbsp;120,&nbsp;215)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M06-2X&nbsp;(Zhao,Truhlar,&nbsp;Theo&nbsp;Chem&nbsp;Acc&nbsp;2008,&nbsp;120,&nbsp;215)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4400&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wB97&nbsp;(J.-D.&nbsp;Chai,&nbsp;M.&nbsp;Head-Gordon,&nbsp;JCP&nbsp;128,&nbsp;084106&nbsp;(2008))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4500&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wB97X&nbsp;(J.-D.&nbsp;Chai,&nbsp;M.&nbsp;Head-Gordon,&nbsp;JCP&nbsp;128,&nbsp;084106&nbsp;(2008))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4600&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wB97X-D&nbsp;(J.-D.&nbsp;Chai,&nbsp;M.&nbsp;Head-Gordon,&nbsp;PCCP&nbsp;10,&nbsp;6615&nbsp;(2008))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4700&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HISS&nbsp;(Henderson,Izmaylov,Scuseria,Savin,&nbsp;JCP&nbsp;127,&nbsp;22103&nbsp;(2007))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4800&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;revTPSSX&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4900&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SOGGA11&nbsp;(Peverati,&nbsp;Zhao,&nbsp;Truhlar,&nbsp;JPCL&nbsp;2,&nbsp;1991&nbsp;(2011))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M11&nbsp;(Peverati,&nbsp;Truhlar,&nbsp;JPCL&nbsp;2,&nbsp;2810&nbsp;(2011))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SOGGA11-X&nbsp;(Peverati,&nbsp;Truhlar,&nbsp;JCP&nbsp;135,&nbsp;191102&nbsp;(2011))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M11-L&nbsp;(Peverati,&nbsp;Truhlar,&nbsp;JPCL&nbsp;3,&nbsp;117&nbsp;(2012))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N12&nbsp;(Peverati,&nbsp;Truhlar,&nbsp;JCTC&nbsp;8,&nbsp;2310&nbsp;(2012))&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5400&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MN12-L&nbsp;(Peverati,&nbsp;Truhlar,&nbsp;PCCP&nbsp;DOI:&nbsp;10.1030/c2cp42025b)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5500&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N12-SX&nbsp;(Peverati,&nbsp;Truhlar,&nbsp;PCCP&nbsp;submitted)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5600&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MN12-SX&nbsp;(Peverati,&nbsp;Truhlar,&nbsp;PCCP&nbsp;submitted)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5700&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[reserved&nbsp;to&nbsp;produce&nbsp;B&nbsp;values&nbsp;for&nbsp;XDM]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5800&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[reserved&nbsp;to&nbsp;run&nbsp;HF&nbsp;+&nbsp;XDM]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CVDFT&nbsp;exchange&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


So 100 is Hartree-Fock, 200 is Hartree-Fock-Slater, 205 is Local Spin Density, and 402 is BLYP.


* 1xxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;Hirao’s&nbsp;long-range&nbsp;correction&nbsp;(JCP&nbsp;115(2001)&nbsp;3540).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;Harris&nbsp;XC&nbsp;with&nbsp;full&nbsp;J.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3xxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;Harris&nbsp;with&nbsp;the&nbsp;specified&nbsp;functional.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4xxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;Harris&nbsp;XC&nbsp;with&nbsp;DFTB-style&nbsp;J.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5xxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;Harris&nbsp;XC&nbsp;with&nbsp;improved&nbsp;DFTB-style&nbsp;J.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/75)
Number of radial and angular points in numerical integration for DFT.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(-5).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SG1&nbsp;pruned&nbsp;grid.&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Even&nbsp;sleazier&nbsp;grid&nbsp;than&nbsp;SG1&nbsp;used&nbsp;for&nbsp;CPHF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pruned&nbsp;(75,194)&nbsp;which&nbsp;is&nbsp;not&nbsp;good&nbsp;for&nbsp;much.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FineGrid.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FineGrid&nbsp;unless&nbsp;uncontracting,&nbsp;then&nbsp;199302.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UltraFine.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UltraFine&nbsp;unless&nbsp;uncontracting,&nbsp;then&nbsp;199590.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SuperFine.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SuperFine&nbsp;unless&nbsp;uncontracting,&nbsp;then&nbsp;299974.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* IIIJJJ&nbsp;&nbsp;&nbsp;&nbsp;III&nbsp;radial&nbsp;points,&nbsp;JJJ&nbsp;angular&nbsp;points.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -IIIJJJ&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;III&nbsp;radial&nbsp;points,&nbsp;and&nbsp;a&nbsp;spherical&nbsp;product&nbsp;angular&nbsp;grid&nbsp;with&nbsp;JJJ&nbsp;theta&nbsp;points&nbsp;and&nbsp;2*JJJ&nbsp;phi&nbsp;points.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/76)
Mixing of HF and DFT. Negative values correspond to standard combinations of HF exchange, local and non-local exchange, and local and non-local correlation.


* -36&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PBE-QIDH&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -35&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PBE0-DH&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -34&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DSD-PBEP86&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -33&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PW6B95&nbsp;and&nbsp;PW6B95-D3&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M08-HX&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -31&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MN15&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SOGGA11-X&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -29&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HSEH1,&nbsp;N12-SX&nbsp;and&nbsp;MN12-SX&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -28&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M06-2X&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -27&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M06,&nbsp;wB97,&nbsp;wB97X,&nbsp;wB97X-D,&nbsp;HISS-B,&nbsp;HISS-A,&nbsp;M11&nbsp;and&nbsp;LC-wHPBE&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -26&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M06-HF&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -25&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mPW2PLYP&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -24&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B2PLYP&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -23&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;APF&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -22&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Unused.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -21&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;LC-wPBE&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CAM-B3LYP&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -19&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OAPF&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -18&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;M05-2X&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -17&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TPSSh&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -16&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BMK&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -15&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;X3LYP&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -14&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tHCTH&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -13&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B1B95/M05&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -12&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HSE1PBE,&nbsp;HSE2PBE&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Unused&nbsp;&nbsp;&nbsp;&nbsp;
* -10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;O3LYP&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B97-2&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B97-1&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HCTH&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B98&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mPW91PW91&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Becke3&nbsp;coefficients:&nbsp;aLSD&nbsp;+&nbsp;(1-a)HF&nbsp;+&nbsp;b(dBx)&nbsp;+&nbsp;VWN&nbsp;+&nbsp;c(LYP-VWN),&nbsp;with&nbsp;a=0.8&nbsp;b=0.72&nbsp;c=0.81&nbsp;Note&nbsp;that&nbsp;Becke&nbsp;actually&nbsp;used&nbsp;Perdew&nbsp;correlation&nbsp;rather&nbsp;than&nbsp;LYP.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Becke"Half&nbsp;and&nbsp;Half"&nbsp;0.5&nbsp;HF&nbsp;+&nbsp;0.5&nbsp;Xc&nbsp;+&nbsp;Corr&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Coefficients&nbsp;of&nbsp;0&nbsp;and&nbsp;0&nbsp;(no&nbsp;exchange).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Coefficients&nbsp;of&nbsp;0.0&nbsp;and&nbsp;1.0&nbsp;for&nbsp;DFT&nbsp;and&nbsp;HF,&nbsp;respectively.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;pure&nbsp;HF,&nbsp;DFT&nbsp;or&nbsp;mixed&nbsp;in&nbsp;accord&nbsp;with&nbsp;IOp(3/76)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMMMMNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mixture&nbsp;of&nbsp;MMMMM/10000&nbsp;DFT&nbsp;exchange&nbsp;and&nbsp;NNNNN/10000&nbsp;HF&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


The DFT exchange factor multiplies any implied by IOp(74) or set by IOp(77).




### IOp(3/77)
Mixing of local and non-local exchange.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;for&nbsp;both.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(coefficients&nbsp;of&nbsp;1&nbsp;and&nbsp;zero&nbsp;or&nbsp;as&nbsp;determined&nbsp;by&nbsp;IOp(76)).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMMMMNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MMMMM/10000&nbsp;non-local&nbsp;plus&nbsp;NNNNN/10000&nbsp;local.&nbsp;Sign&nbsp;is&nbsp;applied&nbsp;to&nbsp;the&nbsp;local&nbsp;term.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


For the HSE03 functional, these coefficients scale the short range (MMMMM) and long range (NNNNN) terms.




### IOp(3/78)
Mixing of local and non-local correlation.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;for&nbsp;both.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(coefficients&nbsp;of&nbsp;1&nbsp;and&nbsp;zero&nbsp;as&nbsp;determined&nbsp;by&nbsp;IOp(76)).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMMMMNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MMMMM/10000&nbsp;non-local&nbsp;plus&nbsp;NNNNN/10000&nbsp;local.&nbsp;Sign&nbsp;is&nbsp;applied&nbsp;to&nbsp;the&nbsp;local&nbsp;term.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


In L510, 1 to set up for CAS-MP2 or 2 to do spin-orbit calculation.




### IOp(3/79)
Range cutoff in Becke weights.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(SS&nbsp;weights).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;SS&nbsp;weights.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Becke&nbsp;weights&nbsp;with&nbsp;default&nbsp;cutoff&nbsp;of&nbsp;30&nbsp;au.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Savin&nbsp;weights.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -M<-3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;SS&nbsp;weights&nbsp;with&nbsp;XCal&nbsp;=&nbsp;M/1000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Becke&nbsp;weights&nbsp;with&nbsp;cutoff&nbsp;N&nbsp;Bohr.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/80)
Range for micro-batching in DFT. Negative to turn off screening of basis functions and grid points. 1000000000 turns of micro-batching logic.




### IOp(3/82)
Fitting density basis set for Coulomb in DFT.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(-1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;numbering&nbsp;of&nbsp;basis&nbsp;sets&nbsp;as&nbsp;for&nbsp;AO&nbsp;basis,&nbsp;including&nbsp;7=General&nbsp;basis.&nbsp;See&nbsp;comments&nbsp;for&nbsp;IOp(3/5)&nbsp;and&nbsp;IOp(3/6)&nbsp;28=Generate&nbsp;automatically&nbsp;from&nbsp;AO&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/83)
Equivalent of IOp(3/6) for density basis. For auto-generated
basis sets:


* MN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-1&nbsp;keep&nbsp;all&nbsp;generated&nbsp;functions.&nbsp;Otherwise,&nbsp;an&nbsp;AO&nbsp;shell&nbsp;with&nbsp;angular&nbsp;momentum&nbsp;LAO&nbsp;generates&nbsp;a&nbsp;DBF&nbsp;shell&nbsp;with&nbsp;angular&nbsp;momenta&nbsp;0&nbsp;up&nbsp;to&nbsp;LDB,&nbsp;where&nbsp;if&nbsp;LVal&nbsp;is&nbsp;the&nbsp;highest&nbsp;valence&nbsp;(occupied)&nbsp;LAO&nbsp;then&nbsp;if&nbsp;LAO&nbsp;≤&nbsp;LVal,&nbsp;LDB&nbsp;=&nbsp;2*LAO,&nbsp;while&nbsp;if&nbsp;LAO&nbsp;>&nbsp;LVal&nbsp;LDB&nbsp;=&nbsp;LAO&nbsp;+&nbsp;Max(LVal,1)&nbsp;+&nbsp;M.&nbsp;If&nbsp;N&nbsp;>&nbsp;0&nbsp;then&nbsp;LDB&nbsp;is&nbsp;limited&nbsp;to&nbsp;N-1,&nbsp;i.e.,&nbsp;all&nbsp;angular&nbsp;momenta&nbsp;of&nbsp;N&nbsp;or&nbsp;higher&nbsp;are&nbsp;discarded.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/84)
Equivalent of IOp(3/7) for density basis. For auto-generated basis sets:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(4022).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;all&nbsp;products&nbsp;of&nbsp;AOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;only&nbsp;AO&nbsp;primitives&nbsp;squared&nbsp;in&nbsp;fitting&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;split&nbsp;shells.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Split&nbsp;F&nbsp;and&nbsp;higher&nbsp;shells&nbsp;away&nbsp;from&nbsp;S=P=D.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;1.5&nbsp;+&nbsp;N/4&nbsp;as&nbsp;the&nbsp;test&nbsp;for&nbsp;similar&nbsp;exponents&nbsp;during&nbsp;auto-generation&nbsp;of&nbsp;fitting&nbsp;sets.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;old&nbsp;(G03)&nbsp;algorithm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;new&nbsp;algorithm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;algorithm&nbsp;3.&nbsp;&nbsp;&nbsp;&nbsp;
* 4000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;New&nbsp;iterative&nbsp;merging&nbsp;of&nbsp;shells,&nbsp;monotonic&nbsp;L.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/85)
Pure vs. Cartesian functions in density basis.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(pure&nbsp;for&nbsp;read-in&nbsp;basis).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pure.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Cartesian.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/86)
Discard basis functions based on angular momentum.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;≤&nbsp;Discard&nbsp;basis&nbsp;functions&nbsp;with&nbsp;angular&nbsp;momentum.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/87)
Discard density basis functions based on angular momentum.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N≤&nbsp;Discard&nbsp;density&nbsp;basis&nbsp;functions&nbsp;with&nbsp;angular&nbsp;momentum.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/88)
Modification of internally stored density basis.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;general&nbsp;basis&nbsp;data&nbsp;in&nbsp;addition&nbsp;to&nbsp;setting&nbsp;up&nbsp;a&nbsp;standard&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Massage&nbsp;the&nbsp;data&nbsp;in&nbsp;Common&nbsp;/B/&nbsp;and&nbsp;Common&nbsp;/Mol/.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add&nbsp;ghost&nbsp;atoms&nbsp;to&nbsp;/B/&nbsp;so&nbsp;that&nbsp;every&nbsp;shell&nbsp;is&nbsp;on&nbsp;a&nbsp;separate&nbsp;center.&nbsp;Also&nbsp;done&nbsp;if&nbsp;req.&nbsp;in&nbsp;IOp(3/10).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Split&nbsp;S=P&nbsp;density&nbsp;basis&nbsp;shells&nbsp;into&nbsp;separate&nbsp;S&nbsp;and&nbsp;P&nbsp;shells.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;split&nbsp;S=P&nbsp;density&nbsp;shells.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Split&nbsp;S=P=D=…&nbsp;density&nbsp;shells&nbsp;into&nbsp;S=P,&nbsp;D,&nbsp;F,&nbsp;…&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;split&nbsp;density&nbsp;S=P=D…&nbsp;shells.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/89)
Set up for density fitting.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(102&nbsp;if&nbsp;a&nbsp;fitting&nbsp;set&nbsp;has&nbsp;been&nbsp;included&nbsp;and&nbsp;pure&nbsp;DFT&nbsp;is&nbsp;being&nbsp;used,&nbsp;1&nbsp;otherwise).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;use&nbsp;density&nbsp;fits.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;fits,&nbsp;forming&nbsp;Z&nbsp;=&nbsp;modified&nbsp;A^-1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;fits,&nbsp;solving&nbsp;iterative&nbsp;with&nbsp;stored&nbsp;A.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;fits,&nbsp;solving&nbsp;iterative&nbsp;with&nbsp;direct&nbsp;products,&nbsp;with&nbsp;A&nbsp;formed&nbsp;to&nbsp;generate&nbsp;preconditioning.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Iterative,&nbsp;no&nbsp;formation&nbsp;of&nbsp;A.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Form&nbsp;A’&nbsp;over&nbsp;neutral&nbsp;distributions&nbsp;via&nbsp;multiplies&nbsp;by&nbsp;A.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Form&nbsp;A’&nbsp;over&nbsp;neutral&nbsp;distributions&nbsp;via&nbsp;direct&nbsp;products.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Form&nbsp;inverse&nbsp;matrix&nbsp;once.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Solve&nbsp;iteratively&nbsp;with&nbsp;no&nbsp;preconditioning.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Solve&nbsp;iteratively&nbsp;with&nbsp;diagonal&nbsp;preconditioning.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Solve&nbsp;iteratively&nbsp;with&nbsp;symmetric&nbsp;block-diagonal&nbsp;preconditioning.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Solve&nbsp;iteratively&nbsp;with&nbsp;non-symmetric&nbsp;block-diagonal&nbsp;preconditioning.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Solve&nbsp;non-iterative&nbsp;using&nbsp;precomputed&nbsp;A’^-1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Put&nbsp;all&nbsp;functions&nbsp;into&nbsp;a&nbsp;single&nbsp;block&nbsp;in&nbsp;forming&nbsp;the&nbsp;preconditioning&nbsp;matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xxxxx&nbsp;&nbsp;&nbsp;&nbsp;Form&nbsp;the&nbsp;full&nbsp;preconditioning&nbsp;matrix&nbsp;(not&nbsp;block-diagonal).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;same&nbsp;as&nbsp;1xxxxxx.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;set&nbsp;up&nbsp;fitting&nbsp;if&nbsp;exact&nbsp;exchange&nbsp;is&nbsp;in&nbsp;use.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;up&nbsp;fitting&nbsp;regardless&nbsp;and&nbsp;do&nbsp;one&nbsp;fit&nbsp;with&nbsp;the&nbsp;converged&nbsp;SCF&nbsp;density.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3xxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;up&nbsp;fitting&nbsp;regardless&nbsp;and&nbsp;use&nbsp;for&nbsp;Coulomb&nbsp;during&nbsp;iters.&nbsp;even&nbsp;if&nbsp;exact&nbsp;exchange&nbsp;is
used&nbsp;(NYI).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fit&nbsp;using&nbsp;Coulomb&nbsp;operator&nbsp;(default).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fit&nbsp;using&nbsp;overlaps.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/90)
Thresholds for density fitting.


* MMNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-MM&nbsp;on&nbsp;iterative&nbsp;solution,&nbsp;default&nbsp;MM=09.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-NN&nbsp;on&nbsp;generalized&nbsp;inverse,&nbsp;default&nbsp;NN=06.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/91)
Scalar relativistic core Hamiltonian.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Non-relativistic.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RESC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Douglass-Kroll-Hess&nbsp;0th&nbsp;order.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Douglass-Kroll-Hess&nbsp;2nd&nbsp;order.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DKH&nbsp;4th&nbsp;order,&nbsp;including&nbsp;SO&nbsp;terms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;Boettinger&nbsp;scaling&nbsp;of&nbsp;1e&nbsp;SO&nbsp;to&nbsp;approximate&nbsp;effect&nbsp;of&nbsp;2e&nbsp;terms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;rescale&nbsp;SO&nbsp;terms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Multiply&nbsp;SO&nbsp;terms&nbsp;by&nbsp;10&nbsp;for&nbsp;debugging.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Multiply&nbsp;SO&nbsp;terms&nbsp;by&nbsp;10&nbsp;*&nbsp;10^N-1&nbsp;for&nbsp;debugging.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Multiply&nbsp;SO&nbsp;terms&nbsp;by&nbsp;half.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Multiply&nbsp;SO&nbsp;terms&nbsp;by&nbsp;two.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Multiply&nbsp;SO&nbsp;terms&nbsp;by&nbsp;-two.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/92)
Whether read-in basis sets are in terms of normalized primitives.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(3232).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AO&nbsp;coefficients&nbsp;are&nbsp;for&nbsp;raw&nbsp;primitives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AOs&nbsp;have&nbsp;overlap&nbsp;normalization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AOs&nbsp;have&nbsp;Coulomb&nbsp;normalization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DBF&nbsp;coefficients&nbsp;are&nbsp;for&nbsp;raw&nbsp;primitives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DBFs&nbsp;have&nbsp;overlap&nbsp;normalization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DBFs&nbsp;have&nbsp;Coulomb&nbsp;normalization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;normalize&nbsp;AOs&nbsp;contraction&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;overlap&nbsp;normalization&nbsp;for&nbsp;AOs&nbsp;contraction&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Coulomb&nbsp;normalization&nbsp;for&nbsp;AOs&nbsp;contraction&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;normalize&nbsp;DBFs&nbsp;contraction&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;overlap&nbsp;normalization&nbsp;for&nbsp;DBFs&nbsp;contraction&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Coulomb&nbsp;normalization&nbsp;for&nbsp;DBFs&nbsp;contraction&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/93)
Nuclear charge distribution.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1,&nbsp;unless&nbsp;scalar&nbsp;relativistic).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Point&nbsp;nuclei.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Single&nbsp;s-Gaussians&nbsp;using&nbsp;formula&nbsp;of&nbsp;Quiney&nbsp;et.&nbsp;al.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Very&nbsp;tight&nbsp;single&nbsp;s-Gaussians,&nbsp;for&nbsp;debugging.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;2&nbsp;but&nbsp;exponents&nbsp;are&nbsp;100x&nbsp;smaller,&nbsp;for&nbsp;debugging.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Include&nbsp;nuclear&nbsp;charge&nbsp;distributions&nbsp;in&nbsp;DBF&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Mxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;method&nbsp;M&nbsp;to&nbsp;handle&nbsp;nuclear&nbsp;charges&nbsp;during&nbsp;density&nbsp;fitting.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;nuclear&nbsp;density&nbsp;in&nbsp;core&nbsp;Hamiltonian&nbsp;if&nbsp;present.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;use&nbsp;nuclear&nbsp;density&nbsp;in&nbsp;core&nbsp;Hamiltonian&nbsp;even&nbsp;if&nbsp;present.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/94)
Range of PBC cells in Bohr.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(100).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;Bohr.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -M&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Multiply&nbsp;usual&nbsp;range&nbsp;by&nbsp;M.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/95)
Minimum number of PBC cells.


* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;At&nbsp;least&nbsp;N&nbsp;cells&nbsp;in&nbsp;each&nbsp;direction.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Based&nbsp;on&nbsp;range&nbsp;estimate&nbsp;(IOp(3/94)).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;At&nbsp;least&nbsp;N&nbsp;cells&nbsp;total.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/96)
Number of PBC cells for DFT.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As&nbsp;many&nbsp;as&nbsp;look&nbsp;significant.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;At&nbsp;least&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/97)
Number of PBC cells for exact exchange.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As&nbsp;many&nbsp;as&nbsp;look&nbsp;significant.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;At&nbsp;least&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/98)
Maximum number of density matrices in PBC.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;based&nbsp;on&nbsp;number&nbsp;of&nbsp;cells&nbsp;having&nbsp;overlap&nbsp;with&nbsp;cell&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;more&nbsp;than&nbsp;N&nbsp;matrices.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/99)
`L302`: Whether to set up precomputed quadrature grid.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(4&nbsp;if&nbsp;doing&nbsp;DFT,&nbsp;-1&nbsp;otherwise).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;storing&nbsp;only&nbsp;grid&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;storing&nbsp;grid&nbsp;parameters&nbsp;and&nbsp;weights.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;storing&nbsp;grid&nbsp;parameters,&nbsp;weights,&nbsp;and&nbsp;point&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;storing&nbsp;only&nbsp;dimensions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/100)
Minimum number of PBC cells for PBC-MP2.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;for&nbsp;HF&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/101)
Maximum range of cells.


* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;more&nbsp;than&nbsp;N&nbsp;in&nbsp;each&nbsp;direction.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;limit.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;more&nbsp;than&nbsp;N&nbsp;total.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/102)
Number of density fittings solutions to save from previous SCF iterations. Default is 6 (using 5 previous solutions plus the current right-hand side to generate the initial guess). Negative to use projected equations rather than least-squares.




### IOp(3/103)
Maximum number of vectors allowed in expansion space during iterative density fitting. Default is Max(NDBF/2,1000), where NDBF = # density basis functions.




### IOp(3/104)
Maximum number of iterations during iterative density fitting. Default is Max (1000,NDBF+100).




### IOp(3/105)
Re-use of PBC cell data.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(re-use&nbsp;if&nbsp;present).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reuse.&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;reuse.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;from&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/106)
Override default number of atoms threshold for turning on FMM (for debugging). This number is scaled up appropriately if symmetry is in use, to compensate for the loss of some symmetry with FMM.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(60)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;atoms&nbsp;for&nbsp;the&nbsp;C1&nbsp;case.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/107)
Omega for short/long range Hartree-Fock exchange.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard&nbsp;HF&nbsp;exchange&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMMMMNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Short&nbsp;range&nbsp;HF&nbsp;exchange&nbsp;with&nbsp;NNNNN/10000&nbsp;and&nbsp;long&nbsp;range&nbsp;exchange&nbsp;with&nbsp;MMMMM/10000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/108)
Omega for short/long range DFT exchange.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard&nbsp;DFT&nbsp;exchange&nbsp;or&nbsp;default&nbsp;from&nbsp;functional.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMMMMNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Short&nbsp;range&nbsp;DFT&nbsp;exchange&nbsp;with&nbsp;NNNNN&nbsp;/10000&nbsp;and&nbsp;long&nbsp;range&nbsp;DFT&nbsp;exchange&nbsp;with&nbsp;MMMMM/10000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/109)
Omega for short/long range DFT correlation


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard&nbsp;DFT&nbsp;correlation&nbsp;or&nbsp;default&nbsp;from&nbsp;functional.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMMMMNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Short&nbsp;range&nbsp;DFT&nbsp;correlation&nbsp;with&nbsp;NNNNN/10000&nbsp;and&nbsp;long&nbsp;range&nbsp;DFT&nbsp;correlation&nbsp;with&nbsp;MMMMM/10000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/110)
Threshold in precomputed XC quadrature grid, over-riding default or value in IOp(27).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As&nbsp;implied&nbsp;by&nbsp;IOp(27).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/111)
Extra PBC printing. Default is no print.


* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;table&nbsp;of&nbsp;cells.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/112)
Huckel parameters.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(13).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hoffman&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pykko&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Huckel&nbsp;initial&nbsp;guess&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10&nbsp;for&nbsp;Huckel,&nbsp;20&nbsp;for&nbsp;DFTB).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;standard&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;parameters&nbsp;to&nbsp;override&nbsp;the&nbsp;standard&nbsp;ones.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;parameters&nbsp;from&nbsp;RWF&nbsp;file&nbsp;738.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;parameters&nbsp;from&nbsp;checkpoint&nbsp;file&nbsp;738.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/113)
Generate SABF data.


* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(12).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;AO&nbsp;basis&nbsp;function&nbsp;SABF&nbsp;data&nbsp;if&nbsp;symmetry&nbsp;is&nbsp;on.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Make&nbsp;AO&nbsp;SABF&nbsp;data&nbsp;C1&nbsp;regardless.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;density&nbsp;basis&nbsp;function&nbsp;SABF&nbsp;data&nbsp;if&nbsp;symmetry&nbsp;is&nbsp;on.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Make&nbsp;density&nbsp;basis&nbsp;SABF&nbsp;data&nbsp;C1&nbsp;regardless.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/114)
Factor for number of significant basis functions allocation in XC quadrature allocation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;use&nbsp;amount&nbsp;computed&nbsp;by&nbsp;LdMGrd.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scale&nbsp;values&nbsp;by&nbsp;N/10.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/115)
Factor for number of significant atoms allocation in XC quadrature allocation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;use&nbsp;amount&nbsp;computed&nbsp;by&nbsp;LdMGrd.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scale&nbsp;values&nbsp;by&nbsp;N/10.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/116)
Type of SCF.


* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Take&nbsp;from&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ignore&nbsp;ILSW&nbsp;and&nbsp;determine&nbsp;on&nbsp;the&nbsp;fly.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Take&nbsp;from&nbsp;ILSW.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Real&nbsp;RHF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Real&nbsp;UHF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complex&nbsp;RHF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complex&nbsp;UHF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complex,&nbsp;but&nbsp;use&nbsp;ILSW&nbsp;to&nbsp;decide&nbsp;whether&nbsp;RHF/UHF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GHF&nbsp;using&nbsp;real&nbsp;basis&nbsp;functions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complex&nbsp;RHF,&nbsp;complex&nbsp;spherical&nbsp;harmonic&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 12&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Complex&nbsp;UHF,&nbsp;complex&nbsp;spherical&nbsp;harmonic&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 15&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GHF,&nbsp;complex&nbsp;spin-orbital&nbsp;basis&nbsp;(NYI).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 19&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GHF,&nbsp;spinor&nbsp;basis&nbsp;(NYI).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 23&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DF,&nbsp;spinor&nbsp;basis&nbsp;(NYI).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 101&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Real&nbsp;ROHF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 201&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Unrestricted&nbsp;if&nbsp;derivatives&nbsp;are&nbsp;being&nbsp;done&nbsp;but&nbsp;RO&nbsp;single&nbsp;points;&nbsp;used&nbsp;for&nbsp;RO-compound&nbsp;methods.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/117)
Handling spin-orbit ECPs.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default;&nbsp;include&nbsp;them&nbsp;if&nbsp;present&nbsp;and&nbsp;doing&nbsp;GHF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Always&nbsp;compute&nbsp;SO&nbsp;terms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Never&nbsp;compute&nbsp;SO&nbsp;terms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/118)
Extra memory for integral evaluation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add&nbsp;N&nbsp;words&nbsp;to&nbsp;the&nbsp;estimated&nbsp;memory&nbsp;requirements&nbsp;for&nbsp;direct&nbsp;integral&nbsp;evaluation,&nbsp;in&nbsp;all&nbsp;links.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(3/119)
Coefficients of short/long range Hartree-Fock exchange.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard&nbsp;HF&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMMMMNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NNNNN&nbsp;/10000&nbsp;short&nbsp;range&nbsp;and&nbsp;MMMMM/10000&nbsp;long&nbsp;range&nbsp;exchange.&nbsp;The&nbsp;signs&nbsp;can&nbsp;be&nbsp;changed&nbsp;by&nbsp;IOp(3/130).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/120)
Coefficients of short/long range DFT exchange.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard&nbsp;DFT&nbsp;exchange&nbsp;or&nbsp;default&nbsp;from&nbsp;functional.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMMMMNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NNNNN&nbsp;/10000&nbsp;short&nbsp;range&nbsp;and&nbsp;MMMMM/10000&nbsp;long&nbsp;range.&nbsp;The&nbsp;signs&nbsp;can&nbsp;be&nbsp;changed&nbsp;by&nbsp;IOp(3/131).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/121)
Coefficients of short/long range DFT correlation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard&nbsp;DFT&nbsp;correlation&nbsp;or&nbsp;default&nbsp;from&nbsp;functional.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMMMMNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NNNNN&nbsp;/10000&nbsp;short&nbsp;range&nbsp;and&nbsp;MMMMM/10000&nbsp;long&nbsp;range.&nbsp;The&nbsp;signs&nbsp;can&nbsp;be&nbsp;changed&nbsp;by&nbsp;IOp(3/132).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/123)
Phase convention for complex orbitals.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal;&nbsp;largest&nbsp;coefficient&nbsp;set&nbsp;to&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Largest&nbsp;coefficient&nbsp;set&nbsp;to&nbsp;i&nbsp;in&nbsp;each&nbsp;orbital.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Largest&nbsp;coefficient&nbsp;set&nbsp;to&nbsp;i&nbsp;in&nbsp;first&nbsp;orbital,&nbsp;i^2&nbsp;in&nbsp;second,&nbsp;etc.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Largest&nbsp;coefficient&nbsp;set&nbsp;to&nbsp;phase&nbsp;60&nbsp;degrees.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Largest&nbsp;coefficient&nbsp;set&nbsp;to&nbsp;phase&nbsp;60&nbsp;degrees,&nbsp;then&nbsp;120,&nbsp;etc.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/124)
Empirical dispersion term.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add&nbsp;it&nbsp;regardless.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add&nbsp;it&nbsp;for&nbsp;the&nbsp;DFT&nbsp;functionals&nbsp;for&nbsp;which&nbsp;it&nbsp;has&nbsp;been&nbsp;defined&nbsp;and&nbsp;parameterized&nbsp;and&nbsp;for&nbsp;which&nbsp;a&nbsp;specific&nbsp;name&nbsp;has&nbsp;been&nbsp;defined&nbsp;in&nbsp;Link1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add&nbsp;it&nbsp;for&nbsp;the&nbsp;DFT&nbsp;functionals&nbsp;for&nbsp;which&nbsp;it&nbsp;has&nbsp;been&nbsp;defined&nbsp;and&nbsp;parameterized.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;add&nbsp;it&nbsp;regardless.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;dispersion&nbsp;type&nbsp;1&nbsp;(APF-D).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;dispersion&nbsp;type&nbsp;2&nbsp;(Grimme&nbsp;B97-D).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;dispersion&nbsp;type&nbsp;3&nbsp;(Grimme&nbsp;DFT-D3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;dispersion&nbsp;type&nbsp;4&nbsp;(Grimme&nbsp;DFT-D3(BJ)).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 50&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;dispersion&nbsp;type&nbsp;5&nbsp;(Grimme&nbsp;D3,&nbsp;PM7&nbsp;version).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Whether&nbsp;to&nbsp;change&nbsp;Grimme&nbsp;dispersion&nbsp;based&nbsp;on&nbsp;functional.&nbsp;Defaulted&nbsp;based&nbsp;on&nbsp;lowest&nbsp;digit.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;the&nbsp;change.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;do&nbsp;the&nbsp;change.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NNxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Grimme&nbsp;parameters&nbsp;for&nbsp;hybrid&nbsp;functional&nbsp;NN&nbsp;(see&nbsp;IOp(74)).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMMMxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Grimme&nbsp;parameters&nbsp;for&nbsp;pure&nbsp;functional&nbsp;MMMM&nbsp;(see&nbsp;IOp(74)).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Kill&nbsp;the&nbsp;job&nbsp;when&nbsp;atomic&nbsp;parameters&nbsp;are&nbsp;unavailable.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Continue&nbsp;the&nbsp;calculation&nbsp;even&nbsp;if&nbsp;some&nbsp;of&nbsp;the&nbsp;atomic&nbsp;parameters&nbsp;are&nbsp;unavailable.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(3/125)
Scaling of AA/BB and AB components of E(2).


* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;for&nbsp;AB.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;for&nbsp;AA/BB.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;for&nbsp;both.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1&nbsp;for&nbsp;both).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMMMMNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MMMMM/10000&nbsp;for&nbsp;AA/BB,&nbsp;NNNNN/10000&nbsp;for&nbsp;AB.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/126)
Omega for short/long range 1/r operator in E(2,AA) and E(2,BB) evaluation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard&nbsp;1/r&nbsp;operator.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Short&nbsp;range&nbsp;1/r&nbsp;operator&nbsp;with&nbsp;N/10000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMMMMNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Short&nbsp;range&nbsp;1/r&nbsp;operator&nbsp;with&nbsp;NNNNN/10000&nbsp;and&nbsp;long&nbsp;range&nbsp;1/r&nbsp;operator&nbsp;with&nbsp;MMMMM/10000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(3/127)
Omega for short/long range 1/r operator in E(2,AB) evaluation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard&nbsp;1/r&nbsp;operator.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMMMMNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Short&nbsp;range&nbsp;1/r&nbsp;operator&nbsp;with&nbsp;NNNNN/10000&nbsp;and&nbsp;long&nbsp;range&nbsp;1/r&nbsp;operator&nbsp;with&nbsp;MMMMM/10000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/128)
Coefficients of short/long range combination of 1/r operator in E(2,AA) and E(2,BB) evaluation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard&nbsp;1/r&nbsp;operator.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMMMMNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NNNNN/10000&nbsp;short&nbsp;range&nbsp;and&nbsp;MMMMM/10000&nbsp;long&nbsp;range.&nbsp;The&nbsp;signs&nbsp;can&nbsp;be&nbsp;changed&nbsp;by&nbsp;IOp(3/133).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/129)
Coefficients of short/long range combination of 1/r operator in E(2,AB) evaluation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard&nbsp;1/r&nbsp;operator.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMMMMNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NNNNN/10000&nbsp;short&nbsp;range&nbsp;and&nbsp;MMMMM/10000&nbsp;long&nbsp;range.&nbsp;The&nbsp;signs&nbsp;can&nbsp;be&nbsp;changed&nbsp;by&nbsp;IOp(3/134).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/130)
Coefficient of full range of HF exchange.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;full&nbsp;range&nbsp;coefficient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard&nbsp;full&nbsp;range&nbsp;HF&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NNNNN/10000&nbsp;full&nbsp;range&nbsp;coefficient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;negative&nbsp;of&nbsp;the&nbsp;short&nbsp;range&nbsp;coefficient&nbsp;as&nbsp;set&nbsp;by&nbsp;IOp(3/119).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200000&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;the&nbsp;short&nbsp;range&nbsp;coefficient&nbsp;to&nbsp;zero.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;negative&nbsp;of&nbsp;the&nbsp;long&nbsp;range&nbsp;coefficient&nbsp;as&nbsp;set&nbsp;by&nbsp;IOp(3/119).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;the&nbsp;long&nbsp;range&nbsp;coefficient&nbsp;to&nbsp;zero.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;negative&nbsp;of&nbsp;the&nbsp;mid&nbsp;range&nbsp;coefficient&nbsp;as&nbsp;set&nbsp;by&nbsp;IOp(138).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;the&nbsp;mid&nbsp;range&nbsp;coefficient&nbsp;to&nbsp;zero.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/131)
Coefficient of full range of DFT exchange.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;full&nbsp;range&nbsp;coefficient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard&nbsp;full&nbsp;range&nbsp;DFT&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NNNNN/10000&nbsp;full&nbsp;range&nbsp;coefficient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;negative&nbsp;of&nbsp;the&nbsp;short&nbsp;range&nbsp;coefficient&nbsp;as&nbsp;set&nbsp;by&nbsp;IOp(3/120).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200000&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;the&nbsp;short&nbsp;range&nbsp;coefficient&nbsp;to&nbsp;zero.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;negative&nbsp;of&nbsp;the&nbsp;long&nbsp;range&nbsp;coefficient&nbsp;as&nbsp;set&nbsp;by&nbsp;IOp(3/120).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;the&nbsp;long&nbsp;range&nbsp;coefficient&nbsp;to&nbsp;zero.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/132)
Coefficient of full range of DFT correlation.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;full&nbsp;range&nbsp;coefficient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard&nbsp;full&nbsp;range&nbsp;DFT&nbsp;correlation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NNNNN/10000&nbsp;full&nbsp;range&nbsp;coefficient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;negative&nbsp;of&nbsp;the&nbsp;short&nbsp;range&nbsp;coefficient&nbsp;as&nbsp;set&nbsp;by&nbsp;IOp(3/121).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200000&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;the&nbsp;short&nbsp;range&nbsp;coefficient&nbsp;to&nbsp;zero.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;negative&nbsp;of&nbsp;the&nbsp;long&nbsp;range&nbsp;coefficient&nbsp;as&nbsp;set&nbsp;by&nbsp;IOp(3/121).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;the&nbsp;long&nbsp;range&nbsp;coefficient&nbsp;to&nbsp;zero.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;negative&nbsp;of&nbsp;the&nbsp;mid&nbsp;range&nbsp;coefficient&nbsp;as&nbsp;set&nbsp;by&nbsp;IOp(138).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;the&nbsp;mid&nbsp;range&nbsp;coefficient&nbsp;to&nbsp;zero.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/133)
Coefficient of full range of 1/r operator in E(2,AA) and E(2,BB) evaluation.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;full&nbsp;range&nbsp;coefficient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard&nbsp;full&nbsp;range&nbsp;1/r&nbsp;operator.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NNNNN/10000&nbsp;full&nbsp;range&nbsp;coefficient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the
negative&nbsp;of&nbsp;the&nbsp;short&nbsp;range&nbsp;coefficient&nbsp;as&nbsp;set&nbsp;by&nbsp;IOp(3/128).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;negative&nbsp;of&nbsp;the&nbsp;long&nbsp;range&nbsp;coefficient&nbsp;as&nbsp;set&nbsp;by&nbsp;IOp(3/128).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/134)
Coefficient of full range of 1/r operator in E(2,AB) evaluation.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;full&nbsp;range&nbsp;coefficient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard&nbsp;full&nbsp;range&nbsp;1/r&nbsp;operator.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NNNNN/10000&nbsp;full&nbsp;range&nbsp;coefficient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;negative&nbsp;of&nbsp;the&nbsp;short&nbsp;range&nbsp;coefficient&nbsp;as&nbsp;set&nbsp;by&nbsp;IOp(3/129).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;negative&nbsp;of&nbsp;the&nbsp;long&nbsp;range&nbsp;coefficient&nbsp;as&nbsp;set&nbsp;by&nbsp;IOp(3/129).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(3/135)
Setup for semi-empirical.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1&nbsp;for&nbsp;AM1/PMn&nbsp;full-matrix,&nbsp;2&nbsp;for&nbsp;sparse&nbsp;and&nbsp;other&nbsp;methods).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;New&nbsp;code.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Old&nbsp;code.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Nx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Flags&nbsp;for&nbsp;AM1Par&nbsp;(default&nbsp;2020).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;standard&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;parameters&nbsp;from&nbsp;RWF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;parameters&nbsp;from&nbsp;checkpoint.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;parameters&nbsp;from&nbsp;checkpoint&nbsp;if&nbsp;present;&nbsp;otherwise&nbsp;generate.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 50&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;produce&nbsp;any&nbsp;standard&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;additional&nbsp;parameters&nbsp;from&nbsp;the&nbsp;input&nbsp;stream.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;additional&nbsp;parameters&nbsp;from&nbsp;the&nbsp;input&nbsp;stream&nbsp;using&nbsp;MOPAC&nbsp;format&nbsp;and&nbsp;units.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;additional&nbsp;parameters&nbsp;in&nbsp;both&nbsp;formats,&nbsp;Gaussian&nbsp;internal&nbsp;format&nbsp;first.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;parameters&nbsp;on&nbsp;RWF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;save&nbsp;parameters&nbsp;on&nbsp;RWF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/136)
Printing of semi-empirical parameters.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2&nbsp;or&nbsp;parameters&nbsp;read&nbsp;in&nbsp;≤&nbsp;2&nbsp;unless&nbsp;IPrint).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;parameters&nbsp;for&nbsp;elements&nbsp;used&nbsp;in&nbsp;this&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;print&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;parameters&nbsp;for&nbsp;all&nbsp;elements.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;parameters&nbsp;in&nbsp;human-readable&nbsp;form.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;parameters&nbsp;in&nbsp;input&nbsp;format.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;parameters&nbsp;in&nbsp;both&nbsp;formats.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(100).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;only&nbsp;non-zero&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;all&nbsp;parameters&nbsp;including&nbsp;zero&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/137)
Control of FMM for nuclear repulsion.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;Use&nbsp;for&nbsp;5K&nbsp;or&nbsp;more&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;for&nbsp;N&nbsp;or&nbsp;more&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Always&nbsp;use&nbsp;FMM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Never&nbsp;use&nbsp;FMM;&nbsp;necessary&nbsp;when&nbsp;doing&nbsp;external&nbsp;point&nbsp;charges&nbsp;if&nbsp;one&nbsp;coincides&nbsp;with&nbsp;a&nbsp;(ghost)&nbsp;nucleus.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/138)
Mid-range coefficients for split-range functionals:


* MMMMMNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NNNNN/10000&nbsp;HF&nbsp;and&nbsp;MMMMM/10000&nbsp;XC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/140)
Override PCM solution method.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Leave&nbsp;unchanged.&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;inversion.&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;iterative.&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;simultaneous&nbsp;in&nbsp;L502.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/141)
Override PCM FoFCou accuracy parameter.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Leave&nbsp;unchanged.&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/142)
Convergence for iterative PCM solution.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;10^-6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/143)
Iteration limit for PCM solution.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(400)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/144)
Threshold for discarding small surface elements.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1.d-12).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/158)
Over-ride defaults for PCM:


* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal&nbsp;default&nbsp;for&nbsp;model&nbsp;(26).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DPCM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CPCM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Isotropic&nbsp;non-symmetric&nbsp;IEFPCM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Anisotropic&nbsp;non-symmetric&nbsp;IEFPCM&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ionic&nbsp;non-symmetric&nbsp;IEFPCM&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Isotropic&nbsp;symmetric&nbsp;IEFPCM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add&nbsp;spheres,&nbsp;default&nbsp;ofac=0.8&nbsp;rmin=0.5.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;add&nbsp;spheres.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/159)
Override defaults for atomic densities:


* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal&nbsp;defaults.&nbsp;&nbsp;&nbsp;&nbsp;
* NN>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;is&nbsp;NN.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -NN<0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;type&nbsp;NN&nbsp;regardless&nbsp;of&nbsp;input.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/160)
Operation of L316:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1121).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;out&nbsp;2e&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;print&nbsp;out&nbsp;2e&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Write&nbsp;fortran&nbsp;unformatted&nbsp;matrix&nbsp;element&nbsp;file,&nbsp;using&nbsp;the&nbsp;default&nbsp;name&nbsp;("Gau-#####.EUF",&nbsp;where&nbsp;#####&nbsp;is&nbsp;the&nbsp;PID)&nbsp;in&nbsp;the&nbsp;scratch&nbsp;directory.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;write&nbsp;matrix&nbsp;element&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Write&nbsp;the&nbsp;matrix&nbsp;element&nbsp;file,&nbsp;reading&nbsp;the&nbsp;file&nbsp;name&nbsp;from&nbsp;an&nbsp;input&nbsp;section&nbsp;(with&nbsp;terminating&nbsp;blank&nbsp;line).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Include&nbsp;only&nbsp;active&nbsp;nuclei&nbsp;in&nbsp;the&nbsp;molecule&nbsp;data&nbsp;on&nbsp;the&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Include&nbsp;all&nbsp;centers&nbsp;in&nbsp;the&nbsp;molecule&nbsp;data&nbsp;on&nbsp;the&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;full&nbsp;size&nbsp;integers&nbsp;for&nbsp;labels&nbsp;of&nbsp;packed&nbsp;matrices.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Integer*4&nbsp;for&nbsp;labels&nbsp;of&nbsp;packed&nbsp;matrices;&nbsp;ignored&nbsp;on&nbsp;machines&nbsp;which&nbsp;do&nbsp;not&nbsp;support&nbsp;I*4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;same&nbsp;size&nbsp;integer&nbsp;labels&nbsp;for&nbsp;4d&nbsp;matrices&nbsp;(2e&nbsp;integrals)&nbsp;as&nbsp;for&nbsp;other&nbsp;data.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Integer*2&nbsp;labels&nbsp;for&nbsp;4d&nbsp;matrices;&nbsp;ignored&nbsp;on&nbsp;machines&nbsp;which&nbsp;do&nbsp;not&nbsp;support&nbsp;16-bit&nbsp;integers.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store&nbsp;binary&nbsp;data&nbsp;with&nbsp;no&nbsp;record&nbsp;marks,&nbsp;appropriate&nbsp;to&nbsp;reading&nbsp;in&nbsp;c/c++/perl/python.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/161)
Saving/Restoring L302 results for SCF=Restart:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(22)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;the&nbsp;XC&nbsp;dimensioning&nbsp;and&nbsp;orthonormal&nbsp;vectors&nbsp;on&nbsp;the&nbsp;chk&nbsp;file&nbsp;as&nbsp;well&nbsp;as&nbsp;the&nbsp;rwf.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;store&nbsp;on&nbsp;the&nbsp;chk&nbsp;file&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Restore&nbsp;the&nbsp;information&nbsp;from&nbsp;the&nbsp;chk&nbsp;file&nbsp;if&nbsp;present.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;restore&nbsp;the&nbsp;information.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/165)
Generate and test d/dx V = d/dx S^-1/2 for testing.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Nx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;step-size&nbsp;10^-N&nbsp;in&nbsp;numerical&nbsp;differentiation,&nbsp;default&nbsp;4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Mxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;threashold&nbsp;10^-M&nbsp;for&nbsp;linear&nbsp;dependence&nbsp;test,&nbsp;default&nbsp;6.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/166)
PCM point density:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(5&nbsp;pts/A^2&nbsp;for&nbsp;default&nbsp;quadrature).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;pts/A^2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TSAre=N,&nbsp;forces&nbsp;old&nbsp;quadrature.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(3/167)
Size of core (for general basis input):


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;for&nbsp;internal&nbsp;basis&nbsp;sets,&nbsp;minimal&nbsp;if&nbsp;GBS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N-zeta&nbsp;core.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/168, 3/169)
Bitmap of allowed prism paths if non-zero, 0-24 in word 168, 25-49 in 169, or 168=-1/-2 for OSOnly/MDOnly




### IOp(3/172)
Damping/switching function for APF empirical dispersion.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(-5,&nbsp;see&nbsp;details&nbsp;in&nbsp;subroutines&nbsp;R6DAPF).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/173)
Range for APF switching function.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(50).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A&nbsp;value&nbsp;of&nbsp;NNNN/1000&nbsp;of&nbsp;the&nbsp;hard&nbsp;cutoff.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/174)
S6 scale factor in Grimme’s D2/D3/D3BJ dispersion.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(see&nbsp;subroutine&nbsp;R6DS6).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;S6&nbsp;to&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NNNNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A&nbsp;value&nbsp;of&nbsp;NNNNNNNN/1000000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/175)
S8 scale factor in Grimme’s D2/D3/D3BJ dispersion.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(see&nbsp;subroutine&nbsp;R6DS8).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;S8&nbsp;to&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NNNNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A&nbsp;value&nbsp;of&nbsp;NNNNNNNN/1000000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/176)
SR6 scale factor in Grimme’s D2/D3/D3BJ dispersion.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(see&nbsp;subroutine&nbsp;R6DSR6).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;SR6&nbsp;to&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NNNNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A&nbsp;value&nbsp;of&nbsp;NNNNNNNN/1000000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/177)
A1 parameter in Becke-Johnson damping for D3BJ and XDM.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(see&nbsp;subroutine&nbsp;R6DABJ/XDMABJ).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;A1&nbsp;to&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NNNNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A&nbsp;value&nbsp;of&nbsp;NNNNNN/1000000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(3/178)
A2 parameter in Becke-Johnson damping for D3BJ and XDM.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(see&nbsp;subroutine&nbsp;R6DABJ/XDMABJ).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;A2&nbsp;to&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NNNNNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A&nbsp;value&nbsp;of&nbsp;NNNNNN/1000000&nbsp;Ang.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




## Overlay 4 
### IOp(4/5)
Type of guess.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;This&nbsp;uses&nbsp;the&nbsp;Harris&nbsp;functional&nbsp;except&nbsp;for&nbsp;semi-empirical,&nbsp;for&nbsp;which&nbsp;the&nbsp;modified&nbsp;core&nbsp;Hamiltonian&nbsp;is&nbsp;diagonalized.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Skip&nbsp;out&nbsp;and&nbsp;leave&nbsp;all&nbsp;files&nbsp;as&nbsp;left&nbsp;over&nbsp;on&nbsp;the&nbsp;rwf&nbsp;from&nbsp;whatever&nbsp;was&nbsp;done&nbsp;previously.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;guess&nbsp;from&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Guessfrom&nbsp;model&nbsp;Hamiltonian,&nbsp;chosen&nbsp;via&nbsp;IOp(4/11).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Huckel&nbsp;guess&nbsp;(only&nbsp;valid&nbsp;for&nbsp;NDDO-type&nbsp;methods).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Projected&nbsp;ZDO&nbsp;guess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Renormalize&nbsp;and&nbsp;orthogonalize&nbsp;the&nbsp;coefficients&nbsp;which&nbsp;are&nbsp;on&nbsp;the&nbsp;read-write&nbsp;files.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Renormalize&nbsp;and&nbsp;orthogonalize&nbsp;intermediate&nbsp;SCF&nbsp;results&nbsp;which&nbsp;are&nbsp;on&nbsp;the&nbsp;RWF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;intermediate&nbsp;SCF&nbsp;results&nbsp;which&nbsp;are&nbsp;on&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;the&nbsp;generalized&nbsp;density&nbsp;specified&nbsp;by&nbsp;IOp(4/38)&nbsp;from&nbsp;the&nbsp;checkpoint&nbsp;file&nbsp;and&nbsp;generate&nbsp;natural&nbsp;orbitals&nbsp;from&nbsp;it.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;the&nbsp;generalized&nbsp;density&nbsp;specified&nbsp;by&nbsp;IOp(4/38)&nbsp;from&nbsp;the&nbsp;RWF&nbsp;file&nbsp;and&nbsp;generate&nbsp;natural&nbsp;orbitals&nbsp;from&nbsp;it.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10-14&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generated&nbsp;internally&nbsp;and&nbsp;correspond&nbsp;to&nbsp;0&nbsp;and&nbsp;5-8&nbsp;for&nbsp;sparse.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 16&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;orthonormal&nbsp;set&nbsp;provided&nbsp;by&nbsp;L302&nbsp;as&nbsp;MOs,&nbsp;avoiding&nbsp;any&nbsp;diagonalization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 17&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store&nbsp;unit&nbsp;matrices&nbsp;for&nbsp;a&nbsp;dummy&nbsp;guess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 18&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Copy&nbsp;orbitals&nbsp;and&nbsp;densities&nbsp;that&nbsp;are&nbsp;in&nbsp;the&nbsp;chk&nbsp;file&nbsp;without&nbsp;checking&nbsp;or&nbsp;alteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Convert&nbsp;Guess=Check&nbsp;to&nbsp;Guess=Restart&nbsp;or&nbsp;to&nbsp;generating&nbsp;guess&nbsp;depending&nbsp;on&nbsp;what&nbsp;if&nbsp;anything&nbsp;is&nbsp;on&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;simultaneous&nbsp;optimization&nbsp;recipe:&nbsp;S^-0.5*&nbsp;V.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1&nbsp;for&nbsp;PBC&nbsp;without&nbsp;alter,&nbsp;otherwise&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Re-use&nbsp;Fock&nbsp;matrices&nbsp;instead&nbsp;of&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Re-use&nbsp;orbitals&nbsp;not&nbsp;Fock&nbsp;matrices.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;the&nbsp;name&nbsp;of&nbsp;a&nbsp;checkpoint&nbsp;file&nbsp;from&nbsp;the&nbsp;input&nbsp;stream&nbsp;and&nbsp;read&nbsp;guess&nbsp;MOs&nbsp;from&nbsp;it,&nbsp;or&nbsp;read&nbsp;an&nbsp;option&nbsp;for&nbsp;how&nbsp;to&nbsp;generate&nbsp;the&nbsp;guess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


Note that variable IGuess here has 4,3,2,1 corresponding to 1,2,3,4 above. IGuess values of 10-14 are generatedinternally and are the sparse versions of 0 and 5-8.




### IOp(4/6)
`L401`: Projection, orthogonalization, and checking of initial guess.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1&nbsp;except&nbsp;3&nbsp;for&nbsp;IOp(129)=1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;projected&nbsp;read-in&nbsp;guess,&nbsp;even&nbsp;when&nbsp;bases&nbsp;are&nbsp;identical.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Suppress&nbsp;projection.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Project&nbsp;only&nbsp;if&nbsp;basis&nbsp;sets&nbsp;are&nbsp;different.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;orthogonalization&nbsp;(perform&nbsp;if&nbsp;Guess=Cards).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Schmidt&nbsp;orthogonalize&nbsp;guess&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Suppress&nbsp;orthogonalization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;MO&nbsp;checking&nbsp;(check&nbsp;if&nbsp;Guess=Cards&nbsp;or&nbsp;Guess=Mix).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check&nbsp;MOs&nbsp;for&nbsp;othornormality.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;check&nbsp;MOs&nbsp;for&nbsp;othornormality.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;all&nbsp;3&nbsp;to&nbsp;on&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;all&nbsp;3&nbsp;to&nbsp;off.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/8)
`L401`: Alteration of configuration.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;pairs&nbsp;of&nbsp;integers&nbsp;in&nbsp;free&nbsp;format&nbsp;indicating&nbsp;which&nbsp;pairs&nbsp;of&nbsp;MO’s&nbsp;are&nbsp;to&nbsp;be&nbsp;interchanged.&nbsp;&nbsp;Pairs&nbsp;are&nbsp;read&nbsp;until&nbsp;a&nbsp;blank&nbsp;card&nbsp;is&nbsp;encountered.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;a&nbsp;permutation&nbsp;of&nbsp;the&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;alter&nbsp;configuration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;alteration&nbsp;information&nbsp;from&nbsp;the&nbsp;read-write&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;alpha&nbsp;orbitals&nbsp;for&nbsp;guess&nbsp;for&nbsp;both&nbsp;alpha&nbsp;and&nbsp;beta.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Biorthogonalize&nbsp;UHF&nbsp;MOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


Note: If the configuration is altered on an open shell system, two sets of data as described above will be expected, first for alpha, second for beta.




### IOp(4/9)
`L401`:  SCF symmetry control.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;same&nbsp;as&nbsp;104&nbsp;except&nbsp;4&nbsp;for&nbsp;IGuess=16,&nbsp;and&nbsp;204&nbsp;if&nbsp;C1&nbsp;symmetry.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;groups&nbsp;of&nbsp;irreducible&nbsp;representations&nbsp;to&nbsp;combine&nbsp;in&nbsp;the&nbsp;SCF.&nbsp;These&nbsp;are&nbsp;read&nbsp;before&nbsp;any&nbsp;orbitals&nbsp;and&nbsp;before
alteration&nbsp;commands.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;no&nbsp;symmetry&nbsp;in&nbsp;the&nbsp;SCF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pick&nbsp;up&nbsp;the&nbsp;symmetry&nbsp;mixing&nbsp;information&nbsp;from&nbsp;the&nbsp;alteration&nbsp;read-write&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;full&nbsp;Abelian&nbsp;point&nbsp;group,&nbsp;as&nbsp;represented&nbsp;by&nbsp;the&nbsp;symmetry&nbsp;adapted&nbsp;basis&nbsp;functions&nbsp;produced&nbsp;by&nbsp;link&nbsp;301.&nbsp;Initial&nbsp;guess&nbsp;orbital&nbsp;symmetries&nbsp;are&nbsp;assigned.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Use&nbsp;symmetry&nbsp;in&nbsp;SCF&nbsp;if&nbsp;possible,&nbsp;but&nbsp;do&nbsp;not&nbsp;assign&nbsp;initial&nbsp;guess&nbsp;Abelian&nbsp;symmetries).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Localize&nbsp;all&nbsp;occupied&nbsp;orbitals&nbsp;together&nbsp;and&nbsp;all&nbsp;virtual&nbsp;orbitals&nbsp;together.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Localize&nbsp;the&nbsp;orbitals&nbsp;within&nbsp;the&nbsp;selected&nbsp;or&nbsp;defaulted&nbsp;symmetry.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Localize&nbsp;all&nbsp;occupied&nbsp;and&nbsp;virtual&nbsp;orbitals&nbsp;together.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;localize.&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Assign&nbsp;orbital&nbsp;symmetries&nbsp;for&nbsp;printing&nbsp;in&nbsp;full&nbsp;symmetry.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;assign&nbsp;orbital&nbsp;symmetries&nbsp;in&nbsp;full&nbsp;symmetry.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;the&nbsp;guess&nbsp;orbitals&nbsp;to&nbsp;have&nbsp;the&nbsp;Abelian&nbsp;symmetry.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NN0000&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;localization&nbsp;method&nbsp;NN-1&nbsp;(see&nbsp;LocMO).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


This option can cause the symmetry adapted basis function common blocks to be modified.




### IOp(4/11)
`L401`:  Type of Guess.


For iterative ZDO Guess:


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;old&nbsp;path&nbsp;using&nbsp;old&nbsp;Huckel.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Best&nbsp;available&nbsp;(8,4&nbsp;in&nbsp;order&nbsp;of&nbsp;preference).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Old&nbsp;Huckel.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CNDO.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;INDO.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;New&nbsp;Huckel.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Iterative&nbsp;extended&nbsp;Huckel.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Harris,&nbsp;converted&nbsp;to&nbsp;IGuess=3&nbsp;and&nbsp;IZDO=3&nbsp;here.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Harris&nbsp;with&nbsp;interpolated&nbsp;QEq&nbsp;atomic&nbsp;charges,&nbsp;converted&nbsp;to&nbsp;IGuess=3&nbsp;IZDO=5&nbsp;here.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Harris&nbsp;with&nbsp;new&nbsp;densities.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Iterated&nbsp;Harris&nbsp;with&nbsp;QEq&nbsp;guess,&nbsp;converted&nbsp;to&nbsp;IGuess=3&nbsp;IZDO=7.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Unused.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NYI?&nbsp;Harris&nbsp;using&nbsp;charges&nbsp;from&nbsp;previous&nbsp;SCF,&nbsp;converted&nbsp;to&nbsp;IGuess=3&nbsp;IZDO=9.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


For unprojected single diagonalization guess:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default(1&nbsp;for&nbsp;DFTB,&nbsp;2&nbsp;for&nbsp;AM1/PM6,&nbsp;3&nbsp;for&nbsp;).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;bare&nbsp;core&nbsp;matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dress&nbsp;core&nbsp;Hamiltonian&nbsp;with&nbsp;QEq-based&nbsp;density.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Harris&nbsp;Functional&nbsp;with&nbsp;old&nbsp;densities.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Neutral&nbsp;atom&nbsp;AM1/PMx&nbsp;guess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Harris&nbsp;functional&nbsp;with&nbsp;interpolated&nbsp;QEq&nbsp;charges.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Harris&nbsp;functional&nbsp;with&nbsp;iterated&nbsp;charges.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Harris&nbsp;functional&nbsp;with&nbsp;iterated&nbsp;charges&nbsp;starting&nbsp;from&nbsp;QEq.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Harris&nbsp;Functional&nbsp;with&nbsp;new&nbsp;densities.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Harris&nbsp;using&nbsp;charges&nbsp;from&nbsp;previous&nbsp;SCF&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;same&nbsp;as&nbsp;2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;at&nbsp;least&nbsp;SG1&nbsp;in&nbsp;Harris&nbsp;guess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;at&nbsp;least&nbsp;FineGrid&nbsp;in&nbsp;Harris&nbsp;guess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;at&nbsp;least&nbsp;UltraFine&nbsp;in&nbsp;Harris&nbsp;guess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 400&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;an&nbsp;unpruned&nbsp;(199,590)&nbsp;or&nbsp;(399,590)&nbsp;grid&nbsp;depending&nbsp;on&nbsp;the&nbsp;range&nbsp;of&nbsp;primitive&nbsp;exponents..&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 500&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use(399,974)&nbsp;and&nbsp;10^-12&nbsp;in&nbsp;Harris&nbsp;functional.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;energy&nbsp;in&nbsp;Gen(43)&nbsp;for&nbsp;Harris&nbsp;functional.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMMM00000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;functional&nbsp;MMMM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/13)
`L401`: Mixing of orbitals.


* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;mixing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mix&nbsp;HOMO&nbsp;and&nbsp;LUMO&nbsp;(skipping&nbsp;beta&nbsp;high-spin&nbsp;orbitals&nbsp;for&nbsp;GHF).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;Mix&nbsp;HOMO&nbsp;and&nbsp;LUMO&nbsp;to&nbsp;make&nbsp;complex&nbsp;guess&nbsp;for&nbsp;CRHF&nbsp;and&nbsp;CUHF&nbsp;if&nbsp;generating&nbsp;RUHF&nbsp;guess,&nbsp;otherwise&nbsp;do&nbsp;nothing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* >0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bits&nbsp;request&nbsp;actions&nbsp;as&nbsp;follows:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   0:&nbsp;Mix&nbsp;HOMO&nbsp;and&nbsp;LUMO&nbsp;(skipping&nbsp;beta&nbsp;high-spin&nbsp;virtuals&nbsp;for&nbsp;GHF),&nbsp;done&nbsp;after&nbsp;complex/spin&nbsp;mixings.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   1:&nbsp;Do&nbsp;complex&nbsp;mixing,&nbsp;changing&nbsp;spin&nbsp;direction&nbsp;for&nbsp;GHF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   2:&nbsp;Use&nbsp;real&nbsp;rather&nbsp;than&nbsp;imaginary&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   3:&nbsp;Flip&nbsp;sign&nbsp;of&nbsp;complex&nbsp;mixing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   4:&nbsp;Read&nbsp;in&nbsp;a&nbsp;spin-vector&nbsp;and&nbsp;rotate&nbsp;to&nbsp;align&nbsp;spins&nbsp;in&nbsp;this&nbsp;direction&nbsp;instead&nbsp;of&nbsp;Z.&nbsp;GHF&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   5:&nbsp;Read&nbsp;in&nbsp;two&nbsp;spin-vectors&nbsp;and&nbsp;use&nbsp;them&nbsp;for&nbsp;alternate&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   6:&nbsp;Reverse&nbsp;rotation&nbsp;direction&nbsp;applied&nbsp;to&nbsp;spin.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note&nbsp;that&nbsp;this&nbsp;will&nbsp;usually&nbsp;destroy&nbsp;both&nbsp;spatial&nbsp;and&nbsp;alpha/beta&nbsp;symmetry.&nbsp;The&nbsp;mixing&nbsp;is&nbsp;done&nbsp;after&nbsp;any&nbsp;alterations.&nbsp;Bits&nbsp;1-3&nbsp;are&nbsp;only&nbsp;relevant&nbsp;for&nbsp;complex&nbsp;wfns.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/14)
`L401`: Reading of specific orbitals.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;For&nbsp;alpha&nbsp;orbitals,&nbsp;read&nbsp;one&nbsp;card&nbsp;with&nbsp;the&nbsp;format&nbsp;for&nbsp;the&nbsp;orbitals,&nbsp;followed&nbsp;by&nbsp;zero&nbsp;or&nbsp;more&nbsp;sets&nbsp;of&nbsp;IVec&nbsp;(I5):&nbsp;vector&nbsp;to&nbsp;replace.&nbsp;If&nbsp;IVec&nbsp;is&nbsp;-1,&nbsp;all&nbsp;NBasis&nbsp;vectors&nbsp;follow.(Vector(I),&nbsp;I=1,&nbsp;NBasis):&nbsp;vector&nbsp;in&nbsp;the&nbsp;specified&nbsp;format.&nbsp;Input&nbsp;is&nbsp;terminated&nbsp;by&nbsp;IVec=0.&nbsp;For&nbsp;b&nbsp;orbitals,&nbsp;the&nbsp;same&nbsp;format&nbsp;as&nbsp;for&nbsp;a&nbsp;is&nbsp;used.&nbsp;Note&nbsp;that&nbsp;if&nbsp;Alter&nbsp;is&nbsp;also&nbsp;specified,&nbsp;the&nbsp;replacements&nbsp;are&nbsp;read&nbsp;before&nbsp;the&nbsp;corr.&nbsp;alterations&nbsp;(thus&nbsp;the&nbsp;order&nbsp;is&nbsp;a&nbsp;orbitals,&nbsp;a&nbsp;alterations,&nbsp;b&nbsp;orbitals,&nbsp;b&nbsp;alterations).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;Read&nbsp;using&nbsp;the&nbsp;format&nbsp;described&nbsp;in&nbsp;Routine&nbsp;RdMO2.&nbsp;Here&nbsp;a&nbsp;range&nbsp;of&nbsp;MOs&nbsp;is&nbsp;indicated&nbsp;by&nbsp;two&nbsp;integers&nbsp;followed&nbsp;by&nbsp;an&nbsp;integer&nbsp;giving&nbsp;the&nbsp;number&nbsp;of&nbsp;basis&nbsp;functions.&nbsp;Then&nbsp;a&nbsp;list&nbsp;of&nbsp;MO&nbsp;energies&nbsp;are&nbsp;given.&nbsp;Lastly,&nbsp;the&nbsp;MO&nbsp;coefficients&nbsp;are&nbsp;read&nbsp;in&nbsp;sequence.&nbsp;All&nbsp;of&nbsp;the&nbsp;reading&nbsp;is&nbsp;carried&nbsp;out&nbsp;in&nbsp;free&nbsp;format.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Orbitals&nbsp;are&nbsp;assumed&nbsp;to&nbsp;have&nbsp;mixed&nbsp;normalization&nbsp;for&nbsp;Cartesian&nbsp;d&nbsp;and&nbsp;higher&nbsp;functions&nbsp;(equivalent&nbsp;to&nbsp;having&nbsp;AdjMO&nbsp;applied&nbsp;to&nbsp;them).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reorder&nbsp;d&nbsp;and&nbsp;f&nbsp;coefficients&nbsp;from&nbsp;the&nbsp;order&nbsp;used&nbsp;in&nbsp;NWChem&nbsp;(as&nbsp;of&nbsp;January,&nbsp;2013)&nbsp;to&nbsp;the&nbsp;conventional&nbsp;order&nbsp;used&nbsp;in&nbsp;Gaussian.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 900&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;permutation&nbsp;arrays&nbsp;for&nbsp;p&nbsp;and&nbsp;higher&nbsp;functions&nbsp;for&nbsp;use&nbsp;in&nbsp;reordering&nbsp;read-in&nbsp;MO&nbsp;coefficients.&nbsp;(NYI)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/15)
`L401`: Spin-state for initial guess.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;multiplicity&nbsp;in&nbsp;/Mol/.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;multiplicity&nbsp;N.&nbsp;Useful&nbsp;for&nbsp;generating&nbsp;guesses&nbsp;for&nbsp;open-shell&nbsp;singlets&nbsp;or&nbsp;unusual&nbsp;spin&nbsp;states&nbsp;involving&nbsp;orthogonal&nbsp;orbs&nbsp;by&nbsp;treating&nbsp;them&nbsp;as&nbsp;high-spin&nbsp;in&nbsp;the&nbsp;guess&nbsp;(which&nbsp;only&nbsp;does&nbsp;UHF).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/16)
`L401`: Whether to translate basis functions of read in guess.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;basis&nbsp;functions&nbsp;as&nbsp;is.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Translate&nbsp;to&nbsp;the&nbsp;current&nbsp;atomic&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Translate&nbsp;to&nbsp;the&nbsp;current&nbsp;atomic&nbsp;coordinates,&nbsp;and&nbsp;determine&nbsp;an&nbsp;overall&nbsp;rotation&nbsp;to&nbsp;provide&nbsp;to&nbsp;the&nbsp;read-in&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/17)
`L402`:  Number of open-shell orbitals (not electrons).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number&nbsp;of&nbsp;open&nbsp;electrons.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L405`: Number of electrons in the CAS space.




### IOp(4/18)
`L402`: Number of orbitals in CI. Default is number of open shells.


Number of orbitals in the CAS space.




### IOp(4/19)
`L402`: Spin change in CI (default based on multiplicity).
`L405`: Truncation level for excitations — default full CAS.




### IOp(4/20)
`L402`: Type of model. (This is also tested in L401 to see whether atomic numbers greater than 102 are special flags).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(AM1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CNDO.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;INDO.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MINDO/3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MNDO.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AM1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Unused.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PM3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PM3&nbsp;with&nbsp;mechanics&nbsp;correction.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dreiding&nbsp;mechanics.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UFF&nbsp;mechanics.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AMBER&nbsp;mechanics.&nbsp;&nbsp;&nbsp;&nbsp;
* 12&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MM2&nbsp;mechanics.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 13&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MM3&nbsp;mechanics.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 14&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Extended&nbsp;Huckel,&nbsp;Hoffmann&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 15&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Extended&nbsp;Huckel,&nbsp;Muller&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 16&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Extended&nbsp;Huckel,&nbsp;Initial&nbsp;guess&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 17&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;External&nbsp;program.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 18&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MMFF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 19&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QFF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/21)
`L402`: SCF type.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(no&nbsp;Pulay,&nbsp;no&nbsp;Camp-King,&nbsp;3/4&nbsp;point&nbsp;on&nbsp;unless&nbsp;Pulay&nbsp;or&nbsp;Camp-King,&nbsp;use&nbsp;pseudo-diagonalization).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3/4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;3/4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;Pulay&nbsp;(DIIS).&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pulay.&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;Camp-King.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Camp-King.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;pseudo-diagonalization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;pseudo-diagonalization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L405`: Flags for MCSCF.


* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;options&nbsp;from&nbsp;input&nbsp;stream.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Slater&nbsp;determinants.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Just&nbsp;list&nbsp;configurations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;determinant&nbsp;basis&nbsp;with&nbsp;Sz=b/2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Write&nbsp;unformatted&nbsp;file&nbsp;(NDATA)&nbsp;of&nbsp;symbolic&nbsp;matrix&nbsp;elements.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Write&nbsp;formatted&nbsp;file&nbsp;of&nbsp;symbolic&nbsp;matrix&nbsp;elements.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/22)
`L402`: Derivatives to do:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1st&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2nd&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;
* 12&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Restart&nbsp;2nd&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;1st&nbsp;derivatives&nbsp;analytically&nbsp;if&nbsp;possible.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/23)
`L402`: Number of iterations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L405`: NDiag.




### IOp(4/24)
`L402`: Whether to update orbitals, eigenvalues, /Mol/, and ILSW on the RWF.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(don’t&nbsp;update).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update,&nbsp;multiplying&nbsp;by&nbsp;S^-1/2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;update.&nbsp;(For&nbsp;Opt=MNDOFC).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update,&nbsp;but&nbsp;don’t&nbsp;convert&nbsp;from&nbsp;Lowdin&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update&nbsp;second&nbsp;force&nbsp;array&nbsp;instead&nbsp;of&nbsp;first.&nbsp;(For&nbsp;Opt=MNDOFC).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L405`: NRow.




### IOp(4/25)
`L402`: Wavefunction.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Same&nbsp;as&nbsp;1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Single&nbsp;determinant,&nbsp;RHF/UHF&nbsp;from&nbsp;IOp(4/5).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ROHF&nbsp;(NYI).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bi-radical&nbsp;1/2&nbsp;CI&nbsp;(only&nbsp;for&nbsp;MINDO3,&nbsp;MNDO,&nbsp;AM1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Closed-shell&nbsp;1/3&nbsp;CI&nbsp;(only&nbsp;for&nbsp;MINDO3,&nbsp;MNDO,&nbsp;AM1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;General&nbsp;CI,&nbsp;using&nbsp;specified&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;General&nbsp;CI,&nbsp;with&nbsp;N&nbsp;microstates&nbsp;read&nbsp;in.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L405`: 10 binary switches.




### IOp(4/26)
Whether to mix orbitals in generated guess density.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;mix&nbsp;valence&nbsp;occupieds&nbsp;with&nbsp;0.05&nbsp;au&nbsp;(according&nbsp;to&nbsp;ZDO)&nbsp;of&nbsp;the&nbsp;HOMO&nbsp;and&nbsp;virtuals&nbsp;within&nbsp;0.15&nbsp;au.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;mix&nbsp;valence&nbsp;orbitals&nbsp;and&nbsp;an&nbsp;equal&nbsp;number&nbsp;of&nbsp;virtuals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;mix&nbsp;all&nbsp;equally.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Equal&nbsp;occupations&nbsp;of&nbsp;the&nbsp;lowest&nbsp;N&nbsp;virtuals&nbsp;and&nbsp;high&nbsp;N&nbsp;occupieds.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/28)
`L402`: SCF Convergence (10^-N, default 10^-7).




### IOp(4/29)
`L405`: Number of core orbitals.




### IOp(4/33)
Printing of guess.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;printing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;the&nbsp;MO&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;everything.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/34)
Dump option.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;dump.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;on&nbsp;all&nbsp;possible&nbsp;printing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/35)
Overlap matrix.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(copy&nbsp;on&nbsp;disk&nbsp;is&nbsp;used).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Overlap&nbsp;assumed&nbsp;to&nbsp;be&nbsp;unity.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Copy&nbsp;on&nbsp;disk&nbsp;is&nbsp;used.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/36)
ZIndo reformatting.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;reformat&nbsp;ZIndo&nbsp;integrals&nbsp;and&nbsp;wavefunction&nbsp;into&nbsp;RWF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/37)
`L402`: Selection of old MNDO parameters.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Defaults.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Old&nbsp;Si&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Old&nbsp;S&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/38)
Generalized density to use for natural orbitals.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(-1,&nbsp;current&nbsp;for&nbsp;method&nbsp;on&nbsp;chk).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Density&nbsp;number&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/39)
Angle for mixing during Guess=Mix.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Pi/4).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pi/N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/43)
`L402`: Handling of background charge distribution. 


* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;21&nbsp;for&nbsp;MM,&nbsp;22&nbsp;for&nbsp;everything&nbsp;else.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Consider&nbsp;external&nbsp;charges.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;consider&nbsp;external&nbsp;charges.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Consider&nbsp;self-consistent&nbsp;solvent&nbsp;charges.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;consider&nbsp;self-consistent&nbsp;solvent&nbsp;charges.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* `L405`:&nbsp;=&nbsp;IDiEij:&nbsp;=&nbsp;switch&nbsp;for&nbsp;direct&nbsp;matrix&nbsp;element&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For&nbsp;normal&nbsp;route,&nbsp;with&nbsp;all&nbsp;matrix&nbsp;elements&nbsp;calculated&nbsp;here&nbsp;and&nbsp;stored&nbsp;on&nbsp;disk.&nbsp;Configs&nbsp;printed&nbsp;as&nbsp;normal.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For&nbsp;direct&nbsp;route.&nbsp;Eij’s&nbsp;calculated&nbsp;here&nbsp;and&nbsp;stored&nbsp;on&nbsp;disk.&nbsp;A&nbsp;flag&nbsp;is&nbsp;automatically&nbsp;sent&nbsp;to&nbsp;L510&nbsp;to&nbsp;tell&nbsp;it&nbsp;to&nbsp;compute&nbsp;the&nbsp;remaining&nbsp;matrix&nbsp;elements&nbsp;directly.This&nbsp;type&nbsp;of&nbsp;computation&nbsp;can&nbsp;only&nbsp;be&nbsp;done&nbsp;in&nbsp;a&nbsp;CAS&nbsp;comp.&nbsp;Also&nbsp;L510&nbsp;must&nbsp;use&nbsp;Lanczos.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Like&nbsp;option&nbsp;1,&nbsp;but&nbsp;all&nbsp;configurations&nbsp;are&nbsp;printed.&nbsp;This&nbsp;will&nbsp;be&nbsp;the&nbsp;only&nbsp;way&nbsp;to&nbsp;print&nbsp;configs&nbsp;in&nbsp;a&nbsp;direct&nbsp;matrix&nbsp;element&nbsp;calc,&nbsp;since&nbsp;there&nbsp;can&nbsp;be&nbsp;many&nbsp;thousands&nbsp;in&nbsp;a&nbsp;large&nbsp;CAS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/44)
`L405`: Prepare input for CAS-MPZ when set to 1.




### IOp(4/45)
Ipairs= number of GVB pairs in GVBCAS.


* 0      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;No&nbsp;pairs,&nbsp;normal&nbsp;CAS&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There&nbsp;are&nbsp;N&nbsp;pairs:&nbsp;2*n&nbsp;extra&nbsp;orbitals&nbsp;and&nbsp;electrons&nbsp;will&nbsp;be&nbsp;added&nbsp;into&nbsp;the&nbsp;active&nbsp;space&nbsp;later.&nbsp;L405&nbsp;performs&nbsp;a&nbsp;CAS&nbsp;on&nbsp;the&nbsp;inner&nbsp;space,&nbsp;and&nbsp;sets&nbsp;up&nbsp;L510&nbsp;to&nbsp;compute&nbsp;extra&nbsp;matrix&nbsp;elements&nbsp;etc.&nbsp;implicitly.&nbsp;This&nbsp;is&nbsp;a&nbsp;normal&nbsp;GVBCAS&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There&nbsp;are&nbsp;N&nbsp;pairs:&nbsp;2*n&nbsp;orbitals&nbsp;and&nbsp;electrons&nbsp;of&nbsp;the&nbsp;specified&nbsp;CAS&nbsp;are&nbsp;to&nbsp;be&nbsp;considered&nbsp;to&nbsp;be&nbsp;GVB&nbsp;type&nbsp;orbitals&nbsp;when&nbsp;generating&nbsp;configs/matrix&nbsp;elements.&nbsp;L510&nbsp;will&nbsp;execute&nbsp;normally.&nbsp;This&nbsp;occupies&nbsp;as&nbsp;such&nbsp;space&nbsp;as&nbsp;a&nbsp;full&nbsp;CAS&nbsp;in&nbsp;this&nbsp;link,&nbsp;but&nbsp;is&nbsp;smaller&nbsp;subsequently.&nbsp;This&nbsp;is&nbsp;the&nbsp;GVBCAS&nbsp;test&nbsp;mode.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/46)
CI basis in CASSCF.


* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hartree-Waller&nbsp;functions&nbsp;for&nbsp;singlets.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hartree-Waller&nbsp;functions&nbsp;for&nbsp;triplets.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Slater&nbsp;determinants.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Write&nbsp;SME&nbsp;on&nbsp;disk.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/47)
Convert to sparse storage after generating guess.


* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;sparse&nbsp;storage&nbsp;Fock&nbsp;matrix&nbsp;for&nbsp;guess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;full&nbsp;storage&nbsp;Fock&nbsp;matrix&nbsp;for&nbsp;guess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No,&nbsp;use&nbsp;the&nbsp;Lewis&nbsp;dot&nbsp;structure&nbsp;to&nbsp;generate&nbsp;a&nbsp;sparse&nbsp;guess&nbsp;directly.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(-1&nbsp;if&nbsp;sparse&nbsp;is&nbsp;turned&nbsp;on).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/48)
`L402`: Whether to do (sparse) conjugate gradient methods.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;Use&nbsp;Lewis&nbsp;dot&nbsp;structure&nbsp;guess&nbsp;density.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;Use&nbsp;diagonal&nbsp;guess&nbsp;density.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/60)
Override standard values of IRadAn.




### IOp(4/61)
Override standard values of IRanWt.




### IOp(4/62)
Override standard values of IRanGd.




### IOp(4/63)
Flags for which terms to include in MM energy.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(111111).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;on&nbsp;all&nbsp;terms,&nbsp;r^-1&nbsp;Coulomb.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;on&nbsp;all&nbsp;terms,&nbsp;r^-2&nbsp;Coulomb.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;on&nbsp;non-bonded&nbsp;terms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;on&nbsp;inversions/improper&nbsp;torsions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;on&nbsp;torsions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;on&nbsp;angle&nbsp;bending.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;on&nbsp;bond&nbsp;stretches.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/65)
Tighten the zero thresholds as the SCF calculation proceeds.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;Yes,&nbsp;initial&nbsp;threshold&nbsp;5×10-5.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;variable&nbsp;thresholds.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;initial&nbsp;threshold&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N<-100&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;initial&nbsp;threshold&nbsp;5&nbsp;x&nbsp;10&nbsp;^N+100.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/66)
Dielectric constant to be used in MM calculations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Eps&nbsp;=&nbsp;1.0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Eps&nbsp;=&nbsp;N&nbsp;/&nbsp;1000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/67)
Whether to use QEq to assign MM charges.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(211&nbsp;if&nbsp;UFF,&nbsp;2&nbsp;otherwise,&nbsp;1⇒&nbsp;221).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;QEq.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;do&nbsp;QEq.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(20).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;for&nbsp;atoms&nbsp;which&nbsp;were&nbsp;not&nbsp;explicitly&nbsp;typed.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;for&nbsp;all&nbsp;atoms&nbsp;regardless&nbsp;of&nbsp;typing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(200).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;for&nbsp;atoms&nbsp;which&nbsp;have&nbsp;charge&nbsp;specified&nbsp;or&nbsp;defaulted&nbsp;to&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;for&nbsp;all&nbsp;atoms&nbsp;regardless&nbsp;of&nbsp;initial&nbsp;charge.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/68)
`L402`: Convergencecriterion for micro-iterations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/69)
Whether to do a new additional guess in addition to reading orbitals from the RWF.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes&nbsp;if&nbsp;no&nbsp;Guess=Alter,&nbsp;Harris&nbsp;guess,&nbsp;and&nbsp;not&nbsp;a&nbsp;small&nbsp;geometry&nbsp;step.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;do&nbsp;the&nbsp;extra&nbsp;guess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;the&nbsp;extra&nbsp;guess&nbsp;and&nbsp;store&nbsp;as&nbsp;the&nbsp;initial&nbsp;Fock&nbsp;matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;the&nbsp;extra&nbsp;guess&nbsp;regardless.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store&nbsp;the&nbsp;normal&nbsp;guess&nbsp;as&nbsp;the&nbsp;alternative&nbsp;(for&nbsp;SimOpt).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10&nbsp;for&nbsp;PBC,&nbsp;20&nbsp;otherwise).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;the&nbsp;Harris&nbsp;guess&nbsp;as&nbsp;an&nbsp;initial&nbsp;Fock&nbsp;matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Just&nbsp;generate&nbsp;orbitals&nbsp;from&nbsp;the&nbsp;Harris&nbsp;guess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/71)
`L402`: Write out AM1 integrals.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/72)
Irreps to keep in MCSCF CI-wavefunction.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* IJKLMNOP&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;List&nbsp;of&nbsp;up&nbsp;to&nbsp;8&nbsp;irreducible&nbsp;representation&nbsp;numbers&nbsp;to&nbsp;include.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/80)
The maximum conjugate gradient step size (MMNN).


* 0000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;maximum&nbsp;step&nbsp;size.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step&nbsp;size&nbsp;of&nbsp;MM.NN.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/81)
Sparse SCF Parameters.


* MM&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum&nbsp;number&nbsp;of&nbsp;SCF&nbsp;DIIS&nbsp;cycles.&nbsp;(MM=00&nbsp;defaults&nbsp;to&nbsp;20&nbsp;cycles,&nbsp;MM=01&nbsp;turns&nbsp;DIIS&nbsp;off).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NN00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;F(Mu,Nu)&nbsp;atom–atom&nbsp;cutoff&nbsp;criterion&nbsp;(angstroms)&nbsp;Mu,&nbsp;Nu&nbsp;are&nbsp;basis&nbsp;functions&nbsp;on&nbsp;the&nbsp;same&nbsp;atom.(defaults&nbsp;to&nbsp;no&nbsp;F(Mu,Nu)&nbsp;cutoff).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* PP0000&nbsp;&nbsp;&nbsp;&nbsp;F(Mu,Lambda)&nbsp;atom–atom&nbsp;cutoff&nbsp;criterion&nbsp;(angstroms)&nbsp;Mu,&nbsp;Lambda&nbsp;are&nbsp;basis&nbsp;functions&nbsp;on&nbsp;different&nbsp;atoms.&nbsp;(defaults&nbsp;to&nbsp;15&nbsp;angstroms).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/82)
Conjugate-Gradient Parameters.


* MM&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum&nbsp;number&nbsp;of&nbsp;CG&nbsp;cycles&nbsp;per&nbsp;SCF&nbsp;iteration.&nbsp;(defaults&nbsp;to&nbsp;4&nbsp;CG&nbsp;cycles).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NN00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum&nbsp;number&nbsp;of&nbsp;purification&nbsp;cycles&nbsp;per&nbsp;CG&nbsp;iteration.&nbsp;(defaults&nbsp;to&nbsp;3&nbsp;cycles).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;use&nbsp;CG&nbsp;DIIS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;CG&nbsp;DIIS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000000&nbsp;&nbsp;&nbsp;&nbsp;Polak-Ribiere&nbsp;CG&nbsp;minimization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Fletcher-Reeves&nbsp;CG&nbsp;minimization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;diagonal&nbsp;preconditioning&nbsp;in&nbsp;Conjugate-Gradient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;preconditioning.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/90)
`L402`: Step size in dynamics (see IOp(4/8) in L118).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(0.025&nbsp;femtosec).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N*0.0001&nbsp;femtosec.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/91)
`L402`: Trajectory type and initial velocity (see IOp(4/9) in L118).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;4).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;initial&nbsp;Cartesian&nbsp;velocity.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;initial&nbsp;mass&nbsp;weighted&nbsp;Cartesian&nbsp;velocity.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/92)
`L402`: Maximum points in one trajectory (see IOp(4/42) in L118).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(100).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;points&nbsp;in&nbsp;trajectory.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/93)
`L402`: Read isotopes for trajectory (see IOp(4/45) in L118).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;read&nbsp;isotopes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;isotopes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/110)
`L402`: Scaling of rigid fragment steps during micro-iterations.


* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scale&nbsp;by&nbsp;(#&nbsp;fragatoms)^-1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scale&nbsp;by&nbsp;1/SQRT&nbsp;(#&nbsp;fragatoms).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scale&nbsp;by&nbsp;N/1000.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/111)
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/112)
Compression for ONIOM.


* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compressed&nbsp;Hessian&nbsp;over&nbsp;active&nbsp;atoms.&nbsp;For&nbsp;MM&nbsp;calculations&nbsp;on&nbsp;the&nbsp;real&nbsp;system,&nbsp;this&nbsp;converts&nbsp;a&nbsp;second&nbsp;derivative&nbsp;calculation&nbsp;to&nbsp;just&nbsp;forces,&nbsp;since&nbsp;the&nbsp;real&nbsp;system&nbsp;2nd&nbsp;derivatives&nbsp;are&nbsp;computed&nbsp;during&nbsp;micro-iterations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N≥4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Full&nbsp;storage.&nbsp;(default)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/113)
`L402`: Which external method to use for ONIOM calculations using different external commands for 2 or more levels.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(First&nbsp;external&nbsp;command).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N^thexternal&nbsp;command&nbsp;(command&nbsp;N&nbsp;in&nbsp;file&nbsp;747).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/114)
Which ONIOM system is being done, which is sometimes needed by external procedures.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Real&nbsp;system.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Model&nbsp;system&nbsp;for&nbsp;2-layer,&nbsp;middle&nbsp;for&nbsp;3-layer.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Small&nbsp;model&nbsp;system&nbsp;for&nbsp;3-layer.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/115)
Mixing of orbitals for GHF/Complex testing.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No,&nbsp;unless&nbsp;generate&nbsp;guess&nbsp;for&nbsp;complex).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Make&nbsp;MO&nbsp;coefficients&nbsp;complex.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;rotate&nbsp;real&nbsp;and&nbsp;imaginary&nbsp;components&nbsp;of&nbsp;MOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mix&nbsp;alpha&nbsp;and&nbsp;beta&nbsp;orbitals&nbsp;for&nbsp;GHF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;S&nbsp;vector&nbsp;to&nbsp;apply&nbsp;to&nbsp;FC&nbsp;perturbation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;complex-style&nbsp;SR,&nbsp;SI&nbsp;for&nbsp;GHF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;FC&nbsp;perturbation&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FC&nbsp;with&nbsp;MBS&nbsp;core&nbsp;orbitals&nbsp;blanked.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Full&nbsp;FC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/116)
Functional to use in Harris guess.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;PBEPBE&nbsp;for&nbsp;HSE2PBE,&nbsp;HSE(H)1PBE&nbsp;and&nbsp;any&nbsp;functional&nbsp;involving&nbsp;the&nbsp;kinetic&nbsp;energy&nbsp;or&nbsp;Laplacian,&nbsp;the&nbsp;pure&nbsp;version&nbsp;of&nbsp;the&nbsp;functional&nbsp;for&nbsp;pure&nbsp;and&nbsp;hybrid&nbsp;GGAs,&nbsp;and&nbsp;SVWN3&nbsp;for&nbsp;HF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Functional&nbsp;#&nbsp;(see&nbsp;values&nbsp;in&nbsp;3/74).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/117)
Set flag for BD Guess=Read.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/118)
Whether to do GHF/Complex diagonalization for Harris and Core guesses.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No,&nbsp;generate&nbsp;UHF&nbsp;guess&nbsp;and&nbsp;convert.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/119)
Printing MM energy contributions and force field parameters.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(print&nbsp;contributions&nbsp;if&nbsp;#p).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;contributions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;print&nbsp;contributions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(20).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;all&nbsp;terms&nbsp;in&nbsp;the&nbsp;force&nbsp;field.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;print&nbsp;the&nbsp;force&nbsp;field.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/120)
`L402`: Number of MM microiterations allowed.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;based&nbsp;on&nbsp;&nbsp;Atoms&nbsp;but&nbsp;at&nbsp;least&nbsp;5000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/121)
Convergence of iterative Harris guess.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(0.02).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/10000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N<0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/122)
Maximum number of iterations for iterated Harris:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;20.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




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


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/128)
Whether to print analysis of projection for read-in guesses:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(122&nbsp;if&nbsp;using&nbsp;symmetry&nbsp;in&nbsp;diagonalization,&nbsp;222&nbsp;otherwise).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Symmetrically&nbsp;orthogonalize&nbsp;core&nbsp;and&nbsp;valence&nbsp;occupieds&nbsp;together.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Symmetrically&nbsp;orthogonalize&nbsp;core&nbsp;and&nbsp;valence&nbsp;occupieds&nbsp;separately.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Always&nbsp;project&nbsp;virtuals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Only&nbsp;project&nbsp;virtuals&nbsp;for&nbsp;CAS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(4/129)
Whether to read energy from chk during Guess=Read (i.e., with SCF=Skip):


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/130)
Store dispersion energy and derivatives as total?


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/131)
`L402`: Whether to include charges in MM calculations in.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(check&nbsp;ILSW&nbsp;for&nbsp;whether&nbsp;ONIOM&nbsp;or&nbsp;QM/MM-style).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ONIOM-style,&nbsp;so&nbsp;include.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;include.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(4/132)
Copy MOs from chk file to reference phase file on rwf. Reference CIS/TD amplitudes are also copied, if found on the chk file.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Copy.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Flip&nbsp;sign&nbsp;of&nbsp;MOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Flip&nbsp;sign&nbsp;of&nbsp;amplitudes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Flip&nbsp;sign&nbsp;of&nbsp;both&nbsp;MOs&nbsp;and&nbsp;amplitudes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




## Overlay 5 
### IOp(5/5)
`L502, L508`: Direct SCF control.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;the&nbsp;integrals&nbsp;off&nbsp;disk.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;2e&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;2e&nbsp;integrals&nbsp;and&nbsp;store&nbsp;in-core.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;2e&nbsp;integrals&nbsp;and&nbsp;forbid&nbsp;in-core.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NNNNx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;option&nbsp;NNNNN&nbsp;in&nbsp;control&nbsp;of&nbsp;2e&nbsp;integral&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000000&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;—&nbsp;incremental&nbsp;Fock&nbsp;matrix&nbsp;formation&nbsp;only&nbsp;for&nbsp;direct&nbsp;SCF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Form&nbsp;full&nbsp;Fock&nbsp;matrix&nbsp;every&nbsp;time.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200000&nbsp;&nbsp;&nbsp;&nbsp;Form&nbsp;delta-F&nbsp;each&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clear&nbsp;in-core&nbsp;integrals&nbsp;for&nbsp;testing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/6)
Convergence (RMS density except in L506 (SQCDF), L508 (rms rotation gradient), and L510 (Energy)).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-8,&nbsp;except&nbsp;10^-7&nbsp;for&nbsp;PBC,&nbsp;and&nbsp;10^-10&nbsp;for&nbsp;SQCDF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/7)
Maximum number of iterations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;128&nbsp;(except&nbsp;512&nbsp;in&nbsp;L503&nbsp;and&nbsp;L508,&nbsp;and&nbsp;64&nbsp;in&nbsp;L506).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;CI&nbsp;only&nbsp;in&nbsp;L510.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;CI&nbsp;and&nbsp;density&nbsp;matrices&nbsp;only&nbsp;in&nbsp;L510.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;a&nbsp;single&nbsp;iteration&nbsp;in&nbsp;L510.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/8)
`L503`: Selection of the procedure of direct minimizations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Steepest&nbsp;descent&nbsp;with&nbsp;search&nbsp;parameters&nbsp;default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Steepest&nbsp;descent&nbsp;with&nbsp;search&nbsp;parameters&nbsp;read&nbsp;(see&nbsp;below).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Classical&nbsp;SCF&nbsp;(Roothaan’s&nbsp;method&nbsp;of&nbsp;repeated&nbsp;diagonalization).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Conjugate&nbsp;gradients&nbsp;with&nbsp;search&nbsp;parameters&nbsp;default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Conjugate&nbsp;gradients&nbsp;with&nbsp;search&nbsp;parameters&nbsp;read&nbsp;(see&nbsp;below).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;search&nbsp;parameters&nbsp;are&nbsp;max.&nbsp;number&nbsp;of&nbsp;search&nbsp;points&nbsp;(I1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Min.&nbsp;number&nbsp;of&nbsp;search&nbsp;points&nbsp;(I1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initial&nbsp;step&nbsp;size,&nbsp;TAU&nbsp;(G18.5).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scaling&nbsp;factor&nbsp;for&nbsp;subseq.&nbsp;TAU&nbsp;(G20.5)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Q&nbsp;(G20.5)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L508`: Search method.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1123).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Steepest&nbsp;descent.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scaled&nbsp;steepest&nbsp;descent.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Quadratic&nbsp;convergence&nbsp;(after&nbsp;rotation&nbsp;gradient&nbsp;is&nbsp;sufficiently&nbsp;small).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Exit&nbsp;when&nbsp;NR&nbsp;point&nbsp;is&nbsp;reached,&nbsp;so&nbsp;L502&nbsp;can&nbsp;take&nbsp;over.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;linear&nbsp;search&nbsp;(full&nbsp;search).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;a&nbsp;full&nbsp;linear&nbsp;search&nbsp;to&nbsp;locate&nbsp;a&nbsp;minimum.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;a&nbsp;linear&nbsp;search&nbsp;only&nbsp;if&nbsp;the&nbsp;energy&nbsp;goes&nbsp;up&nbsp;after&nbsp;the&nbsp;initial&nbsp;step.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;handling&nbsp;of&nbsp;wrong&nbsp;curvature&nbsp;(switch&nbsp;direction).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reverse&nbsp;direction&nbsp;if&nbsp;curvature&nbsp;in&nbsp;NR&nbsp;step&nbsp;direction&nbsp;is&nbsp;wrong.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Take&nbsp;pure&nbsp;NR&nbsp;steps,&nbsp;even&nbsp;if&nbsp;curvature&nbsp;is&nbsp;wrong.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;on&nbsp;linear&nbsp;search&nbsp;and&nbsp;variable&nbsp;step&nbsp;logic.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;linear&nbsp;search&nbsp;and&nbsp;variable&nbsp;step&nbsp;logic.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L510`: Flags used.


* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IRdF2,&nbsp;read&nbsp;damping&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IFrzCI,&nbsp;freeze&nbsp;CI&nbsp;coefficients&nbsp;after&nbsp;1st&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;unformatted&nbsp;symbolic&nbsp;matrix&nbsp;elements&nbsp;from&nbsp;NDATA&nbsp;instead&nbsp;of&nbsp;RWF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;damping&nbsp;factors&nbsp;from&nbsp;cards.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Levy&nbsp;damping.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;Fock&nbsp;matrix&nbsp;restriction&nbsp;matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/9)
`L503 only`: Switch to classical SCF after density matrix has achieved a certain convergency.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;criterion&nbsp;default&nbsp;10^-3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;criterion&nbsp;read&nbsp;in&nbsp;(Format&nbsp;G16.10).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L504, L506`: Number of pair iterations.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None;&nbsp;coefficients&nbsp;are&nbsp;frozen&nbsp;at&nbsp;initial&nbsp;values&nbsp;(L504&nbsp;only,&nbsp;causes&nbsp;coefficients&nbsp;to&nbsp;be&nbsp;read&nbsp;in&nbsp;order&nbsp;11&nbsp;12&nbsp;22).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L511`: IDoV in Harris functional.




### IOp(5/10)
Error: label name not recognized
### IOp(5/11)
`L502, L503 (only 4 point), L505`:  3 and 4 Point Density extrapolation control.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Both&nbsp;three-point&nbsp;and&nbsp;four-point&nbsp;extrapolation&nbsp;are&nbsp;performed&nbsp;when&nbsp;applicable.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Three-point&nbsp;extrapolation&nbsp;is&nbsp;inhibited,&nbsp;but&nbsp;the&nbsp;program&nbsp;will&nbsp;still&nbsp;perform&nbsp;four-point&nbsp;extrapolation&nbsp;when&nbsp;possible.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Both&nbsp;three-point&nbsp;and&nbsp;four-point&nbsp;extrapolation&nbsp;schemes&nbsp;are&nbsp;‘locked&nbsp;out’&nbsp;(IE.&nbsp;disabled).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(20).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;Camp-King&nbsp;always,&nbsp;taking&nbsp;one&nbsp;step&nbsp;using&nbsp;if&nbsp;|Lpred-1|&nbsp;³&nbsp;Thresh.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;do&nbsp;Camp-King.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;Camp-King&nbsp;only&nbsp;if&nbsp;the&nbsp;energy&nbsp;rises&nbsp;by&nbsp;at&nbsp;least&nbsp;Thresh.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;1,&nbsp;but&nbsp;CK&nbsp;also&nbsp;done&nbsp;if&nbsp;the&nbsp;energy&nbsp;goes&nbsp;up.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NNN00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Threshold&nbsp;for&nbsp;CK&nbsp;is&nbsp;NNN/1000&nbsp;(step&nbsp;for&nbsp;10,&nbsp;Hartrees&nbsp;for&nbsp;30).&nbsp;Default&nbsp;is&nbsp;0.3&nbsp;for&nbsp;10,0.001&nbsp;for&nbsp;30;&nbsp;with&nbsp;30,999&nbsp;implies&nbsp;10^-10.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/12)
Whether to allocate only two N^2 arrays for RHF.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


Number of GVB pairs (L506). If non-zero, the number of orbitals in each pair is read in format (30I2). Each pair consists of the highest available occupied from the guess (after high spin orbs are accounted for) and the lowest available virtuals. If <0, pair coefficients are read; otherwise standard initial values are used.




### IOp(5/13)
`L502`:  Action on convergence failure.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Continue&nbsp;the&nbsp;run&nbsp;even&nbsp;on&nbsp;non-convergence.&nbsp;The&nbsp;ILSW&nbsp;flag&nbsp;for&nbsp;convergence&nbsp;failure&nbsp;is&nbsp;set.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Terminate&nbsp;on&nbsp;non-convergence.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/14)
`L502`:  Special functions.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;the&nbsp;current&nbsp;RHF&nbsp;run&nbsp;into&nbsp;a&nbsp;uhf&nbsp;run&nbsp;at&nbsp;the&nbsp;end&nbsp;of&nbsp;this&nbsp;link.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Terminate&nbsp;after&nbsp;computing&nbsp;the&nbsp;2e&nbsp;terms&nbsp;at&nbsp;the&nbsp;first&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Just&nbsp;recompute&nbsp;band&nbsp;structure&nbsp;from&nbsp;stored&nbsp;real-space&nbsp;Fock&nbsp;matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ADMP/FOSimult,&nbsp;later&nbsp;cycles:&nbsp;&nbsp;transform&nbsp;the&nbsp;density&nbsp;from&nbsp;L103/L121&nbsp;before&nbsp;calculating&nbsp;the&nbsp;energy&nbsp;and&nbsp;Fock&nbsp;matrices.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ADMP/FOSimult,&nbsp;first&nbsp;cycle:&nbsp;&nbsp;use&nbsp;initial&nbsp;AO&nbsp;densities.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Generalized&nbsp;energy-weighted&nbsp;density&nbsp;routines&nbsp;regardless.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;use&nbsp;GEW&nbsp;routines&nbsp;even&nbsp;for&nbsp;CP.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fit&nbsp;the&nbsp;converged&nbsp;density&nbsp;even&nbsp;if&nbsp;fitting&nbsp;is&nbsp;not&nbsp;in&nbsp;use&nbsp;during&nbsp;the&nbsp;SCF.&nbsp;Also&nbsp;redoes&nbsp;the&nbsp;fit&nbsp;at&nbsp;the&nbsp;end&nbsp;even&nbsp;if&nbsp;using&nbsp;fits&nbsp;during&nbsp;SCF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculation&nbsp;is&nbsp;performed&nbsp;(provided&nbsp;of&nbsp;course&nbsp;that&nbsp;enough&nbsp;space&nbsp;exists&nbsp;in&nbsp;the&nbsp;RW-files).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculation&nbsp;is&nbsp;bypassed.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculation&nbsp;is&nbsp;performed,&nbsp;contingent&nbsp;on&nbsp;space,&nbsp;and&nbsp;the&nbsp;system&nbsp;RW-files&nbsp;for&nbsp;the&nbsp;appropriate&nbsp;density&nbsp;matrices&nbsp;are&nbsp;updated&nbsp;(useful&nbsp;if&nbsp;one&nbsp;wants&nbsp;a&nbsp;population&nbsp;analysis).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L503`: Reordering of the orbitals (maintaining continuity of the wavefunction along the search path).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;On.&nbsp;Bessel&nbsp;criterion.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;On.&nbsp;Stronger&nbsp;individual-overlap&nbsp;criterion.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Off.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


Flags for MCSCF.


* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Skip&nbsp;valence-valence&nbsp;Fock&nbsp;matrix&nbsp;elements.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Skip&nbsp;core-valence&nbsp;Fock&nbsp;matrix&nbsp;elements.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Skip&nbsp;valence-virtual&nbsp;Fock&nbsp;matrix&nbsp;elements.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Skip&nbsp;core-valence&nbsp;Fock&nbsp;matrix&nbsp;elements.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;full&nbsp;diagonalization&nbsp;method&nbsp;rather&nbsp;than&nbsp;Lanczos.&nbsp;(Obsolete;&nbsp;use&nbsp;IOp(5/17)).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;State&nbsp;average&nbsp;density&nbsp;matrices.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/15)
Apply Abelian symmetry constraints on orbitals.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1&nbsp;for&nbsp;L502,&nbsp;2&nbsp;for&nbsp;L501&nbsp;and&nbsp;L506).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;keep&nbsp;occupation&nbsp;of&nbsp;each&nbsp;irreducible&nbsp;representation&nbsp;the&nbsp;same&nbsp;as&nbsp;the&nbsp;initial&nbsp;guess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;keep&nbsp;overall&nbsp;wavefunction&nbsp;the&nbsp;same&nbsp;as&nbsp;the&nbsp;initial&nbsp;guess,&nbsp;but&nbsp;doing&nbsp;the&nbsp;minimal&nbsp;amount&nbsp;of&nbsp;orbital&nbsp;switching&nbsp;to&nbsp;accomplish&nbsp;this.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(use&nbsp;Abelian&nbsp;symmetry&nbsp;in&nbsp;diagonalization).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Abelian&nbsp;symmetry&nbsp;in&nbsp;diagonalization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;use&nbsp;Abelian&nbsp;symmetry&nbsp;in&nbsp;diagonalization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L503`: Controls the auto adjustment of TAU.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Done.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TAU&nbsp;is&nbsp;kept&nbsp;fixed.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/16)
`L502`: Diagonalization method.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1&nbsp;for&nbsp;full&nbsp;matrices&nbsp;HF/DFT,&nbsp;-30&nbsp;for&nbsp;semi-empirical,&nbsp;4&nbsp;for&nbsp;sparse).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pseudo-diagonalization&nbsp;with&nbsp;real&nbsp;diagonalization&nbsp;every&nbsp;N^th&nbsp;cycle.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DiagD.&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;KyDiag.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pseudo-diagonalization&nbsp;whenever&nbsp;allowed&nbsp;by&nbsp;internal&nbsp;tests.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CGDMS.&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CEM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sign&nbsp;Matrix&nbsp;Method.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SNRDMS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Unused.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Jacobi&nbsp;diagonalization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;formation&nbsp;of&nbsp;the&nbsp;Fock&nbsp;matrix&nbsp;using&nbsp;full&nbsp;storage.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;formation&nbsp;of&nbsp;the&nbsp;Fock&nbsp;matrix&nbsp;using&nbsp;sparse&nbsp;storage.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;By&nbsp;eigenvalue.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;By&nbsp;energy&nbsp;least&nbsp;change.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;By&nbsp;orbital&nbsp;least&nbsp;change.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;eigenvector.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C(1)=&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C(N)=&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/17)
`L503`: Condition off-diagonal terms of the Fock matrix.


Set to zero if Abs(F(I,J)).LE.FUZZY; delete coupling terms between almost degenerate (DELTA E .LE. DEGEN) M.O. vectors.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FUZZY=1.D-10,&nbsp;DEGEN=2.D-5.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FUZZY&nbsp;and&nbsp;DEGEN&nbsp;read&nbsp;in&nbsp;(2D20.14).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L506`: Selection of virtual orbitals.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Virtuals&nbsp;obtained&nbsp;by&nbsp;diagonalization&nbsp;of&nbsp;Hamiltonians.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Virtuals&nbsp;obtained&nbsp;by&nbsp;Schmidt&nbsp;orthogonalization&nbsp;to&nbsp;occupieds.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L502, L508`: Use of symmetry.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1032&nbsp;for&nbsp;502,&nbsp;1012&nbsp;for&nbsp;508).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Choose&nbsp;LinEq&nbsp;convergence&nbsp;based&nbsp;on&nbsp;orbital&nbsp;gradient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Always&nbsp;use&nbsp;tight&nbsp;convergence.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tighten&nbsp;convergence&nbsp;by&nbsp;an&nbsp;extra&nbsp;factor&nbsp;of&nbsp;10.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If&nbsp;2E&nbsp;symmetry&nbsp;is&nbsp;on,&nbsp;symmetrize&nbsp;Fock&nbsp;matrices&nbsp;and&nbsp;require&nbsp;proper&nbsp;density&nbsp;matrix&nbsp;symmetry.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If&nbsp;2E&nbsp;symmetry&nbsp;is&nbsp;on,&nbsp;replicate&nbsp;integrals&nbsp;so&nbsp;that&nbsp;density&nbsp;matrices&nbsp;and&nbsp;wavefunctions&nbsp;need&nbsp;not&nbsp;be&nbsp;symmetric.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If&nbsp;2E&nbsp;symmetry&nbsp;is&nbsp;on,&nbsp;choose&nbsp;between&nbsp;replicating&nbsp;integrals&nbsp;and&nbsp;symmetrizing&nbsp;the&nbsp;Fock&nbsp;matrix&nbsp;based&nbsp;on&nbsp;whether&nbsp;the&nbsp;current&nbsp;density&nbsp;matrix&nbsp;is&nbsp;symmetric.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;30&nbsp;in&nbsp;502&nbsp;but&nbsp;20&nbsp;in&nbsp;508.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;the&nbsp;density&nbsp;matrix&nbsp;to&nbsp;have&nbsp;full&nbsp;symmetry&nbsp;at&nbsp;the&nbsp;first&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;the&nbsp;density&nbsp;matrix&nbsp;to&nbsp;have&nbsp;full&nbsp;symmetry&nbsp;at&nbsp;every&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1000).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If&nbsp;the&nbsp;density&nbsp;matrices&nbsp;pass&nbsp;the&nbsp;symmetry&nbsp;test,&nbsp;symmetrize&nbsp;them&nbsp;to&nbsp;ensure&nbsp;that&nbsp;they&nbsp;are&nbsp;exactly&nbsp;symmetric.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;symmetrize&nbsp;the&nbsp;density&nbsp;matrices.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(20000,&nbsp;except&nbsp;if&nbsp;IOp(8)&nbsp;requests&nbsp;old&nbsp;algorithm).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Always&nbsp;pseudocanonicalize&nbsp;in&nbsp;L508.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Only&nbsp;pseudocanonicalize&nbsp;in&nbsp;L508&nbsp;when&nbsp;doing&nbsp;a&nbsp;Newton-Raphson&nbsp;step.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L510`: MCSCF flags.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Orthogonalize&nbsp;C,O,V&nbsp;by&nbsp;separate&nbsp;Lowdin,&nbsp;then&nbsp;schmidt.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Lowdin&nbsp;orthogonalize&nbsp;C+O&nbsp;and&nbsp;V,&nbsp;then&nbsp;schmidt.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Just&nbsp;schmidt.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;use&nbsp;natural&nbsp;orbitals&nbsp;each&nbsp;iteration.&nbsp;Bad&nbsp;for&nbsp;1^st&nbsp;order&nbsp;method.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;full&nbsp;2nd&nbsp;order&nbsp;convergence.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2nd&nbsp;order&nbsp;iteration&nbsp;at&nbsp;end,&nbsp;in&nbsp;preparation&nbsp;for&nbsp;CPMCSCF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;data&nbsp;for&nbsp;multi-reference&nbsp;MP2?&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Attempt&nbsp;to&nbsp;control&nbsp;root&nbsp;flipping&nbsp;in&nbsp;CI.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;CI&nbsp;vector&nbsp;and&nbsp;use&nbsp;it&nbsp;every&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;full&nbsp;diagonalization&nbsp;method&nbsp;rather&nbsp;than&nbsp;Lanczos.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;State&nbsp;Average&nbsp;density&nbsp;matrices&nbsp;(the&nbsp;weights&nbsp;8F10.8)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;SA&nbsp;and&nbsp;prepare&nbsp;for&nbsp;SA-CPMCSCF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;SA&nbsp;and&nbsp;prepare&nbsp;for&nbsp;Gradient&nbsp;of&nbsp;Energy&nbsp;difference.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;SA&nbsp;and&nbsp;prepare&nbsp;for&nbsp;SA&nbsp;Second&nbsp;Derivative&nbsp;Computation&nbsp;(terms&nbsp;involving&nbsp;2nd&nbsp;order&nbsp;orbital&nbsp;rotation&nbsp;derivatives&nbsp;not&nbsp;included).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/18)
`L502`: Mixing when doing damping.


* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MO&nbsp;damping&nbsp;at&nbsp;all&nbsp;iterations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;damping.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dynamic&nbsp;selection&nbsp;of&nbsp;density&nbsp;damping&nbsp;based&nbsp;on&nbsp;band&nbsp;gap&nbsp;and&nbsp;DIIS&nbsp;error.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(-1&nbsp;unless&nbsp;re-optimizing&nbsp;during&nbsp;Stable=Opt).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/100&nbsp;new&nbsp;density,&nbsp;(100-N)/100&nbsp;old&nbsp;density.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L503`: Cutoff criteria in symmetry determination of M.O.S (L503). Symmetry is determined if largest off-diagonal M.O. Fock-matrix element Abs(F(I,J))>STHRS elements Abs(F(I,J))<SPAN are considered to be 0.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;STHRS=1.D-4,
SPAN=5.D-7.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;STHRS
and&nbsp;SPAN&nbsp;read&nbsp;in&nbsp;(2D20.14).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L506`:  Damping.




### IOp(5/19)
`L501, L502, L506, L508`: Override integral storage control.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Choose&nbsp;the&nbsp;best&nbsp;given&nbsp;amount&nbsp;of&nbsp;memory&nbsp;available.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;if&nbsp;possible,&nbsp;otherwise&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Forbid&nbsp;in-core:&nbsp;&nbsp;force&nbsp;re-reading&nbsp;of&nbsp;integrals&nbsp;even&nbsp;if&nbsp;they&nbsp;fit&nbsp;in&nbsp;2&nbsp;buffers&nbsp;if&nbsp;conventional,&nbsp;do&nbsp;not&nbsp;convert&nbsp;to&nbsp;in-core&nbsp;if&nbsp;direct&nbsp;and&nbsp;enough&nbsp;memory&nbsp;for&nbsp;in-core&nbsp;is&nbsp;available.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;allocation&nbsp;for&nbsp;1&nbsp;or&nbsp;2&nbsp;buffer&nbsp;case&nbsp;conventional&nbsp;case&nbsp;(VV¹IBuf2E).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;Lower-triangular&nbsp;in-memory&nbsp;storage.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obsolete.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;generated&nbsp;integrals&nbsp;on&nbsp;disk&nbsp;(file&nbsp;610).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;computation&nbsp;of&nbsp;raff&nbsp;1&nbsp;and&nbsp;2&nbsp;integrals&nbsp;even&nbsp;for&nbsp;RHF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;save&nbsp;integrals&nbsp;(same&nbsp;as&nbsp;0x).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L503`: Print F(1),T. (Read one card with start, end 2I2).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/20)
`L501, L502, L504`: Final non-DIIS iteration.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(only&nbsp;if&nbsp;doing&nbsp;pseudo-diagonalization&nbsp;or&nbsp;QNDMS).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;do&nbsp;a&nbsp;final&nbsp;unextrapolated&nbsp;diagonalization&nbsp;after&nbsp;convergence&nbsp;is&nbsp;reached.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No,&nbsp;just&nbsp;quit&nbsp;when&nbsp;extrapolated&nbsp;convergence&nbsp;is&nbsp;reached.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;a&nbsp;full&nbsp;diagonalization&nbsp;at&nbsp;the&nbsp;end&nbsp;without&nbsp;recomputing&nbsp;a&nbsp;new&nbsp;Fock&nbsp;matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L506`: Orbital rotation control.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;On&nbsp;all&nbsp;the&nbsp;time.&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rotations&nbsp;are&nbsp;turned&nbsp;on&nbsp;when&nbsp;SQCDF&nbsp;is&nbsp;below&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/21)
DIIS error for density damping, maximum virtual mixing for MO damping.


For density damping.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Damp&nbsp;if&nbsp;error&nbsp;>&nbsp;0.001).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Damp&nbsp;if&nbsp;error&nbsp;>&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


For MO damping:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;no&nbsp;more&nbsp;than&nbsp;1/3&nbsp;virtual&nbsp;component&nbsp;for&nbsp;any&nbsp;occupied&nbsp;at&nbsp;each&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum&nbsp;N/1000&nbsp;virtual&nbsp;component.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L503`: Action if OTEST detects problems.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Abort&nbsp;run&nbsp;via&nbsp;LNK1E.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Continue&nbsp;run.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check&nbsp;orthonormality&nbsp;at&nbsp;first&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L506`: Extrapolation control.


MCSCFp flags.


* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;MOs&nbsp;using&nbsp;UHF&nbsp;natural&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IRdNLp.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/22)
`L501, L502, L504`: Use of DIIS extrapolation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1042)&nbsp;for&nbsp;calculations&nbsp;using&nbsp;diagonalization&nbsp;(2)&nbsp;for&nbsp;calculations&nbsp;using&nbsp;sparse&nbsp;diagonalization&nbsp;replacements.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;with&nbsp;Fermi&nbsp;broadening&nbsp;as&nbsp;well,&nbsp;deciding&nbsp;on&nbsp;the&nbsp;fly&nbsp;between&nbsp;the&nbsp;two&nbsp;forms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;with&nbsp;"pFON"&nbsp;version&nbsp;of&nbsp;Fermi&nbsp;broadening.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;with&nbsp;"FON"&nbsp;version&nbsp;of&nbsp;Fermi&nbsp;broadening.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Regular&nbsp;DIIS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Energy-based&nbsp;mixing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Energy&nbsp;DIIS&nbsp;when&nbsp;DIIS&nbsp;error&nbsp;has&nbsp;increased&nbsp;significantly&nbsp;or&nbsp;is&nbsp;above&nbsp;threshold.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Energy&nbsp;DIIS&nbsp;when&nbsp;DIIS&nbsp;error&nbsp;has&nbsp;increased&nbsp;significantly,&nbsp;otherwise,&nbsp;mixture&nbsp;of&nbsp;energy&nbsp;and&nbsp;commutator.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;energy&nbsp;DIIS&nbsp;when&nbsp;commutator&nbsp;gives&nbsp;huge&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Nxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Switch&nbsp;from&nbsp;energy&nbsp;to&nbsp;commutator&nbsp;when&nbsp;error&nbsp;is&nbsp;10^-N&nbsp;in&nbsp;method&nbsp;3;&nbsp;use&nbsp;(DIIS&nbsp;error/10^-N)&nbsp;for&nbsp;weight&nbsp;of&nbsp;energy&nbsp;DIIS&nbsp;in&nbsp;method&nbsp;4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Mxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;print&nbsp;level&nbsp;M&nbsp;in&nbsp;DIIS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L506`: Orbital mixing control.




### IOp(5/23)
`L506, L509`: Flag for later points of an optimization, so that pair and Hamiltonian information can be reused.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;from&nbsp;input&nbsp;stream.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;from&nbsp;RWF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;from&nbsp;checkpoint.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/24)
`L506`: Orbital freezing.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Optimize&nbsp;all&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Freeze&nbsp;all&nbsp;closed,&nbsp;high&nbsp;spin&nbsp;and&nbsp;first&nbsp;natural&nbsp;orbitals.&nbsp;Optimize&nbsp;only&nbsp;2nd&nbsp;and&nbsp;higher&nbsp;naturals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/25)
`L506`: Rotation application.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(exponentiate&nbsp;rotation&nbsp;angles).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Apply&nbsp;rotations&nbsp;sequentially.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/26)
Number of Hamiltonians to read in (L506). If zero, the unpaired orbitals are assumed to be high spin. If -1, an open-shell singlet is assumed.




### IOp(5/28)
Root of CI to use in MCSCF.xxx


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Defaults&nbsp;to&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;N^th&nbsp;root.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/29)
Use of Raffenetti integrals during direct SCF.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All&nbsp;integrals&nbsp;done&nbsp;as&nbsp;Raffenetti.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;let&nbsp;FoFJK&nbsp;decide.&nbsp;It&nbsp;will&nbsp;never&nbsp;use&nbsp;Raffenetti&nbsp;for&nbsp;SCF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All&nbsp;integrals&nbsp;are&nbsp;done&nbsp;as&nbsp;regular&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Integrals&nbsp;with&nbsp;degree&nbsp;of&nbsp;contraction&nbsp;greater&nbsp;than&nbsp;or&nbsp;equal&nbsp;to&nbsp;N&nbsp;are&nbsp;done&nbsp;at&nbsp;regular&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/30)
`L502, L505, (not needed in L506)`: Whether to symmetrize final orbitals using Abelian symmetry operations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Yes).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Symmetrize&nbsp;even&nbsp;if&nbsp;symmetry&nbsp;blocking&nbsp;was&nbsp;done,&nbsp;and&nbsp;print&nbsp;symmetries.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/31)
`L508, L509`: Number of vectors to form at a time during micro-iterations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(3&nbsp;in&nbsp;L509).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/32)
`L502, L510`: Sleazy SCF.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;use&nbsp;loose&nbsp;integral&nbsp;cutoffs,&nbsp;convergence&nbsp;on&nbsp;either&nbsp;energy&nbsp;or&nbsp;density&nbsp;and&nbsp;always&nbsp;do&nbsp;incremental&nbsp;Fock&nbsp;formation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Thresholds&nbsp;similar&nbsp;to&nbsp;DGauss&nbsp;for&nbsp;convergence&nbsp;and&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;doing&nbsp;an&nbsp;inexpensive&nbsp;pass&nbsp;0&nbsp;and&nbsp;then&nbsp;full&nbsp;accuracy&nbsp;in&nbsp;pass&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Decide&nbsp;between&nbsp;1&nbsp;and&nbsp;4&nbsp;based&nbsp;on&nbsp;details&nbsp;of&nbsp;the&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;iterations&nbsp;with&nbsp;sleazy&nbsp;XC&nbsp;grid,&nbsp;then&nbsp;one&nbsp;iteration&nbsp;with&nbsp;next&nbsp;grid&nbsp;up.&nbsp;The&nbsp;default&nbsp;is&nbsp;CoarseGrid&nbsp;for&nbsp;iterations&nbsp;and&nbsp;SG1&nbsp;for&nbsp;final&nbsp;energy.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;longer&nbsp;used.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;longer&nbsp;used.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* I000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;approximation&nbsp;I,&nbsp;0=normal&nbsp;1=Linear&nbsp;approximation&nbsp;to&nbsp;Xc.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;general&nbsp;DBF&nbsp;logic&nbsp;only&nbsp;if&nbsp;the&nbsp;DBF&nbsp;RWF&nbsp;is&nbsp;present.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;use&nbsp;of&nbsp;1c&nbsp;instead&nbsp;of&nbsp;general&nbsp;DBF&nbsp;logic.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;use&nbsp;of&nbsp;general&nbsp;DBF&nbsp;logic.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/33)
Print option.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Only&nbsp;summary&nbsp;results&nbsp;are&nbsp;printed&nbsp;(with&nbsp;possible&nbsp;control&nbsp;from&nbsp;the&nbsp;‘no-print’&nbsp;option).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;eigenvalues&nbsp;and&nbsp;the&nbsp;M.&nbsp;O.&nbsp;coefficients&nbsp;are&nbsp;printed&nbsp;at&nbsp;the&nbsp;end&nbsp;of&nbsp;the&nbsp;SCF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;IOp(5/33)=1,&nbsp;but&nbsp;additionally&nbsp;the&nbsp;density&nbsp;matrix&nbsp;is&nbsp;printed.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;IOp(5/33)=2,&nbsp;but&nbsp;at&nbsp;the&nbsp;end&nbsp;of&nbsp;each&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;IOp(5/33)=3,&nbsp;but&nbsp;all&nbsp;matrix&nbsp;transactions&nbsp;are&nbsp;printed&nbsp;(Beware:&nbsp;Lots&nbsp;of&nbsp;output.)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/34)
Dump option. Regular system defaults apply here.




### IOp(5/35)
`L501, L502`: Whether basis is orthonormal.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/36)
Whether to checkpoint after every SCF cycle.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(checkpoint&nbsp;only&nbsp;if&nbsp;direct).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Checkpoint.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;checkpoint.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/37)
`L502, L508`: Frequency at which to do full Fock formation instead of incremental.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;do&nbsp;incremental&nbsp;Fock&nbsp;formation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(every&nbsp;20&nbsp;for&nbsp;direct,&nbsp;except&nbsp;40&nbsp;if&nbsp;Camp-King&nbsp;is&nbsp;on).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Every&nbsp;N^th&nbsp;cycle.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/38)
Whether to vary integral cutoffs during direct SCF.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(5).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;do&nbsp;integrals&nbsp;3&nbsp;digits&nbsp;more&nbsp;accurately&nbsp;than&nbsp;current&nbsp;convergence.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;do&nbsp;integrals&nbsp;at&nbsp;same&nbsp;accuracy&nbsp;as&nbsp;convergence&nbsp;until&nbsp;final&nbsp;iteration,&nbsp;then&nbsp;2&nbsp;digits&nbsp;more&nbsp;accurately.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Converge&nbsp;to&nbsp;10^-5&nbsp;with&nbsp;integrals&nbsp;good&nbsp;to&nbsp;10^-6&nbsp;first,&nbsp;then&nbsp;full&nbsp;convergence.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VarAcc&nbsp;allowed,&nbsp;decide&nbsp;based&nbsp;on&nbsp;details&nbsp;of&nbsp;problems.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VarAcc&nbsp;forbidden&nbsp;because&nbsp;of&nbsp;Guess=Read;&nbsp;allows&nbsp;different&nbsp;default&nbsp;actions&nbsp;for&nbsp;PBC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Full&nbsp;accuracy&nbsp;for&nbsp;2e&nbsp;part,&nbsp;but&nbsp;do&nbsp;pass&nbsp;0&nbsp;with&nbsp;cheaper&nbsp;XC&nbsp;grid.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Full&nbsp;grid&nbsp;throughout,&nbsp;but&nbsp;do&nbsp;pass&nbsp;0&nbsp;with&nbsp;cheaper&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/39)
On the fly symbolic matrix element generator.




### IOp(5/40)
Use of reaction field; only used now for Onsager and control of details of SCIPCM.


* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Multipoles&nbsp;of&nbsp;order&nbsp;N,&nbsp;increment&nbsp;field&nbsp;in&nbsp;Gen(2-4).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Multipoles&nbsp;of&nbsp;order&nbsp;N,&nbsp;store&nbsp;field&nbsp;in&nbsp;Gen(2-4).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(for&nbsp;SCIPCM,&nbsp;same&nbsp;as&nbsp;10000).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update&nbsp;surface&nbsp;every&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update&nbsp;surface&nbsp;every&nbsp;iteration&nbsp;in&nbsp;pass&nbsp;1&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update&nbsp;surface&nbsp;on&nbsp;pass&nbsp;2&nbsp;iterations&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;3,&nbsp;but&nbsp;re-use&nbsp;1e&nbsp;matrix&nbsp;instead&nbsp;of&nbsp;surface&nbsp;terms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 50000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update&nbsp;surface&nbsp;and&nbsp;restart&nbsp;DIIS&nbsp;when&nbsp;within&nbsp;10^-2&nbsp;of&nbsp;convergence.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/41)
Whether to converge on maximum density change as well or instead of RMS.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum&nbsp;allowed&nbsp;change&nbsp;is&nbsp;10^N&nbsp;larger&nbsp;than&nbsp;RMS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum&nbsp;allowed&nbsp;changed&nbsp;is&nbsp;same&nbsp;as&nbsp;RMS&nbsp;(i.e.,&nbsp;convergence&nbsp;only&nbsp;on&nbsp;maximum).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Converge&nbsp;only&nbsp;on&nbsp;RMS&nbsp;density&nbsp;change.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Converge&nbsp;on&nbsp;energy&nbsp;to&nbsp;10^N*RMS-density-accuracy.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L510`: Davidson options. Option xx is used also by Lanczos if IOp(5/39)=10000n or 20000n.


* xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum&nbsp;dimension&nbsp;of&nbsp;reduced&nbsp;Hamiltonian&nbsp;used&nbsp;as&nbsp;guess&nbsp;is&nbsp;100*xx.&nbsp;Default=Min(NSec,500).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* yy00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum&nbsp;dimension&nbsp;of&nbsp;iterative&nbsp;subspace&nbsp;is&nbsp;10*yy.&nbsp;Default=Max(50*NStates,200).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* zz0000&nbsp;&nbsp;&nbsp;&nbsp;Number&nbsp;of&nbsp;guess&nbsp;vectors&nbsp;generated:&nbsp;&nbsp;Default=&nbsp;NStates*k.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* k000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reduction&nbsp;factor&nbsp;between&nbsp;number&nbsp;of&nbsp;guess&nbsp;vectors&nbsp;provided&nbsp;and&nbsp;number&nbsp;of&nbsp;vectors&nbsp;wanted&nbsp;at&nbsp;the&nbsp;end&nbsp;(1&nbsp;≤&nbsp;k&nbsp;≤&nbsp;9).&nbsp;Default:&nbsp;1&nbsp;if&nbsp;reading&nbsp;guess&nbsp;vectors&nbsp;from&nbsp;prev.&nbsp;calc&nbsp;for&nbsp;all&nbsp;states,&nbsp;otherwise&nbsp;2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* ll0000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Davidson&nbsp;iteration&nbsp;after&nbsp;which&nbsp;to&nbsp;scale&nbsp;back&nbsp;the&nbsp;number&nbsp;of&nbsp;vectors.&nbsp;Warning:&nbsp;For&nbsp;overflow&nbsp;reasons,&nbsp;value&nbsp;must&nbsp;be&nbsp;0&nbsp;≤&nbsp;ll&nbsp;≤&nbsp;20.&nbsp;Default=2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/42)
`L510`: Number of orbitals to localize.


* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Localize&nbsp;all&nbsp;active&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Localize&nbsp;first&nbsp;N&nbsp;(strongly&nbsp;occupied!)&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/47)
`L510`.


* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;up&nbsp;for&nbsp;CAS-MP2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;spin-orbit&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/48)
Options to be passed to CalDFT.


* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Control&nbsp;flag&nbsp;for&nbsp;CalDFT&nbsp;is&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L510`: Whether to use reorthogonalization procedure in Lanczos.




### IOp(5/49)
Use of sparse storage and Conjugate Gradient optimization instead of N^2 memory and diagonalization.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(11,&nbsp;or&nbsp;22&nbsp;if&nbsp;sparse&nbsp;is&nbsp;set&nbsp;in&nbsp;ILSW).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Diagonalization.&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Conjugate&nbsp;gradient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Square&nbsp;storage&nbsp;(only&nbsp;in&nbsp;Fock&nbsp;formation&nbsp;if&nbsp;CG).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Linear&nbsp;storage&nbsp;(only&nbsp;in&nbsp;Fock&nbsp;formation&nbsp;if&nbsp;diagonalization).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L510`: Option for using Lanczos in CPMCSCF calculations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Lanczos&nbsp;except&nbsp;for&nbsp;the&nbsp;last&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/53)
PCM input and solvent type.


* N>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Solvent&nbsp;type&nbsp;N,&nbsp;default&nbsp;parameters.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N<0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dielectric&nbsp;constant&nbsp;|N|/1000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/55)
How many HOMOs and LUMOs to solve for after CG.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;of&nbsp;each.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/56)
A0for Onsager SCRF.


* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/1000&nbsp;Bohr.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/57)
First iteration at which to level shift and do FON.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default=&nbsp;1&nbsp;unless&nbsp;doing&nbsp;Stable=Opt,&nbsp;then&nbsp;start&nbsp;after&nbsp;instability&nbsp;searches.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Iteration&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/60)
Override standard values of IRadAn.




### IOp(5/61)
Override standard values of IRanWt




### IOp(5/62)
Override standard values of IRanGd.




### IOp(5/63)
Whether to do FMM.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;global&nbsp;default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;FMM&nbsp;here&nbsp;regardless.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;both&nbsp;FMM&nbsp;and&nbsp;FoFCou&nbsp;here.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/64)
Override default value of FMFlags.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;use&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/65)
Override NFx parameter.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;use&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/66)
Override the choice of XC functional.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;global&nbsp;values.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;functional&nbsp;N,&nbsp;with&nbsp;the&nbsp;same&nbsp;values&nbsp;as&nbsp;for&nbsp;IOp(5/74)&nbsp;in&nbsp;overlay&nbsp;3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/70)
Maximum initial temperature for FON (non-PBC), or temperature for broadening (PBC and IOp(5/74)=[1-4]xx).


* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Start&nbsp;at&nbsp;a&nbsp;high&nbsp;temperature&nbsp;(limited&nbsp;only&nbsp;by&nbsp;DIIS&nbsp;error).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(3000K&nbsp;=&nbsp;10&nbsp;milliHartrees&nbsp;for&nbsp;non-PBC,&nbsp;600K&nbsp;for&nbsp;PBC).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;degrees.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/71)
`L502`:  Number of steps to apply simulated annealing.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;—&nbsp;10&nbsp;steps&nbsp;FON&nbsp;/&nbsp;20&nbsp;steps&nbsp;PFON.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;steps.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/72)
Whether L510 should save a state density as the SCF density and whether it should save any excited state densities as CI/TD densities. Requires that Slater determinants be used so that spin densities can be computed, and cannot be used when doing forces or frequencies.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;the&nbsp;pair&nbsp;of&nbsp;states&nbsp;to&nbsp;use&nbsp;to&nbsp;compute&nbsp;the&nbsp;density&nbsp;saved&nbsp;as&nbsp;the&nbsp;SCF&nbsp;density.&nbsp;&nbsp;Only&nbsp;one&nbsp;number&nbsp;gives&nbsp;the&nbsp;total&nbsp;rather&nbsp;than&nbsp;transition&nbsp;density.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store&nbsp;the&nbsp;lowest&nbsp;state&nbsp;as&nbsp;the&nbsp;SCF&nbsp;density&nbsp;and&nbsp;the&nbsp;higher&nbsp;states,&nbsp;if&nbsp;any,&nbsp;as&nbsp;CIS/TD&nbsp;excited&nbsp;state&nbsp;densities.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/73)
Options for ADMP.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2&nbsp;for&nbsp;ADMP,&nbsp;1&nbsp;for&nbsp;QNDMS).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Lowdin&nbsp;basis&nbsp;for&nbsp;CP&nbsp;orthonormal&nbsp;transform.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Cholesky&nbsp;basis&nbsp;for&nbsp;CP&nbsp;orthonormal&nbsp;transform.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/74)
Type of k-point integration.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(911,&nbsp;should&nbsp;be&nbsp;193&nbsp;for&nbsp;metals).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;LT&nbsp;method&nbsp;(interpolation).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Occupy&nbsp;entire&nbsp;points&nbsp;(used&nbsp;together&nbsp;with&nbsp;broadening).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Full&nbsp;points&nbsp;for&nbsp;insulators,&nbsp;temperature&nbsp;broadening&nbsp;for&nbsp;metals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Occupy&nbsp;lowest&nbsp;NE&nbsp;at&nbsp;each&nbsp;k&nbsp;point&nbsp;regardless&nbsp;of&nbsp;the&nbsp;energies.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Improved&nbsp;LT&nbsp;with&nbsp;quadratic&nbsp;corrections.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Original&nbsp;LT&nbsp;method.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 90&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;concern&nbsp;for&nbsp;corrections.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Smearing&nbsp;Marzari&nbsp;method&nbsp;I.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Smearing&nbsp;Marzari&nbsp;method&nbsp;II.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;First&nbsp;order&nbsp;Hermite-Gaussian&nbsp;of&nbsp;Paxton&nbsp;and&nbsp;Methfessel.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 400&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gaussian&nbsp;smearing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 500&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Classical&nbsp;Fermi-Dirac&nbsp;broadening.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 900&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;broadening&nbsp;(this&nbsp;will&nbsp;be&nbsp;Gaussian&nbsp;broadening&nbsp;with&nbsp;small&nbsp;T).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/75-78)
Number of alpha electrons, alpha orbitals, beta electrons, and beta orbitals for fractional occupation.




### IOp(5/79)
Range around Fermi level around which temperature distribution will be applied if broadening is turned on for PBC.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;a&nbsp;value&nbsp;will&nbsp;be&nbsp;chosen&nbsp;in&nbsp;ZInLT1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/80)
The maximum conjugate gradient step size.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;maximum&nbsp;step&nbsp;size.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;maximum&nbsp;(.8).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Step&nbsp;size&nbsp;of&nbsp;MM.NN.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/81)
Conjugate-Gradient parameters.


* MM&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum&nbsp;Number&nbsp;of&nbsp;CG&nbsp;cycles&nbsp;per&nbsp;SCF&nbsp;iteration.&nbsp;(defaults&nbsp;to&nbsp;4&nbsp;CG&nbsp;cycles).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NN00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Maximum&nbsp;Number&nbsp;of&nbsp;purification&nbsp;cycles&nbsp;per&nbsp;CG&nbsp;iteration.&nbsp;(defaults&nbsp;to&nbsp;3&nbsp;cycles).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;use&nbsp;CG&nbsp;DIIS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;CG&nbsp;DIIS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000000&nbsp;&nbsp;&nbsp;&nbsp;Polak-Ribiere&nbsp;CG&nbsp;minimization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Fletcher-Reeves&nbsp;CG&nbsp;minimization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;diagonal&nbsp;preconditioning&nbsp;in&nbsp;Conjugate-Gradient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;preconditioning.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/82)
C.G. Convergence criterion.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Defaults&nbsp;&nbsp;to&nbsp;10^-7.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/83)
Maximum SCF DIIS vectors.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(20,&nbsp;except&nbsp;40&nbsp;if&nbsp;Camp-King&nbsp;is&nbsp;on).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;SCF&nbsp;DIIS&nbsp;with&nbsp;N&nbsp;vectors.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/84)
`L509`: Restart.


`L502`: Restart using Fock matrix.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Yes&nbsp;for&nbsp;PBC&nbsp;and&nbsp;sparse&nbsp;with&nbsp;guess&nbsp;Fock).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(5/85)
Over-riding of maximum cycles for XQC.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;for&nbsp;first&nbsp;step&nbsp;(32).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Limit&nbsp;is&nbsp;N&nbsp;cycles.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/86)
`L502`:  Strategy options.


* 000000&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(101100).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1&nbsp;except&nbsp;during&nbsp;Stable=Opt,&nbsp;then&nbsp;4).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Just&nbsp;continue&nbsp;as&nbsp;usual&nbsp;if&nbsp;energy&nbsp;goes&nbsp;up.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reduce&nbsp;DIIS&nbsp;space&nbsp;when&nbsp;energy&nbsp;rises&nbsp;from&nbsp;previous&nbsp;cycle.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reduce&nbsp;DIIS&nbsp;space&nbsp;when&nbsp;energy&nbsp;goes&nbsp;above&nbsp;the&nbsp;lowest&nbsp;energy.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reduce&nbsp;DIIS&nbsp;space&nbsp;whenever&nbsp;energy&nbsp;is&nbsp;above&nbsp;the&nbsp;lowest&nbsp;energy.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;on&nbsp;dynamic&nbsp;level&nbsp;shift&nbsp;from&nbsp;the&nbsp;beginning.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;on&nbsp;dynamic&nbsp;level&nbsp;shift&nbsp;only&nbsp;after&nbsp;FON&nbsp;is&nbsp;over.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Keep&nbsp;level&nbsp;shift&nbsp;after&nbsp;energy&nbsp;rises.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;level&nbsp;shift&nbsp;after&nbsp;energy&nbsp;rises.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level&nbsp;shift&nbsp;to&nbsp;a&nbsp;maximum&nbsp;of&nbsp;the&nbsp;goal.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level&nbsp;shift&nbsp;to&nbsp;a&nbsp;maximum&nbsp;of&nbsp;2*goal.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level&nbsp;shift&nbsp;as&nbsp;much&nbsp;as&nbsp;necessary&nbsp;for&nbsp;HOMO&nbsp;>&nbsp;LUMO.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level&nbsp;shift&nbsp;only&nbsp;if&nbsp;the&nbsp;HOMO-LUMO&nbsp;gap&nbsp;is&nbsp;zero.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level&nbsp;shift&nbsp;only&nbsp;if&nbsp;the&nbsp;HOMO-LUMO&nbsp;gap&nbsp;is&nbsp;zero&nbsp;or&nbsp;insignificant&nbsp;(>&nbsp;-0.1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Level&nbsp;shift&nbsp;only&nbsp;if&nbsp;the&nbsp;gap&nbsp;is&nbsp;zero&nbsp;or&nbsp;insignificant&nbsp;(>&nbsp;-0.1),&nbsp;up&nbsp;to&nbsp;twice&nbsp;the&nbsp;goal.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N0000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;longer&nbsp;used.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;3&nbsp;and&nbsp;4&nbsp;point&nbsp;extrapolation&nbsp;if&nbsp;DIIS&nbsp;is&nbsp;on.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200000&nbsp;&nbsp;&nbsp;&nbsp;Retain&nbsp;3&nbsp;and&nbsp;4&nbsp;point&nbsp;extrapolation&nbsp;if&nbsp;DIIS&nbsp;is&nbsp;on.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* The&nbsp;energy&nbsp;is&nbsp;only&nbsp;checked&nbsp;after&nbsp;FON&nbsp;has&nbsp;been&nbsp;turned&nbsp;off.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/87)
Accuracy criterion in Fock matrix formation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;set&nbsp;in&nbsp;FoFCou/CalDSu&nbsp;based&nbsp;on&nbsp;accuracy&nbsp;part&nbsp;of&nbsp;IOp(5/5).&nbsp;Typically&nbsp;10^-10&nbsp;for&nbsp;molecules&nbsp;and&nbsp;10^-12&nbsp;for&nbsp;periodic&nbsp;systems.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/88)
No longer used.




### IOp(5/89)
Linearly dependent basis control for PBC; this and ZFormV should be moved to L302.




### IOp(5/90)
Whether to generate sparse guess here.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;do&nbsp;preliminary&nbsp;AM1&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;do&nbsp;preliminary&nbsp;AM1&nbsp;calculation&nbsp;and&nbsp;compare&nbsp;with&nbsp;guess&nbsp;from&nbsp;previous&nbsp;step&nbsp;in&nbsp;geometry&nbsp;optimization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/91)
Control option for Chebyshev sparse control.




### IOp(5/92)
How to do exact exchange.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Normal&nbsp;processing&nbsp;based&nbsp;on&nbsp;FMM&nbsp;for&nbsp;non-PBC,&nbsp;separate&nbsp;Coulomb&nbsp;and&nbsp;NFx&nbsp;exchange&nbsp;for&nbsp;PBC).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FoFCou&nbsp;for&nbsp;Coulomb,&nbsp;separate&nbsp;FoFCou/NFx&nbsp;for&nbsp;exchange.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/93)
Number of initial iterations for which damping is allowed.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;iterations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/95)
`L510`: Whether to do Davidson during RFO.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(5/96)
`L509`: Override IRadAn for CPHF-like step.


`L502`: Override IRadAn for pass 0 grid.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;grid&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L510`: Prepares for direct RAS method. The CAS active space is subdivided into three RAS active subspaces:  Ras1, Ras2 and Ras3. In the reference space, Ras1 orbitals are doubly occupied, and Ras3 orbitals are empty. We also need to define the maximum number of holes in the Ras1 space (i.e., the number of electrons that can be excited out of the Ras1 subspace) and the maximum number of electrons in the Ras3 space.


* ww&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ww&nbsp;=&nbsp;Number&nbsp;of&nbsp;Ras1&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* xx00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;xx&nbsp;=&nbsp;Maximum&nbsp;number&nbsp;of&nbsp;holes&nbsp;in&nbsp;Ras1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* yy0000&nbsp;&nbsp;&nbsp;&nbsp;yy&nbsp;=&nbsp;Number&nbsp;of&nbsp;Ras3&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* zz000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;zz&nbsp;=&nbsp;Maximum&nbsp;number&nbsp;of&nbsp;electrons&nbsp;in&nbsp;Ras3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/97)
Whether to update precomputed grid data with timing information.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Yes,&nbsp;if&nbsp;available).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L510`: Hopping threshold during trajectories.




### IOp(5/98)
Whether to save eigenvalues and orbitals at all k-points.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Yes).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L510`: Hopping options.


### IOp(5/99)
Grid for numerical k-integration in FT-LT method.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;32,12,8&nbsp;for&nbsp;1,2,3d.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number&nbsp;of&nbsp;points&nbsp;in&nbsp;the&nbsp;grid.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/100)
Tight convergence during CGDMS.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/101)
SDif test on numerical accuracy of PBC diagonalization.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;test.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Abort&nbsp;if&nbsp;SDif&nbsp;is&nbsp;larger&nbsp;than&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/102)
Maximum number of configurations for CAS-MP2.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1000).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/103)
Number of occupied and virtual orbitals to print for each k-point.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;of&nbsp;5&nbsp;occupieds&nbsp;and&nbsp;5&nbsp;virtuals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;is&nbsp;5&nbsp;if&nbsp;printing&nbsp;turned&nbsp;up;&nbsp;otherwise&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;occupieds&nbsp;and&nbsp;N&nbsp;virtuals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/105)
`L510`:  Convergence for Davidson iterations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(6&nbsp;digits&nbsp;on&nbsp;coefficients).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N&nbsp;on&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/106)
`L510`:  Saving and restart for iterative CI.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;CI&nbsp;vectors.&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Restart&nbsp;CI,&nbsp;possibly&nbsp;adding&nbsp;states.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(5/107)
`L510`: Maximum number of Davidson iterations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(huge,&nbsp;number&nbsp;of&nbsp;CI&nbsp;configurations).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;limit.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;iterations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/108)
Minimum number of iterations at which to damp density.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1&nbsp;if&nbsp;transition&nbsp;metals&nbsp;present,&nbsp;otherwise&nbsp;0).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/120)
Whether to store nuclear repulsion energy as total energy.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/121)
IDoVI for HarFok in test calculations.


* xx0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ones&nbsp;digit&nbsp;always&nbsp;set&nbsp;to&nbsp;4&nbsp;here.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/122)
Whether to do Hirshfeld analysis of spin orientations and compute spin each iteration.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(yes&nbsp;for&nbsp;GHF/GKS,&nbsp;no&nbsp;otherwise).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/123)
Number of iterations for Pseudodiagonalization.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1&nbsp;for&nbsp;semi-empirical,&nbsp;-1&nbsp;for&nbsp;HF/DFT).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sweep&nbsp;until&nbsp;variable&nbsp;convergence&nbsp;is&nbsp;reached.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;a&nbsp;maximum&nbsp;of&nbsp;N&nbsp;sweeps.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(5/124)
Variable convergence in pseudodiagonalization:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1&nbsp;for&nbsp;ab&nbsp;initio,&nbsp;2&nbsp;for&nbsp;semi-empirical).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Off-diagonals&nbsp;larger&nbsp;than&nbsp;the&nbsp;initial&nbsp;max/10^N&nbsp;are&nbsp;swept.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Off-diagonals&nbsp;larger&nbsp;than&nbsp;OVMax*10^-N&nbsp;are&nbsp;swept,&nbsp;with&nbsp;OVMax&nbsp;updated&nbsp;each&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/125)
Scale factor for Diag/PseudoDiag tradeoff. Roughly related to the ratio of Diag to Fock formation for large systems.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;test.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(30&nbsp;for&nbsp;ab&nbsp;intio,&nbsp;15&nbsp;for&nbsp;semi-empirical).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pseudodiag&nbsp;must&nbsp;be&nbsp;estimated&nbsp;to&nbsp;be&nbsp;at&nbsp;least&nbsp;N/10&nbsp;times&nbsp;faster&nbsp;than&nbsp;full&nbsp;diag&nbsp;to&nbsp;be&nbsp;used.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/126)
`L508`: Initial step size for linear searches.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(300).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/127)
`L508`: Maximum rotation gradient for Newton-Raphson (above this value, scaled steepest descent is used):


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1.d-2).&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/128)
`L502`:  Diagonalization algorithm.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(GSYEVD&nbsp;if&nbsp;memory&nbsp;permits,&nbsp;otherwise&nbsp;GSPEV).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Algorithm&nbsp;N&nbsp;in&nbsp;DiagDS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(5/129)
Threshold for trying alternate initial guess:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ignore&nbsp;the&nbsp;alternate&nbsp;guess.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Try&nbsp;the&nbsp;alternate&nbsp;if&nbsp;the&nbsp;DIIS&nbsp;error&nbsp;&gteq;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/131)
Whether to match phases with reference orbitals (useful during numerical differentiation).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Match&nbsp;if&nbsp;file&nbsp;of&nbsp;reference&nbsp;orbitals&nbsp;exists.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;match.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(5/139)
`L510`: Large-scale CI method


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Shaopeng&nbsp;for&nbsp;CAS,&nbsp;Klene&nbsp;for&nbsp;RAS).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Shaopeng&nbsp;(NYI&nbsp;for&nbsp;RAS).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Klene.&nbsp;&nbsp;&nbsp;&nbsp;




## Overlay 6 
### IOp(6/7)
Printing of MOs.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;1&nbsp;for&nbsp;molecules,&nbsp;2&nbsp;for&nbsp;PBC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;the&nbsp;occupied&nbsp;and&nbsp;first&nbsp;5&nbsp;virtual&nbsp;MOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;print&nbsp;any&nbsp;MOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;all&nbsp;MOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Biorthogonalize&nbsp;unrestricted&nbsp;MOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;biorthogonalized&nbsp;MOs&nbsp;over&nbsp;canonical&nbsp;ones.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




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


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;the&nbsp;normal&nbsp;amount.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;print.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;verbosely.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/13)
Whether to save computed electric field on disk for use in Tomasi RF calculations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/14)
`L602`: Specification of other properties to be calculated.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Evaluate&nbsp;the&nbsp;electric&nbsp;potential,&nbsp;the&nbsp;electric&nbsp;field,&nbsp;and&nbsp;the&nbsp;electric&nbsp;field&nbsp;gradient&nbsp;at&nbsp;each&nbsp;center.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Evaluate&nbsp;the&nbsp;potential&nbsp;and&nbsp;the&nbsp;electric&nbsp;field&nbsp;at&nbsp;each&nbsp;center.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Evaluate&nbsp;only&nbsp;the&nbsp;potential&nbsp;at&nbsp;each&nbsp;center.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Evaluate&nbsp;none.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/15)
Specification of additional centers. If more than one of these is requested, the lists are in separate input sections in the order listed below.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;additional&nbsp;centers.&nbsp;Evaluate&nbsp;the&nbsp;properties&nbsp;only&nbsp;at&nbsp;each&nbsp;atomic&nbsp;center.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;additional&nbsp;centers.&nbsp;One&nbsp;card&nbsp;per&nbsp;center&nbsp;with&nbsp;the&nbsp;X,&nbsp;Y,&nbsp;and&nbsp;Z&nbsp;coordinates&nbsp;in&nbsp;Angstroms&nbsp;(free&nbsp;format).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;coordinates&nbsp;as&nbsp;for&nbsp;1.&nbsp;Starting&nbsp;at&nbsp;each&nbsp;point,&nbsp;located&nbsp;the&nbsp;nearest&nbsp;stationary&nbsp;point&nbsp;in&nbsp;the&nbsp;electric&nbsp;potential.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;a&nbsp;set&nbsp;of&nbsp;cards&nbsp;specifying&nbsp;a&nbsp;grid&nbsp;of&nbsp;points&nbsp;at&nbsp;which&nbsp;the&nbsp;electric&nbsp;potential&nbsp;will&nbsp;be&nbsp;computed.&nbsp;Two&nbsp;forms&nbsp;of&nbsp;specifications&nbsp;are&nbsp;below.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;potential-derived&nbsp;charges.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 16&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Constrain&nbsp;the&nbsp;dipole&nbsp;in&nbsp;fitting&nbsp;charges.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;centers&nbsp;at&nbsp;which&nbsp;to&nbsp;evaluate&nbsp;the&nbsp;potential&nbsp;from&nbsp;the&nbsp;RWF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 128&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;grid;&nbsp;do&nbsp;not&nbsp;default&nbsp;cube.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


Grid specifications for option 4


A. Evenly spaced rectangular grid. Three cards are required:


* KTape,XO,YO,ZO&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;—output&nbsp;unit&nbsp;and&nbsp;coordinates&nbsp;of&nbsp;one&nbsp;corner&nbsp;of&nbsp;grid.&nbsp;If&nbsp;KTape&nbsp;is&nbsp;0,&nbsp;it&nbsp;defaults&nbsp;to&nbsp;51.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N1,X1,Y1,Z1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;—number&nbsp;of&nbsp;increments&nbsp;and&nbsp;vector.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N2,X2,Y2,Z2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;—number&nbsp;of&nbsp;increments&nbsp;and&nbsp;vector.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


N1 records will be written to unit KTape, with N2 values in each record.


B. An arbitrary list of points. Only one card is needed: N,NEFG,LTape,KTape.


The coordinates of N points in Angstroms will be read unit LTape in format (3F20.12). The potential (NEFG=3), potential and field (NEFG=2), or potential, field, and field gradient (NEFG=1) will be computed and written along with the coordinates to unit KTape in format (4F20.12). Thus if NEFG=3 for each point there will be 4 cards written per point, containing:


* X-coord,Y-coord,Z-coord,Potential&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* X-field,Y-field,Z-field,XX-EFG&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* YY-EFG,ZZ-EFG,XY-EFG,XZ-EFG&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* YZ-EFG&nbsp;&nbsp;&nbsp;&nbsp;


Note that either form of grid should be specified with respect to the standard orientation of the molecule.




### IOp(6/16)
`L602`: Cutoffs.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;full&nbsp;accuracy&nbsp;in&nbsp;calculations&nbsp;at&nbsp;specific&nbsp;points,&nbsp;but&nbsp;use&nbsp;sleazy&nbsp;cutoffs&nbsp;in&nbsp;mapping&nbsp;a&nbsp;grid&nbsp;of&nbsp;points.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;all&nbsp;points&nbsp;to&nbsp;full&nbsp;accuracy.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/17)
`L602`: Debugging control.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;all&nbsp;contributions&nbsp;to&nbsp;selected&nbsp;properties.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;only&nbsp;the&nbsp;nuclear&nbsp;contribution.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;only&nbsp;the&nbsp;electronic&nbsp;contribution.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;only&nbsp;the&nbsp;contribution&nbsp;of&nbsp;shell&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/18)
Whether to update dipole RWF.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/19)
Whether to rotate exact polarizability before comparing with approximate (which will be calculated in the standard orientation). This is like IOp(6/9) in L9999.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;same&nbsp;as&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Exact&nbsp;is&nbsp;still&nbsp;in&nbsp;standard&nbsp;orientation;&nbsp;use&nbsp;as-is.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Exact&nbsp;is&nbsp;already&nbsp;in&nbsp;z-matrix&nbsp;orientation,&nbsp;so&nbsp;rotate.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/20)
How to do electrostatic-potential derived charges.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;a&nbsp;list&nbsp;of&nbsp;points&nbsp;at&nbsp;which&nbsp;to&nbsp;fit,&nbsp;one&nbsp;per&nbsp;line.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Merz-Kollman&nbsp;point&nbsp;selection.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CHELP&nbsp;point&nbsp;selection.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CHELPG&nbsp;point&nbsp;selection.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MK&nbsp;but&nbsp;with&nbsp;2xUFF&nbsp;radii.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hu,&nbsp;Lu,&nbsp;and&nbsp;Yang&nbsp;point&nbsp;selection/weighting.&nbsp;By&nbsp;default,&nbsp;HLY’s&nbsp;atomic&nbsp;densities&nbsp;are&nbsp;used.&nbsp;These&nbsp;are&nbsp;available&nbsp;only&nbsp;up&nbsp;to&nbsp;Ar.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;radii&nbsp;are&nbsp;those&nbsp;defined&nbsp;with&nbsp;the&nbsp;selected&nbsp;method.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;Merz-Kollman&nbsp;radii.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 15&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Gaussian’s&nbsp;atomic&nbsp;density&nbsp;expansions&nbsp;instead&nbsp;of&nbsp;HLY’s.&nbsp;Gaussian’s&nbsp;are&nbsp;defined&nbsp;for&nbsp;all&nbsp;elements&nbsp;up&nbsp;to&nbsp;112.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;CHELP&nbsp;(Francl)&nbsp;recommended&nbsp;radii.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;CHELPG&nbsp;(Breneman)&nbsp;recommended&nbsp;radii.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;2xUFF&nbsp;Radii.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;replacement&nbsp;radii&nbsp;for&nbsp;selected&nbsp;atom&nbsp;types&nbsp;as&nbsp;pairs&nbsp;(IAn,Rad)&nbsp;or&nbsp;(Symbol,Rad),&nbsp;terminated&nbsp;by&nbsp;a&nbsp;blank&nbsp;line.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;replacement&nbsp;radii&nbsp;for&nbsp;selected&nbsp;atoms&nbsp;as&nbsp;pairs&nbsp;(I,Rad),&nbsp;terminated&nbsp;by&nbsp;a&nbsp;blank&nbsp;line.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fit&nbsp;united&nbsp;atoms&nbsp;(heavy&nbsp;atoms&nbsp;only)&nbsp;rather&nbsp;than&nbsp;all&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10000).&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;only&nbsp;active&nbsp;atoms&nbsp;in&nbsp;the&nbsp;fit.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;all&nbsp;atoms&nbsp;in&nbsp;the&nbsp;fit.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fix&nbsp;the&nbsp;charges&nbsp;of&nbsp;all&nbsp;atoms&nbsp;with&nbsp;a&nbsp;non-zero&nbsp;MM&nbsp;charge.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/22)
`L601, L602, L604`: Selection of density matrix.


* -1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;density&nbsp;matrices&nbsp;from&nbsp;.checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* +1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;density&nbsp;matrices&nbsp;from&nbsp;.checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All&nbsp;available&nbsp;transition&nbsp;densities.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Transition&nbsp;density&nbsp;between&nbsp;the&nbsp;states&nbsp;given&nbsp;by&nbsp;IOp(6/29)&nbsp;and&nbsp;IOp(6/30).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Density&nbsp;for&nbsp;the&nbsp;excited&nbsp;state&nbsp;given&nbsp;by&nbsp;IOp(6/29).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;all&nbsp;available&nbsp;density&nbsp;matrices.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;density&nbsp;matrix&nbsp;for&nbsp;the&nbsp;current&nbsp;method,&nbsp;or&nbsp;the&nbsp;HF&nbsp;density&nbsp;if&nbsp;the&nbsp;one&nbsp;for&nbsp;the&nbsp;current&nbsp;method&nbsp;is&nbsp;not&nbsp;available.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N≥0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;density&nbsp;matrix&nbsp;for&nbsp;method&nbsp;N&nbsp;(see&nbsp;Link&nbsp;1&nbsp;for&nbsp;the&nbsp;numbering&nbsp;scheme).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/23)
`L604`: Density values to evaluate over grid.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Density&nbsp;values.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Density&nbsp;values&nbsp;and&nbsp;gradients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Density&nbsp;values,&nbsp;gradients&nbsp;and&nbsp;divergence.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/24)
Frozen core.


* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Freeze&nbsp;N&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Yes).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/25)
`L601`: Whether to compute Coulomb self-energy.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;classically&nbsp;(including&nbsp;self&nbsp;terms&nbsp;—&nbsp;requires&nbsp;2e&nbsp;integrals,&nbsp;O(N^4)).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;quantum&nbsp;mechanically&nbsp;(no&nbsp;self&nbsp;terms&nbsp;—&nbsp;requires&nbsp;2e&nbsp;integrals,&nbsp;and&nbsp;only&nbsp;available&nbsp;for&nbsp;HF.&nbsp;O(N^5)).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/26)
`L602, L604`: Which density to use.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Total.&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Alpha.&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Beta.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Spin.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/27)
Choice of population analysis.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(12).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;do&nbsp;Mulliken&nbsp;populations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;Mulliken&nbsp;populations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;do&nbsp;bonding&nbsp;Mulliken&nbsp;populations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;bonding&nbsp;Mulliken&nbsp;populations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;minimal&nbsp;population&nbsp;analysis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;weightings&nbsp;for&nbsp;atoms&nbsp;pairs&nbsp;for&nbsp;unequally&nbsp;split&nbsp;Mulliken.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/28)
Mark SCF density as current density.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No:&nbsp;save&nbsp;SCF&nbsp;density,&nbsp;but&nbsp;do&nbsp;not&nbsp;mark.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes:&nbsp;mark&nbsp;as&nbsp;well.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/29)
Excited state to use if requested by IOp(6/22).




### IOp(6/30)
2nd excited state for transition density.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Transition&nbsp;density&nbsp;between&nbsp;state&nbsp;IOp(6/29)&nbsp;and&nbsp;g.s.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Transition&nbsp;density&nbsp;between&nbsp;state&nbsp;IOp(6/29)&nbsp;and&nbsp;state&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/31)
Whether to determine natural orbitals from densities.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;using&nbsp;total&nbsp;density.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;using&nbsp;alpha&nbsp;and&nbsp;beta&nbsp;separately&nbsp;for&nbsp;UHF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store&nbsp;only&nbsp;alpha&nbsp;NOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store&nbsp;only&nbsp;beta&nbsp;NOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;spin&nbsp;density.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/32)
`L609`: Control parameters for COVBON (not to be changed under most circumstances).


100000*IPrSma+10000*MItLoc+1000*ITlLoc+100*IDcInt+IPrLoc, where:


* IPrSma&nbsp;&nbsp;&nbsp;&nbsp;When&nbsp;printing&nbsp;MOs&nbsp;in&nbsp;terms&nbsp;of&nbsp;AOIMs,&nbsp;include&nbsp;only&nbsp;MOs&nbsp;with&nbsp;occupancies&nbsp;per&nbsp;spin&nbsp;greater&nbsp;than&nbsp;10^-IPrSma&nbsp;and&nbsp;AOIMs&nbsp;with&nbsp;squares&nbsp;of&nbsp;coefficients&nbsp;greater&nbsp;than&nbsp;10^-IPrSma&nbsp;(1…9,&nbsp;the&nbsp;default&nbsp;of&nbsp;0&nbsp;implies&nbsp;printing&nbsp;of&nbsp;all&nbsp;MOs&nbsp;and&nbsp;AOIMs).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MItLoc&nbsp;&nbsp;&nbsp;&nbsp;MItLoc*NOrb*(NOrb-1)/2&nbsp;is&nbsp;the&nbsp;maximum&nbsp;number&nbsp;of&nbsp;iterations&nbsp;in&nbsp;localization&nbsp;of&nbsp;(spin)&nbsp;orbitals&nbsp;(1…9,&nbsp;default&nbsp;6).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* ITlLoc&nbsp;&nbsp;&nbsp;&nbsp;10.^-ITlLoc&nbsp;is&nbsp;the&nbsp;convergence&nbsp;criterion&nbsp;for&nbsp;(spin)orbital&nbsp;localization&nbsp;(1…9,&nbsp;default&nbsp;9).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* IDcInt&nbsp;&nbsp;&nbsp;&nbsp;Localized&nbsp;(spin)orbitals&nbsp;with&nbsp;atomic&nbsp;occupancies&nbsp;less&nbsp;than&nbsp;0.01*IDcInt&nbsp;are&nbsp;interpreted&nbsp;as&nbsp;lone&nbsp;pair&nbsp;MOs&nbsp;rather&nbsp;than&nbsp;bond&nbsp;MOs&nbsp;(1…99,&nbsp;default&nbsp;10).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* IPrLoc&nbsp;&nbsp;&nbsp;&nbsp;0:&nbsp;Print&nbsp;the&nbsp;atomic&nbsp;occupancies&nbsp;of&nbsp;localized&nbsp;(spin)orbitals&nbsp;(default).
1:&nbsp;Do&nbsp;not&nbsp;print&nbsp;the&nbsp;atomic&nbsp;occupancies.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L605, L606`: naming of RPAC interface file.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Make&nbsp;this&nbsp;a&nbsp;scratch&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name&nbsp;this&nbsp;file&nbsp;‘rpac.11’&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/35)
`L609`: What to do:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Determine&nbsp;attractors,&nbsp;attractor&nbsp;interaction&nbsp;lines,&nbsp;ring&nbsp;points,&nbsp;and&nbsp;cage&nbsp;points.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Determine&nbsp;zero-flux&nbsp;surfaces&nbsp;(IDoZrF).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;charges&nbsp;of&nbsp;AIMs&nbsp;(IDoAtC).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;kinetic&nbsp;energies&nbsp;and&nbsp;multipole&nbsp;moments&nbsp;of&nbsp;AIMs&nbsp;(IDoPrp).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;energies&nbsp;of&nbsp;electrostatic&nbsp;interactions&nbsp;between&nbsp;AIMs&nbsp;(IDoPot).&nbsp;This&nbsp;precludes&nbsp;calculations&nbsp;of&nbsp;atomic&nbsp;property&nbsp;derivatives&nbsp;with&nbsp;respect&nbsp;to&nbsp;nuclear&nbsp;displacements.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;atomic&nbsp;overlap&nbsp;matrices&nbsp;(IDoAOM).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;other&nbsp;atomic&nbsp;matrix&nbsp;elements&nbsp;(IDoAMa).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 400&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Include&nbsp;zero-flux&nbsp;surface&nbsp;relaxation&nbsp;terms&nbsp;in&nbsp;all&nbsp;atomic&nbsp;matrix&nbsp;elements&nbsp;(IDoSRe).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;derivatives&nbsp;of&nbsp;atomic&nbsp;properties&nbsp;with&nbsp;respect&nbsp;to&nbsp;electric&nbsp;field&nbsp;(IDoSeP).&nbsp;Note&nbsp;that&nbsp;IDoSRe&nbsp;should&nbsp;be&nbsp;set&nbsp;to&nbsp;1&nbsp;in&nbsp;order&nbsp;to&nbsp;obtain&nbsp;correct&nbsp;results!&nbsp;Also&nbsp;note&nbsp;that&nbsp;analytical&nbsp;polarizabilities&nbsp;have&nbsp;to&nbsp;be&nbsp;available&nbsp;but&nbsp;force&nbsp;constants&nbsp;have&nbsp;to&nbsp;be&nbsp;absent!&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;derivatives&nbsp;of&nbsp;atomic&nbsp;properties&nbsp;with&nbsp;respect&nbsp;to&nbsp;nuclear&nbsp;displacements&nbsp;as&nbsp;well&nbsp;(IDoNuD).&nbsp;Note&nbsp;that&nbsp;analytical&nbsp;force&nbsp;constants&nbsp;have&nbsp;to&nbsp;be&nbsp;available!&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;localized&nbsp;orbitals&nbsp;and&nbsp;bond&nbsp;orders&nbsp;(IDoLoc).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;atomic&nbsp;orbitals&nbsp;in&nbsp;molecule&nbsp;(IDoAOs).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;If&nbsp;necessary,&nbsp;augment&nbsp;valence&nbsp;electron&nbsp;densities&nbsp;with&nbsp;relativistic&nbsp;core&nbsp;contributions,&nbsp;which&nbsp;is&nbsp;a&nbsp;default&nbsp;anyway&nbsp;(IHwAug&nbsp;=&nbsp;0).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200000&nbsp;&nbsp;&nbsp;&nbsp;If&nbsp;necessary,&nbsp;augment&nbsp;valence&nbsp;electron&nbsp;densities&nbsp;with&nbsp;non-relativistic&nbsp;core&nbsp;contributions&nbsp;(IHwAug&nbsp;=&nbsp;1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 400000&nbsp;&nbsp;&nbsp;&nbsp;Abort&nbsp;if&nbsp;pseudo-potentials&nbsp;have&nbsp;been&nbsp;used&nbsp;(IHwAug&nbsp;=&nbsp;3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reduce&nbsp;accuracy&nbsp;so&nbsp;atomic&nbsp;charges&nbsp;can&nbsp;be&nbsp;computed&nbsp;more&nbsp;rapidly&nbsp;(IQuick).&nbsp;No&nbsp;other&nbsp;properties&nbsp;can&nbsp;be&nbsp;calculated.&nbsp;This&nbsp;option&nbsp;sets&nbsp;IPrNDe=5,&nbsp;IPrNA&nbsp;t=&nbsp;5,&nbsp;and&nbsp;IEpsIn&nbsp;=&nbsp;100.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;numerical&nbsp;instead&nbsp;of&nbsp;analytic&nbsp;integration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;numerical&nbsp;instead&nbsp;of&nbsp;analytic&nbsp;integration&nbsp;and&nbsp;use&nbsp;reduced&nbsp;cutoffs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Full&nbsp;accuracy&nbsp;and&nbsp;analytic&nbsp;integration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/36)
`L609`: Control parameters for neglect of orbitals and primitives.


10000*INoZer+100*IPrNDe+IPrNAt, where…


* INoZer&nbsp;&nbsp;&nbsp;&nbsp;0:&nbsp;Ignore&nbsp;(spin)orbitals&nbsp;with&nbsp;zero&nbsp;occupancies&nbsp;(default).
1:&nbsp;Do&nbsp;not&nbsp;ignore&nbsp;(spin)orbitals&nbsp;with&nbsp;zero&nbsp;occupancies.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* IPrNDe&nbsp;&nbsp;&nbsp;&nbsp;Neglect&nbsp;primitive&nbsp;contributions&nbsp;below&nbsp;10.^-IPrNDe&nbsp;in&nbsp;evaluations&nbsp;of&nbsp;electron&nbsp;density&nbsp;and&nbsp;its&nbsp;derivatives&nbsp;(0…99,&nbsp;default&nbsp;7).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* IPrNAt&nbsp;&nbsp;&nbsp;&nbsp;Neglect&nbsp;primitive&nbsp;contributions&nbsp;below&nbsp;10.^-IPrNAt&nbsp;in&nbsp;integrations&nbsp;over&nbsp;atomic&nbsp;basins&nbsp;(0…99,&nbsp;default&nbsp;7).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/37)
`L609`: Control parameters for ATINLI, RNGPNT, and CAGPNT (not to be changed under most circumstances).


1000000*MxBpIt+100000*SBpMax+1000*NGrd+LookUp, where…


* MxBpIt&nbsp;&nbsp;&nbsp;&nbsp;Maximum&nbsp;number&nbsp;of&nbsp;iterations&nbsp;in&nbsp;trial&nbsp;path&nbsp;determination&nbsp;(1…99,&nbsp;default&nbsp;10).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* SBpMax&nbsp;&nbsp;&nbsp;&nbsp;Maximum&nbsp;value&nbsp;of&nbsp;the&nbsp;control&nbsp;sum&nbsp;(1…9,&nbsp;default&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NGrd&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Length&nbsp;of&nbsp;Fourier&nbsp;expansion&nbsp;for&nbsp;the&nbsp;trial&nbsp;path&nbsp;(1…99,&nbsp;default&nbsp;20).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* LookUp&nbsp;&nbsp;&nbsp;&nbsp;Number&nbsp;of&nbsp;grid&nbsp;points&nbsp;in&nbsp;critical&nbsp;point&nbsp;search&nbsp;(1…999,&nbsp;default&nbsp;100).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/38)
`L609`: Control parameters for ZRFLUX and OIGAPI (not to be changed under most circumstances):


100000*INStRK+10000*IHowFa+1000*IGueDi+100*IPraIn+10*IRScal+IRtFSe


* INStRK&nbsp;&nbsp;&nbsp;&nbsp;10*INStRK&nbsp;is&nbsp;the&nbsp;number&nbsp;of&nbsp;steps&nbsp;in&nbsp;the&nbsp;Runge-Kutta&nbsp;integrations&nbsp;along&nbsp;gradient&nbsp;paths&nbsp;(1…9,&nbsp;default&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* IHowFa&nbsp;&nbsp;&nbsp;&nbsp;IHowFa&nbsp;is&nbsp;the&nbsp;maximum&nbsp;distance&nbsp;in&nbsp;the&nbsp;Runge-Kutta&nbsp;integrations&nbsp;along&nbsp;gradient&nbsp;paths&nbsp;(1…9,&nbsp;default&nbsp;5),&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* IGueDi&nbsp;&nbsp;&nbsp;&nbsp;10.^-IGueDi&nbsp;is&nbsp;the&nbsp;initial&nbsp;displacement&nbsp;from&nbsp;the&nbsp;critical&nbsp;point&nbsp;in&nbsp;the&nbsp;Runge-Kutta&nbsp;integrations&nbsp;(1v9,&nbsp;default&nbsp;6).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* IPraIn&nbsp;&nbsp;&nbsp;&nbsp;10.*IPraIn&nbsp;is&nbsp;the&nbsp;cut-off&nbsp;for&nbsp;zero-flux&nbsp;surfaces&nbsp;(1…9,&nbsp;default&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* IRScal&nbsp;&nbsp;&nbsp;&nbsp;IRScal&nbsp;is&nbsp;the&nbsp;scaling&nbsp;factor&nbsp;in&nbsp;the&nbsp;nonlinear&nbsp;transformation&nbsp;used&nbsp;in&nbsp;the&nbsp;intersection&nbsp;search&nbsp;(1…9,&nbsp;default&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* IRtFSe&nbsp;&nbsp;&nbsp;&nbsp;10.*IRtFSe&nbsp;is&nbsp;the&nbsp;safety&nbsp;factor&nbsp;used&nbsp;in&nbsp;the&nbsp;intersection&nbsp;search&nbsp;(1…9,&nbsp;default&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/39)
`L609`: More control parameters for ZRFLUX and OIGAPI (not to be changed under most circumstances):


1000000*IToler+100000*INInGr+10000*INInCh+1000*IEpsSf+10*IEpsIn+INTrig


* IToler&nbsp;&nbsp;&nbsp;&nbsp;10.^-5-IToler&nbsp;is&nbsp;the&nbsp;tolerance&nbsp;for&nbsp;the&nbsp;intersection&nbsp;search&nbsp;(1…9,&nbsp;default&nbsp;5).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* INInGr&nbsp;&nbsp;&nbsp;&nbsp;10*INInGr&nbsp;is&nbsp;the&nbsp;initial&nbsp;number&nbsp;of&nbsp;grid&nbsp;points&nbsp;in&nbsp;theta&nbsp;and&nbsp;phi&nbsp;in&nbsp;the&nbsp;adaptive&nbsp;integration&nbsp;subroutine&nbsp;(1…9,&nbsp;default&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* INInCh&nbsp;&nbsp;&nbsp;&nbsp;5+INInCh&nbsp;is&nbsp;the&nbsp;initial&nbsp;number&nbsp;of&nbsp;sampling&nbsp;points&nbsp;in&nbsp;the&nbsp;intersection&nbsp;search&nbsp;(1…9,&nbsp;default&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* IEpsSf&nbsp;&nbsp;&nbsp;&nbsp;IEpsSf&nbsp;is&nbsp;the&nbsp;safety&nbsp;factor&nbsp;used&nbsp;for&nbsp;patches&nbsp;with&nbsp;surface&nbsp;faults&nbsp;in&nbsp;the&nbsp;adaptive&nbsp;integration&nbsp;subroutine&nbsp;(1…9,&nbsp;default&nbsp;6).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* IEpsIn&nbsp;&nbsp;&nbsp;&nbsp;0.0001*IEpsIn&nbsp;is&nbsp;the&nbsp;target&nbsp;for&nbsp;integration&nbsp;error&nbsp;(1…99,&nbsp;default&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* INTrig&nbsp;&nbsp;&nbsp;&nbsp;10*INTrig&nbsp;is&nbsp;the&nbsp;number&nbsp;of&nbsp;sine&nbsp;and&nbsp;cosine&nbsp;functions&nbsp;in&nbsp;the&nbsp;trial&nbsp;function&nbsp;for&nbsp;surface&nbsp;sheets&nbsp;(1…9,&nbsp;default&nbsp;2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/40)
`L607`: Control.


* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Skip&nbsp;NBO&nbsp;analysis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;only&nbsp;NPA.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(-2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;NBO&nbsp;analysis&nbsp;—&nbsp;don’t&nbsp;read&nbsp;input.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;input&nbsp;data&nbsp;to&nbsp;control&nbsp;NBO&nbsp;analysis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Delete&nbsp;selected&nbsp;elements&nbsp;of&nbsp;NBO&nbsp;Fock&nbsp;matrix&nbsp;and&nbsp;form&nbsp;a&nbsp;new&nbsp;density,&nbsp;whose&nbsp;energy&nbsp;can&nbsp;then&nbsp;be&nbsp;computed&nbsp;by&nbsp;one&nbsp;of&nbsp;the&nbsp;SCF&nbsp;links.&nbsp;This&nbsp;link&nbsp;must&nbsp;have&nbsp;been&nbsp;invoked&nbsp;with&nbsp;IOp(40)&nbsp;=&nbsp;0&nbsp;or&nbsp;1&nbsp;prior&nbsp;to&nbsp;invoking&nbsp;it&nbsp;with&nbsp;IOp(40)&nbsp;=&nbsp;2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;the&nbsp;deletion&nbsp;energy&nbsp;produced&nbsp;by&nbsp;a&nbsp;previous&nbsp;run&nbsp;with&nbsp;IOp(40)&nbsp;=&nbsp;2&nbsp;and&nbsp;print&nbsp;it.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NBO&nbsp;should&nbsp;not&nbsp;delete&nbsp;its&nbsp;internal&nbsp;data&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/41)
Number of layers in esp charge fit.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(4).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;layers,&nbsp;must&nbsp;be&nbsp;≤&nbsp;4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/42)
Density of points per unit area in esp fit.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Points&nbsp;per&nbsp;unit&nbsp;area.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/43)
Increment between layers in MK charge fit.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(0.4/Sqrt(#layers)),&nbsp;where&nbsp;#&nbsp;layers&nbsp;=&nbsp;IOP&nbsp;(6/41)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.01*N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/44)
`L604`: Type of calculation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;same&nbsp;as&nbsp;2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;the&nbsp;molar&nbsp;volume.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Evaluate&nbsp;the&nbsp;density&nbsp;over&nbsp;a&nbsp;cube&nbsp;of&nbsp;points.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Evaluate&nbsp;MOs&nbsp;over&nbsp;a&nbsp;cube&nbsp;of&nbsp;points.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Skip&nbsp;header&nbsp;information&nbsp;in&nbsp;cube&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/45)
Number of points per Bohr^3 for Monte-Carlo calculation of molar volume.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;from&nbsp;input.&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(20).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;points&nbsp;—&nbsp;for&nbsp;tight&nbsp;accuracy,&nbsp;50&nbsp;is&nbsp;recommended.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/46)
Threshold for molecular volume integration.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;—&nbsp;10^-3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;from&nbsp;input.&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N*10^-4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/47)
Scale factor to apply to van der Waals radii for the box size during volume integration.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N*0.01&nbsp;—&nbsp;for&nbsp;debugging.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/48)
Use of cutoffs.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10^-6&nbsp;accuracy&nbsp;for&nbsp;cubes,&nbsp;1&nbsp;digit&nbsp;better&nbsp;than&nbsp;desired&nbsp;accuracy&nbsp;for&nbsp;volumes).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/49)
`L602, L604`: Approximate number of points per side in cube.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(80).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;points.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;from&nbsp;cards.&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Coarse&nbsp;grid,&nbsp;3&nbsp;points/Bohr.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Medium&nbsp;grid,&nbsp;6&nbsp;points/Bohr.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fine&nbsp;grid,&nbsp;12&nbsp;points/Bohr.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N>4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Grid&nbsp;using&nbsp;1000&nbsp;/&nbsp;N&nbsp;points/Bohr.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/50)
Whether to write Antechamber file during ESP charge fitting.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/51)
Whether to apply Extended Koopman’s Theorem (EKT).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;on&nbsp;non-SCF&nbsp;densities,&nbsp;up&nbsp;to&nbsp;N&nbsp;IPs&nbsp;and&nbsp;EAs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;on&nbsp;non-SCF&nbsp;densities,&nbsp;all&nbsp;possible&nbsp;IPs&nbsp;and&nbsp;EAs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/52)
`L609`: Number of radial integration points.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(100).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/53)
`L609`: Distribution of radial points.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(cubic).&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Polynomial&nbsp;of&nbsp;order&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/54)
Maximum number of domains.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(100000).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/55)
`L609`: Number of inner angular points in numerical integration.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0(no&nbsp;inner&nbsp;sphere).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;302.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;point&nbsp;Lebedev&nbsp;grid&nbsp;(see&nbsp;AngQad).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/56)
`L608`: Whether to read in density matrix from input stream.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/57)
Whether to generate data over a grid using the total SCF density.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;read&nbsp;in&nbsp;name&nbsp;for&nbsp;output&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;also&nbsp;read&nbsp;in&nbsp;name&nbsp;for&nbsp;input&nbsp;file&nbsp;with&nbsp;a&nbsp;different&nbsp;grid&nbsp;and&nbsp;compare.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Output&nbsp;in&nbsp;the&nbsp;form&nbsp;of&nbsp;data&nbsp;statements.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fit&nbsp;atomic&nbsp;density&nbsp;to&nbsp;Gaussians.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fit&nbsp;atomic&nbsp;density&nbsp;to&nbsp;Gaussians,&nbsp;forcing&nbsp;positive&nbsp;definiteness.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/58)
Grid to use in generating tables of density and potential if IOp(57) = 1–3. Must be an unpruned grid.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(99001).&nbsp;&nbsp;&nbsp;&nbsp;


If IOp(57) = 4–5, whether to remove primitives which have all zero coefficients in the expansion:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/59)
Approximations to Exc


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Test&nbsp;superposition&nbsp;of&nbsp;atomic&nbsp;densities&nbsp;using&nbsp;L608:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;correct&nbsp;energies.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;correct&nbsp;energies&nbsp;and&nbsp;0th&nbsp;order&nbsp;approximation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;correct&nbsp;energies&nbsp;and&nbsp;0th-1st&nbsp;order&nbsp;approximations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;correct&nbsp;energies&nbsp;and&nbsp;0th-2nd&nbsp;order&nbsp;approximations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/60–62)
Over-ride standard values of IRadAn, IRanWt, and IRanGd. The default is 3 steps smaller grid for HLY charges in L602 and the global default otherwise.




### IOp(6/63)
`L608`: Suppress number of electrons test in XC quadrature (for debugging with small grids):


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(do&nbsp;test).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Suppress&nbsp;test.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;test&nbsp;as&nbsp;usual.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/64)
Natural Chemical Shielding Analysis.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;of&nbsp;isotropic&nbsp;value.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;of&nbsp;diagonal&nbsp;tensor&nbsp;elements&nbsp;and&nbsp;isotropic&nbsp;value.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;of&nbsp;all&nbsp;tensor&nbsp;components.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/65)
Threshold for printing of NCS contributions.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Zero.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1&nbsp;pmm).&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/1000&nbsp;ppm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/72)
`L602`: Whether to read isotopes for hyperfine interactions and do hyperfine terms.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;if&nbsp;open-shell,&nbsp;NMR&nbsp;data&nbsp;is&nbsp;available,&nbsp;and&nbsp;other&nbsp;terms&nbsp;are&nbsp;being&nbsp;computed.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;regardless&nbsp;of&nbsp;other&nbsp;terms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;reading&nbsp;isotopes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/73)
Whether to save orbitals from NBO.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;NBOs&nbsp;in&nbsp;place&nbsp;of&nbsp;regular&nbsp;MOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;NLMOs&nbsp;in&nbsp;place&nbsp;of&nbsp;regular&nbsp;MOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;NLMO&nbsp;occupieds&nbsp;and&nbsp;NBO&nbsp;virtuals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Suppress&nbsp;re-orthogonalization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 110&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Suppress&nbsp;sorting.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/74)
Whether to use Gaussian connectivity in choosing Lewis structure for NBO.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(use&nbsp;if&nbsp;present&nbsp;and&nbsp;choose&nbsp;is&nbsp;selected&nbsp;in&nbsp;NBO&nbsp;input).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;use.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/75)
`L602`: Model for CM2 charges.




### IOp(6/76)
`L607`: Threshold for linear dependence.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1.D-6).&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/77)
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.d-4.&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;*&nbsp;10^-5.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/78)
Use MOs instead of density in AtmTab.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;density.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;MOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/79)
Whether to calculate Hirshfeld charges.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;do&nbsp;atom-atom&nbsp;electrostatic&nbsp;interactions&nbsp;as&nbsp;well.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;iterative&nbsp;charges.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;iterative&nbsp;charges&nbsp;and&nbsp;read&nbsp;initial&nbsp;values.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;partitioning&nbsp;of&nbsp;density&nbsp;by&nbsp;abelian&nbsp;irrep.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NNNxxx&nbsp;&nbsp;&nbsp;&nbsp;Maximum&nbsp;number&nbsp;of&nbsp;iterations.&nbsp;Default&nbsp;is&nbsp;50.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/80)
Whether to calculate Lowdin charges and Mayer bond orders.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/81)
Print kinetic energy of orbitals?


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(yes,&nbsp;if&nbsp;doing&nbsp;other&nbsp;orbital&nbsp;results).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;for&nbsp;the&nbsp;top&nbsp;5&nbsp;occupieds&nbsp;and&nbsp;lowest&nbsp;5&nbsp;virtuals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;for&nbsp;all&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/82)
Tensors for hyperfine spectra.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;compute&nbsp;if&nbsp;there&nbsp;are&nbsp;100&nbsp;or&nbsp;fewer&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;QEq&nbsp;tensors&nbsp;and&nbsp;for&nbsp;open-shell&nbsp;systems&nbsp;compute&nbsp;isotropic&nbsp;and&nbsp;anisotropic&nbsp;splitting&nbsp;tensors.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;compute&nbsp;tensors.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/83)
Orbital angular momentum analysis.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;do&nbsp;total&nbsp;angular&nbsp;momentum&nbsp;contribution&nbsp;to&nbsp;each&nbsp;MO.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Report&nbsp;the&nbsp;largest&nbsp;atomic&nbsp;d&nbsp;and&nbsp;f&nbsp;contributions&nbsp;to&nbsp;orbitals&nbsp;specified&nbsp;by&nbsp;IOp(6/84).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Report&nbsp;the&nbsp;largest&nbsp;transition&nbsp;metal&nbsp;atomic&nbsp;d&nbsp;and&nbsp;f&nbsp;contribs.&nbsp;to&nbsp;orbitals&nbsp;specified&nbsp;by&nbsp;IOp(6/84).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;a&nbsp;list&nbsp;of&nbsp;atoms&nbsp;whose&nbsp;d&nbsp;and&nbsp;f&nbsp;contributions&nbsp;will&nbsp;be&nbsp;analyzed.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 90&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;do&nbsp;atomic&nbsp;d&nbsp;and&nbsp;f&nbsp;contributions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Report&nbsp;the&nbsp;population&nbsp;of&nbsp;each&nbsp;angular&nbsp;momentum&nbsp;on&nbsp;each&nbsp;atom.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/84)
Orbitals to analyze for d and f contributions.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Just&nbsp;occupied&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Occupieds&nbsp;plus&nbsp;lowest&nbsp;N&nbsp;virtuals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/86)
Computation of multipole moments.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1,&nbsp;except&nbsp;for&nbsp;PBC&nbsp;and&nbsp;old&nbsp;semi-empirical).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculate&nbsp;with&nbsp;DipInt.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;stored&nbsp;moment&nbsp;operators.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/87)
`L608`: Accuracy criterion in Fock matrix formation


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/88)
Thresholds for orbital atomic angular momentum printing.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10%).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;At&nbsp;least&nbsp;NN&nbsp;%&nbsp;to&nbsp;print&nbsp;contribution&nbsp;from&nbsp;L&nbsp;on&nbsp;a&nbsp;particular&nbsp;atom.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/89)
Do Natural Transition Orbital Analysis.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;if&nbsp;ground&nbsp;to&nbsp;excited&nbsp;transition&nbsp;density&nbsp;requested.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;over&nbsp;canonical&nbsp;MOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/90)
Whether to include p’s as valence for transition metals and actinides during NBO analysis.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Yes).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/91)
Whether to compute electron-electron spin-spin coupling.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;if&nbsp;multiplicity&nbsp;>2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/92)
Thresholds for HLY charge fitting.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Tiny=1.d-8,&nbsp;ThrGrd=1.D-8)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MMNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tiny=10^-MM,&nbsp;ThrGrd=10^-NN.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/93)
Reference density for HLY charge fitting.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Zero.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Exp(-9)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/100.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/94)
Sigma parameter for HLY charge fitting.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.8.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/1000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/95)
`L608`: Whether to diagonalize Fock matrices.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;with&nbsp;Davidson.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;with&nbsp;DiagDN.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/96)
Analyze all orbitals by atom and angular momentum contribution.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Highest&nbsp;10&nbsp;occupieds&nbsp;and&nbsp;lowest&nbsp;10&nbsp;virtuals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;for&nbsp;all&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For&nbsp;highest&nbsp;N&nbsp;occupieds&nbsp;and&nbsp;lowest&nbsp;N&nbsp;virtuals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/113)
`L612`: Which external method to use.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Command&nbsp;N&nbsp;in&nbsp;file&nbsp;747.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/114)
Which ONIOM system is being done, which is sometimes needed by external procedures.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Real&nbsp;system.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Model&nbsp;system&nbsp;for&nbsp;2-layer,&nbsp;middle&nbsp;for&nbsp;3-layer.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Small&nbsp;model&nbsp;system&nbsp;for&nbsp;3-layer.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/120)
Store nuclear repulsion energy as total energy? (Here, store only the nuclear contribution to the dipole moment).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(no).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/124)
`L612`: Options for External.




### IOp(6/125)
`L612`: Options for unformatted i/o file.




### IOp(6/126)
`L612`: IDefCm for external.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;to&nbsp;Gau_External.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;to&nbsp;runnbo6.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/127)
Whether to compute BEBO energy corrections.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1&nbsp;if&nbsp;parameters&nbsp;available).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;number&nbsp;of&nbsp;pairs&nbsp;(including&nbsp;core)&nbsp;rather&nbsp;than&nbsp;number&nbsp;of&nbsp;lone&nbsp;pairs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;number&nbsp;of&nbsp;lone&nbsp;pairs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/128)
`L608`: Compute core and valence energies.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(01).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;regular&nbsp;calculations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;core-valence.&nbsp;&nbsp;&nbsp;&nbsp;
* 11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;both.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(6/129)
Whether to do DCT charge transfer analysis on the selected excited state densities:


* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;the&nbsp;analysis&nbsp;if&nbsp;excited&nbsp;state&nbsp;densities&nbsp;are&nbsp;available,&nbsp;and&nbsp;for&nbsp;the&nbsp;relaxed&nbsp;excited&nbsp;state&nbsp;density&nbsp;if&nbsp;this&nbsp;was&nbsp;selected.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NNNx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;a&nbsp;maximum&nbsp;of&nbsp;NNN&nbsp;matrices&nbsp;at&nbsp;a&nbsp;time.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




## Overlay 7 
### IOp(7/7)
Use of internal coordinates.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;but&nbsp;neglect&nbsp;first&nbsp;derivatives&nbsp;in&nbsp;conversion&nbsp;of&nbsp;second&nbsp;derivatives&nbsp;to&nbsp;internal&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/8)
Harmonic frequency calculation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10003).&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;with&nbsp;most&nbsp;common&nbsp;isotopes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;with&nbsp;read-in&nbsp;isotopes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;higher&nbsp;precision&nbsp;normal&nbsp;modes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;normal&nbsp;mode&nbsp;displacements&nbsp;in&nbsp;redundant&nbsp;internals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;both&nbsp;HP&nbsp;modes&nbsp;and&nbsp;internal&nbsp;displacements.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;only&nbsp;intensities&nbsp;and&nbsp;not&nbsp;modes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Nxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;scale&nbsp;factor&nbsp;is&nbsp;#N&nbsp;(1=HF,&nbsp;1/1.12,&nbsp;(2=CBS4=0.91671,&nbsp;3=CBSQ=0.91844).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Mxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If&nbsp;M=1,&nbsp;only&nbsp;harmonic&nbsp;thermochemistry.&nbsp;If&nbsp;M=2,&nbsp;do&nbsp;hindered&nbsp;rotor&nbsp;analysis.&nbsp;If&nbsp;M=3,&nbsp;Read&nbsp;hindered&nbsp;rotor&nbsp;parameters&nbsp;from&nbsp;input.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Lxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;L=1&nbsp;diagonalize&nbsp;full&nbsp;NAt3^2&nbsp;force&nbsp;constant&nbsp;matrix&nbsp;and&nbsp;print&nbsp;low&nbsp;modes,&nbsp;unless&nbsp;there&nbsp;are&nbsp;frozen&nbsp;atoms.&nbsp;L=2&nbsp;do&nbsp;not&nbsp;diagonalize&nbsp;full&nbsp;FC&nbsp;matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Kxxxxx&nbsp;&nbsp;&nbsp;&nbsp;K=1&nbsp;print&nbsp;eigenvalues&nbsp;of&nbsp;FC&nbsp;matrices.&nbsp;K=2&nbsp;also&nbsp;read&nbsp;file&nbsp;names&nbsp;and&nbsp;dump&nbsp;mass-weighted&nbsp;FC&nbsp;matrices&nbsp;(full&nbsp;and&nbsp;projected)&nbsp;to&nbsp;disk.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Jxxxxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;J=1&nbsp;print&nbsp;normal-mode&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/9)
Whether to rotate derivatives back to the z-matrix orientation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


Whether to rotate and process derivative properties.


* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(yes).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/10)
First/second derivative control.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;only&nbsp;first&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;only&nbsp;second&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;both.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/11)
Control of integral derivative algorithm.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default;&nbsp;use&nbsp;IsAlg&nbsp;to&nbsp;decide.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scalar&nbsp;Rys&nbsp;SPDF.&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Berny&nbsp;SP,&nbsp;Scalar&nbsp;Rys&nbsp;DF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Old&nbsp;vector&nbsp;Rys&nbsp;SPDF&nbsp;(obsolete).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Berny&nbsp;SP,&nbsp;old&nbsp;vector&nbsp;Rys&nbsp;DF&nbsp;(obsolete).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FoFJK:&nbsp;Rys&nbsp;spdf&nbsp;(obsolete).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Berny&nbsp;SP,&nbsp;FoFJK&nbsp;Rys&nbsp;df&nbsp;(obsolete).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FoFJK:&nbsp;HGP&nbsp;sp,&nbsp;Rys&nbsp;df&nbsp;(obsolete).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Berny&nbsp;SP,&nbsp;FoFJK&nbsp;Rys&nbsp;df&nbsp;(same&nbsp;as&nbsp;7).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FoFJK:&nbsp;HGP&nbsp;spd,&nbsp;Rys&nbsp;f&nbsp;(obsolete).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Berny&nbsp;SP,&nbsp;FoFJK&nbsp;HGP&nbsp;d&nbsp;Rys&nbsp;f&nbsp;(obsolete).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 12&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FoFJK:&nbsp;HGP&nbsp;spdf.&nbsp;&nbsp;&nbsp;&nbsp;
* 13&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Berny&nbsp;SP,&nbsp;FoFJK&nbsp;HGP&nbsp;df&nbsp;(obsolete).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 14&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FoFJK:&nbsp;PRISM&nbsp;spdf.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 15&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FoFJK:&nbsp;Berny&nbsp;SP,&nbsp;PRISM&nbsp;df&nbsp;(obsolete).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/12)
Selection of density matrix.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Usual&nbsp;SCF&nbsp;density.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;generalized&nbsp;density&nbsp;number&nbsp;N&nbsp;for&nbsp;both&nbsp;the&nbsp;one-electron&nbsp;integral&nbsp;derivatives&nbsp;and&nbsp;the&nbsp;corresponding&nbsp;2PDM&nbsp;terms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/13)
Contraction with two-particle density matrices.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;HF&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;external&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;both&nbsp;HF&nbsp;and&nbsp;external&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;2PDM&nbsp;from&nbsp;CIS/TD&nbsp;square&nbsp;1PDM&nbsp;(for&nbsp;debugging)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;2PDM&nbsp;from&nbsp;CIS/TD&nbsp;square&nbsp;1PDM&nbsp;and&nbsp;use&nbsp;HF/Z&nbsp;2PDM&nbsp;as&nbsp;well.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contract&nbsp;with&nbsp;external&nbsp;2PDM&nbsp;derivatives.&nbsp;The&nbsp;types&nbsp;of&nbsp;derivatives&nbsp;are&nbsp;given&nbsp;by&nbsp;IOp(7/15).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Form&nbsp;derivative&nbsp;2PDM&nbsp;from&nbsp;CIS&nbsp;and&nbsp;HF&nbsp;deriv.&nbsp;dens.&nbsp;matrices.&nbsp;IOp(7/15)&nbsp;gives&nbsp;types&nbsp;of&nbsp;derives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;TDA/TDnon-adiabatic&nbsp;coupling&nbsp;in&nbsp;addition&nbsp;to&nbsp;forces.&nbsp;Uses&nbsp;
generaized&nbsp;density,&nbsp;does&nbsp;not&nbsp;compute&nbsp;ground-state&nbsp;or&nbsp;T*T&nbsp;force&nbsp;terms,&nbsp;
and&nbsp;does&nbsp;the&nbsp;half-overlap&nbsp;term&nbsp;in&nbsp;L701.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;only&nbsp;TDA/TD&nbsp;non-adiabatic&nbsp;coupling.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Leave&nbsp;the&nbsp;external&nbsp;2PDM&nbsp;on&nbsp;the&nbsp;disk&nbsp;instead&nbsp;of&nbsp;deleting&nbsp;it.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


2-5, 8 imply use of the generalized density in L701, while 6-7 imply use of gen. density derivatives in L701.




### IOp(7/14)
State for CIS/TD derivatives; gradients. Defaults to 1.




### IOp(7/15)
The nature of the perturbation(s).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1st&nbsp;order&nbsp;nuclear&nbsp;and&nbsp;electric&nbsp;field).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* IJK&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nuclear&nbsp;Kth&nbsp;order.&nbsp;Electric&nbsp;field&nbsp;Jth&nbsp;order.&nbsp;Magnetic&nbsp;field&nbsp;Ith&nbsp;order.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;simulated&nbsp;density&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


Only 1, 10, and 11 are valid in overlay 7 (I is used in other overlays).




### IOp(7/16)
Number of translations and rotations to remove during redundant coordinate transformations.


* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal&nbsp;(6&nbsp;or&nbsp;5&nbsp;for&nbsp;linear&nbsp;molecules).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;same&nbsp;as&nbsp;-1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/18)
Derivative accuracy option.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;to&nbsp;10^-8&nbsp;accuracy.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;as&nbsp;accurately&nbsp;as&nbsp;possible&nbsp;in&nbsp;L702.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;original&nbsp;‘BERNY’&nbsp;values&nbsp;in&nbsp;L702.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;as&nbsp;accurately&nbsp;as&nbsp;possible&nbsp;in&nbsp;L703.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;sleazier&nbsp;cutoffs&nbsp;in&nbsp;L703.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;as&nbsp;accurately&nbsp;as&nbsp;possible&nbsp;in&nbsp;L708.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;sleazier&nbsp;cutoffs&nbsp;in&nbsp;L708.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/19)
`L703`: Sets ICntrl for DFT.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;based&nbsp;on&nbsp;job.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Added&nbsp;to&nbsp;default&nbsp;to&nbsp;use&nbsp;DBF&nbsp;logic&nbsp;for&nbsp;spherical&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;N+100/200&nbsp;for&nbsp;2nd/1st&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/25)
Type of derivatives available.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;First.&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Second.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Third.&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;derivatives&nbsp;from&nbsp;checkpoint&nbsp;file&nbsp;(in&nbsp;input&nbsp;orientation).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;almost&nbsp;all&nbsp;derivatives&nbsp;from&nbsp;chk&nbsp;file&nbsp;(in&nbsp;the&nbsp;input&nbsp;
orientation),&nbsp;except&nbsp;take&nbsp;fd&nbsp;tensor&nbsp;derivatives&nbsp;from&nbsp;the&nbsp;rwf&nbsp;in&nbsp;the&nbsp;
standard&nbsp;orientation.&nbsp;For&nbsp;the&nbsp;second&nbsp;step&nbsp;of&nbsp;Raman/ROA&nbsp;using&nbsp;mixed&nbsp;basis
&nbsp;sets.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;10,&nbsp;but&nbsp;set&nbsp;up&nbsp;for&nbsp;anharmonic&nbsp;differentiation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;30,&nbsp;but&nbsp;after&nbsp;VibFrq&nbsp;store&nbsp;derivs&nbsp;from&nbsp;chk&nbsp;file&nbsp;in&nbsp;file&nbsp;
IOCPFX&nbsp;and&nbsp;leave&nbsp;derivs&nbsp;from&nbsp;the&nbsp;current&nbsp;job&nbsp;in&nbsp;the&nbsp;standard&nbsp;places.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3rd&nbsp;derivatives,&nbsp;DEDerv,&nbsp;D2FDPrp,&nbsp;DMag&nbsp;are&nbsp;Cartesian&nbsp;(numerical)&nbsp;derivatives&nbsp;(default).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3rd&nbsp;derivatives,&nbsp;DEDerv,&nbsp;D2FDPrp,&nbsp;DMag&nbsp;are&nbsp;normal-mode&nbsp;(numerical)&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/28)
`L703`: Skip option to defer integral evaluation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;as&nbsp;normal.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;all&nbsp;gradient&nbsp;integrals&nbsp;in&nbsp;L703.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/29)
`L716`: Mode of use.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal,&nbsp;same&nbsp;as&nbsp;2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal&nbsp;+&nbsp;Generate&nbsp;estimated&nbsp;initial&nbsp;force&nbsp;constants.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nuclear&nbsp;repulsion&nbsp;only&nbsp;(useful&nbsp;for&nbsp;testing).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/30)
Use of symmetry in overlay 7.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;(subject&nbsp;to&nbsp;availability).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;use.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/31)
Handling of forces contributions.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Just&nbsp;use&nbsp;the&nbsp;forces&nbsp;in&nbsp;IRWFX.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;HF&nbsp;forces&nbsp;from&nbsp;D2E&nbsp;file&nbsp;&&nbsp;incr.&nbsp;both&nbsp;FX&nbsp;and&nbsp;FXYZ&nbsp;(non-O11&nbsp;PSCF&nbsp;grad&nbsp;&&nbsp;HF&nbsp;freq).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;FX&nbsp;in&nbsp;conversion&nbsp;of&nbsp;force&nbsp;constants&nbsp;to&nbsp;internal&nbsp;coordinates&nbsp;(HF&nbsp;freq,&nbsp;PSCF&nbsp;Freq=Numer).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;FXYZ&nbsp;in&nbsp;conversion&nbsp;of&nbsp;forces&nbsp;constants&nbsp;to&nbsp;internal&nbsp;cords&nbsp;(PSCF&nbsp;opt&nbsp;with&nbsp;HF&nbsp;2nd&nbsp;deriv).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/32)
Punch option.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Punch&nbsp;energy&nbsp;in&nbsp;format&nbsp;D24.16,&nbsp;forces&nbsp;and&nbsp;lower&nbsp;triangular&nbsp;force&nbsp;constants&nbsp;in&nbsp;format&nbsp;6F12.8.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Punch&nbsp;nuclear&nbsp;coordinate&nbsp;derivatives.&nbsp;Forces&nbsp;are&nbsp;punched&nbsp;in&nbsp;3D20.12&nbsp;
format,&nbsp;one&nbsp;card&nbsp;per&nbsp;atom.&nbsp;Force&nbsp;constants&nbsp;and&nbsp;third&nbsp;derivatives&nbsp;are&nbsp;
punched&nbsp;in&nbsp;4E20.12&nbsp;format&nbsp;in&nbsp;compressed&nbsp;form.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Punch&nbsp;energy,&nbsp;coordinates,&nbsp;and&nbsp;derivatives&nbsp;in&nbsp;Cartesians&nbsp;and&nbsp;redundant&nbsp;internals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Punch&nbsp;energy,&nbsp;coordinates,&nbsp;and&nbsp;derivatives&nbsp;in&nbsp;redundant&nbsp;internals&nbsp;only&nbsp;in&nbsp;compressed&nbsp;form.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Punch&nbsp;energy,&nbsp;first&nbsp;and&nbsp;second&nbsp;derivatives&nbsp;in&nbsp;both&nbsp;Cartesian&nbsp;and&nbsp;internal&nbsp;coordinates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;punch&nbsp;only&nbsp;if&nbsp;second&nbsp;derivatives&nbsp;are&nbsp;available.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/42)
1PDM.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;SCF&nbsp;total&nbsp;density.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;generalized&nbsp;density&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/44)
Handling of an applied electric field.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;add&nbsp;electric&nbsp;field&nbsp;terms&nbsp;to&nbsp;forces.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update&nbsp;forces&nbsp;for&nbsp;a&nbsp;uniform&nbsp;electric&nbsp;field.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update&nbsp;forces&nbsp;for&nbsp;the&nbsp;self-consistent&nbsp;reaction&nbsp;field&nbsp;(SCRF)&nbsp;method.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update&nbsp;forces&nbsp;for&nbsp;a&nbsp;uniform&nbsp;electric&nbsp;field,&nbsp;with&nbsp;forces&nbsp;done&nbsp;the&nbsp;usual&nbsp;way&nbsp;for&nbsp;CIS&nbsp;or&nbsp;MP2&nbsp;2nd&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/45)
Controlling the projection of the reaction path.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;project.&nbsp;The&nbsp;point&nbsp;is&nbsp;a&nbsp;stationary&nbsp;point.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Project&nbsp;the&nbsp;reaction&nbsp;path&nbsp;and&nbsp;compute&nbsp;3N-7&nbsp;frequencies.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Project&nbsp;using&nbsp;the&nbsp;Newton-Raphson&nbsp;step.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Project&nbsp;using&nbsp;forces&nbsp;if&nbsp;the&nbsp;RMS&nbsp;force&nbsp;is&nbsp;larger&nbsp;than&nbsp;1.d-3&nbsp;atomic&nbsp;mass&nbsp;units.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Conical&nbsp;intersection&nbsp;seam,&nbsp;state&nbsp;2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Conical&nbsp;intersection&nbsp;seam,&nbsp;state&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Conical&nbsp;intersection&nbsp;seam,&nbsp;final&nbsp;processing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/60-62)
Override standard values of IRadAn, IRanWt, and IRanGd.




### IOp(7/63)
Whether to do FMM.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;global&nbsp;default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;FMM&nbsp;here&nbsp;regardless.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;on&nbsp;FMM&nbsp;here&nbsp;if&nbsp;it&nbsp;is&nbsp;on&nbsp;elsewhere.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;on&nbsp;FMM&nbsp;here&nbsp;regardless.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;FoFCou&nbsp;as&nbsp;well&nbsp;as&nbsp;FMM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/64)
Type of simulated spectrum in output.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Lines.&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Lorentzians.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Both.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/65)
Harmonic constraints with respect to initial structure during geometry optimization.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Yes,&nbsp;if&nbsp;ref&nbsp;structure&nbsp;is&nbsp;present&nbsp;and&nbsp;has&nbsp;non-zero&nbsp;force&nbsp;constants).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/70)
Do vibro-rotational analysis.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/71)
Do vibrational 2nd order perturbation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;initial&nbsp;point.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;FC.&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;FCHT.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;HT.&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;emission&nbsp;rather&nbsp;than&nbsp;absorption.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/72)
Read additional parameters for anharmonic computations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;an&nbsp;input&nbsp;section&nbsp;specifying&nbsp;the&nbsp;normal&nbsp;modes&nbsp;to&nbsp;consider&nbsp;in&nbsp;the&nbsp;anharmonic&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;both.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/74)
Non-equilibrium PCM gradients.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/75)
Threshold for printing redundant internal contributions to normal mode displacements.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10%).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Zero&nbsp;(all&nbsp;printed).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


The threshold is automatically lowered for each mode until 90% of the absolute displacements are included.




### IOp(7/76)
`L703`: Override use of FoFCou.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;default&nbsp;choice&nbsp;as&nbsp;the&nbsp;rest&nbsp;of&nbsp;the&nbsp;program.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Defaults&nbsp;to&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;FoFCou.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Prohibit&nbsp;FoFCou.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/77)
Debugging options for DBFs.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal&nbsp;processing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Omit&nbsp;subtraction&nbsp;and&nbsp;do&nbsp;P(Fit)*Jx*P.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Copy&nbsp;fit&nbsp;density&nbsp;over&nbsp;real&nbsp;density&nbsp;and&nbsp;do&nbsp;P(Fit)*Jx*P(Fit).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;1c&nbsp;logic&nbsp;for&nbsp;1c&nbsp;DBF&nbsp;case.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clear&nbsp;real&nbsp;density&nbsp;and&nbsp;do&nbsp;-1/2&nbsp;P(Fit)*Jx*P(Fit).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/87)
Accuracy in FoFJK/CalDSu.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;10^-10&nbsp;for&nbsp;molecules,&nbsp;10^-12&nbsp;for&nbsp;PBC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/88)
Compression of output force constants.


* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;constants&nbsp;are&nbsp;stored&nbsp;over&nbsp;active&nbsp;atoms&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* &#8800&nbsp;4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All&nbsp;other&nbsp;values&nbsp;mean&nbsp;full&nbsp;storage&nbsp;here&nbsp;(default).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/89)
IDoV for Harris gradient.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/90)
Vibrational analysis for large systems.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;regular&nbsp;vibrational&nbsp;analysis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;full&nbsp;analysis,&nbsp;but&nbsp;exclude&nbsp;frozen&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;full&nbsp;analysis,&nbsp;but&nbsp;exclude&nbsp;frozen&nbsp;atoms,&nbsp;and&nbsp;only&nbsp;print&nbsp;the&nbsp;non-frozen&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;N&nbsp;lowest&nbsp;modes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/91)
Selection of particular normal modes for analysis.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Show&nbsp;all&nbsp;normal&nbsp;modes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;input&nbsp;specifying&nbsp;how&nbsp;to&nbsp;select&nbsp;modes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Show&nbsp;all&nbsp;modes,&nbsp;sorted&nbsp;by&nbsp;layer.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Show&nbsp;all&nbsp;modes&nbsp;which&nbsp;are&nbsp;primarily&nbsp;on&nbsp;the&nbsp;smallest&nbsp;model&nbsp;system.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Show&nbsp;all&nbsp;modes&nbsp;which&nbsp;are&nbsp;primarily&nbsp;on&nbsp;either&nbsp;model&nbsp;system&nbsp;in&nbsp;a&nbsp;3-layer&nbsp;ONIOM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/92)
Whether to save normal modes and intensities on disk, or read them from disk.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(save&nbsp;unless&nbsp;reading).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;Save.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;selected&nbsp;modes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(don’t&nbsp;read).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;Read.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/93)
Whether to zero out derivatives with respect to frozen atoms.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check&nbsp;ICNUse.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/102)
Control of FMM for nuclear repulsion.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;Use&nbsp;for&nbsp;5K&nbsp;or&nbsp;more&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;for&nbsp;N&nbsp;or&nbsp;more&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Always&nbsp;use&nbsp;FMM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Never&nbsp;use&nbsp;FMM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/120)
Store nuclear repulsion energy as total energy?


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/121)
Read additional parameters for FCHT calculations:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;an&nbsp;input&nbsp;section&nbsp;specifying&nbsp;the&nbsp;normal&nbsp;modes&nbsp;to&nbsp;consider&nbsp;in&nbsp;the&nbsp;anharmonic&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;both.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/122)
Generation of G- in L716. (IAprBG in Red2BG).




### IOp(7/123)
Print partitioning of ONIOM vibrational frequencies into 
contributions from individual sub-calculations. see Vreven et al. JCTC, 
2012, DOI: 10.1021/ct300612m


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;do&nbsp;ONIOM&nbsp;frequency&nbsp;analysis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;ONIOM&nbsp;frequency&nbsp;analysis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/124)
Reserved for options for VibRot.




### IOp(7/125)
Mode of operation of L717:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GDV&nbsp;defaults.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pisa&nbsp;defaults.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(7/126)
Type of overlay 7, for printing:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal&nbsp;derivative&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Process&nbsp;integrated&nbsp;ONIOM&nbsp;or&nbsp;counterpoise&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




## Overlay 8 
### IOp(8/5)
Whether to pseudo-canonicalize ROHF orbitals.


* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;and&nbsp;save&nbsp;over&nbsp;canonical&nbsp;MOs&nbsp;setting&nbsp;ILSW&nbsp;for&nbsp;UHF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Yes&nbsp;if&nbsp;ROHF).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/6)
Bucket selection.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Buckets&nbsp;for&nbsp;MP2:&nbsp;(IA/JB).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Buckets&nbsp;for&nbsp;stability:&nbsp;(IA/JB),&nbsp;(IJ/AB).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Buckets&nbsp;for&nbsp;CID&nbsp;or&nbsp;MP3:&nbsp;(IJ/AB),&nbsp;(IA/JB),&nbsp;(IJ/KL).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Buckets&nbsp;for&nbsp;semi-direct&nbsp;MP4DQ,&nbsp;CISD,&nbsp;QCISD,&nbsp;BD:&nbsp;(IJ/AB),&nbsp;(IA/JB),&nbsp;(IK/KL),&nbsp;(IJ/KA).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CISD&nbsp;or&nbsp;MP4SDQ&nbsp;or&nbsp;MP4SDTQ,&nbsp;but&nbsp;includes&nbsp;(IA/BC).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;complete&nbsp;set&nbsp;of&nbsp;transformed&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Full&nbsp;transformation&nbsp;if&nbsp;this&nbsp;is&nbsp;consistent&nbsp;with&nbsp;MaxDisk,&nbsp;otherwise&nbsp;same&nbsp;as&nbsp;3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Full&nbsp;transformation&nbsp;if&nbsp;this&nbsp;is&nbsp;consistent&nbsp;with&nbsp;MaxDisk,&nbsp;otherwise&nbsp;same&nbsp;as&nbsp;4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/7)
SCF convergence test.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Test&nbsp;that&nbsp;SCF&nbsp;has&nbsp;converged.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;test&nbsp;SCF&nbsp;convergence&nbsp;(mainly&nbsp;used&nbsp;for&nbsp;testing).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/8)
`L811`: Whether to delete MO integrals.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/9)
`L802`: Debug control.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Operate&nbsp;normally.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;N&nbsp;orbitals&nbsp;per&nbsp;pass.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L804`: Direct Transformation Control.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Operate&nbsp;normally.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;and&nbsp;test&nbsp;RInt3&nbsp;array&nbsp;(L804).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Accumulate&nbsp;MP2&nbsp;force&nbsp;constant&nbsp;terms&nbsp;in&nbsp;direct&nbsp;fashion.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Write&nbsp;the&nbsp;MO&nbsp;basis&nbsp;first&nbsp;derivative&nbsp;ERI’s&nbsp;to&nbsp;disk.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;fully&nbsp;in-Core&nbsp;algorithm&nbsp;(L804&nbsp;only).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;transformed&nbsp;integrals&nbsp;in&nbsp;Core&nbsp;algorithm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;semi-direct&nbsp;transformation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;output&nbsp;bucket&nbsp;in&nbsp;Core&nbsp;anti-symmetrization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;sorting&nbsp;for&nbsp;output&nbsp;bucks.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;semi-direct&nbsp;mode&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;semi-direct&nbsp;mode&nbsp;2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;semi-direct&nbsp;mode&nbsp;3&nbsp;if&nbsp;IOp(8/6)=3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;semi-direct&nbsp;mode&nbsp;4&nbsp;if&nbsp;IOp(8/6)=3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10000).&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;symmetry&nbsp;compress&nbsp;transformed&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;symmetry&nbsp;compress&nbsp;transformed&nbsp;integrals&nbsp;(buckets)&nbsp;(This&nbsp;will&nbsp;cause&nbsp;windowed&nbsp;MOs,&nbsp;reordered&nbsp;in&nbsp;the&nbsp;order&nbsp;of&nbsp;representations&nbsp;like&nbsp;occ-rep1,occ-rep2,…&nbsp;virt-rep1,virt-rep2,…&nbsp;eigenvalues&nbsp;and&nbsp;symm.&nbsp;assignment&nbsp;vectors&nbsp;will&nbsp;be&nbsp;put&nbsp;in&nbsp;correspondence&nbsp;with&nbsp;vectors.&nbsp;VGZ).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Symmetry&nbsp;compress&nbsp;transformed&nbsp;integrals&nbsp;only&nbsp;if&nbsp;RHF.&nbsp;(Upper&nbsp;triangle&nbsp;of&nbsp;symmetry&nbsp;compressed&nbsp;integrals&nbsp;for&nbsp;IOp(8/6)=5&nbsp;or&nbsp;4&nbsp;only!&nbsp;(VGZ)).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store&nbsp;buckets&nbsp;of&nbsp;single-bar&nbsp;integrals,&nbsp;not&nbsp;symmetry&nbsp;compressed.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Reorder&nbsp;MOs,&nbsp;eigenvalues&nbsp;and&nbsp;symmetry&nbsp;assignment&nbsp;vectors&nbsp;according&nbsp;to&nbsp;the&nbsp;representations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/10)
Window is selected as follows:


* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;top&nbsp;N&nbsp;occupieds&nbsp;and&nbsp;lowest&nbsp;N&nbsp;virtuals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;same&nbsp;as&nbsp;4.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;≤&nbsp;N&nbsp;≤&nbsp;89&nbsp;selects&nbsp;frozen-core&nbsp;type&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;largest&nbsp;noble&nbsp;gas&nbsp;core&nbsp;is&nbsp;frozen.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G2&nbsp;frozen-core:&nbsp;the&nbsp;largest&nbsp;noble&nbsp;gas&nbsp;core&nbsp;and&nbsp;main&nbsp;group&nbsp;d&nbsp;orbitals&nbsp;are&nbsp;frozen,&nbsp;except&nbsp;that&nbsp;the&nbsp;outer&nbsp;sp&nbsp;electrons&nbsp;of&nbsp;3rd&nbsp;row&nbsp;and&nbsp;later&nbsp;alkali&nbsp;and&nbsp;alkali&nbsp;earth&nbsp;elements&nbsp;are&nbsp;retained.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;next&nbsp;to&nbsp;the&nbsp;largest&nbsp;noble&nbsp;gas&nbsp;core&nbsp;is&nbsp;frozen.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;largest&nbsp;noble&nbsp;gas&nbsp;core&nbsp;and&nbsp;main&nbsp;group&nbsp;d’s&nbsp;are&nbsp;frozen.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G3&nbsp;frozen-core:&nbsp;the&nbsp;largest&nbsp;noble&nbsp;gas&nbsp;core&nbsp;is&nbsp;frozen,&nbsp;except&nbsp;that&nbsp;the&nbsp;outer&nbsp;sp&nbsp;electrons&nbsp;of&nbsp;3rd&nbsp;row&nbsp;and&nbsp;later&nbsp;alkali&nbsp;and&nbsp;alkali&nbsp;earth&nbsp;elements&nbsp;are&nbsp;retained.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;G4&nbsp;frozen-core:&nbsp;the&nbsp;largest&nbsp;noble&nbsp;gas&nbsp;core&nbsp;is&nbsp;frozen,&nbsp;except&nbsp;that&nbsp;the&nbsp;outer&nbsp;sp&nbsp;electrons&nbsp;of&nbsp;2nd&nbsp;row&nbsp;and&nbsp;later&nbsp;alkali&nbsp;and&nbsp;alkali&nbsp;earth&nbsp;elements&nbsp;are&nbsp;retained.&nbsp;For&nbsp;basis&nbsp;sets&nbsp;with&nbsp;double-zeta&nbsp;cores,&nbsp;core&nbsp;virtuals&nbsp;are&nbsp;also&nbsp;frozen.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CBS-Wes&nbsp;core:&nbsp;&nbsp;noble&nbsp;gas&nbsp;except&nbsp;3sp&nbsp;valence&nbsp;K-Zn,&nbsp;3d&nbsp;valence&nbsp;Ga-As.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 90&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;all&nbsp;MOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 91&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;window&nbsp;is&nbsp;specified&nbsp;by&nbsp;IOp(8/37-38).&nbsp;If&nbsp;IOp(8/37)&nbsp;is&nbsp;0,&nbsp;a&nbsp;card&nbsp;is&nbsp;read&nbsp;in&nbsp;indicating&nbsp;the&nbsp;start&nbsp;and&nbsp;the&nbsp;end.&nbsp;A&nbsp;negative&nbsp;value&nbsp;for&nbsp;the&nbsp;end&nbsp;deletes&nbsp;the&nbsp;top&nbsp;virtuals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 92&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;window&nbsp;is&nbsp;recovered&nbsp;from&nbsp;RWF&nbsp;569.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 93&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;window&nbsp;is&nbsp;recovered&nbsp;from&nbsp;file&nbsp;569&nbsp;on&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 94&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;a&nbsp;list&nbsp;of&nbsp;orbitals&nbsp;to&nbsp;freeze.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(200).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;orbital&nbsp;energies&nbsp;to&nbsp;choose&nbsp;core&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;overlap&nbsp;with&nbsp;atomic&nbsp;core&nbsp;orbitals&nbsp;from&nbsp;Harris&nbsp;to&nbsp;choose&nbsp;core&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;overlap&nbsp;with&nbsp;atomic&nbsp;core&nbsp;orbitals&nbsp;from&nbsp;Core&nbsp;Ham&nbsp;to&nbsp;choose&nbsp;core&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/11)
MO coefficient, orbital energy, and number of electrons test.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;same&nbsp;as&nbsp;2&nbsp;except&nbsp;for&nbsp;during&nbsp;BD&nbsp;iterations&nbsp;or&nbsp;BD=Read.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Just&nbsp;print&nbsp;a&nbsp;warning&nbsp;message.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Kill&nbsp;the&nbsp;job&nbsp;if&nbsp;any&nbsp;MO&nbsp;coefficients&nbsp;are&nbsp;greater&nbsp;than&nbsp;1000.0&nbsp;or&nbsp;the&nbsp;smallest&nbsp;difference&nbsp;between&nbsp;occupied&nbsp;and&nbsp;virtual&nbsp;orbital&nbsp;energies&nbsp;is&nbsp;less&nbsp;than&nbsp;0.001.&nbsp;Also,&nbsp;kill&nbsp;a&nbsp;frozen-core&nbsp;job&nbsp;if&nbsp;there&nbsp;is&nbsp;significant&nbsp;core-valence&nbsp;mixing&nbsp;in&nbsp;the&nbsp;canonical&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;same&nbsp;as&nbsp;10.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Suppress&nbsp;such&nbsp;a&nbsp;test&nbsp;(CPHF&nbsp;may&nbsp;still&nbsp;be&nbsp;done&nbsp;for&nbsp;such&nbsp;a&nbsp;case).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Kill&nbsp;the&nbsp;job&nbsp;if&nbsp;there&nbsp;is&nbsp;no&nbsp;corr.&nbsp;energy;&nbsp;e.g.,&nbsp;if&nbsp;there&nbsp;is&nbsp;only&nbsp;1&nbsp;electron&nbsp;or&nbsp;1&nbsp;virtual&nbsp;spin-orbital.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/16)
`L811`: Maximum number of orbitals per pass (only if integral derivative file is being written). Default is as many as fit with Max Disk.




### IOp(8/18)
`L811`: Which type of derivative transformation to do.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;same&nbsp;as&nbsp;3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Non-canonical,&nbsp;Uij,x&nbsp;=&nbsp;-1/2&nbsp;Sij,x.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Canonical,&nbsp;Uij,x&nbsp;=&nbsp;(Fij,x&nbsp;–&nbsp;EjSij,x)&nbsp;/&nbsp;(Ei-Ej)&nbsp;Note&nbsp;that&nbsp;this&nbsp;blows&nbsp;up&nbsp;for&nbsp;degenerate&nbsp;orbitals&nbsp;and&nbsp;is&nbsp;intended&nbsp;primarily&nbsp;for&nbsp;debugging.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Non-canonical,&nbsp;Uij,x&nbsp;=&nbsp;-1/2&nbsp;Sij,x,&nbsp;except&nbsp;canonical&nbsp;in&nbsp;frozen-active&nbsp;blocks.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Non-canonical,&nbsp;Uij,x&nbsp;=&nbsp;-Sij,x&nbsp;Uji,x&nbsp;=&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Canonical&nbsp;occupieds,&nbsp;Uab,x&nbsp;=&nbsp;-Sab,x/2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Canonical&nbsp;virtuals,&nbsp;Uij,x&nbsp;=&nbsp;-Sij,x/2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/19)
`L811`: The nature of the perturbation(s).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1st&nbsp;order&nbsp;nuclear&nbsp;and&nbsp;electric&nbsp;field).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* IJK&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nuclear&nbsp;Kth&nbsp;order.&nbsp;Electric&nbsp;field&nbsp;Jth&nbsp;order.&nbsp;Magnetic&nbsp;field&nbsp;Ith&nbsp;order.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/20)
`L811`: Which terms to include.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;11).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MO&nbsp;derivative&nbsp;times&nbsp;integral&nbsp;term.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MO&nbsp;times&nbsp;integral&nbsp;derivative&nbsp;term.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/23)
`L811`: Algorithm control.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(32).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Unused.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Accumulate&nbsp;MP2&nbsp;force&nbsp;constant&nbsp;terms&nbsp;in&nbsp;direct&nbsp;fashion.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Write&nbsp;the&nbsp;MO&nbsp;basis&nbsp;first&nbsp;derivative&nbsp;ERI’s&nbsp;to&nbsp;disk.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;fully&nbsp;direct.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;semi-direct.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/24)
Whether to try to transform old amplitudes on the checkpoint file.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;1&nbsp;if&nbsp;doing&nbsp;BD=Read&nbsp;and&nbsp;amplitudes&nbsp;are&nbsp;present;&nbsp;2&nbsp;otherwise.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Transform&nbsp;Z-amplitudes&nbsp;as&nbsp;well.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;transform&nbsp;Z-amplitudes&nbsp;as&nbsp;well.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;transform&nbsp;EOM&nbsp;amplitudes&nbsp;if&nbsp;transforming&nbsp;ground-state&nbsp;ones.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Transform&nbsp;EOM&nbsp;amplitudes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;transform&nbsp;EOM&nbsp;amplitudes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/28)
`L921, L922`: Hack number of occupieds for full CI.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Transform&nbsp;all&nbsp;orbitals&nbsp;(after&nbsp;freezing&nbsp;core)&nbsp;as&nbsp;occupieds&nbsp;(i.e.,&nbsp;set&nbsp;NOA=NOB=NROrb&nbsp;in&nbsp;transformation).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Transform&nbsp;N&nbsp;orbitals&nbsp;(after&nbsp;frozen&nbsp;core)&nbsp;as&nbsp;occupieds&nbsp;(i.e.,&nbsp;set&nbsp;NOA=NOB=N&nbsp;for&nbsp;purposes&nbsp;of&nbsp;transformation).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/29)
`L811`: Requested diskusage. This will determine the number of times AO integrals and derivatives are evaluated unless overridden by IOp(8/31). This only applies if the integral derivatives are not stored.


* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;as&nbsp;much&nbsp;as&nbsp;desired,&nbsp;independent&nbsp;of&nbsp;MAXDISK.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;an&nbsp;amount&nbsp;which&nbsp;is&nbsp;similar&nbsp;to&nbsp;the&nbsp;maximum&nbsp;disk&nbsp;usage&nbsp;in&nbsp;other&nbsp;parts&nbsp;of&nbsp;the&nbsp;MP2&nbsp;freq.&nbsp;code.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;as&nbsp;much&nbsp;as&nbsp;needed&nbsp;for&nbsp;maximum&nbsp;efficiency,&nbsp;subject&nbsp;to&nbsp;the&nbsp;limit&nbsp;imposed&nbsp;by&nbsp;MAXDISK.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(-1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;evaluations&nbsp;and&nbsp;hence&nbsp;N&nbsp;coarse&nbsp;tiled&nbsp;batches&nbsp;(1…6&nbsp;are&nbsp;the&nbsp;currently&nbsp;implemented&nbsp;options).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/30)
Type of window.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;Set&nbsp;up&nbsp;/Orb/&nbsp;as&nbsp;indicated&nbsp;by&nbsp;IOp(8/10).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Test&nbsp;window.&nbsp;Set&nbsp;up&nbsp;for&nbsp;full&nbsp;but&nbsp;zero&nbsp;core&nbsp;MOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;up&nbsp;/Orb/&nbsp;for&nbsp;a&nbsp;full&nbsp;window&nbsp;but&nbsp;then&nbsp;blank&nbsp;the&nbsp;wavefunction&nbsp;coefficients&nbsp;in&nbsp;L804.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/36)
Whether to update force constants with the MP2 product of MP2 integral derivatives term (only applies if integral derivative file is not written).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Yes).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;on&nbsp;whether&nbsp;to&nbsp;make&nbsp;Poo&nbsp;and&nbsp;Pvv&nbsp;for&nbsp;MP2.&nbsp;(Yes&nbsp;if&nbsp;Ix&nbsp;is&nbsp;not&nbsp;stored,&nbsp;no&nbsp;otherwise).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/37)
Integer specifying first window parameter (n).




### IOp(8/38)
Integer specifying second window parameter (m).




### IOp(8/39)
Localized orbital method adopted in SAC/SAC-CI.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;No&nbsp;localization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Boys&nbsp;method.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Population&nbsp;method.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Boys&nbsp;+&nbsp;population&nbsp;method.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/40)
Handling of ROHF window.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;ROMP2&nbsp;approach,&nbsp;forming&nbsp;pseudo-canonical&nbsp;alpha&nbsp;and&nbsp;beta&nbsp;orbitals&nbsp;and&nbsp;doing&nbsp;UHF&nbsp;transformation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Treat&nbsp;as&nbsp;RHF,&nbsp;transforming&nbsp;only&nbsp;alpha&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/41)
Transformation of spin-orbitals (alpha only) within occupied and unoccupied orbital subspaces by minimum orbital-deformation (MOD) method.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No,&nbsp;but&nbsp;save&nbsp;MOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;Take&nbsp;reference&nbsp;MOs&nbsp;from&nbsp;disk&nbsp;if&nbsp;available.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;for&nbsp;the&nbsp;1st&nbsp;geometry&nbsp;of&nbsp;opt,&nbsp;yes&nbsp;otherwise.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/42)
Whether to reorder MOs during potential surface exploration.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes&nbsp;(for&nbsp;SAC-CI&nbsp;single&nbsp;point&nbsp;calculation).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;orbital&nbsp;energies&nbsp;in&nbsp;ordering.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;use&nbsp;orbital&nbsp;energies&nbsp;in&nbsp;ordering.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;second&nbsp;moments&nbsp;in&nbsp;ordering.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;use&nbsp;second&nbsp;moments&nbsp;in&nbsp;ordering.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;dipole&nbsp;moments&nbsp;in&nbsp;ordering.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;use&nbsp;dipole&nbsp;moments&nbsp;in&nbsp;ordering.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/46)
Indicates special case of non-HF calculation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;–&nbsp;MOs&nbsp;are&nbsp;canonical&nbsp;HF&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input&nbsp;orbitals&nbsp;are&nbsp;not&nbsp;canonical&nbsp;HF&nbsp;and&nbsp;pseudo-canonical&nbsp;orbitals&nbsp;must&nbsp;be&nbsp;generated&nbsp;here&nbsp;for&nbsp;the&nbsp;post-SCF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;HF&nbsp;pseudo-canonical&nbsp;even&nbsp;if&nbsp;the&nbsp;original&nbsp;SCF&nbsp;method&nbsp;was&nbsp;not&nbsp;(i.e.,&nbsp;Kohn-Sham).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/47)
Whether L804/L811 should generate results compressed over active atoms.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Active&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Full&nbsp;list.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Full&nbsp;list,&nbsp;but&nbsp;blank&nbsp;contributions&nbsp;from&nbsp;inactive&nbsp;atoms&nbsp;(no&nbsp;difference&nbsp;from&nbsp;2&nbsp;for&nbsp;overlay&nbsp;8).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Active&nbsp;atoms,&nbsp;and&nbsp;store&nbsp;Hessian&nbsp;contributions&nbsp;over&nbsp;active&nbsp;atoms&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/60-62)
Over-ride standard values of IRadAn, IRanWt, and IRanGd. For DFTCV, IRadAn defaults to 299974 rather than the global default.




### IOp(8/68)
EOM-CCSD


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;EOM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;EOM&nbsp;with&nbsp;the&nbsp;default&nbsp;algorithm&nbsp;(right&nbsp;and&nbsp;left&nbsp;spaces&nbsp;separately).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;EOM&nbsp;doing&nbsp;only&nbsp;the&nbsp;transition&nbsp;energy&nbsp;(right&nbsp;space).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 21&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;EOM&nbsp;doing&nbsp;right&nbsp;and&nbsp;left&nbsp;eigenvectors&nbsp;using&nbsp;the&nbsp;same&nbsp;expansion&nbsp;space&nbsp;for&nbsp;both.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 31&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;EOM&nbsp;doing&nbsp;right&nbsp;and&nbsp;left&nbsp;eigenvectors&nbsp;using&nbsp;biorthogonal&nbsp;expansion&nbsp;spaces.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/69)
EOM: Number of states per irreducible representation (largest Abelian subgroup) to do.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;per&nbsp;irreducible&nbsp;representation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;the&nbsp;number&nbsp;for&nbsp;each&nbsp;irreducible&nbsp;representation,&nbsp;all&nbsp;from&nbsp;one&nbsp;line.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


The order of irreducible representations is the same as printed for symmetry-adapted basis functions by L301.




### IOp(8/87)
Accuracy of integrals.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(12).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/105)
Convergence of amplitudes for EOM iterations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1.d-5).&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/106)
Number of EOM states for LR transition densities.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(None).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;First&nbsp;N&nbsp;of&nbsp;each&nbsp;symmetry.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/107)
EOM state of most interest.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1st&nbsp;excited&nbsp;state).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N^thexcited&nbsp;state.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/108)
EOM-CCSD: Total number of states to do. Guesses are taken from the checkpoint file if RdAmp was specified, with remaining states taken from the CIS guess in CIS energy order.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2*NIrrep)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(8/109)
IFact for Davidson in EOM-CC.




### IOp(8/110)
State-to-State transition dipoles in EOM-CC:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;From&nbsp;state&nbsp;NRoot&nbsp;to&nbsp;higher&nbsp;states.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;From&nbsp;state&nbsp;NRoot&nbsp;to&nbsp;higher&nbsp;and&nbsp;lower&nbsp;states.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




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


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Include&nbsp;empirical&nbsp;corrections&nbsp;for&nbsp;total&nbsp;energies.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;include&nbsp;empirical&nbsp;corrections.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


The default is not to compute the correction, and if the correction is requested, to include the total energy terms only for CBS-Wes style frozen-core (the only case for which they have been determined). Corrections are only included for elements H-Ar.




### IOp(8/123)
Flag for SOS in EOM.




## Overlay 9 
### IOp(9/5)
Method


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CISD.&nbsp;Configuration&nbsp;interaction&nbsp;with&nbsp;all&nbsp;single&nbsp;and&nbsp;double&nbsp;substitutions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CID.&nbsp;CI&nbsp;with&nbsp;all&nbsp;double&nbsp;substitutions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MP3.&nbsp;Third-order&nbsp;perturbation&nbsp;theory.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MP4(DQ).&nbsp;Fourth-order&nbsp;perturbation&nbsp;theory&nbsp;in&nbsp;the&nbsp;space&nbsp;double&nbsp;and&nbsp;quadruple&nbsp;substitutions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MP4(SDQ).&nbsp;Fourth-order&nbsp;perturbation&nbsp;theory&nbsp;in&nbsp;the&nbsp;space&nbsp;single,&nbsp;double&nbsp;and&nbsp;quadruple&nbsp;substitutions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MP4(SDTQ).&nbsp;Full&nbsp;fourth-order&nbsp;perturbation&nbsp;theory&nbsp;in&nbsp;the&nbsp;space&nbsp;of&nbsp;single,&nbsp;double,&nbsp;triple,&nbsp;and&nbsp;quadruple&nbsp;substitutions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCD.&nbsp;Coupled&nbsp;cluster&nbsp;theory&nbsp;with&nbsp;double&nbsp;substitutions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CCSD.&nbsp;Coupled&nbsp;cluster&nbsp;theory&nbsp;with&nbsp;single&nbsp;and&nbsp;double&nbsp;substitutions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QCISD.&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BD.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/6)
`L913`: Criteria for termination of the iteration.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;convergence&nbsp;criterion&nbsp;and&nbsp;maxcycle.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;regular&nbsp;default&nbsp;maxcycles&nbsp;even&nbsp;for&nbsp;BD.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;maxcycles&nbsp;and&nbsp;convergence&nbsp;criterion&nbsp;(I2,D18.13).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Max&nbsp;N&nbsp;cycles.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/7)
Update the energy in Common/GEN/.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;with&nbsp;the&nbsp;correlation&nbsp;energy,&nbsp;ECID&nbsp;in&nbsp;CID,&nbsp;ECISD&nbsp;in&nbsp;CISD&nbsp;EUMP3&nbsp;in&nbsp;MP3,&nbsp;and&nbsp;EUMP4&nbsp;in&nbsp;MP4&nbsp;calculations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;with&nbsp;EUMP3.&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;with&nbsp;EMP4(SDQ)&nbsp;or&nbsp;EMP4(DQ)&nbsp;If&nbsp;singles&nbsp;are&nbsp;not&nbsp;available.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/8)
`L902`: Constraint on output wavefunction for stability calculations (see link 902).


`L907, L919`: Number of roots (default 1 in 907 and 10 in 919).


`L906`: Term and method selection for debugging.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;—&nbsp;all&nbsp;terms,&nbsp;L&nbsp;using&nbsp;AOs&nbsp;if&nbsp;frozen-core,&nbsp;using&nbsp;MOs&nbsp;if&nbsp;full.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;AA&nbsp;only&nbsp;(semidirect&nbsp;only).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;AB&nbsp;only&nbsp;(semidirect&nbsp;only).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;BB&nbsp;only&nbsp;(semidirect&nbsp;only).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;BA&nbsp;only&nbsp;(semidirect&nbsp;only).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;out-of-core&nbsp;semidirect&nbsp;method.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;out-of-core&nbsp;and&nbsp;quartic&nbsp;I/O&nbsp;method&nbsp;for&nbsp;L.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;out-of-core&nbsp;and&nbsp;qintic&nbsp;I/O&nbsp;method&nbsp;for&nbsp;L.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;L&nbsp;using&nbsp;AO&nbsp;integrals&nbsp;rather&nbsp;than&nbsp;<ia||bc>.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;L&nbsp;using&nbsp;<ia||bc>.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;2nd&nbsp;order&nbsp;sigmas&nbsp;instead&nbsp;of&nbsp;L.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 400&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;2nd&nbsp;order&nbsp;sigmas&nbsp;for&nbsp;ionization&nbsp;of&nbsp;active&nbsp;occupieds&nbsp;only,&nbsp;including&nbsp;contributions&nbsp;from&nbsp;all&nbsp;orbitals&nbsp;including&nbsp;inactive&nbsp;ones.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NN000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Permute&nbsp;occupieds&nbsp;as&nbsp;for&nbsp;NN&nbsp;processors,&nbsp;regardless&nbsp;of&nbsp;actual&nbsp;number.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L913`: Whether to use fast routines.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Slava,&nbsp;fast&nbsp;and&nbsp;R&nbsp;where&nbsp;possible).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Original&nbsp;code&nbsp;(DD1,2,3,&nbsp;UMP41,2,3,4)&nbsp;for&nbsp;first&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;DD[1-3]R&nbsp;and&nbsp;UMP4xR&nbsp;(closed-shell)&nbsp;on&nbsp;1st&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Original&nbsp;code&nbsp;for&nbsp;2nd&nbsp;and&nbsp;later&nbsp;iterations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;DD[1-3]R&nbsp;and&nbsp;UMP4xR&nbsp;(closed-shell).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;DD1,&nbsp;UMp41U,&nbsp;UMP42,&nbsp;UMP43,&nbsp;DD4UQ.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;DD1R,&nbsp;UMP41R,&nbsp;UMP42,&nbsp;UMP43,&nbsp;DD4RQ&nbsp;(closed-shell).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;same&nbsp;as&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Original&nbsp;routines.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Slava&nbsp;routines.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


The defaults are 22 for RCI, 11 for UCI, 42 for RQCI, and 31 for UQCI.


`L914`: State of interest.


* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Repeating&nbsp;stable=opt.&nbsp;End&nbsp;diag.&nbsp;as&nbsp;soon&nbsp;as&nbsp;we&nbsp;have&nbsp;a&nbsp;vector&nbsp;with&nbsp;a&nbsp;negative&nbsp;diagonal&nbsp;element.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;a&nbsp;stable=opt&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;a&nbsp;stability&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We&nbsp;are&nbsp;not&nbsp;doing&nbsp;gradients,&nbsp;FP&nbsp;or&nbsp;CIS-MP2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We&nbsp;are&nbsp;interested&nbsp;in&nbsp;the&nbsp;N^th&nbsp;excited&nbsp;state.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/9)
Convergence criterion (on energy for L913, wavefunction for L914).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;L913&nbsp;single&nbsp;point:&nbsp;10^-7&nbsp;energy,&nbsp;10^-5&nbsp;wfn.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;L913&nbsp;gradient&nbsp;or&nbsp;EOM-CCSD:&nbsp;10^-8&nbsp;energy,&nbsp;10^-6&nbsp;wfn.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;L914&nbsp;single&nbsp;point:&nbsp;10^-4&nbsp;wfn.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;L914&nbsp;gradient:&nbsp;10^-6&nbsp;wfn.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/10)
`L914`: Whether to do "fake" frozen-core (i.e., with a full transformation).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No;&nbsp;follow&nbsp;/Orb/.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For&nbsp;AO&nbsp;usage&nbsp;(unused&nbsp;here).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;note&nbsp;number&nbsp;of&nbsp;frozen&nbsp;core&nbsp;and&nbsp;virtual&nbsp;and&nbsp;reset&nbsp;/Orb/&nbsp;for&nbsp;full.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;and&nbsp;store&nbsp;full&nbsp;/Orb/&nbsp;back&nbsp;on&nbsp;disk.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L902`: Test flag.




### IOp(9/11)
`L908`: Flags for Green’s function calculations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal&nbsp;use&nbsp;of&nbsp;MO&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;direct&nbsp;computation&nbsp;of&nbsp;<ab||cd>&nbsp;contributions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;direct&nbsp;computation&nbsp;of&nbsp;<ia||bc>&nbsp;contributions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal&nbsp;production&nbsp;of&nbsp;intermediates&nbsp;(in-core&nbsp;if&nbsp;possible).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;use&nbsp;of&nbsp;sort&nbsp;for&nbsp;intermediates.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;window&nbsp;of&nbsp;MOs&nbsp;to&nbsp;refine&nbsp;in&nbsp;the&nbsp;same&nbsp;format&nbsp;as&nbsp;801,&nbsp;but&nbsp;with&nbsp;two&nbsp;ranges&nbsp;on&nbsp;the&nbsp;same&nbsp;line&nbsp;for&nbsp;open-shell.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;N^3&nbsp;algorithm&nbsp;in&nbsp;GFSCMA.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;P3&nbsp;for&nbsp;ionizations&nbsp;and&nbsp;affinities.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OVGF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OVGF&nbsp;+&nbsp;P3&nbsp;for&nbsp;ionization&nbsp;(+&nbsp;P3&nbsp;for&nbsp;affinities,&nbsp;if&nbsp;<ia||bc>&nbsp;present)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 40000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2nd&nbsp;order&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 50000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;P3&nbsp;+&nbsp;PPH3&nbsp;(ionization)&nbsp;,&nbsp;or&nbsp;HHP3&nbsp;(affinities).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 60000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Truncation&nbsp;of&nbsp;virtual&nbsp;space.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 70000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Make&nbsp;OVGF&nbsp;but&nbsp;remove&nbsp;(C1+D1).&nbsp;i.e.&nbsp;PPH3r.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 80000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(P3&nbsp;for&nbsp;ionizations).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;EMin,&nbsp;EMax,&nbsp;and&nbsp;pole&nbsp;strength&nbsp;warning&nbsp;level&nbsp;on&nbsp;one&nbsp;line.&nbsp;Link&nbsp;909&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;Dyson&nbsp;orbitals&nbsp;over&nbsp;the&nbsp;canonical&nbsp;MOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L902`: Test flag.


`L913`: Spin projection control.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;basic&nbsp;projection.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Include&nbsp;triples.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/12)
`L902`: Test flag.


`L908`: Debug flag.




### IOp(9/13)
`L902`: Symmetry constraint of output wavefunction from Stable=Opt.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L909`: 1 for Test mode.




### IOp(9/14)
Non-iterative corrections.


ICNonI


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fourth-order&nbsp;triples.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fourth-&nbsp;and&nbsp;fifth-order&nbsp;singles&nbsp;and&nbsp;triples&nbsp;–QCISD(T),&nbsp;BD(T).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;2,&nbsp;but&nbsp;save&nbsp;the&nbsp;amplitudes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;2,&nbsp;but&nbsp;do&nbsp;E4T&nbsp;as&nbsp;well.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/15)
Type of derivative information generated.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;Lagrangian&nbsp;in&nbsp;L906,&nbsp;L913,&nbsp;L914,&nbsp;L916.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;AO&nbsp;1st&nbsp;derivative&nbsp;terms&nbsp;as&nbsp;well&nbsp;in&nbsp;L906&nbsp;and&nbsp;L914.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;up&nbsp;for&nbsp;second&nbsp;derivatives&nbsp;in&nbsp;L906&nbsp;and&nbsp;L914,&nbsp;doing&nbsp;the&nbsp;non-separable&nbsp;AO&nbsp;2nd&nbsp;derivative&nbsp;terms&nbsp;in&nbsp;L906.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;L&nbsp;and&nbsp;GIAO&nbsp;L(x)&nbsp;in&nbsp;L906.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;up&nbsp;for&nbsp;second&nbsp;derivatives&nbsp;without&nbsp;AO&nbsp;terms.&nbsp;Same&nbsp;as&nbsp;3&nbsp;for&nbsp;L914;&nbsp;skips&nbsp;AO&nbsp;derivatives&nbsp;in&nbsp;L906.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/16)
`L906`: Control of (Semi-) Direct MP2.


* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;a&nbsp;maximum&nbsp;of&nbsp;(-N-6)&nbsp;occupieds&nbsp;per&nbsp;pass,&nbsp;using&nbsp;the&nbsp;fully&nbsp;out-of-core&nbsp;algorithm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;the&nbsp;fully&nbsp;in-core&nbsp;algorithm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Try&nbsp;to&nbsp;minimize&nbsp;integral&nbsp;evaluations&nbsp;as&nbsp;for&nbsp;-3,&nbsp;but&nbsp;also&nbsp;force&nbsp;use&nbsp;of&nbsp;the&nbsp;fully&nbsp;out-of-core&nbsp;algorithm&nbsp;in&nbsp;Tran4D.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;a&nbsp;single&nbsp;integral&nbsp;evaluation&nbsp;as&nbsp;for&nbsp;-2,&nbsp;but&nbsp;also&nbsp;force&nbsp;use&nbsp;of&nbsp;the&nbsp;fully&nbsp;out-of-core&nbsp;algorithm&nbsp;in&nbsp;Tran4D.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Try&nbsp;to&nbsp;minimize&nbsp;integral&nbsp;evals,&nbsp;using&nbsp;fully&nbsp;direct&nbsp;methods&nbsp;if&nbsp;possible,&nbsp;otherwise&nbsp;spill&nbsp;to&nbsp;disk.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;a&nbsp;single&nbsp;integral&nbsp;evaluation&nbsp;(two&nbsp;for&nbsp;UMP2)&nbsp;using&nbsp;disk-based&nbsp;algorithm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;in-memory&nbsp;algorithm&nbsp;(fully&nbsp;direct&nbsp;MP2,&nbsp;requires&nbsp;2OVN&nbsp;words&nbsp;of&nbsp;memory&nbsp;for&nbsp;E2,&nbsp;2N^3&nbsp;words&nbsp;for&nbsp;derivatives).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;-3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* M&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;disk&nbsp;storage&nbsp;for&nbsp;partially&nbsp;transformed&nbsp;integrals&nbsp;handling&nbsp;M&nbsp;occupieds&nbsp;at&nbsp;once.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L913, L914`: Control of in-core integrals for W(Tilde).


* -6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;in-core&nbsp;storage.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Suppress&nbsp;in-core&nbsp;storage.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;in-core&nbsp;if&nbsp;possible.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;AO&nbsp;integral&nbsp;algorithm&nbsp;(L914&nbsp;only).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/17)
`L914`: Functional to use.


`L918`: Auto-adjustment of TAU.




### IOp(9/18)
Iteration scheme: DE = (in A(S) = W(S)/(DE-DELTA(S))) I.E. in the formation of a new wavefunction.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;DE&nbsp;depending&nbsp;on&nbsp;the&nbsp;method&nbsp;used.&nbsp;(IOp(9/5)).&nbsp;For&nbsp;method&nbsp;=&nbsp;0,1&nbsp;DE&nbsp;=&nbsp;W(0)/A0.&nbsp;For&nbsp;method&nbsp;GT.1&nbsp;DE&nbsp;=&nbsp;0.&nbsp;Note&nbsp;that&nbsp;for&nbsp;perturbation&nbsp;methods&nbsp;(Method=2,3,4,5)&nbsp;DE&nbsp;is&nbsp;not&nbsp;really&nbsp;needed&nbsp;since&nbsp;the&nbsp;wavefunction&nbsp;formed&nbsp;never&nbsp;gets&nbsp;used.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;W(0)/A0.&nbsp;Always.&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.&nbsp;Always.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/19)
Extrapolation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;CI&nbsp;using&nbsp;old&nbsp;extrapolation,&nbsp;CC/QCI&nbsp;using&nbsp;RLE.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;extrapolate.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;BFGS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;DIIS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;old&nbsp;extrapolation&nbsp;for&nbsp;CI.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;RLE.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;A&nbsp;as&nbsp;guess&nbsp;for&nbsp;Z.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;scaled&nbsp;A&nbsp;as&nbsp;guess&nbsp;for&nbsp;Z.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reset&nbsp;RLE&nbsp;for&nbsp;Z&nbsp;iterations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/20)
`L901`: Whether to update the total energy with the MP2 energy.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;(used&nbsp;in&nbsp;HF&nbsp;second&nbsp;derivative&nbsp;calculations).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/21)
`L902`: Guess for eigenvector of y-matrix.




### IOp(9/22)
`L919`: Conversion factor.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;factor&nbsp;in&nbsp;format&nbsp;D20.10.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;of&nbsp;10^-8.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/23)
`L919`: Localization of orbitals.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Localize&nbsp;occupieds.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Localize&nbsp;virtuals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Localize&nbsp;both.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;10).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Choose&nbsp;configurations&nbsp;by&nbsp;simple&nbsp;truncation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;configurations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rettrup-Davidson&nbsp;RPA.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Jorgensen-Linderberg&nbsp;Hermetian&nbsp;RPA.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Out-of-core&nbsp;method.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In-core&nbsp;method.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Singlet&nbsp;states.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Triplet&nbsp;states.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L921, L922`: Maximum order of perturbation theory.


`L914`: Correction to CIS.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;primitive&nbsp;CIS-DFT.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes&nbsp;(in&nbsp;primitive&nbsp;in-core&nbsp;program).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes&nbsp;(in&nbsp;MO&nbsp;Basis&nbsp;disk&nbsp;routine).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;CIS-DFT&nbsp;instead.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;CIS(D)&nbsp;with&nbsp;old&nbsp;N^6&nbsp;algorithm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;CIS(D)&nbsp;with&nbsp;N^5&nbsp;algorithm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


The functional is given by IOp(17).




### IOp(9/25)
Print pair contribution and weight to correlation energy.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;at&nbsp;the&nbsp;end&nbsp;of&nbsp;CI.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;at&nbsp;each&nbsp;cycle.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;at&nbsp;one&nbsp;cycle&nbsp;given&nbsp;by&nbsp;input&nbsp;(I3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;at&nbsp;first&nbsp;cycle&nbsp;and&nbsp;at&nbsp;end.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/26)
Normalization of the wavefunction.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normalized&nbsp;to&nbsp;A(0)&nbsp;=&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SUM(S)&nbsp;A(S)^2&nbsp;=&nbsp;1&nbsp;(ALL&nbsp;S).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


NOTE: Perturbation theoretical results are valid with NORM=0 ONLY.




### IOp(9/28)
Printing of dominant configurations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(print&nbsp;coefficients&nbsp;0.1&nbsp;and&nbsp;above).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;print&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;all&nbsp;coefficients&nbsp;every&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scan&nbsp;the&nbsp;‘A’&nbsp;vector&nbsp;and&nbsp;print&nbsp;all&nbsp;coefficients.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scan&nbsp;the&nbsp;‘A’&nbsp;vector&nbsp;and&nbsp;print&nbsp;all&nbsp;coefficients&nbsp;having&nbsp;coefficients&nbsp;greater&nbsp;than&nbsp;0.0001*N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/30)
Calculation of the one-particle density matrices:


* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(21&nbsp;for&nbsp;CI,&nbsp;22&nbsp;otherwise).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;the&nbsp;CI&nbsp;one-particle&nbsp;density&nbsp;matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;form&nbsp;the&nbsp;CI&nbsp;one-particle&nbsp;density&nbsp;matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;the&nbsp;density&nbsp;correct&nbsp;to&nbsp;second&nbsp;order&nbsp;(NOT&nbsp;the&nbsp;same&nbsp;as&nbsp;the&nbsp;density&nbsp;corresponding&nbsp;to&nbsp;the&nbsp;MP2&nbsp;energy).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;compute&nbsp;the&nbsp;density&nbsp;correct&nbsp;to&nbsp;second&nbsp;order.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/31)
`L902, L918`: Print vectors and matrices.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/36)
Compute the T1 Diagnostic of T.J. Lee.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/37)
The Maximum dimension for the coupled cluster extrapolation. The default is 5 for RLE, and 10 for BFGS.




### IOp(9/38)
Minimum dimension for the BFGS coupled cluster. The default is 3. Not meaningful for DIIS extrapolation.




### IOp(9/39)
`L914`: Pick out guesses from restart file or orthogonalize guesses to the states already on restart file (IOp(49) must be set to 1 or 2 for this option to be valid)


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Just&nbsp;take&nbsp;guess&nbsp;from&nbsp;restart&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Make&nbsp;N&nbsp;additional&nbsp;orthogonal&nbsp;guesses&nbsp;to&nbsp;those&nbsp;present.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;which&nbsp;N&nbsp;states&nbsp;to&nbsp;use&nbsp;(free&nbsp;format&nbsp;integers).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


Warning: The states on the restart file MUST be orthogonal to the convergence requested (ie; the previous job indicates wavefunction not just expansion vectors has converged).




### IOp(9/40)
`L906`: Reference wavefunction for MP2.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(HF).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CASSCF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L913, L914`: Threshold for printing eigenvector components.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ITHR&nbsp;=&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ITHR&nbsp;=&nbsp;N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


Where threshold = GFLOAT(10)^-ITHR




### IOp(9/41)
`L914`: Number of states to seek when using Davidson or number of states to print out information for when using DODIAG.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;to&nbsp;2&nbsp;lowest.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;states.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;in&nbsp;principle&nbsp;component&nbsp;of&nbsp;N&nbsp;guesses&nbsp;(DAVIDSON)&nbsp;format&nbsp;I5&nbsp;on&nbsp;last&nbsp;card&nbsp;before&nbsp;EOF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/42)
Method and matrix blocks to work on in L914 (See below)


* -NNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mapped&nbsp;directly&nbsp;to&nbsp;NNN&nbsp;below.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AO&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In-core.&nbsp;Mapped&nbsp;to&nbsp;2,&nbsp;222,&nbsp;or&nbsp;20&nbsp;as&nbsp;appropriate.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MO&nbsp;Mapped&nbsp;to&nbsp;3,&nbsp;333,&nbsp;or&nbsp;30&nbsp;as&nbsp;appropriate.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DEFAULT&nbsp;IS:&nbsp;3&nbsp;(RHF&nbsp;reference&nbsp;state)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 333&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(UHF&nbsp;reference&nbsp;state)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


Bits Matrix Method


* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AA,BB&nbsp;}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AB&nbsp;(NYI)&nbsp;}–>&nbsp;Force&nbsp;DAVIDSON&nbsp;in&nbsp;A.O.&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BA&nbsp;(NYI)&nbsp;}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AA,BB&nbsp;}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AB&nbsp;}–>&nbsp;Force&nbsp;DODIAG&nbsp;to&nbsp;find&nbsp;all&nbsp;roots.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BA&nbsp;}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AA,BB&nbsp;}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AB&nbsp;}–>&nbsp;Force&nbsp;DAVIDSON&nbsp;in&nbsp;M.O.&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BA&nbsp;}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/43)
`L914`: How to handle subsequent Davidson iterations.


* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reduce&nbsp;after&nbsp;iteration&nbsp;N&nbsp;but&nbsp;also&nbsp;include&nbsp;states&nbsp;skipped&nbsp;due&nbsp;to&nbsp;energy&nbsp;criteria&nbsp;at&nbsp;the&nbsp;first&nbsp;iteration&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;only&nbsp;the&nbsp;requested&nbsp;number&nbsp;of&nbsp;states&nbsp;from&nbsp;the&nbsp;beginning.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;(0&nbsp;if&nbsp;restart,&nbsp;1&nbsp;for&nbsp;TD,&nbsp;2&nbsp;for&nbsp;TDA).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Davidson&nbsp;reduces&nbsp;the&nbsp;number&nbsp;of&nbsp;states&nbsp;after&nbsp;iteration&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


The number of extra states to do initially is set by IOp(117).




### IOp(9/44)
`L914`: Density matrix control for filling RWF 633.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;densities&nbsp;of&nbsp;each&nbsp;excited&nbsp;state.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;densities&nbsp;and&nbsp;transition&nbsp;densities&nbsp;from&nbsp;ground.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;densities,&nbsp;transition&nbsp;densities&nbsp;from&nbsp;ground,&nbsp;and&nbsp;transitions&nbsp;densities&nbsp;among&nbsp;all&nbsp;excited&nbsp;states.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;DCT&nbsp;analysis&nbsp;of&nbsp;charge-transfer&nbsp;character&nbsp;for&nbsp;each&nbsp;state.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/45)
`L914`: Debug option for comparing previous results.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Phycon&nbsp;to&nbsp;convert&nbsp;to&nbsp;eV’s.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;old&nbsp;conversion&nbsp;to&nbsp;eV’s.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/46)
`L914`: Control of Davidson convergence.


* <0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Ortvec&nbsp;convergence&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Converge&nbsp;on&nbsp;the&nbsp;number&nbsp;of&nbsp;roots&nbsp;–&nbsp;IOp(41).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Converge&nbsp;on&nbsp;Ci&nbsp;Amplitudes&nbsp;for&nbsp;N&nbsp;lowest&nbsp;states.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/47)
`L914`: Control of Davidson iterations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Usual.&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;do&nbsp;any&nbsp;iterations&nbsp;(Guess=Print).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stop&nbsp;after&nbsp;first&nbsp;iteration.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/48)
Restriction on types of roots (Davidson RHF only).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Guess&nbsp;only&nbsp;singlets.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Guess&nbsp;both&nbsp;singlets&nbsp;and&nbsp;triplets.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Guess&nbsp;only&nbsp;triplets.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


Note: A singlet guess may result in a triplet root in extreme cases (small number of roots sought).




### IOp(9/49)
`L914`: Initial guess vectors.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Make&nbsp;a&nbsp;guess&nbsp;based&nbsp;on&nbsp;diagonal&nbsp;elements.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;guess&nbsp;vectors&nbsp;already&nbsp;on&nbsp;RWF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;guess&nbsp;vectors&nbsp;already&nbsp;on&nbsp;CHK.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;guesses&nbsp;from&nbsp;CIS&nbsp;densities&nbsp;on&nbsp;CHK.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;guesses&nbsp;from&nbsp;CIS&nbsp;densities&nbsp;on&nbsp;RWF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(20&nbsp;for&nbsp;CIS&nbsp;and&nbsp;TDHF,&nbsp;10&nbsp;for&nbsp;TDDFT).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;SCF&nbsp;virtuals&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;IVOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;IVOs&nbsp;without&nbsp;scaling&nbsp;densities&nbsp;(for&nbsp;debugging).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;HF&nbsp;IVOs&nbsp;even&nbsp;if&nbsp;doing&nbsp;TD-KS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;recomputation&nbsp;of&nbsp;integrals&nbsp;during&nbsp;IVO.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/50)
Frozen-core handling for BD.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2&nbsp;if&nbsp;"fake"&nbsp;frozen-core&nbsp;transformation&nbsp;done).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Old&nbsp;method:&nbsp;core&nbsp;orbitals&nbsp;are&nbsp;not&nbsp;updated&nbsp;from&nbsp;their&nbsp;initial&nbsp;values.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update&nbsp;core&nbsp;orbitals&nbsp;according&nbsp;to&nbsp;BD&nbsp;criteria.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update&nbsp;core&nbsp;orbitals&nbsp;acc.&nbsp;to&nbsp;BD&nbsp;criteria,&nbsp;compressing&nbsp;MO&nbsp;integrals&nbsp;for&nbsp;use&nbsp;during&nbsp;CC&nbsp;iterations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/60)
Override standard values of IRadAn.




### IOp(9/61)
Override standard values of IRanWt.




### IOp(9/62)
Override standard values of IRanGd.




### IOp(9/67)
`L913 and L916`: Type of convergence test.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;energy&nbsp;and&nbsp;gradient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Converge&nbsp;on&nbsp;energy&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Converge&nbsp;on&nbsp;energy&nbsp;and&nbsp;gradient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Converge&nbsp;on&nbsp;gradient&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


Convergence on gradient is for extrapolated CI and QCISD procedures.




### IOp(9/68)
`L914`: IEOM (guess for EOM-CC)


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;Default&nbsp;the&nbsp;number&nbsp;of&nbsp;states&nbsp;to&nbsp;do&nbsp;based&nbsp;on&nbsp;number&nbsp;requested&nbsp;for&nbsp;EOM,&nbsp;and&nbsp;convert&nbsp;reading&nbsp;densities&nbsp;if&nbsp;requested&nbsp;into&nbsp;reading&nbsp;amplitudes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/70)
`L913`: CIS/TDA or TD.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(CIS&nbsp;for&nbsp;HF,&nbsp;1&nbsp;for&nbsp;TD-HF&nbsp;and&nbsp;TD-KS&nbsp;with&nbsp;hybrid&nbsp;functionals,&nbsp;2&nbsp;for&nbsp;TD-KS&nbsp;with&nbsp;pure&nbsp;functionals).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RPA&nbsp;using&nbsp;general,&nbsp;non-Hermitean&nbsp;algorithm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RPA&nbsp;using&nbsp;Hermitean&nbsp;scheme&nbsp;for&nbsp;pure&nbsp;DFT,&nbsp;converted&nbsp;here&nbsp;to&nbsp;1&nbsp;for&nbsp;hybrid&nbsp;functionals&nbsp;and&nbsp;HF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CIS/TDA.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/71)
`L914`: Whether to do an extra iteration after Davidson convergence.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/72)
`L914`: Whether to compute frequency-dependant polarizabilities.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/73)
`L914`: Whether to do non-equilibrium solvation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Yes,&nbsp;if&nbsp;doing&nbsp;excited&nbsp;state&nbsp;energy&nbsp;without&nbsp;gradient,&nbsp;or&nbsp;cLR&nbsp;absorption&nbsp;or&nbsp;VEM,&nbsp;no&nbsp;for&nbsp;stability&nbsp;or&nbsp;cLR&nbsp;noneq=write).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No,&nbsp;use&nbsp;equilibrium.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Linear&nbsp;response.&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Corrected&nbsp;linear&nbsp;response.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Vertical&nbsp;excitation&nbsp;model&nbsp;(NYI).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/74)
`L914`: Override default choice of frequency dependence of the XC functional.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;default&nbsp;value.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;form&nbsp;N&nbsp;(see&nbsp;IOp(9/88)&nbsp;in&nbsp;overlay&nbsp;5).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/75)
`L906`: Whether to save amplitudes and <IJ||AB> integrals.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;only&nbsp;if&nbsp;doing&nbsp;second&nbsp;derivatives&nbsp;(SqS12&nbsp;set).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;amplitudes.&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;amplitudes&nbsp;and&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/76)
`L914`: Maximum number of vectors during Davidson.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;200.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/77)
Whether to save converged amplitudes on checkpoint file.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(check&nbsp;ILSW).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ground-state&nbsp;amplitudes&nbsp;were&nbsp;read&nbsp;in.&nbsp;Set&nbsp;initial&nbsp;SAvail,&nbsp;etc.&nbsp;accordingly.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Act&nbsp;as&nbsp;though&nbsp;amplitudes&nbsp;were&nbsp;not&nbsp;read&nbsp;in.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(check&nbsp;ILSW).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check&nbsp;ILSW&nbsp;to&nbsp;see&nbsp;if&nbsp;Z-amplitudes&nbsp;are&nbsp;available.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Z-amplitudes&nbsp;were&nbsp;read&nbsp;in.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;read&nbsp;Z-amplitudes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/81)
`L904`: Minimum number of Pair Natural Orbitals (PNO) to start the extrapolations from, NStart.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;—&nbsp;5&nbsp;(assuming&nbsp;CBS-4&nbsp;calculations,&nbsp;i.e.&nbsp;6-31+G(d’,p’)).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculate&nbsp;the&nbsp;extrapolated&nbsp;value&nbsp;at&nbsp;N&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Get&nbsp;the&nbsp;lowest&nbsp;energy&nbsp;value&nbsp;between&nbsp;CBS(N)&nbsp;and&nbsp;CBS(NVirt).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/82)
`L904`: Convergence tolerance for CBS localization.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;default.&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;10^-N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/83)
`L904`: Localization method.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;localization.&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(4).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Boys.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Population.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Boys+Population.&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Minimal&nbsp;population.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;localization.&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;2nd&nbsp;order.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Localize&nbsp;core&nbsp;even&nbsp;if&nbsp;not&nbsp;needed.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/84)
`L904`: Save CBS localized orbitals to RWF (this will overwrite the SCF orbitals, intended for visualization).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No,&nbsp;don’t&nbsp;save&nbsp;(default).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;save&nbsp;them.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/85)
Flags for SAC-CI.




### IOp(9/86)
`L906`: Whether to generate data compressed to active atoms during mp2 frequencies with ONIOM.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;and&nbsp;also&nbsp;store&nbsp;Hessian&nbsp;contributions&nbsp;over&nbsp;only&nbsp;active&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/87)
AO Integral threshold.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;N=10.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Discard&nbsp;contributions&nbsp;expected&nbsp;to&nbsp;be&nbsp;smaller&nbsp;than&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/101)
`L914, L926`: Raffenetti in DD1Dir.




### IOp(9/104)
Number of states in CIS guess for EOM-CC.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;regular&nbsp;NState&nbsp;(IOp(9/41).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/105)
Maximum batch size in CISAX:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;unlimited.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;more&nbsp;than&nbsp;N&nbsp;density/Fock&nbsp;matrices&nbsp;at&nbsp;a&nbsp;time&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/108)
`L906`: Whether to use matrix multiplication instead of PTrnI1 to transform the first (or back-transform the last) index.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;Decide&nbsp;on&nbsp;the&nbsp;fly&nbsp;looking&nbsp;at&nbsp;the&nbsp;ratio&nbsp;of&nbsp;NBas2p&nbsp;and&nbsp;NTT.&nbsp;Turned&nbsp;off&nbsp;for&nbsp;now.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* NNN0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;matrix&nbsp;multiplication&nbsp;if&nbsp;the&nbsp;ratio&nbsp;NBas2p/NTT&nbsp;is&nbsp;larger&nbsp;than&nbsp;0.NNN.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/114)
`L914`: Number of EOM states per irreducible representation, used to decide on number of CIS states to do for guesses.




### IOp(9/115)
Abelian symmetry in CIS/TD:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;1&nbsp;for&nbsp;direct,&nbsp;2&nbsp;for&nbsp;in-core.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;petite&nbsp;list.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Replicate&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;integral&nbsp;symmetry&nbsp;used.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;10&nbsp;for&nbsp;petite&nbsp;list,&nbsp;20&nbsp;otherwise.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Symmetrize&nbsp;update&nbsp;vectors&nbsp;in&nbsp;DiskD.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;symmetrize&nbsp;vectors.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/116)
PCM options:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;PTE&nbsp;model:&nbsp;PCM&nbsp;only&nbsp;in&nbsp;the&nbsp;reference.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Activate&nbsp;PTED&nbsp;model&nbsp;for&nbsp;CCSD&nbsp;and&nbsp;BD.&nbsp;This&nbsp;method&nbsp;couples&nbsp;the&nbsp;T&nbsp;and&nbsp;Z&nbsp;equations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PTE-S&nbsp;(ground&nbsp;or&nbsp;excited&nbsp;state).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PTES&nbsp;(ground&nbsp;or&nbsp;excited&nbsp;state).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EOM-PTE&nbsp;model:&nbsp;PTE&nbsp;method&nbsp;for&nbsp;ground&nbsp;state,&nbsp;but&nbsp;state-specific&nbsp;solvent&nbsp;response&nbsp;based&nbsp;on&nbsp;the&nbsp;L-T-R&nbsp;part&nbsp;of&nbsp;the&nbsp;EOM&nbsp;1PDM&nbsp;for&nbsp;the&nbsp;excited&nbsp;state.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Linear&nbsp;Response.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/117)
`L914`: IFact (number of extra vectors for initial iterations):


* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;–&nbsp;Max(4,NOp2),&nbsp;unless&nbsp;IOp(43)&nbsp;turns&nbsp;this&nbsp;off.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Max(4,NOp2,N).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/118)
`L914`: First occupied orbital to include in guesses.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;First&nbsp;non-frozen&nbsp;orbital.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Active&nbsp;orbital&nbsp;number&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/119)
`L914`: Last occupied orbital to include in guesses.


* -M&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All&nbsp;but&nbsp;the&nbsp;highest&nbsp;M&nbsp;active&nbsp;occupieds.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Last&nbsp;non-frozen&nbsp;occupied&nbsp;orbital.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Active&nbsp;occupied&nbsp;orbital&nbsp;number&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/120)
`L914`: Minimum energy threshold for initial guesses.


* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;threshold&nbsp;in&nbsp;Hartrees.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;minimum.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;same&nbsp;as&nbsp;threshold&nbsp;for&nbsp;converged&nbsp;states.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/1000&nbsp;eV.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/121)
`L914`: Minimum energy threshold for converged states.


* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;threshold&nbsp;in&nbsp;Hartrees.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;minimum.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;-1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/1000&nbsp;eV.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/122)
Linear response CCSD:


* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Polarizability.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Specific&nbsp;rotation&nbsp;(modified&nbsp;velocity&nbsp;gauge).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Specific&nbsp;rotation&nbsp;(length&nbsp;gauge).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Specific&nbsp;rotation&nbsp;(both&nbsp;MVG&nbsp;and&nbsp;LG).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Frequency&nbsp;dependent&nbsp;LR.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/124)
Epsilon-infinity for SOS with EOM.




### IOp(9/125)
Whether to make permuted copies of integral buckets.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/126)
Maximum number of matrices to handle at a time in DD1Dir.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(-1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;limit.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;At&nbsp;most&nbsp;N&nbsp;matrices&nbsp;at&nbsp;a&nbsp;time.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/127)
Whether to discard MO integrals at the end of this link.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(21).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;IW{1,2,3}Sav&nbsp;if&nbsp;doing&nbsp;derivatives&nbsp;(for&nbsp;old&nbsp;deriv&nbsp;algs).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;save&nbsp;IW{1,2,3}Sav.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/128)
Approximate CC/EOM.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EOM-MBPT2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;P-EOM-MBPT2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/130)
Algorithm control in CISGrd.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1&nbsp;for&nbsp;CIS,&nbsp;3&nbsp;for&nbsp;TDA/TD-HF/TD-DFT).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Single&nbsp;pass&nbsp;doing&nbsp;AX.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Two&nbsp;passes&nbsp;doing&nbsp;(A+B)(X+Y)&nbsp;and&nbsp;(A-B)(X-Y).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Single&nbsp;pass&nbsp;doing&nbsp;AX&nbsp;+&nbsp;BY.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store&nbsp;XC&nbsp;overlap&nbsp;contributions&nbsp;in&nbsp;W.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store&nbsp;XC&nbsp;overlap&nbsp;contributions&nbsp;in&nbsp;S1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/131)
In-Core Code.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;if&nbsp;possible.&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Off.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;On,&nbsp;error&nbsp;if&nbsp;things&nbsp;don’t&nbsp;fit.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(9/132)
Test kill and restart.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Off.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;On.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




## Overlay 10 
### IOp(10/5)
Calculation of first derivatives of post-SCF energies. Only implemented for closed-shell and UHF.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calc.&nbsp;D&nbsp;E(MP2)&nbsp;/&nbsp;D&nbsp;R&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calc.&nbsp;D&nbsp;E(CID)&nbsp;/&nbsp;D&nbsp;R&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calc.&nbsp;D&nbsp;E(CISD)&nbsp;/&nbsp;D&nbsp;R&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calc.&nbsp;D&nbsp;E(CIS/TD)&nbsp;/&nbsp;D&nbsp;R&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calc.&nbsp;D&nbsp;E(CCD)&nbsp;/&nbsp;D&nbsp;R&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calc.&nbsp;D&nbsp;E(CCSD/QCISD)&nbsp;/&nbsp;D&nbsp;R&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calc.&nbsp;D&nbsp;E(BD)&nbsp;/&nbsp;D&nbsp;R&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calc.&nbsp;D&nbsp;E(MP3)&nbsp;/&nbsp;D&nbsp;R&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calc.&nbsp;D&nbsp;E(MP4)&nbsp;/D&nbsp;R&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;CPHF&nbsp;usage&nbsp;(Z-vector&nbsp;unless&nbsp;HF&nbsp;D2E).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Full&nbsp;3*NAtoms&nbsp;CPHF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Z-Vector&nbsp;method.&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Test&nbsp;Z-Vector&nbsp;using&nbsp;full&nbsp;CPHF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;derivative&nbsp;processing&nbsp;—&nbsp;just&nbsp;set&nbsp;up&nbsp;here&nbsp;unless&nbsp;doing&nbsp;HF&nbsp;2nd&nbsp;derivatives&nbsp;simultaneously.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;F1&nbsp;and&nbsp;S1&nbsp;derivative&nbsp;terms&nbsp;here.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;process&nbsp;any&nbsp;derivative&nbsp;terms&nbsp;here.&nbsp;Setup&nbsp;for&nbsp;external&nbsp;processing&nbsp;of&nbsp;W&nbsp;and&nbsp;Z.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;forces.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;nonadiabatic&nbsp;coupling&nbsp;in&nbsp;addition&nbsp;to&nbsp;forces,&nbsp;skipping&nbsp;CPHF.&nbsp;Only&nbsp;implemented&nbsp;for&nbsp;TD.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;nonadiabatic&nbsp;coupling&nbsp;in&nbsp;addition&nbsp;to&nbsp;forces,&nbsp;doing&nbsp;CPHF.&nbsp;Only&nbsp;implemented&nbsp;for&nbsp;CIS&nbsp;and&nbsp;TD.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;nonadiabatic&nbsp;coupling&nbsp;instead&nbsp;of&nbsp;forces,&nbsp;skipping&nbsp;CPHF.&nbsp;Only&nbsp;implemented&nbsp;for&nbsp;TD.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5xxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;nonadiabatic&nbsp;coupling&nbsp;instead&nbsp;of&nbsp;forces,&nbsp;doing&nbsp;CPHF.&nbsp;Only&nbsp;implemented&nbsp;for&nbsp;CIS&nbsp;and&nbsp;TD.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/6)
Calculation of the second derivatives of the SCF energy. Available for RHF and UHF only. Partially coded but NYI for high-spin ROHF.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;do&nbsp;D2&nbsp;E(SCF)&nbsp;/&nbsp;D&nbsp;R(I)&nbsp;D&nbsp;R(J).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Setup&nbsp;for&nbsp;MP2&nbsp;2nd&nbsp;derivatives&nbsp;(i.e.&nbsp;No&nbsp;contributions&nbsp;to&nbsp;the&nbsp;force&nbsp;constants&nbsp;are&nbsp;done&nbsp;here).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;1,&nbsp;but&nbsp;do&nbsp;not&nbsp;do&nbsp;any&nbsp;3rd&nbsp;order&nbsp;properties.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;0&nbsp;if&nbsp;doing&nbsp;post-SCF&nbsp;gradients&nbsp;or&nbsp;same&nbsp;as&nbsp;2&nbsp;otherwise.&nbsp;This&nbsp;makes&nbsp;possible&nbsp;to&nbsp;run&nbsp;L1014&nbsp;with&nbsp;in&nbsp;the&nbsp;old&nbsp;way,&nbsp;i.e.&nbsp;using&nbsp;IRwP1&nbsp;and&nbsp;IRwW1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;use&nbsp;new&nbsp;Px/Wx&nbsp;digestion&nbsp;code&nbsp;if&nbsp;possible,&nbsp;save&nbsp;as&nbsp;little&nbsp;data&nbsp;as&nbsp;possible.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;old&nbsp;Px/Wx&nbsp;digestion&nbsp;code.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;new&nbsp;Px/Wx&nbsp;code&nbsp;but&nbsp;save&nbsp;both&nbsp;S1&nbsp;and&nbsp;F1&nbsp;over&nbsp;MOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;new&nbsp;Px/Wx&nbsp;code&nbsp;and&nbsp;don’t&nbsp;save&nbsp;S1&nbsp;but&nbsp;do&nbsp;save&nbsp;F1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;dipole&nbsp;derivatives&nbsp;using&nbsp;only&nbsp;electric&nbsp;field&nbsp;CPHF&nbsp;and&nbsp;F(x)&nbsp;matrices.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;dipole-dipole,&nbsp;dipole-quadrupole,&nbsp;and&nbsp;OR&nbsp;tensors.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Combination&nbsp;of&nbsp;100&nbsp;and&nbsp;200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set&nbsp;up&nbsp;for&nbsp;GIAO&nbsp;MP2&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;DFT&nbsp;3rd&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;hyperpolarizabilities&nbsp;for&nbsp;second-harmonic&nbsp;generation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000000&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(don’t&nbsp;do&nbsp;magnetic&nbsp;susceptibility).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;magnetic&nbsp;susceptibility.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200000&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;do&nbsp;magnetic&nbsp;susceptibility.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/7)
RMS convergence on C1(I,A) contributions. The max element is tested against 10* this value.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;1.D-8,&nbsp;except&nbsp;1.D-10&nbsp;for&nbsp;Z-Vector&nbsp;CPHF&nbsp;or&nbsp;SSC&nbsp;including&nbsp;Fermi&nbsp;Contact.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.D-N.&nbsp;&nbsp;&nbsp;&nbsp;


`L1003`: Accuracy of CPMCSCF convergence. Only used for Direct CPMCSCF. Convergence = 10^-K. For default value, see IOp(50).




### IOp(10/8)
Selection of linear equation solution method.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;2,&nbsp;except&nbsp;for&nbsp;ZDO&nbsp;non-ONIOM-EE).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Solve&nbsp;CPHF&nbsp;for&nbsp;each&nbsp;variable&nbsp;in&nbsp;a&nbsp;separate&nbsp;call&nbsp;to&nbsp;LinEq1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Expand&nbsp;each&nbsp;variable&nbsp;in&nbsp;a&nbsp;separate&nbsp;expansion&nbsp;space.&nbsp;This&nbsp;is&nbsp;the&nbsp;default&nbsp;and&nbsp;necessary&nbsp;for&nbsp;frequency-dependent&nbsp;perturbations&nbsp;at&nbsp;multiple&nbsp;frequencies,&nbsp;and&nbsp;is&nbsp;the&nbsp;default&nbsp;if&nbsp;there&nbsp;is&nbsp;only&nbsp;1&nbsp;perturbation&nbsp;or&nbsp;if&nbsp;the&nbsp;convergence&nbsp;is&nbsp;set&nbsp;to&nbsp;less&nbsp;10.d-10.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Solve&nbsp;all&nbsp;equations&nbsp;together,&nbsp;possibly&nbsp;reverting&nbsp;to&nbsp;the&nbsp;old&nbsp;(one&nbsp;variable&nbsp;at&nbsp;a&nbsp;time)&nbsp;method&nbsp;in&nbsp;the&nbsp;secondary&nbsp;solution.&nbsp;This&nbsp;is&nbsp;the&nbsp;default&nbsp;for&nbsp;multiple&nbsp;perturbations&nbsp;at&nbsp;the&nbsp;same&nbsp;or&nbsp;zero&nbsp;frequency&nbsp;with&nbsp;the&nbsp;default&nbsp;convergence.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Invert&nbsp;the&nbsp;A&nbsp;matrix&nbsp;directly.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;&nbsp;2&nbsp;if&nbsp;memory&nbsp;permits,&nbsp;or&nbsp;3&nbsp;if&nbsp;the&nbsp;number&nbsp;of&nbsp;right-hand&nbsp;sides&nbsp;is&nbsp;significantly&nbsp;larger&nbsp;than&nbsp;N0&nbsp;(the&nbsp;number&nbsp;after&nbsp;orthogonalization).&nbsp;If&nbsp;memory&nbsp;does&nbsp;not&nbsp;permit&nbsp;direct&nbsp;solution,&nbsp;then&nbsp;4&nbsp;if&nbsp;there&nbsp;is&nbsp;sufficient&nbsp;memory&nbsp;to&nbsp;form&nbsp;the&nbsp;inverse&nbsp;and&nbsp;the&nbsp;reduced&nbsp;dimension&nbsp;is&nbsp;still&nbsp;below&nbsp;that&nbsp;specified&nbsp;by&nbsp;IOp(11),&nbsp;or&nbsp;1&nbsp;if&nbsp;all&nbsp;others&nbsp;are&nbsp;rejected.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;recursive&nbsp;DIIS&nbsp;with&nbsp;simultaneous&nbsp;solution.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Solve&nbsp;linear&nbsp;equations&nbsp;for&nbsp;all&nbsp;N&nbsp;RHS&nbsp;in&nbsp;reduced&nbsp;space.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Solve&nbsp;linear&nbsp;equations&nbsp;for&nbsp;N0&nbsp;RHS&nbsp;in&nbsp;reduced&nbsp;space.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Invert&nbsp;the&nbsp;reduced&nbsp;A-matrix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;NormTp&nbsp;in&nbsp;LinEq2&nbsp;(3,&nbsp;except&nbsp;for&nbsp;2nd&nbsp;order&nbsp;CPHF&nbsp;for&nbsp;Raman/ROA,&nbsp;where&nbsp;it&nbsp;depends&nbsp;on&nbsp;IOp(92)).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Full&nbsp;normalization&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normalize&nbsp;input&nbsp;vectors&nbsp;with&nbsp;norm&nbsp;>&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3xx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;normalization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/10)
Control of CPMCSCF during avoided crossing/conical intersection searches.


`L1003`: The most useful options for IOp(10) are as follows (assumes L510 is run with IOp(14)=310000 or 300000):


* 600006&nbsp;&nbsp;&nbsp;&nbsp;Optimize&nbsp;lowest&nbsp;energy&nbsp;point&nbsp;on&nbsp;a&nbsp;conical&nbsp;intersection&nbsp;(or&nbsp;n-1)hyperline&nbsp;IOp(10)=600006.&nbsp;This&nbsp;takes&nbsp;one&nbsp;state&nbsp;to&nbsp;be&nbsp;IOp(28)&nbsp;and&nbsp;the&nbsp;other&nbsp;IOp(28)-1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 600005&nbsp;&nbsp;&nbsp;&nbsp;As&nbsp;for&nbsp;IOp(10)=600006&nbsp;but&nbsp;solves&nbsp;CP-MCSCF&nbsp;equation.&nbsp;Usually&nbsp;a&nbsp;very&nbsp;small&nbsp;correction&nbsp;but&nbsp;you&nbsp;must&nbsp;check.&nbsp;Needs&nbsp;IOp(17)=200&nbsp;in&nbsp;l510&nbsp;(Orbital&nbsp;Hessian).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 300006&nbsp;or&nbsp;300005&nbsp;&nbsp;&nbsp;&nbsp;Optimize&nbsp;(e2-e1)^2.&nbsp;Not&nbsp;meaningful&nbsp;alone;&nbsp;can&nbsp;be&nbsp;used&nbsp;to&nbsp;start&nbsp;a&nbsp;diff.&nbsp;crossing&nbsp;search.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 700007&nbsp;&nbsp;&nbsp;&nbsp;Computes&nbsp;the&nbsp;SA-CPMCSCF&nbsp;corrected&nbsp;gradient&nbsp;for&nbsp;the&nbsp;Ivec&nbsp;state,&nbsp;and&nbsp;writes&nbsp;it&nbsp;for&nbsp;use&nbsp;in&nbsp;other&nbsp;links.&nbsp;Also&nbsp;computes&nbsp;the&nbsp;SA&nbsp;second&nbsp;derivatives.&nbsp;(The&nbsp;only&nbsp;approximation&nbsp;is&nbsp;the&nbsp;neglect&nbsp;of&nbsp;the&nbsp;second&nbsp;order&nbsp;orbital&nbsp;rotation&nbsp;derivatives.)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 700006&nbsp;&nbsp;&nbsp;&nbsp;Computes&nbsp;the&nbsp;SA-CPMCSCF&nbsp;corrected&nbsp;gradient&nbsp;for&nbsp;the&nbsp;Ivec&nbsp;state,&nbsp;and&nbsp;writes&nbsp;it&nbsp;for&nbsp;use&nbsp;in&nbsp;other&nbsp;links.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;00X&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Extras&nbsp;at&nbsp;CP-MCSCF,&nbsp;where&nbsp;X=:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1:&nbsp;Non-optimum&nbsp;orbitals&nbsp;(obsolete).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2:&nbsp;Non-optimum&nbsp;vector&nbsp;(obsolete).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3:&nbsp;Non-optimum&nbsp;orbitals&nbsp;without&nbsp;Z-vector&nbsp;trick&nbsp;(obsolete).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4:&nbsp;Calculate&nbsp;Ha&nbsp;contribution&nbsp;to&nbsp;Der&nbsp;Cp&nbsp;via&nbsp;<Ci|H|Cj>&nbsp;disactivated.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5:&nbsp;Conical&nbsp;intersection&nbsp;information.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6:&nbsp;Conical&nbsp;intersection&nbsp;information&nbsp;without&nbsp;solving&nbsp;CP&nbsp;equations&nbsp;(approx.&nbsp;values).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7:&nbsp;Compute&nbsp;approximation&nbsp;of&nbsp;the&nbsp;SA&nbsp;second&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8:&nbsp;Conical&nbsp;intersection&nbsp;information&nbsp;using&nbsp;Z-vector&nbsp;trick.&nbsp;This&nbsp;option&nbsp;should&nbsp;be&nbsp;set&nbsp;if&nbsp;solving&nbsp;the&nbsp;cpmcscf&nbsp;equations&nbsp;for&nbsp;either&nbsp;a&nbsp;SA&nbsp;gradient&nbsp;or&nbsp;conical&nbsp;intersection&nbsp;optimization&nbsp;only&nbsp;compatible&nbsp;with&nbsp;IOp(50=2&nbsp;or&nbsp;3&nbsp;or&nbsp;with&nbsp;Hessian&nbsp;inversion&nbsp;IOp(17=0).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;QL0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reserved&nbsp;for&nbsp;future&nbsp;use.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00N&nbsp;000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Other&nbsp;state&nbsp;in&nbsp;grdiff/dercpl.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N:&nbsp;Calculate&nbsp;the&nbsp;derivative&nbsp;couplings&nbsp;of&nbsp;the&nbsp;Nth&nbsp;state.&nbsp;Defaults&nbsp;to&nbsp;IOp(28)-1&nbsp;so&nbsp;not&nbsp;required.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0M0&nbsp;000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contribution&nbsp;to&nbsp;be&nbsp;included&nbsp;at&nbsp;derivative&nbsp;coupling,&nbsp;where&nbsp;M=:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0:&nbsp;Both&nbsp;CI&nbsp;and&nbsp;orbs&nbsp;are&nbsp;included.&nbsp;DC=Ea+Ex+Ey.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1:&nbsp;Only&nbsp;CI&nbsp;contribution.&nbsp;DC=&nbsp;Ea.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2:&nbsp;CI&nbsp;and&nbsp;ortho&nbsp;contributions&nbsp;will&nbsp;be&nbsp;included.&nbsp;DC=&nbsp;Ea+Ey.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3:&nbsp;Only&nbsp;orbital&nbsp;contribution&nbsp;will&nbsp;be&nbsp;here&nbsp;DC=Ex.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4:&nbsp;Orbital&nbsp;and&nbsp;ortho&nbsp;contributions.&nbsp;DC=Ex+Ey.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* K00&nbsp;000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Which&nbsp;gradient&nbsp;to&nbsp;use&nbsp;at&nbsp;the&nbsp;optimization&nbsp;links,&nbsp;where&nbsp;K=:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0:&nbsp;(Scaled&nbsp;gradient&nbsp;difference&nbsp;or&nbsp;Fxyz).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1:&nbsp;Derivative&nbsp;coupling(without&nbsp;division&nbsp;by&nbsp;energy&nbsp;diff.)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2:&nbsp;-//-&nbsp;-//-&nbsp;(after&nbsp;-//-&nbsp;-//-&nbsp;-//-)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3:&nbsp;Unscaled&nbsp;gradient&nbsp;difference&nbsp;*&nbsp;E2-E1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4:&nbsp;Projection&nbsp;of&nbsp;ivec&nbsp;gradient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5:&nbsp;Read&nbsp;forces&nbsp;from&nbsp;the&nbsp;input&nbsp;stream&nbsp;(test&nbsp;purposes).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6:&nbsp;Normalized&nbsp;gradient&nbsp;difference&nbsp;*&nbsp;E2-E1&nbsp;+&nbsp;projected&nbsp;ivec&nbsp;gradient&nbsp;(conical&nbsp;intersection&nbsp;searches).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7:&nbsp;iVec&nbsp;gradient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
*  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8:&nbsp;force&nbsp;(n-1)&nbsp;intersection&nbsp;search&nbsp;(to&nbsp;be&nbsp;used&nbsp;if&nbsp;GD&nbsp;is&nbsp;small).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/11)
Largest matrix for direct inversion in LinEq2.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(10000).&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Always&nbsp;use&nbsp;DIIS,&nbsp;never&nbsp;invert&nbsp;directly.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;DIIS&nbsp;recursively&nbsp;if&nbsp;the&nbsp;O(N^3)&nbsp;work&nbsp;(N*N*NSolve)&nbsp;is&nbsp;at&nbsp;least&nbsp;N^3.&nbsp;Rounded&nbsp;to&nbsp;an&nbsp;even&nbsp;multiple&nbsp;of&nbsp;1000.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/13)
The nature of the perturbation(s).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1st&nbsp;order&nbsp;nuclear&nbsp;and&nbsp;electric&nbsp;field).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* IJKL&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nuclear&nbsp;Lth&nbsp;order.&nbsp;Electric&nbsp;field&nbsp;Kth&nbsp;order.&nbsp;Magnetic&nbsp;field&nbsp;Jth&nbsp;order.&nbsp;Nuclear&nbsp;magnetic&nbsp;moment&nbsp;Ith&nbsp;order.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/14)
Whether to update dipole and polarizability derivatives.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(yes&nbsp;if&nbsp;IOp(5)&nbsp;=&nbsp;0).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update&nbsp;dipole.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;update&nbsp;dipole&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update&nbsp;polarizability.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;update&nbsp;polarizability.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;2nd&nbsp;order&nbsp;cphf&nbsp;for&nbsp;polarizability&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/15)
What to do with expansion vectors from the linear equations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;vectors&nbsp;at&nbsp;end.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Delete&nbsp;vectors&nbsp;at&nbsp;end&nbsp;of&nbsp;each&nbsp;CPHF.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pass&nbsp;vectors&nbsp;from&nbsp;1st&nbsp;to&nbsp;2nd&nbsp;order&nbsp;CPHF,&nbsp;but&nbsp;delete&nbsp;at&nbsp;end&nbsp;of&nbsp;link&nbsp;(off&nbsp;given&nbsp;defaults&nbsp;in&nbsp;CPHF).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;only&nbsp;static&nbsp;electric&nbsp;field&nbsp;solutions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(use&nbsp;old&nbsp;vectors&nbsp;if&nbsp;available).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;old&nbsp;vectors&nbsp;if&nbsp;available.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ignore&nbsp;old&nbsp;vectors.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


### IOp(10/16)
Convergence in secondary linear equations (only for simultaneous solution).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;standard&nbsp;machine&nbsp;tolerance&nbsp;(MDCutO)&nbsp;on&nbsp;maximum&nbsp;and&nbsp;rms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Convergence&nbsp;is&nbsp;10^-N&nbsp;for&nbsp;max&nbsp;and&nbsp;rms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/17)
Frozen-core.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(use&nbsp;AO&nbsp;2PDM&nbsp;for&nbsp;Lagrangian&nbsp;only&nbsp;if&nbsp;orbitals&nbsp;are&nbsp;frozen&nbsp;in&nbsp;/Orb/).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;C1,&nbsp;C2,&nbsp;S1,&nbsp;and&nbsp;S2&nbsp;off&nbsp;the&nbsp;AO&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Convert&nbsp;/Orb/&nbsp;to&nbsp;full,&nbsp;for&nbsp;debugging&nbsp;frozen-core&nbsp;with&nbsp;integrals&nbsp;over&nbsp;the&nbsp;full&nbsp;window.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;as&nbsp;2,&nbsp;but&nbsp;leave&nbsp;the&nbsp;full&nbsp;version&nbsp;of&nbsp;/Orb/&nbsp;on&nbsp;the&nbsp;disk.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L1003`: Controls direct or in-core version of CPMCSCF.


* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In-core&nbsp;version.&nbsp;Must&nbsp;be&nbsp;used&nbsp;with&nbsp;IOp(5/17=200).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 400&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Direct&nbsp;solution&nbsp;of&nbsp;CPMCSCF&nbsp;equations.&nbsp;Must&nbsp;be&nbsp;used&nbsp;with&nbsp;IOp(5/17=400).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/18)
Whether to do correct or approximate CPHF.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CPHF&nbsp;is&nbsp;done&nbsp;correctly.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;A-matrix&nbsp;is&nbsp;neglected,&nbsp;and&nbsp;hence&nbsp;the&nbsp;U-matrices&nbsp;are&nbsp;set&nbsp;equal&nbsp;to&nbsp;the&nbsp;B-matrices&nbsp;(i.e.,&nbsp;uncoupled&nbsp;Hartree-Fock&nbsp;is&nbsp;used).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;U-matrices&nbsp;are&nbsp;set&nbsp;to&nbsp;zero.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Only&nbsp;a&nbsp;single&nbsp;set&nbsp;of&nbsp;products&nbsp;AX&nbsp;are&nbsp;computed,&nbsp;independent&nbsp;of&nbsp;convergence&nbsp;criteria.&nbsp;Simultaneous&nbsp;solution&nbsp;is&nbsp;implied.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/19)
Whether overlap (S1) terms must be included.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(yes,&nbsp;unless&nbsp;ZDO).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


Note that the appropriate RWF (588) must be present in any case.




### IOp(10/20)
How to handle 2e integral contributions.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(decide&nbsp;on&nbsp;the&nbsp;fly).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;the&nbsp;2e&nbsp;integral&nbsp;files,&nbsp;MO&nbsp;if&nbsp;possible.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;the&nbsp;2e&nbsp;integrals&nbsp;when&nbsp;needed.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;use&nbsp;of&nbsp;AO&nbsp;integrals,&nbsp;even&nbsp;if&nbsp;MO&nbsp;ones&nbsp;are&nbsp;available,&nbsp;i.e.&nbsp;force&nbsp;AO&nbsp;or&nbsp;direct.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;use&nbsp;<IA||BC>&nbsp;integrals,&nbsp;even&nbsp;if&nbsp;present.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MNx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;option&nbsp;MN&nbsp;in&nbsp;control&nbsp;of&nbsp;2e&nbsp;integral&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/21)
Whether to store Uai, Spq, and full MO Fock matrix derivatives in permanent RWFs.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;Disables&nbsp;use&nbsp;of&nbsp;symmetry&nbsp;to&nbsp;reduce&nbsp;the&nbsp;size&nbsp;of&nbsp;the&nbsp;CPHF&nbsp;problem&nbsp;here.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;magnetic&nbsp;MO&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/22)
Which multipole (electric field) perturbations to include? Only used if J part of IOp(10/13) is non-zero.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;Uniform&nbsp;electric&nbsp;field&nbsp;(dipole)&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dipole&nbsp;(uniform&nbsp;electric&nbsp;field).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Quadrupole&nbsp;(electric&nbsp;field&nbsp;gradient,&nbsp;all&nbsp;6&nbsp;Cartesian&nbsp;components).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Octupole.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hexadecapole.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/28)
State for CPCIS/CPTD, CPMCSCF, and NAC.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nth&nbsp;excited&nbsp;state.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/29)
Use of Raffenetti integrals during direct SCF.


* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All&nbsp;integrals&nbsp;done&nbsp;as&nbsp;Raffenetti&nbsp;if&nbsp;there&nbsp;are&nbsp;N&nbsp;or&nbsp;more&nbsp;matrices;&nbsp;all&nbsp;as&nbsp;regular&nbsp;if&nbsp;there&nbsp;are&nbsp;<&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;let&nbsp;FoFJK&nbsp;decide.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All&nbsp;integrals&nbsp;are&nbsp;done&nbsp;as&nbsp;regular&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Integrals&nbsp;with&nbsp;degree&nbsp;of&nbsp;contraction&nbsp;greater&nbsp;than&nbsp;or&nbsp;equal&nbsp;to&nbsp;N&nbsp;are&nbsp;done&nbsp;are&nbsp;regular&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/30)
In-core storage of 2e integrals.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;—&nbsp;do&nbsp;if&nbsp;possible&nbsp;in&nbsp;direct&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;in-core&nbsp;storage;&nbsp;recover&nbsp;ints&nbsp;if&nbsp;available&nbsp;on&nbsp;RWF&nbsp;610.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;recomputation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/31)
Whether to use symmetry to reduce the number of CPHF equations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(yes).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;Override&nbsp;check&nbsp;of&nbsp;density&nbsp;matrix&nbsp;symmetry.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2e&nbsp;integral&nbsp;symmetry&nbsp;in&nbsp;CPHF&nbsp;(default&nbsp;2,&nbsp;except&nbsp;3&nbsp;for&nbsp;nuclear&nbsp;derivatives).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;via&nbsp;petite&nbsp;list&nbsp;if&nbsp;possible,&nbsp;integral&nbsp;replication&nbsp;if&nbsp;not.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;via&nbsp;integral&nbsp;replication.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/32)
`L1014`: Whether to apply interchange.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Yes).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L1003`: Whether to read D2E file.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/45)
Type of gauge transformations to perform to calculate the current distribution within the molecule, and hence the molecule’s other magnetic properties.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(16&nbsp;if&nbsp;doing&nbsp;magnetic&nbsp;CPHF).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;single&nbsp;gauge&nbsp;origin&nbsp;–&nbsp;the&nbsp;gauge&nbsp;used&nbsp;to&nbsp;calculate&nbsp;the&nbsp;angular&nbsp;momentum&nbsp;perturbed&nbsp;wavefunctions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;IGAIM&nbsp;method&nbsp;–&nbsp;gauge&nbsp;origin&nbsp;coincident&nbsp;with&nbsp;the&nbsp;nucleus&nbsp;of&nbsp;the&nbsp;integrated&nbsp;atomic&nbsp;regions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;CSGT&nbsp;method.&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;single&nbsp;gauge&nbsp;origin&nbsp;–&nbsp;the&nbsp;coordinates&nbsp;of&nbsp;which&nbsp;are&nbsp;read&nbsp;in&nbsp;(in&nbsp;Angstroms).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 16&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;GIAOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/46)
Whether to calculate dipole and rotational strengths (VCD).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;(Default).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;only&nbsp;optical&nbsp;rotational&nbsp;using&nbsp;GIAOs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;velocity&nbsp;optical&nbsp;rotation&nbsp;(CPHF&nbsp;for&nbsp;r&nbsp;x&nbsp;Del&nbsp;perturbation).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;velocity&nbsp;optical&nbsp;rotation&nbsp;(CPHF&nbsp;for&nbsp;Del&nbsp;perturbation).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;velocity&nbsp;optical&nbsp;rotation&nbsp;(CPHF&nbsp;for&nbsp;both&nbsp;Del&nbsp;and&nbsp;r&nbsp;x&nbsp;Del).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;length&nbsp;optical&nbsp;rotation&nbsp;with&nbsp;GIAOs&nbsp;(electric&nbsp;field&nbsp;CPHF).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;length&nbsp;optical&nbsp;rotation&nbsp;with&nbsp;GIAOs&nbsp;(magnetic&nbsp;field&nbsp;CPHF).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/47)
Whether to do spin-spin coupling constants.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Just&nbsp;do&nbsp;the&nbsp;Fermi-contact&nbsp;contribution.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;but&nbsp;do&nbsp;not&nbsp;print/store&nbsp;the&nbsp;Fermi-Contact&nbsp;contribution.&nbsp;(This&nbsp;assumes&nbsp;that&nbsp;the&nbsp;FC&nbsp;term&nbsp;was&nbsp;done&nbsp;in&nbsp;a&nbsp;previous&nbsp;job&nbsp;step).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/48)
Whether to operate only over perturbations involving active atoms.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(for&nbsp;nuclear,&nbsp;compress&nbsp;if&nbsp;overlay&nbsp;11&nbsp;did).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compress.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;compress.&nbsp;For&nbsp;SSC&nbsp;or&nbsp;frequencies&nbsp;with&nbsp;frozen&nbsp;atoms,&nbsp;do&nbsp;CPHF&nbsp;for&nbsp;all&nbsp;atoms,&nbsp;even&nbsp;frozen&nbsp;ones.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;compress,&nbsp;but&nbsp;blank&nbsp;contributions&nbsp;for&nbsp;inactive&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compress&nbsp;and&nbsp;store&nbsp;force&nbsp;constants&nbsp;only&nbsp;over&nbsp;active&nbsp;atoms&nbsp;(for&nbsp;ONIOM(MO:MM)&nbsp;Opt=CalcFC&nbsp;with&nbsp;micro-iterations).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Permute&nbsp;the&nbsp;order&nbsp;of&nbsp;permutations&nbsp;here&nbsp;in&nbsp;order&nbsp;to&nbsp;put&nbsp;QM&nbsp;atoms&nbsp;ahead&nbsp;of&nbsp;electronic&nbsp;embedding&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;a&nbsp;list&nbsp;of&nbsp;atoms&nbsp;to&nbsp;include&nbsp;in&nbsp;perturbations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(100).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All&nbsp;ONIOM-active,&nbsp;non-frozen&nbsp;nuclei&nbsp;are&nbsp;included&nbsp;in&nbsp;nuclear&nbsp;perturbations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Atoms&nbsp;which&nbsp;are&nbsp;not&nbsp;used&nbsp;in&nbsp;the&nbsp;redundant&nbsp;internal&nbsp;coordinate&nbsp;set&nbsp;are&nbsp;not&nbsp;included&nbsp;in&nbsp;the&nbsp;list&nbsp;of&nbsp;perturbations.&nbsp;Saves&nbsp;time&nbsp;for&nbsp;ONIOM-EE&nbsp;non-quadratic&nbsp;Opt=CalcFC.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(do&nbsp;not&nbsp;include&nbsp;frozen&nbsp;atom&nbsp;coordinates&nbsp;in&nbsp;perturbations&nbsp;unless&nbsp;saving&nbsp;Fock-derivatives).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Keep&nbsp;frozen&nbsp;atoms&nbsp;in&nbsp;the&nbsp;perturbation&nbsp;list.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Keep&nbsp;frozen&nbsp;atoms&nbsp;in&nbsp;the&nbsp;perturbation&nbsp;list,&nbsp;but&nbsp;zero&nbsp;their&nbsp;B&nbsp;matrices.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


When Fermi-contact spin-spin couplings are read from a previous job step, the same atoms are selected when computing the other terms.




### IOp(10/49)
Flag for doing FD polarizability derivatives.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;do&nbsp;nuclear&nbsp;coord&nbsp;CPHF&nbsp;for&nbsp;Ux&nbsp;and&nbsp;use&nbsp;interchange&nbsp;(production).&nbsp;Default&nbsp;if&nbsp;same&nbsp;basis&nbsp;used&nbsp;to&nbsp;compute&nbsp;both&nbsp;FD&nbsp;polar&nbsp;derivatives&nbsp;and&nbsp;force&nbsp;field.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;do&nbsp;(static)&nbsp;2nd&nbsp;order&nbsp;cphf&nbsp;wrt&nbsp;applied&nbsp;field,&nbsp;compute&nbsp;contribution&nbsp;from&nbsp;F(x)/Bx&nbsp;here&nbsp;and&nbsp;use&nbsp;interchange&nbsp;(production).&nbsp;Default&nbsp;if&nbsp;only&nbsp;computing&nbsp;FD&nbsp;polar&nbsp;derivative&nbsp;using&nbsp;this&nbsp;basis.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;like&nbsp;2,&nbsp;except&nbsp;use&nbsp;L1110&nbsp;to&nbsp;produce&nbsp;F(x)&nbsp;and&nbsp;MakeAB&nbsp;for&nbsp;Bx&nbsp;(debugging&nbsp;option).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;like&nbsp;1,&nbsp;except&nbsp;use&nbsp;partial&nbsp;interchange&nbsp;(debugging&nbsp;option).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;do&nbsp;2nd&nbsp;order&nbsp;CPHF&nbsp;with&nbsp;respect&nbsp;to&nbsp;field&nbsp;and&nbsp;nuclear&nbsp;coord.&nbsp;(debugging&nbsp;option).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Also&nbsp;do&nbsp;dipole-quadrupole&nbsp;polarizability&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Also&nbsp;do&nbsp;dipole-magnetic&nbsp;dipole&nbsp;polarizability&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/50)
`L1003`: This controls mode of action of the CPMCSCF. The 3*(Natom-1) linear equations are either solved in turn or an iterative tridiagonal solution of the inverse of Hessian is developed. The first method is very expensive because it scales as 3*(Natom-1)*Nbasis^2 whereas the second scales as Nbasis^2.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;same&nbsp;as&nbsp;3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Solve&nbsp;each&nbsp;atom&nbsp;in&nbsp;turn.&nbsp;This&nbsp;is&nbsp;the&nbsp;most&nbsp;accurate&nbsp;approach&nbsp;but&nbsp;it&nbsp;is&nbsp;much&nbsp;more&nbsp;expensive.&nbsp;The&nbsp;recommended&nbsp;value&nbsp;of&nbsp;IOp(7)&nbsp;is&nbsp;7&nbsp;(10^-7).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DIIS&nbsp;method&nbsp;with&nbsp;multiple&nbsp;rhs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DIIS&nbsp;method&nbsp;with&nbsp;multiple&nbsp;rhs.&nbsp;Forces&nbsp;scalar&nbsp;multiplications.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tridiagonal&nbsp;solution&nbsp;of&nbsp;inverse&nbsp;of&nbsp;Hessian.&nbsp;(Default).&nbsp;The&nbsp;recommended&nbsp;value&nbsp;of&nbsp;IOp(7)&nbsp;is&nbsp;12&nbsp;(10^-12).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/55)
Options for trajectory surface hopping calculations.


See mcscf.F for descriptions.




### IOp(10/60-62)
Override standard values of IRadAn, IRanWt, and IRanGd. The default for IOp(60) here is -3, two steps down from default, unless post-SCF gradients or spin-spin couplings are being computed, in which case the same grid is used as in the rest of the calculation.


`L1002, L1014`: Special values for IOp(60):


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(-1&nbsp;for&nbsp;post-SCF&nbsp;gradients&nbsp;and&nbsp;spin-spin&nbsp;coupling,&nbsp;otherwise&nbsp;-3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N>1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;specified&nbsp;grid.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;the&nbsp;same&nbsp;grid&nbsp;as&nbsp;the&nbsp;rest&nbsp;of&nbsp;the&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;a&nbsp;grid&nbsp;one&nbsp;step&nbsp;smaller&nbsp;than&nbsp;the&nbsp;general&nbsp;calculation&nbsp;(finegrid&nbsp;for&nbsp;int=ultrafine,&nbsp;sg1&nbsp;for&nbsp;int=finegrid,&nbsp;etc.).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;a&nbsp;grid&nbsp;two&nbsp;steps&nbsp;smaller&nbsp;than&nbsp;the&nbsp;general&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -NN0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A&nbsp;number&nbsp;with&nbsp;two&nbsp;bits&nbsp;for&nbsp;the&nbsp;default&nbsp;in&nbsp;each&nbsp;nuclear&nbsp;case:
N&nbsp;=&nbsp;10(0/1/2/3)&nbsp;+&nbsp;(0/4/8/12)&nbsp;+&nbsp;(0/16/32/48)&nbsp;where&nbsp;the&nbsp;four&nbsp;choices&nbsp;are:
    0&nbsp;=&nbsp;default&nbsp;(same&nbsp;as&nbsp;3&nbsp;and&nbsp;global&nbsp;default).
    1&nbsp;=&nbsp;two&nbsp;steps&nbsp;smaller&nbsp;grid&nbsp;for&nbsp;GGAs,&nbsp;one&nbsp;for&nbsp;tau&nbsp;functionals.
    2&nbsp;=&nbsp;one&nbsp;step&nbsp;smaller&nbsp;grid.
    3&nbsp;=&nbsp;full&nbsp;grid.
and&nbsp;the&nbsp;3&nbsp;terms&nbsp;are&nbsp;for&nbsp;a)&nbsp;CPKS&nbsp;during&nbsp;ground&nbsp;state&nbsp;frequencies,&nbsp;b)&nbsp;CPKS&nbsp;during&nbsp;ground&nbsp;state&nbsp;part&nbsp;of&nbsp;TD&nbsp;and&nbsp;double&nbsp;hybrid&nbsp;frequencies&nbsp;and&nbsp;c)&nbsp;CPTD&nbsp;during&nbsp;TD&nbsp;frequencies.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -640&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sets&nbsp;all&nbsp;flags&nbsp;3&nbsp;to&nbsp;zero&nbsp;so&nbsp;default&nbsp;of&nbsp;two&nbsp;steps&nbsp;everywhere.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


The values ≤-10 are primarily useful in setting alternate defaults in `Default.Route` or on the command line.




### IOp(10/63)
Change FMM defaults.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;Use&nbsp;FMM&nbsp;if&nbsp;turned&nbsp;on&nbsp;globally,&nbsp;use&nbsp;more&nbsp;aggressive&nbsp;cutoffs&nbsp;in&nbsp;Xc&nbsp;integration,&nbsp;use&nbsp;more&nbsp;aggressive&nbsp;cutoffs&nbsp;in&nbsp;integrals&nbsp;and&nbsp;FMM&nbsp;unless&nbsp;doing&nbsp;NFx.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;FMM&nbsp;here&nbsp;regardless.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;FMM&nbsp;if&nbsp;turned&nbsp;on&nbsp;globally.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;FMM&nbsp;on&nbsp;here&nbsp;regardless.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;global&nbsp;cutoffs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;local,&nbsp;lower&nbsp;cutoffs&nbsp;suitable&nbsp;only&nbsp;for&nbsp;CPHF/CPKS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;FoFCou&nbsp;as&nbsp;well&nbsp;as&nbsp;FMM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/70)
`L1003`: Memory estimation scheme:


* 0&nbsp;or&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;Better&nbsp;memory&nbsp;estimation&nbsp;for&nbsp;¾&nbsp;integral&nbsp;transformation&nbsp;(Default).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Old&nbsp;memory&nbsp;estimation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/72)
Whether to do frequency-dependant properties.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No,&nbsp;unless&nbsp;both&nbsp;electric&nbsp;and&nbsp;magnetic&nbsp;properties&nbsp;are&nbsp;requested).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Also&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;with&nbsp;formalism&nbsp;for&nbsp;frequency-dependent&nbsp;XC&nbsp;response.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update&nbsp;frequency-dependent&nbsp;property&nbsp;file&nbsp;if&nbsp;frequency-dep.&nbsp;calculation&nbsp;is&nbsp;performed.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update&nbsp;regardless.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;update.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/73)
Maximum number of CPHF cycles.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1000).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N<0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;cycles&nbsp;but&nbsp;return&nbsp;to&nbsp;default&nbsp;if&nbsp;restarting.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/74)
Whether to do non-equilibrium solvation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;Only&nbsp;if&nbsp;frequency-dependant.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;Not&nbsp;doing&nbsp;state-specific&nbsp;iterations.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Doing&nbsp;state-specific&nbsp;with&nbsp;non-equilibrium&nbsp;solvation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Doing&nbsp;state-specific&nbsp;with&nbsp;equilibrium&nbsp;solvation&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/75)
Print during NMR.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;tensors&nbsp;and&nbsp;eigenvalues.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;eigenvectors&nbsp;as&nbsp;well.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/76)
Override general choice of exchange-correlation frequency dependence.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;global&nbsp;value&nbsp;for&nbsp;this&nbsp;job&nbsp;step.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;type&nbsp;N&nbsp;(see&nbsp;IOp(10/88)&nbsp;in&nbsp;overlay&nbsp;5).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/77)
Test CPHF results by checking the CPHF equations using the complete MO Fock and density derivatives.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/79)
Stop L1002 at selected points for testing restarts.


* MNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stop&nbsp;at&nbsp;pass&nbsp;M&nbsp;(default&nbsp;1),&nbsp;restart&nbsp;point&nbsp;NN.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/80)
Options for trajectory surface hopping calculations. See mcscf.F for descriptions.




### IOp(10/81)
Control of number of passes in AXAO.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;at&nbsp;most&nbsp;96&nbsp;matrices&nbsp;at&nbsp;a&nbsp;time&nbsp;if&nbsp;doing&nbsp;FMM,&nbsp;otherwise&nbsp;no&nbsp;limit.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As&nbsp;few&nbsp;passes&nbsp;(as&nbsp;many&nbsp;matrices)&nbsp;as&nbsp;possible.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;at&nbsp;most&nbsp;N&nbsp;densities&nbsp;per&nbsp;pass.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N<-1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;at&nbsp;least&nbsp;-N&nbsp;passes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/82)
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;recalculation&nbsp;of&nbsp;MO&nbsp;integrals&nbsp;for&nbsp;MOCPHF.&nbsp;Debugging&nbsp;option.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/87)
Accuracy of 2e integrals.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/90)
Whether to do correct or approximate CPCIS.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CPCIS&nbsp;is&nbsp;done&nbsp;correctly.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;A-matrix&nbsp;is&nbsp;neglected,&nbsp;and&nbsp;hence&nbsp;the&nbsp;U-matrices&nbsp;are&nbsp;set&nbsp;equal&nbsp;to&nbsp;the&nbsp;B-matrices&nbsp;(i.e.,&nbsp;uncoupled&nbsp;Hartree-Fock&nbsp;is&nbsp;used).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;U-matrices&nbsp;are&nbsp;set&nbsp;to&nbsp;zero.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Only&nbsp;a&nbsp;single&nbsp;set&nbsp;of&nbsp;products&nbsp;AX&nbsp;are&nbsp;computed,&nbsp;independent&nbsp;of&nbsp;convergence&nbsp;criteria.&nbsp;Simultaneous&nbsp;solution&nbsp;is&nbsp;implied.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/91)
`L1002`: Limit IDoFFX.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;use&nbsp;the&nbsp;best&nbsp;possible.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Limit&nbsp;IDoFFX<=N,&nbsp;N=9=>IDoFFX=0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;IDoFFX=N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/92)
Normalization to speed up Raman/ROA:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/93)
Generate file for AICD. Only works with NMR=CSGT.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;all&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;read&nbsp;in&nbsp;orbitals&nbsp;to&nbsp;include.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(20).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Write&nbsp;small&nbsp;elements&nbsp;in&nbsp;matrices.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;write&nbsp;small&nbsp;elements&nbsp;in&nbsp;matrices.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/94)
`L1014`: Threshold for testing Tx.T.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;5.d-6,&nbsp;continue&nbsp;if&nbsp;test&nbsp;fails.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.d-N,&nbsp;die&nbsp;if&nbsp;test&nbsp;fails.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N<0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.d+N,&nbsp;continue&nbsp;test&nbsp;fails.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -99&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;report&nbsp;but&nbsp;but&nbsp;do&nbsp;not&nbsp;die&nbsp;if&nbsp;test&nbsp;fails.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/95)
`L1014`: Limit IDoFFX.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;&nbsp;use&nbsp;the&nbsp;best&nbsp;possible,&nbsp;currently&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Limit&nbsp;IDoFFX≤N,&nbsp;N=9=>IDoFFX=0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;IDoFFX=N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(3&nbsp;for&nbsp;IDoFFX=6,&nbsp;1&nbsp;otherwise).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;optimize&nbsp;the&nbsp;XC&nbsp;matrices&nbsp;update.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Optimize&nbsp;XC&nbsp;matrices&nbsp;update&nbsp;involving&nbsp;T/Tx,&nbsp;but&nbsp;not&nbsp;G/Gx&nbsp;(this&nbsp;is&nbsp;mostly&nbsp;a&nbsp;debugging&nbsp;option).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Optimize&nbsp;XC&nbsp;matrices&nbsp;update&nbsp;as&nbsp;much&nbsp;as&nbsp;possible.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/96)
`L1014`: Whether to compute transition dipole derivatives.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes&nbsp;(results&nbsp;in&nbsp;minor&nbsp;deviations&nbsp;from&nbsp;optimal&nbsp;IDoFFX).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/100)
`L1014`: Solution method for CPCIS/CPTD.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;same&nbsp;as&nbsp;IOp(10/8)&nbsp;except&nbsp;that&nbsp;separate&nbsp;is&nbsp;done&nbsp;if&nbsp;the&nbsp;convergence&nbsp;is&nbsp;less&nbsp;than&nbsp;the&nbsp;default&nbsp;of&nbsp;1.d-8.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CPHF&nbsp;for&nbsp;each&nbsp;variable&nbsp;in&nbsp;a&nbsp;separate&nbsp;call&nbsp;to&nbsp;LinEq1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Expand&nbsp;each&nbsp;variable&nbsp;in&nbsp;a&nbsp;separate&nbsp;expansion&nbsp;space.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Solve&nbsp;all&nbsp;equations&nbsp;together,&nbsp;possibly&nbsp;reverting&nbsp;to&nbsp;the&nbsp;old&nbsp;(one&nbsp;variable&nbsp;at&nbsp;a&nbsp;time)&nbsp;method&nbsp;in&nbsp;the&nbsp;secondary&nbsp;solution.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Invert&nbsp;the&nbsp;A&nbsp;matrix&nbsp;directly.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/101)
`L1014`: Solution method (no interchange).




### IOp(10/102)
Diagonal shift preconditioning in CPHF:


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Shift&nbsp;Ea-Ei&nbsp;up&nbsp;to&nbsp;a&nbsp;minimum&nbsp;given&nbsp;by&nbsp;IOp(103).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Shift&nbsp;all&nbsp;diagonals&nbsp;by&nbsp;the&nbsp;amount&nbsp;given&nbsp;by&nbsp;IOp(103).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1x).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Flip&nbsp;the&nbsp;sign&nbsp;of&nbsp;Y&nbsp;shifts.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;sign&nbsp;for&nbsp;X&nbsp;and&nbsp;Y.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/103)
Value/threshold for shift during CPHF:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(0.1&nbsp;Hartree).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N/1000&nbsp;Hartree.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/105)
Shift for predconditioning during CPCIS/CPTD.


* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;as&nbsp;0.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Shift&nbsp;Ea-Ei&nbsp;up&nbsp;to&nbsp;a&nbsp;minimum&nbsp;given&nbsp;by&nbsp;IOp(103).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Shift&nbsp;all&nbsp;diagonals&nbsp;by&nbsp;the&nbsp;amount&nbsp;given&nbsp;by&nbsp;IOp(103).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1x).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Flip&nbsp;the&nbsp;sign&nbsp;of&nbsp;Y&nbsp;shifts.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Same&nbsp;sign&nbsp;for&nbsp;X&nbsp;and&nbsp;Y.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/106)
Override of IRadAn for just L1014, taking precedence over IOp(60).




### IOp(10/107)
Override of IRadAn for just XC2E part of L1014, taking precedence over IOp(60) and IOp(107).




### IOp(10/108)
`L1014`: Stop at selected points for testing restarts.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(no&nbsp;stopping).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* BBBNNNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stop&nbsp;at&nbsp;restart&nbsp;point&nbsp;N,&nbsp;in&nbsp;batch&nbsp;BBB&nbsp;if&nbsp;applicable.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(10/109)
`L1014`: Max number of iterations, overriding IOp(73).




### IOp(10/109)
`L1014`: Max number of iterations, overriding IOp(73).




## Overlay 11 
### IOp(11/5)
IFWRT: derivative integral write option.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;produce&nbsp;a&nbsp;D2E&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Produce&nbsp;a&nbsp;D2E&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/6)
IFHFFX: Whether or not to contract integral derivatives with Hartree-Fock density matrix terms to produce Hartree-Fock two-electron contribution to the forces.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;also&nbsp;contracted&nbsp;electric&nbsp;field&nbsp;density&nbsp;matrix&nbsp;derivatives&nbsp;to&nbsp;form&nbsp;thetwo-electron&nbsp;integral&nbsp;derivative&nbsp;contribution&nbsp;to&nbsp;the&nbsp;pol.&nbsp;derivatives,&nbsp;but&nbsp;ignore&nbsp;frequency-dependent&nbsp;density&nbsp;derivs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;do&nbsp;polarizability&nbsp;derivatives&nbsp;using&nbsp;frequency-dependent&nbsp;density&nbsp;derivatives&nbsp;if&nbsp;the&nbsp;FD&nbsp;density&nbsp;derivatives&nbsp;are&nbsp;available.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/7)
IFTPDM: whether or not to contract integral derivatives with a ‘read-in’ two-particle density-matrix.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;but&nbsp;generate&nbsp;and&nbsp;write&nbsp;out&nbsp;the&nbsp;HF&nbsp;2PDM&nbsp;here&nbsp;for&nbsp;debugging&nbsp;purposes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;and&nbsp;use&nbsp;the&nbsp;2PDM&nbsp;for&nbsp;CIS&nbsp;state&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/8)
IFF1: whether or not to compute F1 over AO’s.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;then&nbsp;compress&nbsp;to&nbsp;active&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;active&nbsp;list.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/9)
IDOUT: First-derivative output option.Contains I2*100+I1*10+I0.


* I0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Whether&nbsp;or&nbsp;not&nbsp;to&nbsp;use&nbsp;the&nbsp;contents&nbsp;of&nbsp;IRWFX.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;if&nbsp;not&nbsp;there,&nbsp;merely&nbsp;set&nbsp;the&nbsp;array&nbsp;to&nbsp;zeroes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* I1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Processing&nbsp;of&nbsp;two-electron&nbsp;Hartree-Fock&nbsp;contributions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Take&nbsp;HF&nbsp;contributions&nbsp;from&nbsp;FX1&nbsp;(A&nbsp;LA&nbsp;IFHFFX).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Take&nbsp;HF&nbsp;contributions&nbsp;from&nbsp;F1&nbsp;(A&nbsp;LA&nbsp;IFF1).&nbsp;(forms&nbsp;the&nbsp;1/2(F-H)&nbsp;term&nbsp;in&nbsp;link&nbsp;1110).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Form&nbsp;1/2(F+H)&nbsp;term&nbsp;in&nbsp;link&nbsp;1110.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* I2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Processing&nbsp;of&nbsp;TPDM&nbsp;contributions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;None.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add&nbsp;in&nbsp;contents&nbsp;of&nbsp;FX2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/10)
`L1110`: Whether to compute Fock matrices, Lagrangian, and SCF energy.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;and&nbsp;in&nbsp;addition,&nbsp;compute&nbsp;other&nbsp;pieces&nbsp;necessary&nbsp;for&nbsp;second-order&nbsp;simultaneous&nbsp;optimization.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/11)
Control of integral derivative algorithm.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;use&nbsp;IsAlg&nbsp;to&nbsp;decide.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scalar&nbsp;Rys&nbsp;SPDF.&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Illegal&nbsp;here.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Illegal&nbsp;here.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Illegal&nbsp;here.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Illegal&nbsp;here.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Illegal&nbsp;here.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Illegal&nbsp;here.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Illegal&nbsp;here.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Illegal&nbsp;here.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Illegal&nbsp;here.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 12&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FoFJK:&nbsp;Prism&nbsp;spdf.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 13&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Illegal&nbsp;here.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/12)
`L1102, L1110`: Selection of 1PDM.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Usual&nbsp;SCF&nbsp;density.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;generalized&nbsp;density&nbsp;number&nbsp;N&nbsp;for&nbsp;both&nbsp;the&nbsp;one-electron&nbsp;integral&nbsp;derivatives&nbsp;and&nbsp;the&nbsp;corresponding&nbsp;2PDM&nbsp;terms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contract&nbsp;with&nbsp;HF&nbsp;density,&nbsp;CI&nbsp;density&nbsp;for&nbsp;state&nbsp;N,&nbsp;and&nbsp;CIS&nbsp;1PDM&nbsp;for&nbsp;state&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/13)
`L1112`: Flags.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;for&nbsp;IxÞSx&nbsp;(same&nbsp;as&nbsp;1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;Ix.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;L(x)&nbsp;and&nbsp;Ux*I.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Formation&nbsp;of&nbsp;Ux*I*T&nbsp;terms,&nbsp;default,&nbsp;same&nbsp;as&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N^4&nbsp;I/O&nbsp;algorithm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Old&nbsp;gOV3&nbsp;I/O&nbsp;algorithm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Formation&nbsp;of&nbsp;Fx*T*T&nbsp;terms:&nbsp;default&nbsp;is&nbsp;to&nbsp;choose&nbsp;based&nbsp;on&nbsp;available&nbsp;memory.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;O2V2&nbsp;method.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use(2g+O)V2&nbsp;memory&nbsp;algorithm&nbsp;even&nbsp;if&nbsp;O2V2&nbsp;memory&nbsp;is&nbsp;available.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 300&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;old&nbsp;N^5&nbsp;I/O&nbsp;algorithm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;Ix*T&nbsp;algorithm&nbsp;(1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;new&nbsp;algorithm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;old&nbsp;algorithm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;availability&nbsp;of&nbsp;MO&nbsp;basis&nbsp;Ix&nbsp;—&nbsp;use&nbsp;if&nbsp;avail.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ix&nbsp;file&nbsp;is&nbsp;not&nbsp;available&nbsp;(omit&nbsp;OO/VV&nbsp;blocks&nbsp;of&nbsp;Px,Wx).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ix&nbsp;file&nbsp;is&nbsp;available&nbsp;(i.e.&nbsp;do&nbsp;OO/VV&nbsp;blocks&nbsp;of&nbsp;Px,Wx).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 000000&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;non-zero&nbsp;Delta(ij+ab)&nbsp;processing:&nbsp;if&nbsp;Full&nbsp;and&nbsp;some&nbsp;Delta’s&nbsp;are&nbsp;non-zero.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;addition&nbsp;of&nbsp;these&nbsp;terms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200000&nbsp;&nbsp;&nbsp;&nbsp;Suppress&nbsp;addition&nbsp;of&nbsp;Delta&nbsp;terms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/14)
The nature of the perturbation(s).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1st&nbsp;order&nbsp;nuclear&nbsp;and&nbsp;electric&nbsp;field).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* IJK&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nuclear&nbsp;Kth&nbsp;order.&nbsp;Electric&nbsp;field&nbsp;Jth&nbsp;order.&nbsp;Magnetic&nbsp;field&nbsp;Ith&nbsp;order.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/15)
Controls output of derivatives to rw-files.


* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Load&nbsp;fxyz&nbsp;from&nbsp;rw-files&nbsp;if&nbsp;it&nbsp;exists.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculate&nbsp;nuclear&nbsp;contribution.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculate&nbsp;one-electroon&nbsp;contribution.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Output&nbsp;of&nbsp;‘old’&nbsp;format.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Forces&nbsp;out-of-core&nbsp;algorithm.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/16)
`L1102`: Mode of operation.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;compute&nbsp;dipole&nbsp;derivative&nbsp;matrices&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Also&nbsp;compute&nbsp;dipole&nbsp;derivative&nbsp;integral&nbsp;contribution&nbsp;to&nbsp;the&nbsp;HF&nbsp;dipole&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Also&nbsp;compute&nbsp;HF&nbsp;contribution&nbsp;to&nbsp;the&nbsp;dipole&nbsp;moment.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/17)
`L1111`: Frozen-core.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(use&nbsp;AO&nbsp;2PDM&nbsp;for&nbsp;Lagrangian&nbsp;only&nbsp;if&nbsp;orbitals&nbsp;are&nbsp;frozen&nbsp;in&nbsp;/Orb/).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;C1,&nbsp;C2,&nbsp;S1,&nbsp;and&nbsp;S2&nbsp;off&nbsp;the&nbsp;AO&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Convert&nbsp;/Orb/&nbsp;to&nbsp;full,&nbsp;for&nbsp;debugging&nbsp;frozen-core&nbsp;with&nbsp;integrals&nbsp;over&nbsp;the&nbsp;full&nbsp;window.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;as&nbsp;2,&nbsp;but&nbsp;leave&nbsp;the&nbsp;full&nbsp;version&nbsp;of&nbsp;/Orb/&nbsp;on&nbsp;the&nbsp;disk.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Form&nbsp;the&nbsp;derivative&nbsp;integral&nbsp;contribution&nbsp;to&nbsp;the&nbsp;Lagrangian&nbsp;as&nbsp;well.&nbsp;This&nbsp;is&nbsp;stored&nbsp;on&nbsp;disk&nbsp;as&nbsp;RL(NBasis,NBasis,NAt3,IOpCl+1)&nbsp;in&nbsp;RWF&nbsp;1001.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/18)
`L1111`: Save AO 2PDM?


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;the&nbsp;AO&nbsp;2PDM&nbsp;on&nbsp;RWF&nbsp;N.&nbsp;It&nbsp;is&nbsp;(NTT,NTT)&nbsp;and&nbsp;includes&nbsp;factors&nbsp;(2-Delta(ij))(2-Delta(kl)).&nbsp;It&nbsp;doesn’t&nbsp;include&nbsp;any&nbsp;normalization&nbsp;factor.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/19)
`L1112`: Whether to delete MO integrals after.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Yes).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/20)
`L1112`: How to handle 2e integral contributions.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;the&nbsp;2e&nbsp;integral&nbsp;files,&nbsp;MO&nbsp;if&nbsp;possible.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;the&nbsp;2e&nbsp;integrals&nbsp;when&nbsp;needed.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;use&nbsp;of&nbsp;AO&nbsp;integrals,&nbsp;even&nbsp;if&nbsp;MO&nbsp;ones&nbsp;are&nbsp;available.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* MNx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;option&nbsp;MN&nbsp;in&nbsp;control&nbsp;of&nbsp;2e&nbsp;integral&nbsp;calculation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/21)
Size of buffers for integral derivative file.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Machine&nbsp;dependent;&nbsp;see&nbsp;DSet2E).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N&nbsp;integer&nbsp;words.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/22)
`L1112`: In-core option for W(Tilde) term.


* -6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;in-core&nbsp;storage.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Suppress&nbsp;in-core&nbsp;storage.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;in-core&nbsp;if&nbsp;possible.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/23)
`L1112`: Use of Raffenetti integrals during direct term.


* -N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All&nbsp;integrals&nbsp;done&nbsp;as&nbsp;Raffenetti&nbsp;if&nbsp;there&nbsp;are&nbsp;N&nbsp;or&nbsp;more&nbsp;matrices;&nbsp;all&nbsp;as&nbsp;regular&nbsp;if&nbsp;there&nbsp;are&nbsp;less&nbsp;than&nbsp;N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;let&nbsp;FoFJK&nbsp;decide.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All&nbsp;integrals&nbsp;are&nbsp;done&nbsp;as&nbsp;regular&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Integrals&nbsp;with&nbsp;degree&nbsp;of&nbsp;contraction&nbsp;greater&nbsp;than&nbsp;or&nbsp;equal&nbsp;to&nbsp;N&nbsp;are&nbsp;done&nbsp;at&nbsp;regular&nbsp;integrals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/24)
`L1102`: Output.


* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(01).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contract&nbsp;with&nbsp;density&nbsp;matrix&nbsp;to&nbsp;form&nbsp;dipole&nbsp;derivative&nbsp;contributions.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store&nbsp;dipole&nbsp;derivative&nbsp;matrices&nbsp;on&nbsp;disk.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/26)
Program accuracy option.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;integrals&nbsp;economically&nbsp;to&nbsp;10^-10&nbsp;accuracy.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;‘Test’&nbsp;option&nbsp;bypass&nbsp;cutoffs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/27)
`L1110`: Integral retention parameter if writing d2e file.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Retain&nbsp;integrals&nbsp;GE&nbsp;10^-10&nbsp;in&nbsp;the&nbsp;D2E&nbsp;file&nbsp;(if&nbsp;selected)&nbsp;and/or&nbsp;10^-10&nbsp;in&nbsp;the&nbsp;integral&nbsp;heap&nbsp;if&nbsp;IFF1=1&nbsp;and&nbsp;MODE=2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Retain&nbsp;integrals&nbsp;GE&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


`L1111`: Save unsymmetrized S1 and S2.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/28)
`L1111`: Location or generation of MO 1 and 2 PDMs.


* -16&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;EOM-CCSD&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -15&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;Direct&nbsp;SAC-CI&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -14&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;SAC-CI&nbsp;General-R&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -13&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;SAC-CI&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -12&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;MP4SDQ&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -11&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;MP4DQ&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;MP3&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;BD&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;
* -8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;CCSD&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;QCISD&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;CCD&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;CIS&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;CISD&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;CID&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;MP2&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;HF&nbsp;DMs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(RWFs&nbsp;626,&nbsp;627,&nbsp;and&nbsp;628).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RWFS&nbsp;N&nbsp;(1PDM),&nbsp;N+1&nbsp;(W),&nbsp;and&nbsp;N+2&nbsp;(2PDM).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/29)
What to do:


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nothing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Transform&nbsp;1PDM&nbsp;and&nbsp;Lagrangian&nbsp;from&nbsp;MO&nbsp;to&nbsp;AO.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Transform&nbsp;2PDM&nbsp;from&nbsp;MO&nbsp;to&nbsp;AO.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sort&nbsp;AO&nbsp;2PDM&nbsp;into&nbsp;shell&nbsp;order.&nbsp;If&nbsp;back&nbsp;transformation&nbsp;has&nbsp;not&nbsp;been&nbsp;requested,&nbsp;the&nbsp;double-length&nbsp;AO&nbsp;2PDM&nbsp;is&nbsp;expected&nbsp;in&nbsp;file&nbsp;1001.&nbsp;The&nbsp;sorted&nbsp;2PDM&nbsp;is&nbsp;left&nbsp;in&nbsp;file&nbsp;602.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Form&nbsp;the&nbsp;contribution&nbsp;of&nbsp;the&nbsp;2PDM&nbsp;to&nbsp;the&nbsp;forces&nbsp;right&nbsp;here.&nbsp;Note&nbsp;that&nbsp;if&nbsp;the&nbsp;2PDM&nbsp;is&nbsp;also&nbsp;to&nbsp;be&nbsp;left&nbsp;behind,&nbsp;it&nbsp;will&nbsp;be&nbsp;over&nbsp;6d/10f&nbsp;and&nbsp;have&nbsp;the&nbsp;HGP&nbsp;d&nbsp;and&nbsp;f&nbsp;scale&nbsp;factors&nbsp;in&nbsp;it.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Suppress&nbsp;writing&nbsp;alpha,&nbsp;beta,&nbsp;and&nbsp;spin&nbsp;density&nbsp;RWFs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Form&nbsp;and&nbsp;sort&nbsp;the&nbsp;2PDM&nbsp;derivatives&nbsp;rather&nbsp;than&nbsp;the&nbsp;2PDM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;replicated&nbsp;2PDM&nbsp;copies&nbsp;for&nbsp;testing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/30)
What to compute using integrals or D2E file.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nothing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Energy.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gradient.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/31)
`L1110`: Whether to use symmetry in Rys integral derivatives.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;skip&nbsp;check&nbsp;of&nbsp;density&nbsp;symmetry&nbsp;in&nbsp;L1110.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/32)
`L1111`: Whether to do 2PDM or just Lagrangian.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;full&nbsp;gradient&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;full&nbsp;gradient&nbsp;(same&nbsp;as&nbsp;default).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;density&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;density&nbsp;and&nbsp;W&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;2PDM&nbsp;only,&nbsp;no&nbsp;density&nbsp;or&nbsp;W.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;non-separable&nbsp;terms&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Testing&nbsp;(no&nbsp;lag&nbsp;currently).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;T-relaxed&nbsp;MO-unrelaxed&nbsp;1PDM&nbsp;for&nbsp;(EOM-)CCSD&nbsp;(no&nbsp;need&nbsp;for&nbsp;2PDM.&nbsp;1PDM&nbsp;stored&nbsp;in&nbsp;IODens).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/33)
IPRINT print option.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;printing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;computed&nbsp;first-derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;F1&nbsp;matrices.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/39)
Compression of derivative matrices.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(2&nbsp;if&nbsp;expanded&nbsp;matrices,&nbsp;otherwise&nbsp;4&nbsp;or&nbsp;5).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;over&nbsp;active&nbsp;atoms&nbsp;only.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;over&nbsp;the&nbsp;full&nbsp;list&nbsp;of&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;over&nbsp;the&nbsp;full&nbsp;list&nbsp;of&nbsp;atoms,&nbsp;but&nbsp;blank&nbsp;contributions&nbsp;for&nbsp;inactive&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;over&nbsp;active&nbsp;atoms&nbsp;only,&nbsp;and&nbsp;store&nbsp;second&nbsp;deriv.&nbsp;contributions&nbsp;over&nbsp;only&nbsp;active&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Store&nbsp;only&nbsp;matrices&nbsp;for&nbsp;QM&nbsp;atoms,&nbsp;but&nbsp;include&nbsp;the&nbsp;contribution&nbsp;of&nbsp;EE&nbsp;centers&nbsp;in&nbsp;the&nbsp;matrices.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/42)
Compressed file formats.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;compressed.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;expanded&nbsp;form.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Force&nbsp;compressed&nbsp;form.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compressed&nbsp;Sx&nbsp;but&nbsp;separate&nbsp;H1&nbsp;and&nbsp;F1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/43)
Batching in overlay 11.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;smallest&nbsp;possible&nbsp;number&nbsp;of&nbsp;passes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;at&nbsp;least&nbsp;one&nbsp;pass,&nbsp;but&nbsp;using&nbsp;the&nbsp;out-of-core&nbsp;algorithms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;at&nbsp;least&nbsp;N&nbsp;passes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* For&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rys&nbsp;in&nbsp;L1110,&nbsp;N&nbsp;is&nbsp;0/1/2&nbsp;for&nbsp;default/in-core/out-of-core.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/45)
Force NAt3 instead of NAt3+3 storage of matrices (for debugging).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/46)
Whether to include orbital rotation gradient terms for SAC-CI.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Convert&nbsp;1PDM&nbsp;to&nbsp;canonical&nbsp;representation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;gradients&nbsp;to&nbsp;disk,&nbsp;needed&nbsp;for&nbsp;non-canonical&nbsp;methods.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/53)
Convert forces over shells to field-dependent dipole and forces over atoms (for debugging).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/60)
Override standard values of IRadAn.




### IOp(11/61)
Override standard values of IRanWt.




### IOp(11/62)
Override standard values of IRanGd.




### IOp(11/63)
Whether to do FMM.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;global&nbsp;default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn&nbsp;off&nbsp;FMM&nbsp;here&nbsp;regardless.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/75)
Print during NMR.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;tensors&nbsp;and&nbsp;eigenvalues.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print&nbsp;eigenvectors&nbsp;as&nbsp;well.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/76)
`L1102`: Force DoH1 logic for debugging.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/77)
Debugging option for DBF derivatives.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal&nbsp;processing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ignore&nbsp;fitting&nbsp;density&nbsp;and&nbsp;just&nbsp;process&nbsp;real&nbsp;density&nbsp;in&nbsp;L1110.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Skip&nbsp;increment&nbsp;of&nbsp;Fx&nbsp;with&nbsp;J(Z^-1*Jx(P-Pfit)).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compute&nbsp;only&nbsp;Pfit&nbsp;and&nbsp;not&nbsp;P&nbsp;terms&nbsp;involving&nbsp;2e&nbsp;integral&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Clear&nbsp;both&nbsp;Pfit&nbsp;and&nbsp;P&nbsp;before&nbsp;FoFJK.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;polarizability&nbsp;derivative&nbsp;contribution&nbsp;separately;&nbsp;only&nbsp;works&nbsp;with&nbsp;density&nbsp;fitting.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 11x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;polarizability&nbsp;derivatives&nbsp;for&nbsp;density&nbsp;fitting&nbsp;separately&nbsp;and&nbsp;keep&nbsp;only&nbsp;dbf-ao&nbsp;terms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 21x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;polarizability&nbsp;derivatives&nbsp;for&nbsp;density&nbsp;fitting&nbsp;separately&nbsp;and&nbsp;keep&nbsp;only&nbsp;dbf-dbf&nbsp;terms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 31x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;polarizability&nbsp;derivatives&nbsp;for&nbsp;density&nbsp;fitting&nbsp;separately&nbsp;via&nbsp;2PDM&nbsp;in&nbsp;one&nbsp;call&nbsp;to&nbsp;FoFCou.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/81)
Control of number of passes in GXX.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;at&nbsp;most&nbsp;96&nbsp;matrices&nbsp;at&nbsp;a&nbsp;time&nbsp;if&nbsp;doing&nbsp;FMM,&nbsp;otherwise&nbsp;no&nbsp;limit.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As&nbsp;few&nbsp;passes&nbsp;(as&nbsp;many&nbsp;matrices)&nbsp;as&nbsp;possible.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;at&nbsp;most&nbsp;N&nbsp;densities&nbsp;per&nbsp;pass.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N<-1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;at&nbsp;least&nbsp;-N&nbsp;passes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/87)
`L1110`: Accuracy of 2e integrals.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;10^-N.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/101)
Raffenetti in DD1Dir.




### IOp(11/102)
Control of FMM for nuclear repulsion.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default:&nbsp;Use&nbsp;for&nbsp;5K&nbsp;or&nbsp;more&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;for&nbsp;N&nbsp;or&nbsp;more&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Always&nbsp;use&nbsp;FMM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Never&nbsp;use&nbsp;FMM.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/103)
Flag for PTED with CCSD and BD.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Normal&nbsp;solvation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PTED.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PTE-S.&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PTES.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(11/126)
Maximum number of matrices to handle at a time in DD1Dir.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(-1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;limit.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;At&nbsp;most&nbsp;N&nbsp;matrices&nbsp;at&nbsp;a&nbsp;time.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




## Overlay 99 
### IOp(99/5)
Controls handling of the checkpoint file.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;run&nbsp;is&nbsp;an&nbsp;optimization&nbsp;or&nbsp;frequency&nbsp;run,&nbsp;so&nbsp;both&nbsp;the&nbsp;permanent&nbsp;and&nbsp;restart&nbsp;files&nbsp;are&nbsp;in&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;Delete&nbsp;the&nbsp;restart&nbsp;information&nbsp;if&nbsp;the&nbsp;run&nbsp;is&nbsp;finishing&nbsp;normally&nbsp;(I.E.&nbsp;if&nbsp;the&nbsp;error&nbsp;termination&nbsp;ILSW&nbsp;bit&nbsp;is&nbsp;not&nbsp;set).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;run&nbsp;is&nbsp;not&nbsp;an&nbsp;optimization.&nbsp;Save&nbsp;the&nbsp;permanent&nbsp;information&nbsp;(MOS,&nbsp;basis&nbsp;set&nbsp;info&nbsp;etc.)&nbsp;on&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;write&nbsp;anything&nbsp;to&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Archive&nbsp;data&nbsp;from&nbsp;the&nbsp;checkpoint&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Restart&nbsp;a&nbsp;multi-step&nbsp;job,&nbsp;recovering&nbsp;data&nbsp;from&nbsp;the&nbsp;checkpoint&nbsp;file&nbsp;and&nbsp;figuring&nbsp;out&nbsp;which&nbsp;job&nbsp;step&nbsp;to&nbsp;run&nbsp;next&nbsp;and&nbsp;whether&nbsp;it&nbsp;needs&nbsp;restart&nbsp;if&nbsp;an&nbsp;optimization&nbsp;or&nbsp;numerical&nbsp;frequency.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;data&nbsp;on&nbsp;the&nbsp;checkpoint&nbsp;file,&nbsp;but&nbsp;don’t&nbsp;remove&nbsp;extra&nbsp;data&nbsp;(i.e.,&nbsp;if&nbsp;a&nbsp;new&nbsp;version&nbsp;was&nbsp;not&nbsp;generated&nbsp;in&nbsp;this&nbsp;step).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 0x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Defaults&nbsp;to&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Remove&nbsp;Cartesian&nbsp;force&nbsp;constants&nbsp;from&nbsp;chk&nbsp;file&nbsp;if&nbsp;this&nbsp;is&nbsp;not&nbsp;a&nbsp;frequency&nbsp;job.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Leave&nbsp;Cartesian&nbsp;force&nbsp;constants&nbsp;on&nbsp;the&nbsp;chk&nbsp;file&nbsp;even&nbsp;if&nbsp;this&nbsp;is&nbsp;not&nbsp;a&nbsp;frequency&nbsp;job.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(99/6)
Controls output of data files for other programs.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;PolyAtom&nbsp;output.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PolyAtom&nbsp;output&nbsp;in&nbsp;working&nbsp;precision&nbsp;to&nbsp;Fortran&nbsp;unit&nbsp;8.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;GVB2P5&nbsp;trans&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GVB2P5&nbsp;trans&nbsp;file&nbsp;to&nbsp;unit&nbsp;14.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WFN&nbsp;file&nbsp;output.&nbsp;&nbsp;&nbsp;&nbsp;
* 200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WFNX&nbsp;file&nbsp;output.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;natural&nbsp;orbitals&nbsp;in&nbsp;WFN&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 10000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Regular&nbsp;WFN/WFNX&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 20000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WFN/WFNX&nbsp;file&nbsp;should&nbsp;include&nbsp;magnetic&nbsp;orbital&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 30000&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WFN/WFNX&nbsp;file&nbsp;should&nbsp;include&nbsp;GIAO&nbsp;magnetic&nbsp;orbital&nbsp;derivatives.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 100000&nbsp;&nbsp;&nbsp;&nbsp;Write&nbsp;generate&nbsp;matrix&nbsp;element&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(99/7)
Controls whether MOs are written to the polyatom integral tape in LANL style.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(99/8)
Reading temperature, pressure, and isotopes during multi-step energy calculations.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(same&nbsp;as&nbsp;1).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No,&nbsp;use&nbsp;defaults.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(99/9)
Controls archiving of dipole moment and other electric field
derivatives, except for archiving from the checkpoint file.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Archive&nbsp;all&nbsp;as&nbsp;is.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Archive&nbsp;all,&nbsp;but&nbsp;rotates&nbsp;to&nbsp;z-matrix&nbsp;orientation&nbsp;first.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Don’t&nbsp;archive.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(99/10)
Controls punching of assorted information (i.e., formatted output to unit 7).


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nothing.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Title.&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Atomic&nbsp;numbers&nbsp;and&nbsp;coordinates&nbsp;in&nbsp;format&nbsp;(I3,3D20.12).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Derivatives&nbsp;(forces&nbsp;and&nbsp;force&nbsp;constants)&nbsp;in&nbsp;format&nbsp;(2X,3D20.12).&nbsp;These&nbsp;are&nbsp;in&nbsp;the&nbsp;Z-matrix&nbsp;orientation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;archive&nbsp;entry.&nbsp;This&nbsp;is&nbsp;independent&nbsp;of&nbsp;normal&nbsp;archiving&nbsp;to&nbsp;the&nbsp;main&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 16&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;An&nbsp;input&nbsp;deck&nbsp;for&nbsp;HONDO.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 32&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;molecular&nbsp;orbitals,&nbsp;in&nbsp;format&nbsp;suitable&nbsp;for&nbsp;Guess=Cards,&nbsp;in&nbsp;the&nbsp;standard&nbsp;orientation.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 64&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A&nbsp;GAMESS&nbsp;input&nbsp;deck.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 128&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The&nbsp;natural&nbsp;orbitals&nbsp;generated&nbsp;by&nbsp;link&nbsp;601.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 256&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A&nbsp;WFN&nbsp;file&nbsp;for&nbsp;PROAIMS.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 512&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use&nbsp;natural&nbsp;orbitals&nbsp;in&nbsp;WFN&nbsp;file.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1024&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Output&nbsp;hyperfine&nbsp;tensors&nbsp;as&nbsp;input&nbsp;to&nbsp;Pickett’s&nbsp;program&nbsp;(sent&nbsp;to&nbsp;the&nbsp;output&nbsp;file).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2048&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read&nbsp;a&nbsp;list&nbsp;of&nbsp;atoms&nbsp;to&nbsp;use&nbsp;in&nbsp;the&nbsp;Pickett&nbsp;input.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(99/11)
Which type of database to update.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Old&nbsp;format.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;New&nbsp;format.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Both.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(99/12)
Flag for coordinate optimization.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes;&nbsp;remove&nbsp;/ZMat/&nbsp;and&nbsp;/ZSubst/&nbsp;from&nbsp;the&nbsp;RWF&nbsp;and&nbsp;checkpoint&nbsp;files.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(99/13)
Whether this is the end of the job step.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(Yes).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Go&nbsp;back&nbsp;to&nbsp;Link&nbsp;1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(99/14)
Whether to attempt to express the final optimized structure in terms of the input z-matrix.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes&nbsp;if&nbsp;there&nbsp;are&nbsp;20&nbsp;or&nbsp;fewer&nbsp;atoms.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yes,&nbsp;and&nbsp;update&nbsp;RWFs.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(99/15)
Act as though in multi-step job type IOp(15).




### IOp(99/16)
Treat the job as type (Info(7)) given by IOp(16).




### IOp(99/17)
Override multi-step job defaults.


* NNN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Treat&nbsp;as&nbsp;MSJDon&nbsp;=&nbsp;IOp(17)&nbsp;step&nbsp;in&nbsp;a&nbsp;multi-step&nbsp;job.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* Mxxx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MSJOpt&nbsp;M&nbsp;from&nbsp;L1.&nbsp;If&nbsp;M=2,&nbsp;do&nbsp;not&nbsp;abort&nbsp;if&nbsp;no&nbsp;force&nbsp;constants&nbsp;are&nbsp;found.&nbsp;If&nbsp;M≥2,&nbsp;skip&nbsp;any&nbsp;later&nbsp;optimization&nbsp;steps.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(99/18)
How many virtual orbitals to include in the WFN file.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(None).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* -1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Include&nbsp;all&nbsp;virtual&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Include&nbsp;N&nbsp;virtual&nbsp;orbitals.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(99/19)
Generation of archive entry.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default,&nbsp;generate&nbsp;archive&nbsp;entry&nbsp;unless&nbsp;the&nbsp;job&nbsp;is&nbsp;flagged&nbsp;for&nbsp;error&nbsp;termination&nbsp;or&nbsp;the&nbsp;job&nbsp;was&nbsp;marked&nbsp;by&nbsp;l1&nbsp;as&nbsp;not&nbsp;archivable.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate&nbsp;the&nbsp;entry&nbsp;ignoring&nbsp;the&nbsp;l1&nbsp;flag.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;generate&nbsp;the&nbsp;entry.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(99/20)
Saving atomic charges as MM charges.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(No).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* N&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save&nbsp;charge&nbsp;type&nbsp;N-1&nbsp;as&nbsp;MM&nbsp;charges.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(99/22)
Compress files.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Default&nbsp;(3).&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compress&nbsp;chk.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Compress&nbsp;all&nbsp;files.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Do&nbsp;not&nbsp;compress.&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(99/23)
MinPSp for compression.




### IOp(99/24)
MaxPCp for compression.




### IOp(99/33)
Controls debug print.


* 0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No&nbsp;debug&nbsp;print.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
* 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Debug&nbsp;print.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;




### IOp(99/125)
Options for matrix element file; see WrtUnF.




