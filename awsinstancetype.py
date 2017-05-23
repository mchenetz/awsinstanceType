import requests
from bs4 import BeautifulSoup
import json
import os


class AWSInstanceType:
    def __init__(self, instancetype=None):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'instance.json'),'r') as r:
            rd = json.load(r)
            instances = rd
            r.close()
        self.instances = instances
        if instancetype != None:
            self.instanceType = self.getInstanceDesc(instancetype)

    @staticmethod
    def downloadInstanceTypes():
        totalRecords = {}
        request = requests.get('https://aws.amazon.com/ec2/instance-types/')
        soup = BeautifulSoup(request.content, 'html.parser')
        instances = soup.find(id='instance-type-matrix').find_next(class_='aws-table').table.tr.find_next_siblings('tr')
        for inst in instances:
            td = inst.find_all('td')
            instanceRecord = {
                'Instance Type': td[0].get_text(),
                'vCPU': td[1].get_text(),
                'Memory (GiB)': td[2].get_text(),
                'Storage (GB)': td[3].get_text(),
                'Networking Performance': td[4].get_text(),
                'Physical Processor': td[5].get_text(),
                'Clock Speed (GHz)': td[6].get_text(),
                'Intel AVX†': td[7].get_text(),
                'Intel AVX2†': td[8].get_text(),
                'Intel Turbo': td[9].get_text(),
                'EBS OPT': td[10].get_text(),
                'Enhanced Networking': td[11].get_text()
            }
            totalRecords.update({ td[0].get_text(): instanceRecord })
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'instance.json'), 'w') as w:
            js = json.dumps(totalRecords)
            w.write(js)
            w.close()
            print('Wrote Instance File!')

    def getInstanceDesc(self, instance):
        return self.instances[instance]

    def getInstanceVCPU(self):
        return self.instanceType['vCPU']
    def getInstanceMemory(self):
        return self.instanceType['Memory (GiB)']
    def getInstanceStorage(self):
        return self.instanceType['Storage (GB)']
    def getInstanceNetworkPerformance(self):
        return self.instanceType['Networking Performance']
    def getInstancePhysicalProcessor(self):
        return self.instanceType['Physical Processor']
    def getInstanceClockSpeed(self):
        return self.instanceType['Clock Speed (GHz)']
    def getInstanceIntelAVX(self):
        return self.instanceType['Intel AVX†']
    def getInstanceIntelAVX2(self):
        return self.instanceType['Intel AVX2t']
    def getInstanceIntelTurbo(self):
        return self.instanceType['Intel Turbo']
    def getInstanceEBSOPT(self):
        return self.instanceType['EBS OPT']
    def getInstanceEnhancedNetworking(self):
        return self.instanceType['Enhanced Networking†']

if __name__=='__main__':
    x1x3large = AWSInstanceType('x1.32xlarge')
    print(x1x3large.getInstanceVCPU())
    print(x1x3large.getInstanceMemory())
