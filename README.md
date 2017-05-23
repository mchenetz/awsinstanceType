# AWSInstanceType
## API to grab Instance Information
---
Description: This API will allow you to pull information on an instancetype by name. This script scrapes AWS EC2 Instancetypes from https://aws.amazon.com/ec2/instance-types/

Example:

```
x1x3large = AWSInstanceType('x1.32xlarge')
    print(x1x3large.getInstanceVCPU())
    print(x1x3large.getInstanceMemory())
```

The previous code gets vCPU and memory from the InstanceType ID 'x1.32xlarge'

Information that can be provided by this API is as follows:

```
"vCPU": 128,
"Memory (GiB)": "1,952",
"Storage (GB)": "2 x 1,920 SSD",
"Networking Performance": "20 Gigabit",
"Physical Processor": "Intel Xeon E7-8880 v3",
"Clock Speed (GHz)": "2.3",
"Intel AVX†": "Yes",
"Intel AVX2t": "Yes",
"Intel Turbo": "Yes",
"EBS OPT": "Yes",
"Enhanced Networking†": "Yes"
```

The following methods are available:

```
    def getInstanceVCPU(self):
 
    def getInstanceMemory(self):

    def getInstanceStorage(self):

    def getInstanceNetworkPerformance(self):

    def getInstancePhysicalProcessor(self):

    def getInstanceClockSpeed(self):

    def getInstanceIntelAVX(self):

    def getInstanceIntelAVX2(self):

    def getInstanceIntelTurbo(self):

    def getInstanceEBSOPT(self):

    def getInstanceEnhancedNetworking(self):

```