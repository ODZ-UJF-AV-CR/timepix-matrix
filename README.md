# timepix-matrix: Python scripts for altering Timepix bpc files

## In short:
Alters the mode in 256x256 byte matrix of binary pixel configuration file of a Timepix detector, in order to set individual pixels to specific mode.

## Description:
Assuming the mode in the input file is 0 (Medipix),
this modifies first two bits of the elements of the matrix to either 01 (ToT mode) or 11 (Timepix)
You'll likely need to modify the shift array to suit your application.

Byte for each value describes:

| bits  | contents |
| --- | --- |
| 2 bits | bit mode (Medipix, ToT, 1 hit, Timepix) |
| 4 bits | threshold value (0..15) |
| 1 bit | test bit |
| 1 bit | is the pixel masked |

## Syntax: 
```
$0 <source >output
```
### Source: 
BPC file saved from Pixet Pro - with Medipix mode set for all pixels and threshold values specific for the particular detector.

### Stdout: 
256x256 bytes bytes matrix, with Mode fields shifted.

### Stderr: 
Text sample of the matrix before and after shifting the values.

## Authors: 
Vaclav Stepan, stepan@ujf.cas.cz, 
Marek Sommer, sommer@ujf.cas.cz, 
Ondrej Ploc, ploc@ujf.cas.cz

