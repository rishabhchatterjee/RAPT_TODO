|Project|Lit Review|Methods|Analysis|Final Report|
|:------|:--------:|:-----:|:------:|:-----------|
|[Confidence in Virtual Agents](#)                         |/| | | |
|[Human-Agent Rapport Building](#)                         |/| | | |
|[User Modeling and Memory](#)                             |/| | | |
|[Virtual Agent Dialogue Authoring](#)                     |/| | | |

# Tests to Run for HPCA18

## Priority 1
- Idle Consumption 
  - Active Standby: 
    
    > Not exactly possible because of the periodic reads in the maintenance. We can still disable them in Verilog by sacrificing the correctness. 
    
  - N banks are active
    
    > We need to define the bank combinations. 
    


- Write Consumption
  - ACT-WR-PRE

  - ACT-WR-WR-PRE

  - ACT-WR...WR-PRE (write an entire row)

  - ACT-WR...WR-PRE (write as much as you can) --> IDD4W

    > 0,1,2 WRs for fixed time tRAS
  
    > 0,2,4,8,16 WRs for fixed time T
  
    > Measure IDD4W 
     
     * Use only 3 patterns 0x00, 0x33, 0xFF
     
     * 1,8 Banks Prıo1 2 and 4 Prio 2 IDD4W and IDD4R
     
  
- Data Dependency
  - Varying percentages of 1s 

  - Toggling bits

- Structural Variation
  - Current consumption of different rows 
  - Current consumption of different cols
  - Current consumption of different banks
  - ~~Current consumption of different ranks~~

    > Current set of DIMMs has only single-rank ones.

## Priority 2
- Impact of Bank Interleaving
- Impact of Memory Scheduling

## Priority 3
- Frequency Sweeps
  - Reads :
    - Back-to-back RDs (every 4 cycles)
    - RD every 8 cycles
    - RD every 16 cycles
    - RD every 32 cycles
  - Writes :
    - Back-to-back WRs (every 4 cycles)
    - WR every 8 cycles
    - WR every 16 cycles
    - WR every 32 cycles

- Column Access Effect: After N rd/wr (each consecutive command accesses to another col) N:0->764
    
    > We have the results of reading/writing a whole row only.

## Priority 4
- Impact of Refresh Rate
  - Activation current vs Retention Time

## Priority 5
- Impact of VDD and VDD/2
