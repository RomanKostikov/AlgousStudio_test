import bpy
import requests
import os
from datetime import datetime


class SaveAndSendOperator(bpy.types.Operator):
    """Сохранить сцену и отправить POST-запрос"""
    bl_idname = "object.save_and_send"
    bl_label = "Save Scene and Send Data"

    def execute(self, context):
        try:
            # Проверка: если сцена не была сохранена, сохранить как новый файл
            if not bpy.data.is_saved:
                new_filepath = f"C:/Users/Roman/Desktop/scene_{datetime.now().strftime('%Y%m%d_%H%M%S')}.blend"
                bpy.ops.wm.save_as_mainfile(filepath=new_filepath)
                print(f"Сцена сохранена в новый файл: {new_filepath}")
            else:
                # Перезапись текущей сцены
                bpy.ops.wm.save_mainfile()
                print("Сцена успешно перезаписана.")

            # Сбор информации для отправки
            username = os.getlogin()
            save_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            filepath = bpy.data.filepath

            # Параметры POST-запроса
            url = "http://127.0.0.1:8000/api/save_scene/"
            data = {
                "username": username,
                "save_time": save_time,
                "filepath": filepath
            }

            # Отправка POST-запроса на сервер
            response = requests.post(url, data=data)
            if response.status_code == 201:
                print("POST-запрос успешно отправлен!")
                self.report({'INFO'}, "Сцена сохранена и данные отправлены!")
            else:
                print(f"Ошибка при отправке: {response.status_code} - {response.text}")
                self.report({'ERROR'}, "Ошибка при отправке данных.")
        except Exception as e:
            print(f"Ошибка при выполнении: {e}")
            self.report({'ERROR'}, f"Ошибка: {str(e)}")

        return {'FINISHED'}


# Функция добавления кнопки в меню Mesh -> Add
def menu_func(self, context):
    self.layout.operator(SaveAndSendOperator.bl_idname)


# Регистрация оператора и добавление в меню
def register():
    # Удаляем все предыдущие регистрации оператора и кнопки
    unregister()
    bpy.utils.register_class(SaveAndSendOperator)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)
    print("Оператор и кнопка зарегистрированы.")


# Удаление оператора и кнопки из меню
def unregister():
    try:
        bpy.utils.unregister_class(SaveAndSendOperator)
        print("Оператор удален.")
    except RuntimeError as e:
        print(f"Ошибка при удалении оператора: {e}")

    try:
        bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)
        print("Кнопка удалена.")
    except ValueError:
        print("Кнопка уже была удалена.")


# Запуск скрипта
if __name__ == "__main__":
    register()
