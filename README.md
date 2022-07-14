
## Source Code for our Bandhompage

### Goals

* use fastapi for speed (serve webpages on lowend hardware)
* use markdown for creating the content
* use yaml to configure menus


### Roadmap 
| Milestone                                                                                                         | Date                  |
| :-:                                                                                                               | :-:                   |
| change from yaml to toml configuration format for python-3.11 to take advantage of tomllib from the python stdlib | October/November 2022 |
| major refactoring of css code                                                                                     | -                     |
| deploy proper unittests for next major refactoring of the python code                                             | -                     |
   
#### Quickfixes
  - set /home to root
  - set "fastapi is running" response to /test


### Good to know:
  - uses *.py ending for yaml and markdown files so that uvicorn picks up the changes without restarting
