from flet import *
from classifier import Classifier

model = Classifier()


def DetectionCard(path: str, class_name: str, confidence_score: float):
    label = f"{class_name} ({(confidence_score * 100).round(2)}%)".replace("\n", "")

    return Card(
        content=Column(
            controls=[
                Image(
                    expand=True,
                    src=path,
                    fit=ImageFit.FILL,
                ),
                Container(
                    content=Text(label),
                    padding=padding.all(8),
                ),
            ],
        ),
    )


def main(page: Page):
    ################################################################################
    # 1. Setting up the page layout
    ################################################################################
    page.title = "Flet counter example"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.scroll = ScrollMode.AUTO
    page.appbar = AppBar(
        title=Text("Image Classifier (Eric FP Prototype)"),
    )

    images_grid = GridView(
        controls=[],
        max_extent=500,
        spacing=8,
        run_spacing=8,
    )
    page.add(images_grid)

    ################################################################################
    # 2. Setting up the file picker result event handler
    ################################################################################
    def on_pick_result(e: FilePickerResultEvent):
        # If no files are selected, return
        if e.files == None or len(e.files) == 0:
            return

        # Get the first file
        for f in e.files:
            class_name, confidence = model.inference(f.path)
            card = DetectionCard(f.path, class_name, confidence)
            images_grid.controls.append(card)

        page.update()

    ################################################################################
    # 3. Setting up the file picker which will be triggered by the floating action button
    ################################################################################
    file_picker = FilePicker(on_result=on_pick_result)
    page.overlay.append(file_picker)

    def pick_file(e):
        file_picker.pick_files(
            allow_multiple=True,
            file_type=FilePickerFileType.IMAGE,
        )

    page.floating_action_button = FloatingActionButton(
        icon=icons.UPLOAD_FILE_OUTLINED,
        on_click=pick_file,
    )

    page.update()


app(main)
