import gradio as gr
from src import Opener
import cv2
import pyvirtualcam
import threading


def get_camera_list():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append((index, cap.getBackendName()))
        cap.release()
        index += 1
    return arr

def open_all_urls(task_list):
    for task in task_list:
        print(f"Abrir URL: {task['URL']} - {task['id']}")
        opener.open_conference(task['URL'], task['id'])
    return task_list

def run_virtual_cam(camera_dropdown):
    global stop_threads
    cap = cv2.VideoCapture(int(camera_dropdown[0][0]))
    frame_width =1920
    frame_height = 1080
    fps = 30
    
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    
    # Verifica si la cámara se abrió correctamente
    if not cap.isOpened():
        print("Error: No se puede abrir la cámara")
        return


    with pyvirtualcam.Camera(width=frame_width, height=frame_height, fps=fps) as cam:
        print(f'Using virtual camera: {cam.device}')
        
        while True:
            if stop_threads:
                break
            ret, frame = cap.read()
            if not ret:
                print("Error: No se puede recibir el frame (stream end?). Exiting ...")
                break

            # Convierte el frame de BGR a RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Envía el frame a la cámara virtual
            cam.send(frame_rgb)
            cam.sleep_until_next_frame()

    # Libera la cámara
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":

    stop_threads = False
    camera_list = get_camera_list()

    opener = Opener()

    with gr.Blocks() as demo:
        count = 0 
        tasks = gr.State([])
        new_task = gr.Textbox(label="Nueva URL", autofocus=True)
        camera_dropdown = gr.Dropdown(choices=[f"{index} - {name}" for index, name in camera_list], label="Select Camera",interactive=True)

        def add_task(tasks, new_task_name):
            global count
            count += 1
            return tasks + [{"URL": new_task_name,"id":count}], ""

        new_task.submit(add_task, [tasks, new_task], [tasks, new_task])

        @gr.render(inputs=tasks)
        def render_todos(task_list):
            gr.Markdown(f"URLS")
            for  task in task_list:
                with gr.Row():
                    gr.Textbox(f'{task["URL"]} - {task["id"]}', show_label=False, container=False)
                    done_btn = gr.Button("Abrir", scale=0)
                    def open(task=task):                    
                        print(f"Abrir URL: {task['URL']} - {task['id']}")
                        opener.open_conference(task['URL'], task['id'])
                        return task_list
                    
                    done_btn.click(open, None, [tasks])

                    delete_btn = gr.Button("Eliminar", scale=0, variant="stop")
                    def delete(task=task):
                        task_list.remove(task)
                        return task_list
                    delete_btn.click(delete, None, [tasks])

        open_all_btn = gr.Button("Abrir todas las URL")
        
        open_all_btn.click(open_all_urls, [tasks], [tasks])
        
        star_virtual_cam = gr.Button("Iniciar Cámara Virtual")
        
        virtual_cam_thread = None

        def start_virtual_cam(camera_dropdown):
            global virtual_cam_thread
            global stop_threads
            
            print(f"Starting virtual camera with camera: {camera_dropdown}")

            # Si ya hay un hilo en ejecución, lo detenemos
            if virtual_cam_thread is not None and virtual_cam_thread.is_alive():
                stop_threads = True
                virtual_cam_thread.join()
                stop_threads = False

            # Iniciamos un nuevo hilo
            virtual_cam_thread = threading.Thread(target=run_virtual_cam, args=(camera_dropdown,))
            virtual_cam_thread.start()
            
        star_virtual_cam.click(start_virtual_cam, [camera_dropdown], [camera_dropdown])
        
    demo.launch()

