from pipeline.steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps
    
    def run(self, inputs):
        data = None # First step of pipeline
        for step in self.steps:
            try:
                data = step.process(data, inputs) # Output after each step
            except StepException as e:
                print('Exception happened:', e)
                break