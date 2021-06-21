class PipelineStep:
    def __init__(self):
       pass

    def run(self):
        pass

class Pipeline(PipelineStep):
    self.pipelines = []
    
    def __init__(self, parallel = False):
        self.parallel = parallel

    def add(self, pipeline):
        self.pipelines.append(pipeline)

    def run(self):
        for pipeline in self.pipelines:
            pipeline.run()
