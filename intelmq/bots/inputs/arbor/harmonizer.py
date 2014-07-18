import sys
from intelmq.lib.bot import Bot
from intelmq.lib.event import Event

class ArborHarmonizerBot(Bot):

    def process(self):
        event = self.receive_message()

        if event:
            event.add('feed', 'arbor')
            event.add('feed_url', 'http://atlas-public.ec2.arbor.net/public/ssh_attackers')
            ip_value = event.value('ip')
            event.add('source_ip', ip_value)
            event.add('reported_ip', ip_value)
            event.add('type', 'brute-force')
            
            self.send_message(event)
        self.acknowledge_message()


if __name__ == "__main__":
    bot = ArborHarmonizerBot(sys.argv[1])
    bot.start()

