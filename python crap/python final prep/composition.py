class email():
    def send_message(self,msg):
        print("the {} is being sent through email".format(msg))
class yahoo():
    def send_message(self,msg):
        print("the {} is being sent through yahoo".format(msg))

class message_provider():
    provider = email()
    def provider_services(self,provider):
        self.provider=provider
    def send_message(self,msg):
        self.provider.send_message(msg)
m = message_provider()
m.send_message("hello world")
m.provider_services(yahoo())
m.send_message("hello freind")