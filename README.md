# timepix-matrix: Python scripts for altering Timepix bpc files

Alters the mode in 256x256 byte matrix of binary pixel configuration file of a Timepix detector, in order to set individual pixels to specific mode.

Assuming the mode in the input file is 0 (Medipix),
this modifies first two bits of the elements of the matrix to either 01 (ToT mode) or 11 (Timepix)
You'll likely need to modify the shift array to suit your application.

Syntax: $0 <source >output

Source: BPC file saved from Pixet Pro - with Medipix mode set for all pixels and threshold values specific for the particular detector.

Authors: 
Vaclav Stepan, stepan@ujf.cas.cz, 
Marek Sommer, sommer@ujf.cas.cz, 
Ondrej Ploc, ploc@ujf.cas.cz

