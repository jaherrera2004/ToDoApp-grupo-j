# task_model.py
class TaskModel:
    def __init__(self, task_name):
        self.task_name = task_name
<<<<<<< HEAD
        self.is_completed = False
=======
        self.is_done = False
>>>>>>> juan-tuiran

    def get_task_name(self):
        return self.task_name

<<<<<<< HEAD
    def mark_as_complete(self):
        self.is_completed = True

    def is_completed(self):
        return self.is_completed
    def delete_task(self):
        self.task_name = None
        self.is_completed = False

    def is_completed(self):
        return self.is_completed

=======
    def set_done(self):
        self.is_done = True

    def remove_task(self):
        self.task_name = None
        self.is_done = False

    def is_done(self):
        return self.is_done
>>>>>>> juan-tuiran
