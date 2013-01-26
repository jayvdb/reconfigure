from reconfigure.nodes import Node, PropertyNode
from reconfigure.items.bound import BoundData


class CrontabData(BoundData):
    """Data class for crontab configs"""
    pass


#class CrontabLineData(BoundData):
#    line_type = "comment"
#    fields = ['device', 'mountpoint', 'type', 'options', 'freq', 'passno']
#
#    def template(self):
#        return Node('line', children=[
#            Node('token', children=[PropertyNode('value', 'none')]),
#            Node('token', children=[PropertyNode('value', 'none')]),
#            Node('token', children=[PropertyNode('value', 'auto')]),
#            Node('token', children=[PropertyNode('value', 'none')]),
#            Node('token', children=[PropertyNode('value', '0')]),
#            Node('token', children=[PropertyNode('value', '0')]),
#            ])

class CrontabNormalTaskData(BoundData):
    fields = ['minute', 'hour', 'day_of_month', 'month', 'day_of_week', 'command', 'comment']

    def template(self, **kwargs):
        return Node('normal_task', children=[
            PropertyNode('minute', '0'),
            PropertyNode('hour', '0'),
            PropertyNode('day_of_month', '1'),
            PropertyNode('month', '1'),
            PropertyNode('day_of_week', '1'),
            PropertyNode('command', '')
        ])

class CrontabSpecialTaskData(BoundData):
    fields = ['special', 'command']

    def template(self, **kwargs):
        return Node('special_task', children=[
            PropertyNode('special', '@reboot'),
            PropertyNode('command', '')
        ])

class CrontabEnvSettingData(BoundData):
    fields = ['name', 'value']

    def template(self, **kwargs):
        return Node('env_setting', children=[
            PropertyNode('name', 'ENV_NAME'),
            PropertyNode('value', 'ENV_VALUE')
        ])


def bind_for_fields(bound_data_class):
    for field in bound_data_class.fields:
        bound_data_class.bind_property(field, field)

CrontabData.bind_collection('normal_tasks', selector=lambda x: x.name == 'normal_task', item_class=CrontabNormalTaskData)
bind_for_fields(CrontabNormalTaskData)
CrontabNormalTaskData.bind_attribute('comment', 'comment')
CrontabData.bind_collection('env_settings', selector=lambda x: x.name == 'env_setting', item_class=CrontabEnvSettingData)
bind_for_fields(CrontabEnvSettingData)
CrontabEnvSettingData.bind_attribute('comment', 'comment')
CrontabData.bind_collection('special_tasks', selector=lambda x: x.name == 'special_task', item_class=CrontabSpecialTaskData)
bind_for_fields(CrontabSpecialTaskData)
CrontabSpecialTaskData.bind_attribute('comment', 'comment')
