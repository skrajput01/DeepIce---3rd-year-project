# DeepIce---3rd-year-project
A Deep Neural Network investigation into the Quasi-Liquid Layer

Software Used:
    - LAMMPS - downloaded from: https://www.lammps.org/ (Version: LAMMPS-64bit-20Sep2021) - used to simulate Molecular Dynamics
    - VMD - downloaded from: https://www.ks.uiuc.edu/Research/vmd/ (Version: vmd194a53win64 (1.9.4 - windows 64bit)) - used to visualise atoms in different structures of ice
    - DeepIce - https://github.com/mfulford/DeepIce/blob/master/DeepIce.py - used to train the Deep Neural Network to identify and predict phases
    - Sub networks for DeepIce: https://github.com/mfulford/DeepIce
    - Python (Version: 3.7.11)
    - TensorFlow - Python package (Version: 1.1.15)
    - Keras - Python Package (Version: 2.2.4)

Additional File: 
    https://emckclac-my.sharepoint.com/:f:/g/personal/stra8927_kcl_ac_uk/EjhArtRL-gdPnLS7GpnNa_AB5-UxhKl0kbIwVZ9KjAQBCA?e=Wh9KD8 

Instructions: 


Contributions:

    Bernardo Atolin:
        - LAMMPS simulations (250K Hexagonal and Cubic Ice, 260K Hexagonal Ice, Cubic Ice and Supercooled Water)
        - Radial Pair Distribution Functions
        - DeepIce Predictions
        - Water Number and QLL Thickness graphs using self-generated data
        - Poster and Powerpoint Presentation writing and editing
        
    Sam Male:
        - LAMMPS simulations (250K Cubic Ice, 260K Cubic Ice)
        - DeepIce Training (Cubic Ice at batch size 10 and batch size 30)
        - Poster and Powerpoint Presentation writing and editing
        
    Arnav Avad:
        - LAMMPS Simulations (250K Hexagonal and Cubic Ice, 260K HexagonalIce, Cubic Ice and Supercooled Water)
        - VMD Diffusion Coefficients and Radial Pair Distribution Functions
        - DeepIce Training and Prediciting for all slabs
        - Epoch time, Accuracy and Loss data for different training data sets (batch size 10 and batch size 30)
        - Mismatched training data (trained for hexagonal ice and predicted on cubic ice)
        - VMD Visuals for all slabs
        - Poster and Powerpoint Presentation writing and editing
        
    Shyam Kumar Rajput:
        - VMD visuals (and colouring) for all slabs and reference structures (poster & oral)
        - Slab videos showing variation of QLL for each structure at different temperatures (supplimentary videos for poster & oral)
        - Evolution of crystallisation of a system (LAMMPS simulation for Ice nucleation)
        - Hexagonal Ice at 260K - LAMMPS
        - DeepIce Training at 16 & 13nn.
        - Coloured Slab videos for crystallisation (Poster, Presentation)
        - Colour scheme for temperatures, and structures of ice (poster & oral)
        - Graph plotting and formatting with Python for no. of water molecules, QLL thickness and Crystallisation evolution (presentation & oral)
        - Poster design & layout (poster)
