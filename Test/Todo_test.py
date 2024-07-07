import flet as ft

class Task(ft.Column):
    def __init__(self, task_name, task_delete):
        super().__init__()
        self.task_name = task_name
        self.task_delete = task_delete
        self.display_task = ft.Row( [ft.Text(value=self.task_name)],width=200)

        self.display = ft.Container(
            ft.Row(

                controls=[
                    ft.Checkbox(),
                    self.display_task,
                    ft.IconButton(
                        ft.icons.CREATE_OUTLINED,
                        on_click=None
                    ),
                    ft.IconButton(
                        ft.icons.DELETE_OUTLINE,
                        on_click=self.Delete_clicked
                    )
                ]
            ),
            border=ft.border.all(1,"white"),
            width=500,
            height=60,
            padding=ft.padding.only(left=100)

        )
        
        self.controls = self.display
    def Delete_clicked(self, e):
        self.task_delete(self)


class Todo(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="What to do ?")
        self.Tasks = ft.Column()
        self.controls = [
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.icons.ADD, on_click=self.add
                    )
                ]
            ),
            self.Tasks,
            #this is task list column
        ]
    def add(self, e):
        task = Task(self.new_task.value, self.Delete)
        self.Tasks.controls.append(task)
        self.update()
    def Delete(self, task):
        self.Tasks.controls.remove(task)
        self.update()

def main(page: ft.Page):

    
    page.update()
    app = Todo()
    page.add(ft.Container(
            ft.Column(
                [
                    app
                ]
            )
        )
    )
if __name__ == '__main__':
    ft.app(target=main)