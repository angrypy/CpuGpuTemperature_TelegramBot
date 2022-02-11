import GPUtil


def getGpuTemperature():
    GPUs = GPUtil.getGPUs()
    gpu = GPUs[0]
    return gpu.temperature
