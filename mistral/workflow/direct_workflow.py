# Copyright 2014 - Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from mistral.workflow import base


class DirectWorkflowHandler(base.WorkflowHandler):

    @classmethod
    def start_workflow(cls, workflow_spec, execution, **params):
        # TODO(rakhmerov): Implement.
        raise NotImplementedError

    def on_task_result(cls, workflow_spec, execution, task_db, raw_result):
        # TODO(rakhmerov): Implement.
        raise NotImplementedError