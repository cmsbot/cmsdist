### RPM cms cmssw-patch CMSSW_7_0_9_patch3
Requires: cmssw-patch-tool-conf 

%define runGlimpse      yes
%define useCmsTC        yes
%define saveDeps        yes

#Set it to -cmsX added by cmsBuild (if any) to the base release
%define baserel_postfix %{nil}
## IMPORT cmssw-patch-build
## IMPORT scram-project-build
