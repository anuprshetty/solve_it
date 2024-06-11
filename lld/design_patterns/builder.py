# Builder pattern belongs to creational patterns.

# Builder:
# - Builder pattern lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.
# - Usage:
# -- when too many constructor parameters.
# -- when building individual attributes of the object to be created at different places in the code.
# -- to get rid of a “telescoping constructor” (A telescoping constructor in object-oriented programming refers to a pattern where a class has multiple constructors, each with an increasing number of parameters). [NOTE: Python doesn't support multiple constructors]

import json


class CloudService:
    def __init__(self, builder):
        self._service_type = builder.service_type
        self._contract_duration = builder.contract_duration
        self._default_tools = builder.default_tools
        self._hello_world_app = builder.hello_world_app
        self._script_deployment = builder.script_deployment
        self._orchestrated_deployment = builder.orchestrated_deployment
        self._analytics = builder.analytics
        self._error_tracking = builder.error_tracking
        self._performance_monitoring = builder.performance_monitoring

    @classmethod
    def builder(cls):
        return CloudServiceBuilder()

    def __str__(self):
        return f"{json.dumps(self.__dict__, indent=4)}"


class CloudServiceBuilder:
    def __init__(self):
        self._service_type = ""
        self._contract_duration = 0  # in years
        self._default_tools = ["service_dashboard", "help_center"]
        self._hello_world_app = False  # default app
        self._script_deployment = (
            False  # enables script (shell, python, etc) based deployment
        )
        self._orchestrated_deployment = False  # enables docker, docker compose, kubernetes manifests and helm charts based deployment
        self._analytics = False  # analytics service for app
        self._error_tracking = False  # error tracking service for app
        self._performance_monitoring = False  # performance monitoring service for infra

    def build(self):
        return CloudService(self)

    @property
    def service_type(self):
        return self._service_type

    def set_service_type(self, service_type):
        self._service_type = service_type
        return self

    @property
    def contract_duration(self):
        return self._contract_duration

    def set_contract_duration(self, contract_duration):
        self._contract_duration = contract_duration
        return self

    @property
    def default_tools(self):
        return self._default_tools

    @property
    def hello_world_app(self):
        return self._hello_world_app

    def set_hello_world_app(self, enabled):
        self._hello_world_app = enabled
        return self

    @property
    def script_deployment(self):
        return self._script_deployment

    def set_script_deployment(self, enabled):
        self._script_deployment = enabled
        return self

    @property
    def orchestrated_deployment(self):
        return self._orchestrated_deployment

    def set_orchestrated_deployment(self, enabled):
        self._orchestrated_deployment = enabled
        return self

    @property
    def analytics(self):
        return self._analytics

    def set_analytics(self, enabled):
        self._analytics = enabled
        return self

    @property
    def error_tracking(self):
        return self._error_tracking

    def set_error_tracking(self, enabled):
        self._error_tracking = enabled
        return self

    @property
    def performance_monitoring(self):
        return self._performance_monitoring

    def set_performance_monitoring(self, enabled):
        self._performance_monitoring = enabled
        return self


class CloudServiceDirector:
    def __init__(self, cloud_service_builder):
        self._cloud_service_builder = cloud_service_builder

    def produce_short_term_saas(self):
        return (
            self._cloud_service_builder.set_service_type("short_term_saas")
            .set_contract_duration(1)
            .set_hello_world_app(True)
            .build()
        )

    def produce_long_term_saas(self):
        return (
            self._cloud_service_builder.set_service_type("long_term_saas")
            .set_contract_duration(2)
            .set_hello_world_app(True)
            .build()
        )

    def produce_short_term_paas(self):
        return (
            self._cloud_service_builder.set_service_type("short_term_paas")
            .set_contract_duration(1)
            .set_hello_world_app(True)
            .set_script_deployment(True)
            .set_orchestrated_deployment(True)
            .set_analytics(True)
            .set_error_tracking(True)
            .build()
        )

    def produce_long_term_paas(self):
        return (
            self._cloud_service_builder.set_service_type("long_term_paas")
            .set_contract_duration(2)
            .set_hello_world_app(True)
            .set_script_deployment(True)
            .set_orchestrated_deployment(True)
            .set_analytics(True)
            .set_error_tracking(True)
            .build()
        )

    def produce_short_term_iaas(self):
        return (
            self._cloud_service_builder.set_service_type("short_term_iaas")
            .set_contract_duration(1)
            .set_hello_world_app(True)
            .set_analytics(True)
            .set_error_tracking(True)
            .set_performance_monitoring(True)
            .build()
        )

    def produce_long_term_iaas(self):
        return (
            self._cloud_service_builder.set_service_type("long_term_iaas")
            .set_contract_duration(2)
            .set_hello_world_app(True)
            .set_analytics(True)
            .set_error_tracking(True)
            .set_performance_monitoring(True)
            .build()
        )


if __name__ == "__main__":
    # Software as a Service
    short_term_saas = CloudServiceDirector(
        CloudService.builder()
    ).produce_short_term_saas()
    long_term_saas = CloudServiceDirector(
        CloudService.builder()
    ).produce_long_term_saas()

    # Platform as a Service
    short_term_paas = CloudServiceDirector(
        CloudService.builder()
    ).produce_short_term_paas()
    long_term_paas = CloudServiceDirector(
        CloudService.builder()
    ).produce_long_term_paas()

    # Infrastructure as a Service
    short_term_iaas = CloudServiceDirector(
        CloudService.builder()
    ).produce_short_term_iaas()
    long_term_iaas = CloudServiceDirector(
        CloudService.builder()
    ).produce_long_term_iaas()

    cloud_services = [
        short_term_saas,
        long_term_saas,
        short_term_paas,
        long_term_paas,
        short_term_iaas,
        long_term_iaas,
    ]

    for cloud_service in cloud_services:
        print(f"{cloud_service}\n")
