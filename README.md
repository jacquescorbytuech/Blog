# Static Site

A simple personal website and blog built using the Pelican static site generator.

## Deployment

Run the following commands to generate the site:

### Dev deployment

Used to generate local test versions of the site during development.

    pelican content

### Final deployment

Used to generate the final version of the site, ready to publish to a hosting service.

    pelican content -s publishconf.py




    venv/Scripts/activate
    cd site  