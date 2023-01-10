from .vtk_pipeline import VtkPipeline


DEFAULT_COLOR_MAP = [
    [15, 0, 0, 0],
    [75, 0, 1, 0],
    [100, 1, 0, 0],
    [175, 0, 0, 1],
]

DEFAULT_OPACITY_MAP = [
    [0, 0, 0.7, 1],
    [70, 0.3, 0.2, 1],
    [190, 0.7, 0.5, 1],
    [255, 1, 0.5, 0],
]


def initialize(server, **kwargs):
    state, ctrl = server.state, server.controller
    state.trame__title = "Colormap Editor"
    state.colormap_points = DEFAULT_COLOR_MAP
    state.opacity_points = DEFAULT_OPACITY_MAP

    vtk_pipeline = VtkPipeline(kwargs['dataset_path'])
    state.histogram_data = vtk_pipeline.get_histogram_data(buckets=10)

    @state.change("colormap_points")
    def update_colors(colormap_points, **kwargs):
        vtk_pipeline.update_colors(colormap_points)
        ctrl.view_update()

    @state.change("opacity_points")
    def update_opacity(opacity_points, **kwargs):
        vtk_pipeline.update_opacity(opacity_points)
        ctrl.view_update()

    @ctrl.set("get_render_window")
    def get_render_window():
        return vtk_pipeline.render_window

    @ctrl.set("reset_colormap_points")
    def reset_colormap_points(self):
        self._server.state.colormap_points = DEFAULT_COLOR_MAP
