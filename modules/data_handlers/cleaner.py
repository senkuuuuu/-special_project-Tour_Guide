import os
import gc


class clean:
    def terminate_tasks(self, asyncio_task_list):
        try:
            for task in asyncio_task_list:
                task.cancel()
            print('tasks been deleted')
        except:
            pass

    def terminate_temp(self):
        try:
            os.remove('temp_input.wav')
            os.remove('temp_output.mp3')
            print('temp files has been deleted')
        except:
            pass
    
    def terminate_lingering_obj(self, obj_type):
        
        garbage_objects = [obj for obj in gc.get_objects() if isinstance(obj, obj_type)]
        for obj in garbage_objects:
            print('terminating:',f'{obj} in class {obj_type}' )
            del obj
        gc.collect()
        print('terminated')