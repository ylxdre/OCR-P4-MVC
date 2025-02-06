## Refactored

All models are in `models/models.py`  
Sequence can be seen in `controllers/base.py` in the `Controller.run()` method

for testing purpose, the players_list is created when controller is instantiated

To test, execute the controllers/base.py
- first menu is called from view
- the method to create player just returns the object (doesn't write anything)
- 1 -> creates a new tournament then run it 
