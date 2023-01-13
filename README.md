# Trame Widget: Colormap Editor
This widget can be used in a trame project by the following procedure:

Clone this repository to your machine.
In your trame environment, perform an installation of this widget:
```
pip install [path/to/this/repository]
```

Invoke the trame Engine and UI classes for this widget in your trame project.
```
from colormapper import engine as colormapper_engine
...
colormapper_engine.initialize(server, self.state, self.ctrl, self.vtk_pipeline)
```

```
from colormapper.widget import ColormapEditor
...
ColormapEditor(
    histogram_data=("histogram_data",),
    colors=("colormap_points",),
    opacities=("opacity_points",),
    update_colors="colormap_points = $event",
    update_opacities="opacity_points = $event",
)
```

Run the trame application (follow instructions for that project).


## Development
After making changes to the vue component for the widget, be sure to build it for trame to use the compiled code. You may need to reinstall with pip in your trame environment if you did not install with the editable (`-e`) option.

### Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```
