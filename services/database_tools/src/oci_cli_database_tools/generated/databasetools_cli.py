# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('dbtools.dbtools_root_group.command_name', 'dbtools'), cls=CommandGroupWithAlias, help=cli_util.override('dbtools.dbtools_root_group.help', """Database Tools APIs to manage Connections and Private Endpoints."""), short_help=cli_util.override('dbtools.dbtools_root_group.short_help', """Database Tools"""))
@cli_util.help_option_group
def dbtools_root_group():
    pass


@click.command(cli_util.override('dbtools.database_tools_endpoint_service_group.command_name', 'database-tools-endpoint-service'), cls=CommandGroupWithAlias, help="""Description of DatabaseToolsEndpointService.""")
@cli_util.help_option_group
def database_tools_endpoint_service_group():
    pass


@click.command(cli_util.override('dbtools.database_tools_private_endpoint_group.command_name', 'database-tools-private-endpoint'), cls=CommandGroupWithAlias, help="""Description of DatabaseToolsPrivateEndpoint.""")
@cli_util.help_option_group
def database_tools_private_endpoint_group():
    pass


@click.command(cli_util.override('dbtools.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('dbtools.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('dbtools.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""An asynchronous work request.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('dbtools.database_tools_connection_group.command_name', 'database-tools-connection'), cls=CommandGroupWithAlias, help="""Description of DatabaseToolsConnection.""")
@cli_util.help_option_group
def database_tools_connection_group():
    pass


dbtools_root_group.add_command(database_tools_endpoint_service_group)
dbtools_root_group.add_command(database_tools_private_endpoint_group)
dbtools_root_group.add_command(work_request_error_group)
dbtools_root_group.add_command(work_request_log_entry_group)
dbtools_root_group.add_command(work_request_group)
dbtools_root_group.add_command(database_tools_connection_group)


@database_tools_connection_group.command(name=cli_util.override('dbtools.change_database_tools_connection_compartment.command_name', 'change-compartment'), help=u"""Moves a DatabaseToolsConnection into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeDatabaseToolsConnectionCompartment)""")
@cli_util.option('--database-tools-connection-id', required=True, help=u"""The [OCID] of a DatabaseToolsConnection.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the DatabaseToolsConnection to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "WAITING"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_database_tools_connection_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_tools_connection_id, compartment_id, if_match):

    if isinstance(database_tools_connection_id, six.string_types) and len(database_tools_connection_id.strip()) == 0:
        raise click.UsageError('Parameter --database-tools-connection-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    result = client.change_database_tools_connection_compartment(
        database_tools_connection_id=database_tools_connection_id,
        change_database_tools_connection_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@database_tools_private_endpoint_group.command(name=cli_util.override('dbtools.change_database_tools_private_endpoint_compartment.command_name', 'change-compartment'), help=u"""Moves a DatabaseToolsPrivateEndpoint into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment]. \n[Command Reference](changeDatabaseToolsPrivateEndpointCompartment)""")
@cli_util.option('--database-tools-private-endpoint-id', required=True, help=u"""The [OCID] of a DatabaseToolsPrivateEndpoint.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the DatabaseConnectionProfile to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "WAITING"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_database_tools_private_endpoint_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_tools_private_endpoint_id, compartment_id, if_match):

    if isinstance(database_tools_private_endpoint_id, six.string_types) and len(database_tools_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --database-tools-private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    result = client.change_database_tools_private_endpoint_compartment(
        database_tools_private_endpoint_id=database_tools_private_endpoint_id,
        change_database_tools_private_endpoint_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@database_tools_connection_group.command(name=cli_util.override('dbtools.create_database_tools_connection.command_name', 'create'), help=u"""Creates a new DatabaseToolsConnection. \n[Command Reference](createDatabaseToolsConnection)""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the containing Compartment.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ORACLE_DATABASE"]), help=u"""The DatabaseToolsConnection type.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "WAITING"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsConnection'})
@cli_util.wrap_exceptions
def create_database_tools_connection(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, type, defined_tags, freeform_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['type'] = type

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    result = client.create_database_tools_connection(
        create_database_tools_connection_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@database_tools_connection_group.command(name=cli_util.override('dbtools.create_database_tools_connection_create_database_tools_connection_oracle_database_details.command_name', 'create-database-tools-connection-create-database-tools-connection-oracle-database-details'), help=u"""Creates a new DatabaseToolsConnection. \n[Command Reference](createDatabaseToolsConnection)""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the containing Compartment.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--related-resource', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-string', help=u"""Connect descriptor or Easy Connect Naming method to connect to the database.""")
@cli_util.option('--user-name', help=u"""Database user name.""")
@cli_util.option('--user-password', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--advanced-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Advanced connection properties key-value pair (e.g., oracle.net.ssl_server_dn_match).""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--key-stores', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Oracle wallet or Java Keystores containing trusted certificates for authenticating the server's public certificate and the client private key and associated certificates required for client authentication.

This option is a JSON list with items of type DatabaseToolsKeyStoreDetails.  For documentation on DatabaseToolsKeyStoreDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/databasetools/20201005/datatypes/DatabaseToolsKeyStoreDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--private-endpoint-id', help=u"""The [OCID] of the DatabaseToolsPrivateEndpoint used to access the database in the Customer VCN.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "WAITING"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'related-resource': {'module': 'database_tools', 'class': 'CreateDatabaseToolsRelatedResourceDetails'}, 'user-password': {'module': 'database_tools', 'class': 'DatabaseToolsUserPasswordDetails'}, 'advanced-properties': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'key-stores': {'module': 'database_tools', 'class': 'list[DatabaseToolsKeyStoreDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'related-resource': {'module': 'database_tools', 'class': 'CreateDatabaseToolsRelatedResourceDetails'}, 'user-password': {'module': 'database_tools', 'class': 'DatabaseToolsUserPasswordDetails'}, 'advanced-properties': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'key-stores': {'module': 'database_tools', 'class': 'list[DatabaseToolsKeyStoreDetails]'}}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsConnection'})
@cli_util.wrap_exceptions
def create_database_tools_connection_create_database_tools_connection_oracle_database_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, defined_tags, freeform_tags, related_resource, connection_string, user_name, user_password, advanced_properties, key_stores, private_endpoint_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if related_resource is not None:
        _details['relatedResource'] = cli_util.parse_json_parameter("related_resource", related_resource)

    if connection_string is not None:
        _details['connectionString'] = connection_string

    if user_name is not None:
        _details['userName'] = user_name

    if user_password is not None:
        _details['userPassword'] = cli_util.parse_json_parameter("user_password", user_password)

    if advanced_properties is not None:
        _details['advancedProperties'] = cli_util.parse_json_parameter("advanced_properties", advanced_properties)

    if key_stores is not None:
        _details['keyStores'] = cli_util.parse_json_parameter("key_stores", key_stores)

    if private_endpoint_id is not None:
        _details['privateEndpointId'] = private_endpoint_id

    _details['type'] = 'ORACLE_DATABASE'

    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    result = client.create_database_tools_connection(
        create_database_tools_connection_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@database_tools_private_endpoint_group.command(name=cli_util.override('dbtools.create_database_tools_private_endpoint.command_name', 'create'), help=u"""Creates a new DatabaseToolsPrivateEndpoint. \n[Command Reference](createDatabaseToolsPrivateEndpoint)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the containing Compartment.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--endpoint-service-id', required=True, help=u"""The [OCID] of the DatabaseToolsEndpointService.""")
@cli_util.option('--subnet-id', required=True, help=u"""The [OCID] of the subnet that the private endpoint belongs to.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""A description of the DatabaseToolsPrivateEndpoint.""")
@cli_util.option('--private-endpoint-ip', help=u"""The private IP address that represents the access point for the associated endpoint service.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The [OCID] of the network security groups that the private endpoint's VNIC belongs to.  For more information about NSGs, see [NetworkSecurityGroup].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "WAITING"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'nsg-ids': {'module': 'database_tools', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'nsg-ids': {'module': 'database_tools', 'class': 'list[string]'}}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsPrivateEndpoint'})
@cli_util.wrap_exceptions
def create_database_tools_private_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, endpoint_service_id, subnet_id, defined_tags, freeform_tags, description, private_endpoint_ip, nsg_ids):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['endpointServiceId'] = endpoint_service_id
    _details['subnetId'] = subnet_id

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if description is not None:
        _details['description'] = description

    if private_endpoint_ip is not None:
        _details['privateEndpointIp'] = private_endpoint_ip

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    result = client.create_database_tools_private_endpoint(
        create_database_tools_private_endpoint_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@database_tools_connection_group.command(name=cli_util.override('dbtools.delete_database_tools_connection.command_name', 'delete'), help=u"""Deletes a DatabaseToolsConnection resource by identifier \n[Command Reference](deleteDatabaseToolsConnection)""")
@cli_util.option('--database-tools-connection-id', required=True, help=u"""The [OCID] of a DatabaseToolsConnection.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "WAITING"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_database_tools_connection(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_tools_connection_id, if_match):

    if isinstance(database_tools_connection_id, six.string_types) and len(database_tools_connection_id.strip()) == 0:
        raise click.UsageError('Parameter --database-tools-connection-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    result = client.delete_database_tools_connection(
        database_tools_connection_id=database_tools_connection_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@database_tools_private_endpoint_group.command(name=cli_util.override('dbtools.delete_database_tools_private_endpoint.command_name', 'delete'), help=u"""Deletes a DatabaseToolsPrivateEndpoint resource by identifier \n[Command Reference](deleteDatabaseToolsPrivateEndpoint)""")
@cli_util.option('--database-tools-private-endpoint-id', required=True, help=u"""The [OCID] of a DatabaseToolsPrivateEndpoint.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "WAITING"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_database_tools_private_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, database_tools_private_endpoint_id, if_match):

    if isinstance(database_tools_private_endpoint_id, six.string_types) and len(database_tools_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --database-tools-private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    result = client.delete_database_tools_private_endpoint(
        database_tools_private_endpoint_id=database_tools_private_endpoint_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@database_tools_connection_group.command(name=cli_util.override('dbtools.get_database_tools_connection.command_name', 'get'), help=u"""Gets a DatabaseToolsConnection by identifier \n[Command Reference](getDatabaseToolsConnection)""")
@cli_util.option('--database-tools-connection-id', required=True, help=u"""The [OCID] of a DatabaseToolsConnection.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsConnection'})
@cli_util.wrap_exceptions
def get_database_tools_connection(ctx, from_json, database_tools_connection_id):

    if isinstance(database_tools_connection_id, six.string_types) and len(database_tools_connection_id.strip()) == 0:
        raise click.UsageError('Parameter --database-tools-connection-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    result = client.get_database_tools_connection(
        database_tools_connection_id=database_tools_connection_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_tools_endpoint_service_group.command(name=cli_util.override('dbtools.get_database_tools_endpoint_service.command_name', 'get'), help=u"""Gets a DatabaseToolsEndpointService by identifier \n[Command Reference](getDatabaseToolsEndpointService)""")
@cli_util.option('--database-tools-endpoint-service-id', required=True, help=u"""The [OCID] of a DatabaseToolsEndpointService.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsEndpointService'})
@cli_util.wrap_exceptions
def get_database_tools_endpoint_service(ctx, from_json, database_tools_endpoint_service_id):

    if isinstance(database_tools_endpoint_service_id, six.string_types) and len(database_tools_endpoint_service_id.strip()) == 0:
        raise click.UsageError('Parameter --database-tools-endpoint-service-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    result = client.get_database_tools_endpoint_service(
        database_tools_endpoint_service_id=database_tools_endpoint_service_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_tools_private_endpoint_group.command(name=cli_util.override('dbtools.get_database_tools_private_endpoint.command_name', 'get'), help=u"""Gets a DatabaseToolsPrivateEndpoint by identifier \n[Command Reference](getDatabaseToolsPrivateEndpoint)""")
@cli_util.option('--database-tools-private-endpoint-id', required=True, help=u"""The [OCID] of a DatabaseToolsPrivateEndpoint.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsPrivateEndpoint'})
@cli_util.wrap_exceptions
def get_database_tools_private_endpoint(ctx, from_json, database_tools_private_endpoint_id):

    if isinstance(database_tools_private_endpoint_id, six.string_types) and len(database_tools_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --database-tools-private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    result = client.get_database_tools_private_endpoint(
        database_tools_private_endpoint_id=database_tools_private_endpoint_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('dbtools.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_tools_connection_group.command(name=cli_util.override('dbtools.list_database_tools_connections.command_name', 'list'), help=u"""Returns a list of DatabaseToolsConnections. \n[Command Reference](listDatabaseToolsConnections)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources their lifecycleState matches the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["ORACLE_DATABASE"]), multiple=True, help=u"""A filter to return only resources their endpointServiceId matches the given endpointServiceId.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsConnectionCollection'})
@cli_util.wrap_exceptions
def list_database_tools_connections(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, type, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if type is not None and len(type) > 0:
        kwargs['type'] = type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_database_tools_connections,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_database_tools_connections,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_database_tools_connections(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@database_tools_endpoint_service_group.command(name=cli_util.override('dbtools.list_database_tools_endpoint_services.command_name', 'list'), help=u"""Returns a list of DatabaseToolsEndpointServices. \n[Command Reference](listDatabaseToolsEndpointServices)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources their lifecycleState matches the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name given.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsEndpointServiceCollection'})
@cli_util.wrap_exceptions
def list_database_tools_endpoint_services(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_order, sort_by, lifecycle_state, display_name, name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if name is not None:
        kwargs['name'] = name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_database_tools_endpoint_services,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_database_tools_endpoint_services,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_database_tools_endpoint_services(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@database_tools_private_endpoint_group.command(name=cli_util.override('dbtools.list_database_tools_private_endpoints.command_name', 'list'), help=u"""Returns a list of DatabaseToolsPrivateEndpoints. \n[Command Reference](listDatabaseToolsPrivateEndpoints)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--subnet-id', help=u"""A filter to return only resources their subnetId matches the given subnetId.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--endpoint-service-id', help=u"""A filter to return only resources their type matches the given type.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources their lifecycleState matches the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'DatabaseToolsPrivateEndpointCollection'})
@cli_util.wrap_exceptions
def list_database_tools_private_endpoints(ctx, from_json, all_pages, page_size, compartment_id, subnet_id, limit, page, sort_order, sort_by, endpoint_service_id, lifecycle_state, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if subnet_id is not None:
        kwargs['subnet_id'] = subnet_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if endpoint_service_id is not None:
        kwargs['endpoint_service_id'] = endpoint_service_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_database_tools_private_endpoints,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_database_tools_private_endpoints,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_database_tools_private_endpoints(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('dbtools.list_work_request_errors.command_name', 'list'), help=u"""Return a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, sort_order, sort_by, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_entry_group.command(name=cli_util.override('dbtools.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Return a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, sort_order, sort_by, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('dbtools.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--resource-identifier', help=u"""The [OCID] of the resource.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending. If no value is specified timeAccepted is default.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'WorkRequestCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, resource_identifier, sort_order, sort_by, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if resource_identifier is not None:
        kwargs['resource_identifier'] = resource_identifier
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@database_tools_connection_group.command(name=cli_util.override('dbtools.update_database_tools_connection.command_name', 'update'), help=u"""Updates the DatabaseToolsConnection \n[Command Reference](updateDatabaseToolsConnection)""")
@cli_util.option('--database-tools-connection-id', required=True, help=u"""The [OCID] of a DatabaseToolsConnection.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ORACLE_DATABASE"]), help=u"""The DatabaseToolsConnection type.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "WAITING"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}})
@cli_util.wrap_exceptions
def update_database_tools_connection(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, database_tools_connection_id, type, display_name, defined_tags, freeform_tags, if_match):

    if isinstance(database_tools_connection_id, six.string_types) and len(database_tools_connection_id.strip()) == 0:
        raise click.UsageError('Parameter --database-tools-connection-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    if display_name is not None:
        _details['displayName'] = display_name

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    result = client.update_database_tools_connection(
        database_tools_connection_id=database_tools_connection_id,
        update_database_tools_connection_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@database_tools_connection_group.command(name=cli_util.override('dbtools.update_database_tools_connection_update_database_tools_connection_oracle_database_details.command_name', 'update-database-tools-connection-update-database-tools-connection-oracle-database-details'), help=u"""Updates the DatabaseToolsConnection \n[Command Reference](updateDatabaseToolsConnection)""")
@cli_util.option('--database-tools-connection-id', required=True, help=u"""The [OCID] of a DatabaseToolsConnection.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--related-resource', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-string', help=u"""Connect descriptor or Easy Connect Naming method to connect to the database.""")
@cli_util.option('--user-name', help=u"""Database user name.""")
@cli_util.option('--user-password', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--advanced-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Advanced connection properties key-value pair (e.g., oracle.net.ssl_server_dn_match).""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--key-stores', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Oracle wallet or Java Keystores containing trusted certificates for authenticating the server's public certificate and the client private key and associated certificates required for client authentication.

This option is a JSON list with items of type DatabaseToolsKeyStoreDetails.  For documentation on DatabaseToolsKeyStoreDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/databasetools/20201005/datatypes/DatabaseToolsKeyStoreDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--private-endpoint-id', help=u"""The [OCID] of the DatabaseToolsPrivateEndpoint used to access the database in the Customer VCN.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "WAITING"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'related-resource': {'module': 'database_tools', 'class': 'UpdateDatabaseToolsRelatedResourceDetails'}, 'user-password': {'module': 'database_tools', 'class': 'DatabaseToolsUserPasswordDetails'}, 'advanced-properties': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'key-stores': {'module': 'database_tools', 'class': 'list[DatabaseToolsKeyStoreDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'related-resource': {'module': 'database_tools', 'class': 'UpdateDatabaseToolsRelatedResourceDetails'}, 'user-password': {'module': 'database_tools', 'class': 'DatabaseToolsUserPasswordDetails'}, 'advanced-properties': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'key-stores': {'module': 'database_tools', 'class': 'list[DatabaseToolsKeyStoreDetails]'}})
@cli_util.wrap_exceptions
def update_database_tools_connection_update_database_tools_connection_oracle_database_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, database_tools_connection_id, display_name, defined_tags, freeform_tags, related_resource, connection_string, user_name, user_password, advanced_properties, key_stores, private_endpoint_id, if_match):

    if isinstance(database_tools_connection_id, six.string_types) and len(database_tools_connection_id.strip()) == 0:
        raise click.UsageError('Parameter --database-tools-connection-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or related_resource or user_password or advanced_properties or key_stores:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and related-resource and user-password and advanced-properties and key-stores will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if related_resource is not None:
        _details['relatedResource'] = cli_util.parse_json_parameter("related_resource", related_resource)

    if connection_string is not None:
        _details['connectionString'] = connection_string

    if user_name is not None:
        _details['userName'] = user_name

    if user_password is not None:
        _details['userPassword'] = cli_util.parse_json_parameter("user_password", user_password)

    if advanced_properties is not None:
        _details['advancedProperties'] = cli_util.parse_json_parameter("advanced_properties", advanced_properties)

    if key_stores is not None:
        _details['keyStores'] = cli_util.parse_json_parameter("key_stores", key_stores)

    if private_endpoint_id is not None:
        _details['privateEndpointId'] = private_endpoint_id

    _details['type'] = 'ORACLE_DATABASE'

    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    result = client.update_database_tools_connection(
        database_tools_connection_id=database_tools_connection_id,
        update_database_tools_connection_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@database_tools_private_endpoint_group.command(name=cli_util.override('dbtools.update_database_tools_private_endpoint.command_name', 'update'), help=u"""Updates the DatabaseToolsPrivateEndpoint \n[Command Reference](updateDatabaseToolsPrivateEndpoint)""")
@cli_util.option('--database-tools-private-endpoint-id', required=True, help=u"""The [OCID] of a DatabaseToolsPrivateEndpoint.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""A description of the DatabaseToolsPrivateEndpoint.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The [OCID] of the network security groups that the private endpoint's VNIC belongs to.  For more information about NSGs, see [NetworkSecurityGroup].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "WAITING"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'nsg-ids': {'module': 'database_tools', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'database_tools', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'database_tools', 'class': 'dict(str, string)'}, 'nsg-ids': {'module': 'database_tools', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_database_tools_private_endpoint(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, database_tools_private_endpoint_id, defined_tags, freeform_tags, display_name, description, nsg_ids, if_match):

    if isinstance(database_tools_private_endpoint_id, six.string_types) and len(database_tools_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --database-tools-private-endpoint-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags or nsg_ids:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags and nsg-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    result = client.update_database_tools_private_endpoint(
        database_tools_private_endpoint_id=database_tools_private_endpoint_id,
        update_database_tools_private_endpoint_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@database_tools_connection_group.command(name=cli_util.override('dbtools.validate_database_tools_connection.command_name', 'validate'), help=u"""Validate the DatabaseToolsConnection information details by establishing a connection to the database. \n[Command Reference](validateDatabaseToolsConnection)""")
@cli_util.option('--database-tools-connection-id', required=True, help=u"""The [OCID] of a DatabaseToolsConnection.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ORACLE_DATABASE"]), help=u"""The DatabaseToolsConnection type.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'ValidateDatabaseToolsConnectionResult'})
@cli_util.wrap_exceptions
def validate_database_tools_connection(ctx, from_json, database_tools_connection_id, type, if_match):

    if isinstance(database_tools_connection_id, six.string_types) and len(database_tools_connection_id.strip()) == 0:
        raise click.UsageError('Parameter --database-tools-connection-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    result = client.validate_database_tools_connection(
        database_tools_connection_id=database_tools_connection_id,
        validate_database_tools_connection_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@database_tools_connection_group.command(name=cli_util.override('dbtools.validate_database_tools_connection_validate_database_tools_connection_oracle_database_details.command_name', 'validate-database-tools-connection-validate-database-tools-connection-oracle-database-details'), help=u"""Validate the DatabaseToolsConnection information details by establishing a connection to the database. \n[Command Reference](validateDatabaseToolsConnection)""")
@cli_util.option('--database-tools-connection-id', required=True, help=u"""The [OCID] of a DatabaseToolsConnection.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools', 'class': 'ValidateDatabaseToolsConnectionResult'})
@cli_util.wrap_exceptions
def validate_database_tools_connection_validate_database_tools_connection_oracle_database_details(ctx, from_json, database_tools_connection_id, if_match):

    if isinstance(database_tools_connection_id, six.string_types) and len(database_tools_connection_id.strip()) == 0:
        raise click.UsageError('Parameter --database-tools-connection-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    _details['type'] = 'ORACLE_DATABASE'

    client = cli_util.build_client('database_tools', 'database_tools', ctx)
    result = client.validate_database_tools_connection(
        database_tools_connection_id=database_tools_connection_id,
        validate_database_tools_connection_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
