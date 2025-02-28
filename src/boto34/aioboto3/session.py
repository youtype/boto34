"""
Type annotated wrapper for aioboto3 Session.

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # s3_client is aiobotocore.AioBaseClient
    # with type annotations only in type checking mode
    async with session.s3.client() as s3_client:
        s3_client.list_buckets()

    # s3_resource is aioboto3.AIOBoto3ServiceResource
    # with type annotations only in type checking mode
    async with session.s3.resource() as s3_resource:
        s3_resource.Bucket("bucket").objects.all()
    ```
"""

from aioboto3.session import Session as Aioboto3Session
from types_aiobotocore_accessanalyzer.client import AccessAnalyzerClient
from types_aiobotocore_account.client import AccountClient
from types_aiobotocore_acm.client import ACMClient
from types_aiobotocore_acm_pca.client import ACMPCAClient
from types_aiobotocore_amp.client import PrometheusServiceClient
from types_aiobotocore_amplify.client import AmplifyClient
from types_aiobotocore_amplifybackend.client import AmplifyBackendClient
from types_aiobotocore_amplifyuibuilder.client import AmplifyUIBuilderClient
from types_aiobotocore_apigateway.client import APIGatewayClient
from types_aiobotocore_apigatewaymanagementapi.client import ApiGatewayManagementApiClient
from types_aiobotocore_apigatewayv2.client import ApiGatewayV2Client
from types_aiobotocore_appconfig.client import AppConfigClient
from types_aiobotocore_appconfigdata.client import AppConfigDataClient
from types_aiobotocore_appfabric.client import AppFabricClient
from types_aiobotocore_appflow.client import AppflowClient
from types_aiobotocore_appintegrations.client import AppIntegrationsServiceClient
from types_aiobotocore_application_autoscaling.client import ApplicationAutoScalingClient
from types_aiobotocore_application_insights.client import ApplicationInsightsClient
from types_aiobotocore_application_signals.client import CloudWatchApplicationSignalsClient
from types_aiobotocore_applicationcostprofiler.client import ApplicationCostProfilerClient
from types_aiobotocore_appmesh.client import AppMeshClient
from types_aiobotocore_apprunner.client import AppRunnerClient
from types_aiobotocore_appstream.client import AppStreamClient
from types_aiobotocore_appsync.client import AppSyncClient
from types_aiobotocore_apptest.client import MainframeModernizationApplicationTestingClient
from types_aiobotocore_arc_zonal_shift.client import ARCZonalShiftClient
from types_aiobotocore_artifact.client import ArtifactClient
from types_aiobotocore_athena.client import AthenaClient
from types_aiobotocore_auditmanager.client import AuditManagerClient
from types_aiobotocore_autoscaling.client import AutoScalingClient
from types_aiobotocore_autoscaling_plans.client import AutoScalingPlansClient
from types_aiobotocore_b2bi.client import B2BIClient
from types_aiobotocore_backup.client import BackupClient
from types_aiobotocore_backup_gateway.client import BackupGatewayClient
from types_aiobotocore_backupsearch.client import BackupSearchClient
from types_aiobotocore_batch.client import BatchClient
from types_aiobotocore_bcm_data_exports.client import BillingandCostManagementDataExportsClient
from types_aiobotocore_bcm_pricing_calculator.client import (
    BillingandCostManagementPricingCalculatorClient,
)
from types_aiobotocore_bedrock.client import BedrockClient
from types_aiobotocore_bedrock_agent.client import AgentsforBedrockClient
from types_aiobotocore_bedrock_agent_runtime.client import AgentsforBedrockRuntimeClient
from types_aiobotocore_bedrock_data_automation.client import DataAutomationforBedrockClient
from types_aiobotocore_bedrock_data_automation_runtime.client import (
    RuntimeforBedrockDataAutomationClient,
)
from types_aiobotocore_bedrock_runtime.client import BedrockRuntimeClient
from types_aiobotocore_billing.client import BillingClient
from types_aiobotocore_billingconductor.client import BillingConductorClient
from types_aiobotocore_braket.client import BraketClient
from types_aiobotocore_budgets.client import BudgetsClient
from types_aiobotocore_ce.client import CostExplorerClient
from types_aiobotocore_chatbot.client import ChatbotClient
from types_aiobotocore_chime.client import ChimeClient
from types_aiobotocore_chime_sdk_identity.client import ChimeSDKIdentityClient
from types_aiobotocore_chime_sdk_media_pipelines.client import ChimeSDKMediaPipelinesClient
from types_aiobotocore_chime_sdk_meetings.client import ChimeSDKMeetingsClient
from types_aiobotocore_chime_sdk_messaging.client import ChimeSDKMessagingClient
from types_aiobotocore_chime_sdk_voice.client import ChimeSDKVoiceClient
from types_aiobotocore_cleanrooms.client import CleanRoomsServiceClient
from types_aiobotocore_cleanroomsml.client import CleanRoomsMLClient
from types_aiobotocore_cloud9.client import Cloud9Client
from types_aiobotocore_cloudcontrol.client import CloudControlApiClient
from types_aiobotocore_clouddirectory.client import CloudDirectoryClient
from types_aiobotocore_cloudformation.client import CloudFormationClient
from types_aiobotocore_cloudformation.service_resource import CloudFormationServiceResource
from types_aiobotocore_cloudfront.client import CloudFrontClient
from types_aiobotocore_cloudfront_keyvaluestore.client import CloudFrontKeyValueStoreClient
from types_aiobotocore_cloudhsm.client import CloudHSMClient
from types_aiobotocore_cloudhsmv2.client import CloudHSMV2Client
from types_aiobotocore_cloudsearch.client import CloudSearchClient
from types_aiobotocore_cloudsearchdomain.client import CloudSearchDomainClient
from types_aiobotocore_cloudtrail.client import CloudTrailClient
from types_aiobotocore_cloudtrail_data.client import CloudTrailDataServiceClient
from types_aiobotocore_cloudwatch.client import CloudWatchClient
from types_aiobotocore_cloudwatch.service_resource import CloudWatchServiceResource
from types_aiobotocore_codeartifact.client import CodeArtifactClient
from types_aiobotocore_codebuild.client import CodeBuildClient
from types_aiobotocore_codecatalyst.client import CodeCatalystClient
from types_aiobotocore_codecommit.client import CodeCommitClient
from types_aiobotocore_codeconnections.client import CodeConnectionsClient
from types_aiobotocore_codedeploy.client import CodeDeployClient
from types_aiobotocore_codeguru_reviewer.client import CodeGuruReviewerClient
from types_aiobotocore_codeguru_security.client import CodeGuruSecurityClient
from types_aiobotocore_codeguruprofiler.client import CodeGuruProfilerClient
from types_aiobotocore_codepipeline.client import CodePipelineClient
from types_aiobotocore_codestar_connections.client import CodeStarconnectionsClient
from types_aiobotocore_codestar_notifications.client import CodeStarNotificationsClient
from types_aiobotocore_cognito_identity.client import CognitoIdentityClient
from types_aiobotocore_cognito_idp.client import CognitoIdentityProviderClient
from types_aiobotocore_cognito_sync.client import CognitoSyncClient
from types_aiobotocore_comprehend.client import ComprehendClient
from types_aiobotocore_comprehendmedical.client import ComprehendMedicalClient
from types_aiobotocore_compute_optimizer.client import ComputeOptimizerClient
from types_aiobotocore_config.client import ConfigServiceClient
from types_aiobotocore_connect.client import ConnectClient
from types_aiobotocore_connect_contact_lens.client import ConnectContactLensClient
from types_aiobotocore_connectcampaigns.client import ConnectCampaignServiceClient
from types_aiobotocore_connectcampaignsv2.client import ConnectCampaignServiceV2Client
from types_aiobotocore_connectcases.client import ConnectCasesClient
from types_aiobotocore_connectparticipant.client import ConnectParticipantClient
from types_aiobotocore_controlcatalog.client import ControlCatalogClient
from types_aiobotocore_controltower.client import ControlTowerClient
from types_aiobotocore_cost_optimization_hub.client import CostOptimizationHubClient
from types_aiobotocore_cur.client import CostandUsageReportServiceClient
from types_aiobotocore_customer_profiles.client import CustomerProfilesClient
from types_aiobotocore_databrew.client import GlueDataBrewClient
from types_aiobotocore_dataexchange.client import DataExchangeClient
from types_aiobotocore_datapipeline.client import DataPipelineClient
from types_aiobotocore_datasync.client import DataSyncClient
from types_aiobotocore_datazone.client import DataZoneClient
from types_aiobotocore_dax.client import DAXClient
from types_aiobotocore_deadline.client import DeadlineCloudClient
from types_aiobotocore_detective.client import DetectiveClient
from types_aiobotocore_devicefarm.client import DeviceFarmClient
from types_aiobotocore_devops_guru.client import DevOpsGuruClient
from types_aiobotocore_directconnect.client import DirectConnectClient
from types_aiobotocore_discovery.client import ApplicationDiscoveryServiceClient
from types_aiobotocore_dlm.client import DLMClient
from types_aiobotocore_dms.client import DatabaseMigrationServiceClient
from types_aiobotocore_docdb.client import DocDBClient
from types_aiobotocore_docdb_elastic.client import DocDBElasticClient
from types_aiobotocore_drs.client import DrsClient
from types_aiobotocore_ds.client import DirectoryServiceClient
from types_aiobotocore_ds_data.client import DirectoryServiceDataClient
from types_aiobotocore_dsql.client import AuroraDSQLClient
from types_aiobotocore_dynamodb.client import DynamoDBClient
from types_aiobotocore_dynamodb.service_resource import DynamoDBServiceResource
from types_aiobotocore_dynamodbstreams.client import DynamoDBStreamsClient
from types_aiobotocore_ebs.client import EBSClient
from types_aiobotocore_ec2.client import EC2Client
from types_aiobotocore_ec2.service_resource import EC2ServiceResource
from types_aiobotocore_ec2_instance_connect.client import EC2InstanceConnectClient
from types_aiobotocore_ecr.client import ECRClient
from types_aiobotocore_ecr_public.client import ECRPublicClient
from types_aiobotocore_ecs.client import ECSClient
from types_aiobotocore_efs.client import EFSClient
from types_aiobotocore_eks.client import EKSClient
from types_aiobotocore_eks_auth.client import EKSAuthClient
from types_aiobotocore_elasticache.client import ElastiCacheClient
from types_aiobotocore_elasticbeanstalk.client import ElasticBeanstalkClient
from types_aiobotocore_elastictranscoder.client import ElasticTranscoderClient
from types_aiobotocore_elb.client import ElasticLoadBalancingClient
from types_aiobotocore_elbv2.client import ElasticLoadBalancingv2Client
from types_aiobotocore_emr.client import EMRClient
from types_aiobotocore_emr_containers.client import EMRContainersClient
from types_aiobotocore_emr_serverless.client import EMRServerlessClient
from types_aiobotocore_entityresolution.client import EntityResolutionClient
from types_aiobotocore_es.client import ElasticsearchServiceClient
from types_aiobotocore_events.client import EventBridgeClient
from types_aiobotocore_evidently.client import CloudWatchEvidentlyClient
from types_aiobotocore_finspace.client import FinspaceClient
from types_aiobotocore_finspace_data.client import FinSpaceDataClient
from types_aiobotocore_firehose.client import FirehoseClient
from types_aiobotocore_fis.client import FISClient
from types_aiobotocore_fms.client import FMSClient
from types_aiobotocore_forecast.client import ForecastServiceClient
from types_aiobotocore_forecastquery.client import ForecastQueryServiceClient
from types_aiobotocore_frauddetector.client import FraudDetectorClient
from types_aiobotocore_freetier.client import FreeTierClient
from types_aiobotocore_fsx.client import FSxClient
from types_aiobotocore_gamelift.client import GameLiftClient
from types_aiobotocore_geo_maps.client import LocationServiceMapsV2Client
from types_aiobotocore_geo_places.client import LocationServicePlacesV2Client
from types_aiobotocore_geo_routes.client import LocationServiceRoutesV2Client
from types_aiobotocore_glacier.client import GlacierClient
from types_aiobotocore_glacier.service_resource import GlacierServiceResource
from types_aiobotocore_globalaccelerator.client import GlobalAcceleratorClient
from types_aiobotocore_glue.client import GlueClient
from types_aiobotocore_grafana.client import ManagedGrafanaClient
from types_aiobotocore_greengrass.client import GreengrassClient
from types_aiobotocore_greengrassv2.client import GreengrassV2Client
from types_aiobotocore_groundstation.client import GroundStationClient
from types_aiobotocore_guardduty.client import GuardDutyClient
from types_aiobotocore_health.client import HealthClient
from types_aiobotocore_healthlake.client import HealthLakeClient
from types_aiobotocore_iam.client import IAMClient
from types_aiobotocore_iam.service_resource import IAMServiceResource
from types_aiobotocore_identitystore.client import IdentityStoreClient
from types_aiobotocore_imagebuilder.client import ImagebuilderClient
from types_aiobotocore_importexport.client import ImportExportClient
from types_aiobotocore_inspector.client import InspectorClient
from types_aiobotocore_inspector2.client import Inspector2Client
from types_aiobotocore_inspector_scan.client import InspectorscanClient
from types_aiobotocore_internetmonitor.client import CloudWatchInternetMonitorClient
from types_aiobotocore_invoicing.client import InvoicingClient
from types_aiobotocore_iot.client import IoTClient
from types_aiobotocore_iot_data.client import IoTDataPlaneClient
from types_aiobotocore_iot_jobs_data.client import IoTJobsDataPlaneClient
from types_aiobotocore_iotanalytics.client import IoTAnalyticsClient
from types_aiobotocore_iotdeviceadvisor.client import IoTDeviceAdvisorClient
from types_aiobotocore_iotevents.client import IoTEventsClient
from types_aiobotocore_iotevents_data.client import IoTEventsDataClient
from types_aiobotocore_iotfleethub.client import IoTFleetHubClient
from types_aiobotocore_iotfleetwise.client import IoTFleetWiseClient
from types_aiobotocore_iotsecuretunneling.client import IoTSecureTunnelingClient
from types_aiobotocore_iotsitewise.client import IoTSiteWiseClient
from types_aiobotocore_iotthingsgraph.client import IoTThingsGraphClient
from types_aiobotocore_iottwinmaker.client import IoTTwinMakerClient
from types_aiobotocore_iotwireless.client import IoTWirelessClient
from types_aiobotocore_ivs.client import IVSClient
from types_aiobotocore_ivs_realtime.client import IvsrealtimeClient
from types_aiobotocore_ivschat.client import IvschatClient
from types_aiobotocore_kafka.client import KafkaClient
from types_aiobotocore_kafkaconnect.client import KafkaConnectClient
from types_aiobotocore_kendra.client import KendraClient
from types_aiobotocore_kendra_ranking.client import KendraRankingClient
from types_aiobotocore_keyspaces.client import KeyspacesClient
from types_aiobotocore_kinesis.client import KinesisClient
from types_aiobotocore_kinesis_video_archived_media.client import KinesisVideoArchivedMediaClient
from types_aiobotocore_kinesis_video_media.client import KinesisVideoMediaClient
from types_aiobotocore_kinesis_video_signaling.client import KinesisVideoSignalingChannelsClient
from types_aiobotocore_kinesis_video_webrtc_storage.client import KinesisVideoWebRTCStorageClient
from types_aiobotocore_kinesisanalytics.client import KinesisAnalyticsClient
from types_aiobotocore_kinesisanalyticsv2.client import KinesisAnalyticsV2Client
from types_aiobotocore_kinesisvideo.client import KinesisVideoClient
from types_aiobotocore_kms.client import KMSClient
from types_aiobotocore_lakeformation.client import LakeFormationClient
from types_aiobotocore_lambda.client import LambdaClient
from types_aiobotocore_launch_wizard.client import LaunchWizardClient
from types_aiobotocore_lex_models.client import LexModelBuildingServiceClient
from types_aiobotocore_lex_runtime.client import LexRuntimeServiceClient
from types_aiobotocore_lexv2_models.client import LexModelsV2Client
from types_aiobotocore_lexv2_runtime.client import LexRuntimeV2Client
from types_aiobotocore_license_manager.client import LicenseManagerClient
from types_aiobotocore_license_manager_linux_subscriptions.client import (
    LicenseManagerLinuxSubscriptionsClient,
)
from types_aiobotocore_license_manager_user_subscriptions.client import (
    LicenseManagerUserSubscriptionsClient,
)
from types_aiobotocore_lightsail.client import LightsailClient
from types_aiobotocore_location.client import LocationServiceClient
from types_aiobotocore_logs.client import CloudWatchLogsClient
from types_aiobotocore_lookoutequipment.client import LookoutEquipmentClient
from types_aiobotocore_lookoutmetrics.client import LookoutMetricsClient
from types_aiobotocore_lookoutvision.client import LookoutforVisionClient
from types_aiobotocore_m2.client import MainframeModernizationClient
from types_aiobotocore_machinelearning.client import MachineLearningClient
from types_aiobotocore_macie2.client import Macie2Client
from types_aiobotocore_mailmanager.client import MailManagerClient
from types_aiobotocore_managedblockchain.client import ManagedBlockchainClient
from types_aiobotocore_managedblockchain_query.client import ManagedBlockchainQueryClient
from types_aiobotocore_marketplace_agreement.client import AgreementServiceClient
from types_aiobotocore_marketplace_catalog.client import MarketplaceCatalogClient
from types_aiobotocore_marketplace_deployment.client import MarketplaceDeploymentServiceClient
from types_aiobotocore_marketplace_entitlement.client import MarketplaceEntitlementServiceClient
from types_aiobotocore_marketplace_reporting.client import MarketplaceReportingServiceClient
from types_aiobotocore_marketplacecommerceanalytics.client import MarketplaceCommerceAnalyticsClient
from types_aiobotocore_mediaconnect.client import MediaConnectClient
from types_aiobotocore_mediaconvert.client import MediaConvertClient
from types_aiobotocore_medialive.client import MediaLiveClient
from types_aiobotocore_mediapackage.client import MediaPackageClient
from types_aiobotocore_mediapackage_vod.client import MediaPackageVodClient
from types_aiobotocore_mediapackagev2.client import Mediapackagev2Client
from types_aiobotocore_mediastore.client import MediaStoreClient
from types_aiobotocore_mediastore_data.client import MediaStoreDataClient
from types_aiobotocore_mediatailor.client import MediaTailorClient
from types_aiobotocore_medical_imaging.client import HealthImagingClient
from types_aiobotocore_memorydb.client import MemoryDBClient
from types_aiobotocore_meteringmarketplace.client import MarketplaceMeteringClient
from types_aiobotocore_mgh.client import MigrationHubClient
from types_aiobotocore_mgn.client import MgnClient
from types_aiobotocore_migration_hub_refactor_spaces.client import MigrationHubRefactorSpacesClient
from types_aiobotocore_migrationhub_config.client import MigrationHubConfigClient
from types_aiobotocore_migrationhuborchestrator.client import MigrationHubOrchestratorClient
from types_aiobotocore_migrationhubstrategy.client import MigrationHubStrategyRecommendationsClient
from types_aiobotocore_mq.client import MQClient
from types_aiobotocore_mturk.client import MTurkClient
from types_aiobotocore_mwaa.client import MWAAClient
from types_aiobotocore_neptune.client import NeptuneClient
from types_aiobotocore_neptune_graph.client import NeptuneGraphClient
from types_aiobotocore_neptunedata.client import NeptuneDataClient
from types_aiobotocore_network_firewall.client import NetworkFirewallClient
from types_aiobotocore_networkflowmonitor.client import NetworkFlowMonitorClient
from types_aiobotocore_networkmanager.client import NetworkManagerClient
from types_aiobotocore_networkmonitor.client import CloudWatchNetworkMonitorClient
from types_aiobotocore_notifications.client import UserNotificationsClient
from types_aiobotocore_notificationscontacts.client import UserNotificationsContactsClient
from types_aiobotocore_oam.client import CloudWatchObservabilityAccessManagerClient
from types_aiobotocore_observabilityadmin.client import CloudWatchObservabilityAdminServiceClient
from types_aiobotocore_omics.client import OmicsClient
from types_aiobotocore_opensearch.client import OpenSearchServiceClient
from types_aiobotocore_opensearchserverless.client import OpenSearchServiceServerlessClient
from types_aiobotocore_opsworks.client import OpsWorksClient
from types_aiobotocore_opsworks.service_resource import OpsWorksServiceResource
from types_aiobotocore_opsworkscm.client import OpsWorksCMClient
from types_aiobotocore_organizations.client import OrganizationsClient
from types_aiobotocore_osis.client import OpenSearchIngestionClient
from types_aiobotocore_outposts.client import OutpostsClient
from types_aiobotocore_panorama.client import PanoramaClient
from types_aiobotocore_partnercentral_selling.client import PartnerCentralSellingAPIClient
from types_aiobotocore_payment_cryptography.client import PaymentCryptographyControlPlaneClient
from types_aiobotocore_payment_cryptography_data.client import PaymentCryptographyDataPlaneClient
from types_aiobotocore_pca_connector_ad.client import PcaConnectorAdClient
from types_aiobotocore_pca_connector_scep.client import PrivateCAConnectorforSCEPClient
from types_aiobotocore_pcs.client import ParallelComputingServiceClient
from types_aiobotocore_personalize.client import PersonalizeClient
from types_aiobotocore_personalize_events.client import PersonalizeEventsClient
from types_aiobotocore_personalize_runtime.client import PersonalizeRuntimeClient
from types_aiobotocore_pi.client import PIClient
from types_aiobotocore_pinpoint.client import PinpointClient
from types_aiobotocore_pinpoint_email.client import PinpointEmailClient
from types_aiobotocore_pinpoint_sms_voice.client import PinpointSMSVoiceClient
from types_aiobotocore_pinpoint_sms_voice_v2.client import PinpointSMSVoiceV2Client
from types_aiobotocore_pipes.client import EventBridgePipesClient
from types_aiobotocore_polly.client import PollyClient
from types_aiobotocore_pricing.client import PricingClient
from types_aiobotocore_privatenetworks.client import Private5GClient
from types_aiobotocore_proton.client import ProtonClient
from types_aiobotocore_qapps.client import QAppsClient
from types_aiobotocore_qbusiness.client import QBusinessClient
from types_aiobotocore_qconnect.client import QConnectClient
from types_aiobotocore_qldb.client import QLDBClient
from types_aiobotocore_qldb_session.client import QLDBSessionClient
from types_aiobotocore_quicksight.client import QuickSightClient
from types_aiobotocore_ram.client import RAMClient
from types_aiobotocore_rbin.client import RecycleBinClient
from types_aiobotocore_rds.client import RDSClient
from types_aiobotocore_rds_data.client import RDSDataServiceClient
from types_aiobotocore_redshift.client import RedshiftClient
from types_aiobotocore_redshift_data.client import RedshiftDataAPIServiceClient
from types_aiobotocore_redshift_serverless.client import RedshiftServerlessClient
from types_aiobotocore_rekognition.client import RekognitionClient
from types_aiobotocore_repostspace.client import RePostPrivateClient
from types_aiobotocore_resiliencehub.client import ResilienceHubClient
from types_aiobotocore_resource_explorer_2.client import ResourceExplorerClient
from types_aiobotocore_resource_groups.client import ResourceGroupsClient
from types_aiobotocore_resourcegroupstaggingapi.client import ResourceGroupsTaggingAPIClient
from types_aiobotocore_robomaker.client import RoboMakerClient
from types_aiobotocore_rolesanywhere.client import IAMRolesAnywhereClient
from types_aiobotocore_route53.client import Route53Client
from types_aiobotocore_route53_recovery_cluster.client import Route53RecoveryClusterClient
from types_aiobotocore_route53_recovery_control_config.client import (
    Route53RecoveryControlConfigClient,
)
from types_aiobotocore_route53_recovery_readiness.client import Route53RecoveryReadinessClient
from types_aiobotocore_route53domains.client import Route53DomainsClient
from types_aiobotocore_route53profiles.client import Route53ProfilesClient
from types_aiobotocore_route53resolver.client import Route53ResolverClient
from types_aiobotocore_rum.client import CloudWatchRUMClient
from types_aiobotocore_s3.client import S3Client
from types_aiobotocore_s3.service_resource import S3ServiceResource
from types_aiobotocore_s3control.client import S3ControlClient
from types_aiobotocore_s3outposts.client import S3OutpostsClient
from types_aiobotocore_s3tables.client import S3TablesClient
from types_aiobotocore_sagemaker.client import SageMakerClient
from types_aiobotocore_sagemaker_a2i_runtime.client import AugmentedAIRuntimeClient
from types_aiobotocore_sagemaker_edge.client import SagemakerEdgeManagerClient
from types_aiobotocore_sagemaker_featurestore_runtime.client import (
    SageMakerFeatureStoreRuntimeClient,
)
from types_aiobotocore_sagemaker_geospatial.client import SageMakergeospatialcapabilitiesClient
from types_aiobotocore_sagemaker_metrics.client import SageMakerMetricsClient
from types_aiobotocore_sagemaker_runtime.client import SageMakerRuntimeClient
from types_aiobotocore_savingsplans.client import SavingsPlansClient
from types_aiobotocore_scheduler.client import EventBridgeSchedulerClient
from types_aiobotocore_schemas.client import SchemasClient
from types_aiobotocore_sdb.client import SimpleDBClient
from types_aiobotocore_secretsmanager.client import SecretsManagerClient
from types_aiobotocore_security_ir.client import SecurityIncidentResponseClient
from types_aiobotocore_securityhub.client import SecurityHubClient
from types_aiobotocore_securitylake.client import SecurityLakeClient
from types_aiobotocore_serverlessrepo.client import ServerlessApplicationRepositoryClient
from types_aiobotocore_service_quotas.client import ServiceQuotasClient
from types_aiobotocore_servicecatalog.client import ServiceCatalogClient
from types_aiobotocore_servicecatalog_appregistry.client import AppRegistryClient
from types_aiobotocore_servicediscovery.client import ServiceDiscoveryClient
from types_aiobotocore_ses.client import SESClient
from types_aiobotocore_sesv2.client import SESV2Client
from types_aiobotocore_shield.client import ShieldClient
from types_aiobotocore_signer.client import SignerClient
from types_aiobotocore_simspaceweaver.client import SimSpaceWeaverClient
from types_aiobotocore_sms.client import SMSClient
from types_aiobotocore_sms_voice.client import SMSVoiceClient
from types_aiobotocore_snow_device_management.client import SnowDeviceManagementClient
from types_aiobotocore_snowball.client import SnowballClient
from types_aiobotocore_sns.client import SNSClient
from types_aiobotocore_sns.service_resource import SNSServiceResource
from types_aiobotocore_socialmessaging.client import EndUserMessagingSocialClient
from types_aiobotocore_sqs.client import SQSClient
from types_aiobotocore_sqs.service_resource import SQSServiceResource
from types_aiobotocore_ssm.client import SSMClient
from types_aiobotocore_ssm_contacts.client import SSMContactsClient
from types_aiobotocore_ssm_incidents.client import SSMIncidentsClient
from types_aiobotocore_ssm_quicksetup.client import SystemsManagerQuickSetupClient
from types_aiobotocore_ssm_sap.client import SsmSapClient
from types_aiobotocore_sso.client import SSOClient
from types_aiobotocore_sso_admin.client import SSOAdminClient
from types_aiobotocore_sso_oidc.client import SSOOIDCClient
from types_aiobotocore_stepfunctions.client import SFNClient
from types_aiobotocore_storagegateway.client import StorageGatewayClient
from types_aiobotocore_sts.client import STSClient
from types_aiobotocore_supplychain.client import SupplyChainClient
from types_aiobotocore_support.client import SupportClient
from types_aiobotocore_support_app.client import SupportAppClient
from types_aiobotocore_swf.client import SWFClient
from types_aiobotocore_synthetics.client import SyntheticsClient
from types_aiobotocore_taxsettings.client import TaxSettingsClient
from types_aiobotocore_textract.client import TextractClient
from types_aiobotocore_timestream_influxdb.client import TimestreamInfluxDBClient
from types_aiobotocore_timestream_query.client import TimestreamQueryClient
from types_aiobotocore_timestream_write.client import TimestreamWriteClient
from types_aiobotocore_tnb.client import TelcoNetworkBuilderClient
from types_aiobotocore_transcribe.client import TranscribeServiceClient
from types_aiobotocore_transfer.client import TransferClient
from types_aiobotocore_translate.client import TranslateClient
from types_aiobotocore_trustedadvisor.client import TrustedAdvisorPublicAPIClient
from types_aiobotocore_verifiedpermissions.client import VerifiedPermissionsClient
from types_aiobotocore_voice_id.client import VoiceIDClient
from types_aiobotocore_vpc_lattice.client import VPCLatticeClient
from types_aiobotocore_waf.client import WAFClient
from types_aiobotocore_waf_regional.client import WAFRegionalClient
from types_aiobotocore_wafv2.client import WAFV2Client
from types_aiobotocore_wellarchitected.client import WellArchitectedClient
from types_aiobotocore_wisdom.client import ConnectWisdomServiceClient
from types_aiobotocore_workdocs.client import WorkDocsClient
from types_aiobotocore_workmail.client import WorkMailClient
from types_aiobotocore_workmailmessageflow.client import WorkMailMessageFlowClient
from types_aiobotocore_workspaces.client import WorkSpacesClient
from types_aiobotocore_workspaces_thin_client.client import WorkSpacesThinClientClient
from types_aiobotocore_workspaces_web.client import WorkSpacesWebClient
from types_aiobotocore_xray.client import XRayClient

from boto34.aioboto3.service_factory import ServiceFactory, ServiceResourceFactory


class Session(Aioboto3Session):
    @property
    def accessanalyzer(self) -> ServiceFactory[AccessAnalyzerClient]:
        return ServiceFactory("accessanalyzer", self)

    @property
    def account(self) -> ServiceFactory[AccountClient]:
        return ServiceFactory("account", self)

    @property
    def acm(self) -> ServiceFactory[ACMClient]:
        return ServiceFactory("acm", self)

    @property
    def acm_pca(self) -> ServiceFactory[ACMPCAClient]:
        return ServiceFactory("acm-pca", self)

    @property
    def amp(self) -> ServiceFactory[PrometheusServiceClient]:
        return ServiceFactory("amp", self)

    @property
    def amplify(self) -> ServiceFactory[AmplifyClient]:
        return ServiceFactory("amplify", self)

    @property
    def amplifybackend(self) -> ServiceFactory[AmplifyBackendClient]:
        return ServiceFactory("amplifybackend", self)

    @property
    def amplifyuibuilder(self) -> ServiceFactory[AmplifyUIBuilderClient]:
        return ServiceFactory("amplifyuibuilder", self)

    @property
    def apigateway(self) -> ServiceFactory[APIGatewayClient]:
        return ServiceFactory("apigateway", self)

    @property
    def apigatewaymanagementapi(self) -> ServiceFactory[ApiGatewayManagementApiClient]:
        return ServiceFactory("apigatewaymanagementapi", self)

    @property
    def apigatewayv2(self) -> ServiceFactory[ApiGatewayV2Client]:
        return ServiceFactory("apigatewayv2", self)

    @property
    def appconfig(self) -> ServiceFactory[AppConfigClient]:
        return ServiceFactory("appconfig", self)

    @property
    def appconfigdata(self) -> ServiceFactory[AppConfigDataClient]:
        return ServiceFactory("appconfigdata", self)

    @property
    def appfabric(self) -> ServiceFactory[AppFabricClient]:
        return ServiceFactory("appfabric", self)

    @property
    def appflow(self) -> ServiceFactory[AppflowClient]:
        return ServiceFactory("appflow", self)

    @property
    def appintegrations(self) -> ServiceFactory[AppIntegrationsServiceClient]:
        return ServiceFactory("appintegrations", self)

    @property
    def application_autoscaling(self) -> ServiceFactory[ApplicationAutoScalingClient]:
        return ServiceFactory("application-autoscaling", self)

    @property
    def application_insights(self) -> ServiceFactory[ApplicationInsightsClient]:
        return ServiceFactory("application-insights", self)

    @property
    def application_signals(self) -> ServiceFactory[CloudWatchApplicationSignalsClient]:
        return ServiceFactory("application-signals", self)

    @property
    def applicationcostprofiler(self) -> ServiceFactory[ApplicationCostProfilerClient]:
        return ServiceFactory("applicationcostprofiler", self)

    @property
    def appmesh(self) -> ServiceFactory[AppMeshClient]:
        return ServiceFactory("appmesh", self)

    @property
    def apprunner(self) -> ServiceFactory[AppRunnerClient]:
        return ServiceFactory("apprunner", self)

    @property
    def appstream(self) -> ServiceFactory[AppStreamClient]:
        return ServiceFactory("appstream", self)

    @property
    def appsync(self) -> ServiceFactory[AppSyncClient]:
        return ServiceFactory("appsync", self)

    @property
    def apptest(self) -> ServiceFactory[MainframeModernizationApplicationTestingClient]:
        return ServiceFactory("apptest", self)

    @property
    def arc_zonal_shift(self) -> ServiceFactory[ARCZonalShiftClient]:
        return ServiceFactory("arc-zonal-shift", self)

    @property
    def artifact(self) -> ServiceFactory[ArtifactClient]:
        return ServiceFactory("artifact", self)

    @property
    def athena(self) -> ServiceFactory[AthenaClient]:
        return ServiceFactory("athena", self)

    @property
    def auditmanager(self) -> ServiceFactory[AuditManagerClient]:
        return ServiceFactory("auditmanager", self)

    @property
    def autoscaling(self) -> ServiceFactory[AutoScalingClient]:
        return ServiceFactory("autoscaling", self)

    @property
    def autoscaling_plans(self) -> ServiceFactory[AutoScalingPlansClient]:
        return ServiceFactory("autoscaling-plans", self)

    @property
    def b2bi(self) -> ServiceFactory[B2BIClient]:
        return ServiceFactory("b2bi", self)

    @property
    def backup(self) -> ServiceFactory[BackupClient]:
        return ServiceFactory("backup", self)

    @property
    def backup_gateway(self) -> ServiceFactory[BackupGatewayClient]:
        return ServiceFactory("backup-gateway", self)

    @property
    def backupsearch(self) -> ServiceFactory[BackupSearchClient]:
        return ServiceFactory("backupsearch", self)

    @property
    def batch(self) -> ServiceFactory[BatchClient]:
        return ServiceFactory("batch", self)

    @property
    def bcm_data_exports(self) -> ServiceFactory[BillingandCostManagementDataExportsClient]:
        return ServiceFactory("bcm-data-exports", self)

    @property
    def bcm_pricing_calculator(
        self,
    ) -> ServiceFactory[BillingandCostManagementPricingCalculatorClient]:
        return ServiceFactory("bcm-pricing-calculator", self)

    @property
    def bedrock(self) -> ServiceFactory[BedrockClient]:
        return ServiceFactory("bedrock", self)

    @property
    def bedrock_agent(self) -> ServiceFactory[AgentsforBedrockClient]:
        return ServiceFactory("bedrock-agent", self)

    @property
    def bedrock_agent_runtime(self) -> ServiceFactory[AgentsforBedrockRuntimeClient]:
        return ServiceFactory("bedrock-agent-runtime", self)

    @property
    def bedrock_data_automation(self) -> ServiceFactory[DataAutomationforBedrockClient]:
        return ServiceFactory("bedrock-data-automation", self)

    @property
    def bedrock_data_automation_runtime(
        self,
    ) -> ServiceFactory[RuntimeforBedrockDataAutomationClient]:
        return ServiceFactory("bedrock-data-automation-runtime", self)

    @property
    def bedrock_runtime(self) -> ServiceFactory[BedrockRuntimeClient]:
        return ServiceFactory("bedrock-runtime", self)

    @property
    def billing(self) -> ServiceFactory[BillingClient]:
        return ServiceFactory("billing", self)

    @property
    def billingconductor(self) -> ServiceFactory[BillingConductorClient]:
        return ServiceFactory("billingconductor", self)

    @property
    def braket(self) -> ServiceFactory[BraketClient]:
        return ServiceFactory("braket", self)

    @property
    def budgets(self) -> ServiceFactory[BudgetsClient]:
        return ServiceFactory("budgets", self)

    @property
    def ce(self) -> ServiceFactory[CostExplorerClient]:
        return ServiceFactory("ce", self)

    @property
    def chatbot(self) -> ServiceFactory[ChatbotClient]:
        return ServiceFactory("chatbot", self)

    @property
    def chime(self) -> ServiceFactory[ChimeClient]:
        return ServiceFactory("chime", self)

    @property
    def chime_sdk_identity(self) -> ServiceFactory[ChimeSDKIdentityClient]:
        return ServiceFactory("chime-sdk-identity", self)

    @property
    def chime_sdk_media_pipelines(self) -> ServiceFactory[ChimeSDKMediaPipelinesClient]:
        return ServiceFactory("chime-sdk-media-pipelines", self)

    @property
    def chime_sdk_meetings(self) -> ServiceFactory[ChimeSDKMeetingsClient]:
        return ServiceFactory("chime-sdk-meetings", self)

    @property
    def chime_sdk_messaging(self) -> ServiceFactory[ChimeSDKMessagingClient]:
        return ServiceFactory("chime-sdk-messaging", self)

    @property
    def chime_sdk_voice(self) -> ServiceFactory[ChimeSDKVoiceClient]:
        return ServiceFactory("chime-sdk-voice", self)

    @property
    def cleanrooms(self) -> ServiceFactory[CleanRoomsServiceClient]:
        return ServiceFactory("cleanrooms", self)

    @property
    def cleanroomsml(self) -> ServiceFactory[CleanRoomsMLClient]:
        return ServiceFactory("cleanroomsml", self)

    @property
    def cloud9(self) -> ServiceFactory[Cloud9Client]:
        return ServiceFactory("cloud9", self)

    @property
    def cloudcontrol(self) -> ServiceFactory[CloudControlApiClient]:
        return ServiceFactory("cloudcontrol", self)

    @property
    def clouddirectory(self) -> ServiceFactory[CloudDirectoryClient]:
        return ServiceFactory("clouddirectory", self)

    @property
    def cloudformation(
        self,
    ) -> ServiceResourceFactory[CloudFormationClient, CloudFormationServiceResource]:
        return ServiceResourceFactory("cloudformation", self)

    @property
    def cloudfront(self) -> ServiceFactory[CloudFrontClient]:
        return ServiceFactory("cloudfront", self)

    @property
    def cloudfront_keyvaluestore(self) -> ServiceFactory[CloudFrontKeyValueStoreClient]:
        return ServiceFactory("cloudfront-keyvaluestore", self)

    @property
    def cloudhsm(self) -> ServiceFactory[CloudHSMClient]:
        return ServiceFactory("cloudhsm", self)

    @property
    def cloudhsmv2(self) -> ServiceFactory[CloudHSMV2Client]:
        return ServiceFactory("cloudhsmv2", self)

    @property
    def cloudsearch(self) -> ServiceFactory[CloudSearchClient]:
        return ServiceFactory("cloudsearch", self)

    @property
    def cloudsearchdomain(self) -> ServiceFactory[CloudSearchDomainClient]:
        return ServiceFactory("cloudsearchdomain", self)

    @property
    def cloudtrail(self) -> ServiceFactory[CloudTrailClient]:
        return ServiceFactory("cloudtrail", self)

    @property
    def cloudtrail_data(self) -> ServiceFactory[CloudTrailDataServiceClient]:
        return ServiceFactory("cloudtrail-data", self)

    @property
    def cloudwatch(self) -> ServiceResourceFactory[CloudWatchClient, CloudWatchServiceResource]:
        return ServiceResourceFactory("cloudwatch", self)

    @property
    def codeartifact(self) -> ServiceFactory[CodeArtifactClient]:
        return ServiceFactory("codeartifact", self)

    @property
    def codebuild(self) -> ServiceFactory[CodeBuildClient]:
        return ServiceFactory("codebuild", self)

    @property
    def codecatalyst(self) -> ServiceFactory[CodeCatalystClient]:
        return ServiceFactory("codecatalyst", self)

    @property
    def codecommit(self) -> ServiceFactory[CodeCommitClient]:
        return ServiceFactory("codecommit", self)

    @property
    def codeconnections(self) -> ServiceFactory[CodeConnectionsClient]:
        return ServiceFactory("codeconnections", self)

    @property
    def codedeploy(self) -> ServiceFactory[CodeDeployClient]:
        return ServiceFactory("codedeploy", self)

    @property
    def codeguru_reviewer(self) -> ServiceFactory[CodeGuruReviewerClient]:
        return ServiceFactory("codeguru-reviewer", self)

    @property
    def codeguru_security(self) -> ServiceFactory[CodeGuruSecurityClient]:
        return ServiceFactory("codeguru-security", self)

    @property
    def codeguruprofiler(self) -> ServiceFactory[CodeGuruProfilerClient]:
        return ServiceFactory("codeguruprofiler", self)

    @property
    def codepipeline(self) -> ServiceFactory[CodePipelineClient]:
        return ServiceFactory("codepipeline", self)

    @property
    def codestar_connections(self) -> ServiceFactory[CodeStarconnectionsClient]:
        return ServiceFactory("codestar-connections", self)

    @property
    def codestar_notifications(self) -> ServiceFactory[CodeStarNotificationsClient]:
        return ServiceFactory("codestar-notifications", self)

    @property
    def cognito_identity(self) -> ServiceFactory[CognitoIdentityClient]:
        return ServiceFactory("cognito-identity", self)

    @property
    def cognito_idp(self) -> ServiceFactory[CognitoIdentityProviderClient]:
        return ServiceFactory("cognito-idp", self)

    @property
    def cognito_sync(self) -> ServiceFactory[CognitoSyncClient]:
        return ServiceFactory("cognito-sync", self)

    @property
    def comprehend(self) -> ServiceFactory[ComprehendClient]:
        return ServiceFactory("comprehend", self)

    @property
    def comprehendmedical(self) -> ServiceFactory[ComprehendMedicalClient]:
        return ServiceFactory("comprehendmedical", self)

    @property
    def compute_optimizer(self) -> ServiceFactory[ComputeOptimizerClient]:
        return ServiceFactory("compute-optimizer", self)

    @property
    def config(self) -> ServiceFactory[ConfigServiceClient]:
        return ServiceFactory("config", self)

    @property
    def connect(self) -> ServiceFactory[ConnectClient]:
        return ServiceFactory("connect", self)

    @property
    def connect_contact_lens(self) -> ServiceFactory[ConnectContactLensClient]:
        return ServiceFactory("connect-contact-lens", self)

    @property
    def connectcampaigns(self) -> ServiceFactory[ConnectCampaignServiceClient]:
        return ServiceFactory("connectcampaigns", self)

    @property
    def connectcampaignsv2(self) -> ServiceFactory[ConnectCampaignServiceV2Client]:
        return ServiceFactory("connectcampaignsv2", self)

    @property
    def connectcases(self) -> ServiceFactory[ConnectCasesClient]:
        return ServiceFactory("connectcases", self)

    @property
    def connectparticipant(self) -> ServiceFactory[ConnectParticipantClient]:
        return ServiceFactory("connectparticipant", self)

    @property
    def controlcatalog(self) -> ServiceFactory[ControlCatalogClient]:
        return ServiceFactory("controlcatalog", self)

    @property
    def controltower(self) -> ServiceFactory[ControlTowerClient]:
        return ServiceFactory("controltower", self)

    @property
    def cost_optimization_hub(self) -> ServiceFactory[CostOptimizationHubClient]:
        return ServiceFactory("cost-optimization-hub", self)

    @property
    def cur(self) -> ServiceFactory[CostandUsageReportServiceClient]:
        return ServiceFactory("cur", self)

    @property
    def customer_profiles(self) -> ServiceFactory[CustomerProfilesClient]:
        return ServiceFactory("customer-profiles", self)

    @property
    def databrew(self) -> ServiceFactory[GlueDataBrewClient]:
        return ServiceFactory("databrew", self)

    @property
    def dataexchange(self) -> ServiceFactory[DataExchangeClient]:
        return ServiceFactory("dataexchange", self)

    @property
    def datapipeline(self) -> ServiceFactory[DataPipelineClient]:
        return ServiceFactory("datapipeline", self)

    @property
    def datasync(self) -> ServiceFactory[DataSyncClient]:
        return ServiceFactory("datasync", self)

    @property
    def datazone(self) -> ServiceFactory[DataZoneClient]:
        return ServiceFactory("datazone", self)

    @property
    def dax(self) -> ServiceFactory[DAXClient]:
        return ServiceFactory("dax", self)

    @property
    def deadline(self) -> ServiceFactory[DeadlineCloudClient]:
        return ServiceFactory("deadline", self)

    @property
    def detective(self) -> ServiceFactory[DetectiveClient]:
        return ServiceFactory("detective", self)

    @property
    def devicefarm(self) -> ServiceFactory[DeviceFarmClient]:
        return ServiceFactory("devicefarm", self)

    @property
    def devops_guru(self) -> ServiceFactory[DevOpsGuruClient]:
        return ServiceFactory("devops-guru", self)

    @property
    def directconnect(self) -> ServiceFactory[DirectConnectClient]:
        return ServiceFactory("directconnect", self)

    @property
    def discovery(self) -> ServiceFactory[ApplicationDiscoveryServiceClient]:
        return ServiceFactory("discovery", self)

    @property
    def dlm(self) -> ServiceFactory[DLMClient]:
        return ServiceFactory("dlm", self)

    @property
    def dms(self) -> ServiceFactory[DatabaseMigrationServiceClient]:
        return ServiceFactory("dms", self)

    @property
    def docdb(self) -> ServiceFactory[DocDBClient]:
        return ServiceFactory("docdb", self)

    @property
    def docdb_elastic(self) -> ServiceFactory[DocDBElasticClient]:
        return ServiceFactory("docdb-elastic", self)

    @property
    def drs(self) -> ServiceFactory[DrsClient]:
        return ServiceFactory("drs", self)

    @property
    def ds(self) -> ServiceFactory[DirectoryServiceClient]:
        return ServiceFactory("ds", self)

    @property
    def ds_data(self) -> ServiceFactory[DirectoryServiceDataClient]:
        return ServiceFactory("ds-data", self)

    @property
    def dsql(self) -> ServiceFactory[AuroraDSQLClient]:
        return ServiceFactory("dsql", self)

    @property
    def dynamodb(self) -> ServiceResourceFactory[DynamoDBClient, DynamoDBServiceResource]:
        return ServiceResourceFactory("dynamodb", self)

    @property
    def dynamodbstreams(self) -> ServiceFactory[DynamoDBStreamsClient]:
        return ServiceFactory("dynamodbstreams", self)

    @property
    def ebs(self) -> ServiceFactory[EBSClient]:
        return ServiceFactory("ebs", self)

    @property
    def ec2(self) -> ServiceResourceFactory[EC2Client, EC2ServiceResource]:
        return ServiceResourceFactory("ec2", self)

    @property
    def ec2_instance_connect(self) -> ServiceFactory[EC2InstanceConnectClient]:
        return ServiceFactory("ec2-instance-connect", self)

    @property
    def ecr(self) -> ServiceFactory[ECRClient]:
        return ServiceFactory("ecr", self)

    @property
    def ecr_public(self) -> ServiceFactory[ECRPublicClient]:
        return ServiceFactory("ecr-public", self)

    @property
    def ecs(self) -> ServiceFactory[ECSClient]:
        return ServiceFactory("ecs", self)

    @property
    def efs(self) -> ServiceFactory[EFSClient]:
        return ServiceFactory("efs", self)

    @property
    def eks(self) -> ServiceFactory[EKSClient]:
        return ServiceFactory("eks", self)

    @property
    def eks_auth(self) -> ServiceFactory[EKSAuthClient]:
        return ServiceFactory("eks-auth", self)

    @property
    def elasticache(self) -> ServiceFactory[ElastiCacheClient]:
        return ServiceFactory("elasticache", self)

    @property
    def elasticbeanstalk(self) -> ServiceFactory[ElasticBeanstalkClient]:
        return ServiceFactory("elasticbeanstalk", self)

    @property
    def elastictranscoder(self) -> ServiceFactory[ElasticTranscoderClient]:
        return ServiceFactory("elastictranscoder", self)

    @property
    def elb(self) -> ServiceFactory[ElasticLoadBalancingClient]:
        return ServiceFactory("elb", self)

    @property
    def elbv2(self) -> ServiceFactory[ElasticLoadBalancingv2Client]:
        return ServiceFactory("elbv2", self)

    @property
    def emr(self) -> ServiceFactory[EMRClient]:
        return ServiceFactory("emr", self)

    @property
    def emr_containers(self) -> ServiceFactory[EMRContainersClient]:
        return ServiceFactory("emr-containers", self)

    @property
    def emr_serverless(self) -> ServiceFactory[EMRServerlessClient]:
        return ServiceFactory("emr-serverless", self)

    @property
    def entityresolution(self) -> ServiceFactory[EntityResolutionClient]:
        return ServiceFactory("entityresolution", self)

    @property
    def es(self) -> ServiceFactory[ElasticsearchServiceClient]:
        return ServiceFactory("es", self)

    @property
    def eventbridge(self) -> ServiceFactory[EventBridgeClient]:
        return ServiceFactory("events", self)

    @property
    def evidently(self) -> ServiceFactory[CloudWatchEvidentlyClient]:
        return ServiceFactory("evidently", self)

    @property
    def finspace(self) -> ServiceFactory[FinspaceClient]:
        return ServiceFactory("finspace", self)

    @property
    def finspace_data(self) -> ServiceFactory[FinSpaceDataClient]:
        return ServiceFactory("finspace-data", self)

    @property
    def firehose(self) -> ServiceFactory[FirehoseClient]:
        return ServiceFactory("firehose", self)

    @property
    def fis(self) -> ServiceFactory[FISClient]:
        return ServiceFactory("fis", self)

    @property
    def fms(self) -> ServiceFactory[FMSClient]:
        return ServiceFactory("fms", self)

    @property
    def forecast(self) -> ServiceFactory[ForecastServiceClient]:
        return ServiceFactory("forecast", self)

    @property
    def forecastquery(self) -> ServiceFactory[ForecastQueryServiceClient]:
        return ServiceFactory("forecastquery", self)

    @property
    def frauddetector(self) -> ServiceFactory[FraudDetectorClient]:
        return ServiceFactory("frauddetector", self)

    @property
    def freetier(self) -> ServiceFactory[FreeTierClient]:
        return ServiceFactory("freetier", self)

    @property
    def fsx(self) -> ServiceFactory[FSxClient]:
        return ServiceFactory("fsx", self)

    @property
    def gamelift(self) -> ServiceFactory[GameLiftClient]:
        return ServiceFactory("gamelift", self)

    @property
    def geo_maps(self) -> ServiceFactory[LocationServiceMapsV2Client]:
        return ServiceFactory("geo-maps", self)

    @property
    def geo_places(self) -> ServiceFactory[LocationServicePlacesV2Client]:
        return ServiceFactory("geo-places", self)

    @property
    def geo_routes(self) -> ServiceFactory[LocationServiceRoutesV2Client]:
        return ServiceFactory("geo-routes", self)

    @property
    def glacier(self) -> ServiceResourceFactory[GlacierClient, GlacierServiceResource]:
        return ServiceResourceFactory("glacier", self)

    @property
    def globalaccelerator(self) -> ServiceFactory[GlobalAcceleratorClient]:
        return ServiceFactory("globalaccelerator", self)

    @property
    def glue(self) -> ServiceFactory[GlueClient]:
        return ServiceFactory("glue", self)

    @property
    def grafana(self) -> ServiceFactory[ManagedGrafanaClient]:
        return ServiceFactory("grafana", self)

    @property
    def greengrass(self) -> ServiceFactory[GreengrassClient]:
        return ServiceFactory("greengrass", self)

    @property
    def greengrassv2(self) -> ServiceFactory[GreengrassV2Client]:
        return ServiceFactory("greengrassv2", self)

    @property
    def groundstation(self) -> ServiceFactory[GroundStationClient]:
        return ServiceFactory("groundstation", self)

    @property
    def guardduty(self) -> ServiceFactory[GuardDutyClient]:
        return ServiceFactory("guardduty", self)

    @property
    def health(self) -> ServiceFactory[HealthClient]:
        return ServiceFactory("health", self)

    @property
    def healthlake(self) -> ServiceFactory[HealthLakeClient]:
        return ServiceFactory("healthlake", self)

    @property
    def iam(self) -> ServiceResourceFactory[IAMClient, IAMServiceResource]:
        return ServiceResourceFactory("iam", self)

    @property
    def identitystore(self) -> ServiceFactory[IdentityStoreClient]:
        return ServiceFactory("identitystore", self)

    @property
    def imagebuilder(self) -> ServiceFactory[ImagebuilderClient]:
        return ServiceFactory("imagebuilder", self)

    @property
    def importexport(self) -> ServiceFactory[ImportExportClient]:
        return ServiceFactory("importexport", self)

    @property
    def inspector(self) -> ServiceFactory[InspectorClient]:
        return ServiceFactory("inspector", self)

    @property
    def inspector_scan(self) -> ServiceFactory[InspectorscanClient]:
        return ServiceFactory("inspector-scan", self)

    @property
    def inspector2(self) -> ServiceFactory[Inspector2Client]:
        return ServiceFactory("inspector2", self)

    @property
    def internetmonitor(self) -> ServiceFactory[CloudWatchInternetMonitorClient]:
        return ServiceFactory("internetmonitor", self)

    @property
    def invoicing(self) -> ServiceFactory[InvoicingClient]:
        return ServiceFactory("invoicing", self)

    @property
    def iot(self) -> ServiceFactory[IoTClient]:
        return ServiceFactory("iot", self)

    @property
    def iot_data(self) -> ServiceFactory[IoTDataPlaneClient]:
        return ServiceFactory("iot-data", self)

    @property
    def iot_jobs_data(self) -> ServiceFactory[IoTJobsDataPlaneClient]:
        return ServiceFactory("iot-jobs-data", self)

    @property
    def iotanalytics(self) -> ServiceFactory[IoTAnalyticsClient]:
        return ServiceFactory("iotanalytics", self)

    @property
    def iotdeviceadvisor(self) -> ServiceFactory[IoTDeviceAdvisorClient]:
        return ServiceFactory("iotdeviceadvisor", self)

    @property
    def iotevents(self) -> ServiceFactory[IoTEventsClient]:
        return ServiceFactory("iotevents", self)

    @property
    def iotevents_data(self) -> ServiceFactory[IoTEventsDataClient]:
        return ServiceFactory("iotevents-data", self)

    @property
    def iotfleethub(self) -> ServiceFactory[IoTFleetHubClient]:
        return ServiceFactory("iotfleethub", self)

    @property
    def iotfleetwise(self) -> ServiceFactory[IoTFleetWiseClient]:
        return ServiceFactory("iotfleetwise", self)

    @property
    def iotsecuretunneling(self) -> ServiceFactory[IoTSecureTunnelingClient]:
        return ServiceFactory("iotsecuretunneling", self)

    @property
    def iotsitewise(self) -> ServiceFactory[IoTSiteWiseClient]:
        return ServiceFactory("iotsitewise", self)

    @property
    def iotthingsgraph(self) -> ServiceFactory[IoTThingsGraphClient]:
        return ServiceFactory("iotthingsgraph", self)

    @property
    def iottwinmaker(self) -> ServiceFactory[IoTTwinMakerClient]:
        return ServiceFactory("iottwinmaker", self)

    @property
    def iotwireless(self) -> ServiceFactory[IoTWirelessClient]:
        return ServiceFactory("iotwireless", self)

    @property
    def ivs(self) -> ServiceFactory[IVSClient]:
        return ServiceFactory("ivs", self)

    @property
    def ivs_realtime(self) -> ServiceFactory[IvsrealtimeClient]:
        return ServiceFactory("ivs-realtime", self)

    @property
    def ivschat(self) -> ServiceFactory[IvschatClient]:
        return ServiceFactory("ivschat", self)

    @property
    def kafka(self) -> ServiceFactory[KafkaClient]:
        return ServiceFactory("kafka", self)

    @property
    def kafkaconnect(self) -> ServiceFactory[KafkaConnectClient]:
        return ServiceFactory("kafkaconnect", self)

    @property
    def kendra(self) -> ServiceFactory[KendraClient]:
        return ServiceFactory("kendra", self)

    @property
    def kendra_ranking(self) -> ServiceFactory[KendraRankingClient]:
        return ServiceFactory("kendra-ranking", self)

    @property
    def keyspaces(self) -> ServiceFactory[KeyspacesClient]:
        return ServiceFactory("keyspaces", self)

    @property
    def kinesis(self) -> ServiceFactory[KinesisClient]:
        return ServiceFactory("kinesis", self)

    @property
    def kinesis_video_archived_media(self) -> ServiceFactory[KinesisVideoArchivedMediaClient]:
        return ServiceFactory("kinesis-video-archived-media", self)

    @property
    def kinesis_video_media(self) -> ServiceFactory[KinesisVideoMediaClient]:
        return ServiceFactory("kinesis-video-media", self)

    @property
    def kinesis_video_signaling(self) -> ServiceFactory[KinesisVideoSignalingChannelsClient]:
        return ServiceFactory("kinesis-video-signaling", self)

    @property
    def kinesis_video_webrtc_storage(self) -> ServiceFactory[KinesisVideoWebRTCStorageClient]:
        return ServiceFactory("kinesis-video-webrtc-storage", self)

    @property
    def kinesisanalytics(self) -> ServiceFactory[KinesisAnalyticsClient]:
        return ServiceFactory("kinesisanalytics", self)

    @property
    def kinesisanalyticsv2(self) -> ServiceFactory[KinesisAnalyticsV2Client]:
        return ServiceFactory("kinesisanalyticsv2", self)

    @property
    def kinesisvideo(self) -> ServiceFactory[KinesisVideoClient]:
        return ServiceFactory("kinesisvideo", self)

    @property
    def kms(self) -> ServiceFactory[KMSClient]:
        return ServiceFactory("kms", self)

    @property
    def lakeformation(self) -> ServiceFactory[LakeFormationClient]:
        return ServiceFactory("lakeformation", self)

    @property
    def lambda_(self) -> ServiceFactory[LambdaClient]:
        return ServiceFactory("lambda", self)

    @property
    def launch_wizard(self) -> ServiceFactory[LaunchWizardClient]:
        return ServiceFactory("launch-wizard", self)

    @property
    def lex_models(self) -> ServiceFactory[LexModelBuildingServiceClient]:
        return ServiceFactory("lex-models", self)

    @property
    def lex_runtime(self) -> ServiceFactory[LexRuntimeServiceClient]:
        return ServiceFactory("lex-runtime", self)

    @property
    def lexv2_models(self) -> ServiceFactory[LexModelsV2Client]:
        return ServiceFactory("lexv2-models", self)

    @property
    def lexv2_runtime(self) -> ServiceFactory[LexRuntimeV2Client]:
        return ServiceFactory("lexv2-runtime", self)

    @property
    def license_manager(self) -> ServiceFactory[LicenseManagerClient]:
        return ServiceFactory("license-manager", self)

    @property
    def license_manager_linux_subscriptions(
        self,
    ) -> ServiceFactory[LicenseManagerLinuxSubscriptionsClient]:
        return ServiceFactory("license-manager-linux-subscriptions", self)

    @property
    def license_manager_user_subscriptions(
        self,
    ) -> ServiceFactory[LicenseManagerUserSubscriptionsClient]:
        return ServiceFactory("license-manager-user-subscriptions", self)

    @property
    def lightsail(self) -> ServiceFactory[LightsailClient]:
        return ServiceFactory("lightsail", self)

    @property
    def location(self) -> ServiceFactory[LocationServiceClient]:
        return ServiceFactory("location", self)

    @property
    def logs(self) -> ServiceFactory[CloudWatchLogsClient]:
        return ServiceFactory("logs", self)

    @property
    def lookoutequipment(self) -> ServiceFactory[LookoutEquipmentClient]:
        return ServiceFactory("lookoutequipment", self)

    @property
    def lookoutmetrics(self) -> ServiceFactory[LookoutMetricsClient]:
        return ServiceFactory("lookoutmetrics", self)

    @property
    def lookoutvision(self) -> ServiceFactory[LookoutforVisionClient]:
        return ServiceFactory("lookoutvision", self)

    @property
    def m2(self) -> ServiceFactory[MainframeModernizationClient]:
        return ServiceFactory("m2", self)

    @property
    def machinelearning(self) -> ServiceFactory[MachineLearningClient]:
        return ServiceFactory("machinelearning", self)

    @property
    def macie2(self) -> ServiceFactory[Macie2Client]:
        return ServiceFactory("macie2", self)

    @property
    def mailmanager(self) -> ServiceFactory[MailManagerClient]:
        return ServiceFactory("mailmanager", self)

    @property
    def managedblockchain(self) -> ServiceFactory[ManagedBlockchainClient]:
        return ServiceFactory("managedblockchain", self)

    @property
    def managedblockchain_query(self) -> ServiceFactory[ManagedBlockchainQueryClient]:
        return ServiceFactory("managedblockchain-query", self)

    @property
    def marketplace_agreement(self) -> ServiceFactory[AgreementServiceClient]:
        return ServiceFactory("marketplace-agreement", self)

    @property
    def marketplace_catalog(self) -> ServiceFactory[MarketplaceCatalogClient]:
        return ServiceFactory("marketplace-catalog", self)

    @property
    def marketplace_deployment(self) -> ServiceFactory[MarketplaceDeploymentServiceClient]:
        return ServiceFactory("marketplace-deployment", self)

    @property
    def marketplace_entitlement(self) -> ServiceFactory[MarketplaceEntitlementServiceClient]:
        return ServiceFactory("marketplace-entitlement", self)

    @property
    def marketplace_reporting(self) -> ServiceFactory[MarketplaceReportingServiceClient]:
        return ServiceFactory("marketplace-reporting", self)

    @property
    def marketplacecommerceanalytics(self) -> ServiceFactory[MarketplaceCommerceAnalyticsClient]:
        return ServiceFactory("marketplacecommerceanalytics", self)

    @property
    def mediaconnect(self) -> ServiceFactory[MediaConnectClient]:
        return ServiceFactory("mediaconnect", self)

    @property
    def mediaconvert(self) -> ServiceFactory[MediaConvertClient]:
        return ServiceFactory("mediaconvert", self)

    @property
    def medialive(self) -> ServiceFactory[MediaLiveClient]:
        return ServiceFactory("medialive", self)

    @property
    def mediapackage(self) -> ServiceFactory[MediaPackageClient]:
        return ServiceFactory("mediapackage", self)

    @property
    def mediapackage_vod(self) -> ServiceFactory[MediaPackageVodClient]:
        return ServiceFactory("mediapackage-vod", self)

    @property
    def mediapackagev2(self) -> ServiceFactory[Mediapackagev2Client]:
        return ServiceFactory("mediapackagev2", self)

    @property
    def mediastore(self) -> ServiceFactory[MediaStoreClient]:
        return ServiceFactory("mediastore", self)

    @property
    def mediastore_data(self) -> ServiceFactory[MediaStoreDataClient]:
        return ServiceFactory("mediastore-data", self)

    @property
    def mediatailor(self) -> ServiceFactory[MediaTailorClient]:
        return ServiceFactory("mediatailor", self)

    @property
    def medical_imaging(self) -> ServiceFactory[HealthImagingClient]:
        return ServiceFactory("medical-imaging", self)

    @property
    def memorydb(self) -> ServiceFactory[MemoryDBClient]:
        return ServiceFactory("memorydb", self)

    @property
    def meteringmarketplace(self) -> ServiceFactory[MarketplaceMeteringClient]:
        return ServiceFactory("meteringmarketplace", self)

    @property
    def mgh(self) -> ServiceFactory[MigrationHubClient]:
        return ServiceFactory("mgh", self)

    @property
    def mgn(self) -> ServiceFactory[MgnClient]:
        return ServiceFactory("mgn", self)

    @property
    def migration_hub_refactor_spaces(self) -> ServiceFactory[MigrationHubRefactorSpacesClient]:
        return ServiceFactory("migration-hub-refactor-spaces", self)

    @property
    def migrationhub_config(self) -> ServiceFactory[MigrationHubConfigClient]:
        return ServiceFactory("migrationhub-config", self)

    @property
    def migrationhuborchestrator(self) -> ServiceFactory[MigrationHubOrchestratorClient]:
        return ServiceFactory("migrationhuborchestrator", self)

    @property
    def migrationhubstrategy(self) -> ServiceFactory[MigrationHubStrategyRecommendationsClient]:
        return ServiceFactory("migrationhubstrategy", self)

    @property
    def mq(self) -> ServiceFactory[MQClient]:
        return ServiceFactory("mq", self)

    @property
    def mturk(self) -> ServiceFactory[MTurkClient]:
        return ServiceFactory("mturk", self)

    @property
    def mwaa(self) -> ServiceFactory[MWAAClient]:
        return ServiceFactory("mwaa", self)

    @property
    def neptune(self) -> ServiceFactory[NeptuneClient]:
        return ServiceFactory("neptune", self)

    @property
    def neptune_graph(self) -> ServiceFactory[NeptuneGraphClient]:
        return ServiceFactory("neptune-graph", self)

    @property
    def neptunedata(self) -> ServiceFactory[NeptuneDataClient]:
        return ServiceFactory("neptunedata", self)

    @property
    def network_firewall(self) -> ServiceFactory[NetworkFirewallClient]:
        return ServiceFactory("network-firewall", self)

    @property
    def networkflowmonitor(self) -> ServiceFactory[NetworkFlowMonitorClient]:
        return ServiceFactory("networkflowmonitor", self)

    @property
    def networkmanager(self) -> ServiceFactory[NetworkManagerClient]:
        return ServiceFactory("networkmanager", self)

    @property
    def networkmonitor(self) -> ServiceFactory[CloudWatchNetworkMonitorClient]:
        return ServiceFactory("networkmonitor", self)

    @property
    def notifications(self) -> ServiceFactory[UserNotificationsClient]:
        return ServiceFactory("notifications", self)

    @property
    def notificationscontacts(self) -> ServiceFactory[UserNotificationsContactsClient]:
        return ServiceFactory("notificationscontacts", self)

    @property
    def oam(self) -> ServiceFactory[CloudWatchObservabilityAccessManagerClient]:
        return ServiceFactory("oam", self)

    @property
    def observabilityadmin(self) -> ServiceFactory[CloudWatchObservabilityAdminServiceClient]:
        return ServiceFactory("observabilityadmin", self)

    @property
    def omics(self) -> ServiceFactory[OmicsClient]:
        return ServiceFactory("omics", self)

    @property
    def opensearch(self) -> ServiceFactory[OpenSearchServiceClient]:
        return ServiceFactory("opensearch", self)

    @property
    def opensearchserverless(self) -> ServiceFactory[OpenSearchServiceServerlessClient]:
        return ServiceFactory("opensearchserverless", self)

    @property
    def opsworks(self) -> ServiceResourceFactory[OpsWorksClient, OpsWorksServiceResource]:
        return ServiceResourceFactory("opsworks", self)

    @property
    def opsworkscm(self) -> ServiceFactory[OpsWorksCMClient]:
        return ServiceFactory("opsworkscm", self)

    @property
    def organizations(self) -> ServiceFactory[OrganizationsClient]:
        return ServiceFactory("organizations", self)

    @property
    def osis(self) -> ServiceFactory[OpenSearchIngestionClient]:
        return ServiceFactory("osis", self)

    @property
    def outposts(self) -> ServiceFactory[OutpostsClient]:
        return ServiceFactory("outposts", self)

    @property
    def panorama(self) -> ServiceFactory[PanoramaClient]:
        return ServiceFactory("panorama", self)

    @property
    def partnercentral_selling(self) -> ServiceFactory[PartnerCentralSellingAPIClient]:
        return ServiceFactory("partnercentral-selling", self)

    @property
    def payment_cryptography(self) -> ServiceFactory[PaymentCryptographyControlPlaneClient]:
        return ServiceFactory("payment-cryptography", self)

    @property
    def payment_cryptography_data(self) -> ServiceFactory[PaymentCryptographyDataPlaneClient]:
        return ServiceFactory("payment-cryptography-data", self)

    @property
    def pca_connector_ad(self) -> ServiceFactory[PcaConnectorAdClient]:
        return ServiceFactory("pca-connector-ad", self)

    @property
    def pca_connector_scep(self) -> ServiceFactory[PrivateCAConnectorforSCEPClient]:
        return ServiceFactory("pca-connector-scep", self)

    @property
    def pcs(self) -> ServiceFactory[ParallelComputingServiceClient]:
        return ServiceFactory("pcs", self)

    @property
    def personalize(self) -> ServiceFactory[PersonalizeClient]:
        return ServiceFactory("personalize", self)

    @property
    def personalize_events(self) -> ServiceFactory[PersonalizeEventsClient]:
        return ServiceFactory("personalize-events", self)

    @property
    def personalize_runtime(self) -> ServiceFactory[PersonalizeRuntimeClient]:
        return ServiceFactory("personalize-runtime", self)

    @property
    def pi(self) -> ServiceFactory[PIClient]:
        return ServiceFactory("pi", self)

    @property
    def pinpoint(self) -> ServiceFactory[PinpointClient]:
        return ServiceFactory("pinpoint", self)

    @property
    def pinpoint_email(self) -> ServiceFactory[PinpointEmailClient]:
        return ServiceFactory("pinpoint-email", self)

    @property
    def pinpoint_sms_voice(self) -> ServiceFactory[PinpointSMSVoiceClient]:
        return ServiceFactory("pinpoint-sms-voice", self)

    @property
    def pinpoint_sms_voice_v2(self) -> ServiceFactory[PinpointSMSVoiceV2Client]:
        return ServiceFactory("pinpoint-sms-voice-v2", self)

    @property
    def pipes(self) -> ServiceFactory[EventBridgePipesClient]:
        return ServiceFactory("pipes", self)

    @property
    def polly(self) -> ServiceFactory[PollyClient]:
        return ServiceFactory("polly", self)

    @property
    def pricing(self) -> ServiceFactory[PricingClient]:
        return ServiceFactory("pricing", self)

    @property
    def privatenetworks(self) -> ServiceFactory[Private5GClient]:
        return ServiceFactory("privatenetworks", self)

    @property
    def proton(self) -> ServiceFactory[ProtonClient]:
        return ServiceFactory("proton", self)

    @property
    def qapps(self) -> ServiceFactory[QAppsClient]:
        return ServiceFactory("qapps", self)

    @property
    def qbusiness(self) -> ServiceFactory[QBusinessClient]:
        return ServiceFactory("qbusiness", self)

    @property
    def qconnect(self) -> ServiceFactory[QConnectClient]:
        return ServiceFactory("qconnect", self)

    @property
    def qldb(self) -> ServiceFactory[QLDBClient]:
        return ServiceFactory("qldb", self)

    @property
    def qldb_session(self) -> ServiceFactory[QLDBSessionClient]:
        return ServiceFactory("qldb-session", self)

    @property
    def quicksight(self) -> ServiceFactory[QuickSightClient]:
        return ServiceFactory("quicksight", self)

    @property
    def ram(self) -> ServiceFactory[RAMClient]:
        return ServiceFactory("ram", self)

    @property
    def rbin(self) -> ServiceFactory[RecycleBinClient]:
        return ServiceFactory("rbin", self)

    @property
    def rds(self) -> ServiceFactory[RDSClient]:
        return ServiceFactory("rds", self)

    @property
    def rds_data(self) -> ServiceFactory[RDSDataServiceClient]:
        return ServiceFactory("rds-data", self)

    @property
    def redshift(self) -> ServiceFactory[RedshiftClient]:
        return ServiceFactory("redshift", self)

    @property
    def redshift_data(self) -> ServiceFactory[RedshiftDataAPIServiceClient]:
        return ServiceFactory("redshift-data", self)

    @property
    def redshift_serverless(self) -> ServiceFactory[RedshiftServerlessClient]:
        return ServiceFactory("redshift-serverless", self)

    @property
    def rekognition(self) -> ServiceFactory[RekognitionClient]:
        return ServiceFactory("rekognition", self)

    @property
    def repostspace(self) -> ServiceFactory[RePostPrivateClient]:
        return ServiceFactory("repostspace", self)

    @property
    def resiliencehub(self) -> ServiceFactory[ResilienceHubClient]:
        return ServiceFactory("resiliencehub", self)

    @property
    def resource_explorer_2(self) -> ServiceFactory[ResourceExplorerClient]:
        return ServiceFactory("resource-explorer-2", self)

    @property
    def resource_groups(self) -> ServiceFactory[ResourceGroupsClient]:
        return ServiceFactory("resource-groups", self)

    @property
    def resourcegroupstaggingapi(self) -> ServiceFactory[ResourceGroupsTaggingAPIClient]:
        return ServiceFactory("resourcegroupstaggingapi", self)

    @property
    def robomaker(self) -> ServiceFactory[RoboMakerClient]:
        return ServiceFactory("robomaker", self)

    @property
    def rolesanywhere(self) -> ServiceFactory[IAMRolesAnywhereClient]:
        return ServiceFactory("rolesanywhere", self)

    @property
    def route53(self) -> ServiceFactory[Route53Client]:
        return ServiceFactory("route53", self)

    @property
    def route53_recovery_cluster(self) -> ServiceFactory[Route53RecoveryClusterClient]:
        return ServiceFactory("route53-recovery-cluster", self)

    @property
    def route53_recovery_control_config(self) -> ServiceFactory[Route53RecoveryControlConfigClient]:
        return ServiceFactory("route53-recovery-control-config", self)

    @property
    def route53_recovery_readiness(self) -> ServiceFactory[Route53RecoveryReadinessClient]:
        return ServiceFactory("route53-recovery-readiness", self)

    @property
    def route53domains(self) -> ServiceFactory[Route53DomainsClient]:
        return ServiceFactory("route53domains", self)

    @property
    def route53profiles(self) -> ServiceFactory[Route53ProfilesClient]:
        return ServiceFactory("route53profiles", self)

    @property
    def route53resolver(self) -> ServiceFactory[Route53ResolverClient]:
        return ServiceFactory("route53resolver", self)

    @property
    def rum(self) -> ServiceFactory[CloudWatchRUMClient]:
        return ServiceFactory("rum", self)

    @property
    def s3(self) -> ServiceResourceFactory[S3Client, S3ServiceResource]:
        return ServiceResourceFactory("s3", self)

    @property
    def s3control(self) -> ServiceFactory[S3ControlClient]:
        return ServiceFactory("s3control", self)

    @property
    def s3outposts(self) -> ServiceFactory[S3OutpostsClient]:
        return ServiceFactory("s3outposts", self)

    @property
    def s3tables(self) -> ServiceFactory[S3TablesClient]:
        return ServiceFactory("s3tables", self)

    @property
    def sagemaker(self) -> ServiceFactory[SageMakerClient]:
        return ServiceFactory("sagemaker", self)

    @property
    def sagemaker_a2i_runtime(self) -> ServiceFactory[AugmentedAIRuntimeClient]:
        return ServiceFactory("sagemaker-a2i-runtime", self)

    @property
    def sagemaker_edge(self) -> ServiceFactory[SagemakerEdgeManagerClient]:
        return ServiceFactory("sagemaker-edge", self)

    @property
    def sagemaker_featurestore_runtime(self) -> ServiceFactory[SageMakerFeatureStoreRuntimeClient]:
        return ServiceFactory("sagemaker-featurestore-runtime", self)

    @property
    def sagemaker_geospatial(self) -> ServiceFactory[SageMakergeospatialcapabilitiesClient]:
        return ServiceFactory("sagemaker-geospatial", self)

    @property
    def sagemaker_metrics(self) -> ServiceFactory[SageMakerMetricsClient]:
        return ServiceFactory("sagemaker-metrics", self)

    @property
    def sagemaker_runtime(self) -> ServiceFactory[SageMakerRuntimeClient]:
        return ServiceFactory("sagemaker-runtime", self)

    @property
    def savingsplans(self) -> ServiceFactory[SavingsPlansClient]:
        return ServiceFactory("savingsplans", self)

    @property
    def scheduler(self) -> ServiceFactory[EventBridgeSchedulerClient]:
        return ServiceFactory("scheduler", self)

    @property
    def schemas(self) -> ServiceFactory[SchemasClient]:
        return ServiceFactory("schemas", self)

    @property
    def sdb(self) -> ServiceFactory[SimpleDBClient]:
        return ServiceFactory("sdb", self)

    @property
    def secretsmanager(self) -> ServiceFactory[SecretsManagerClient]:
        return ServiceFactory("secretsmanager", self)

    @property
    def security_ir(self) -> ServiceFactory[SecurityIncidentResponseClient]:
        return ServiceFactory("security-ir", self)

    @property
    def securityhub(self) -> ServiceFactory[SecurityHubClient]:
        return ServiceFactory("securityhub", self)

    @property
    def securitylake(self) -> ServiceFactory[SecurityLakeClient]:
        return ServiceFactory("securitylake", self)

    @property
    def serverlessrepo(self) -> ServiceFactory[ServerlessApplicationRepositoryClient]:
        return ServiceFactory("serverlessrepo", self)

    @property
    def service_quotas(self) -> ServiceFactory[ServiceQuotasClient]:
        return ServiceFactory("service-quotas", self)

    @property
    def servicecatalog(self) -> ServiceFactory[ServiceCatalogClient]:
        return ServiceFactory("servicecatalog", self)

    @property
    def servicecatalog_appregistry(self) -> ServiceFactory[AppRegistryClient]:
        return ServiceFactory("servicecatalog-appregistry", self)

    @property
    def servicediscovery(self) -> ServiceFactory[ServiceDiscoveryClient]:
        return ServiceFactory("servicediscovery", self)

    @property
    def ses(self) -> ServiceFactory[SESClient]:
        return ServiceFactory("ses", self)

    @property
    def sesv2(self) -> ServiceFactory[SESV2Client]:
        return ServiceFactory("sesv2", self)

    @property
    def shield(self) -> ServiceFactory[ShieldClient]:
        return ServiceFactory("shield", self)

    @property
    def signer(self) -> ServiceFactory[SignerClient]:
        return ServiceFactory("signer", self)

    @property
    def simspaceweaver(self) -> ServiceFactory[SimSpaceWeaverClient]:
        return ServiceFactory("simspaceweaver", self)

    @property
    def sms(self) -> ServiceFactory[SMSClient]:
        return ServiceFactory("sms", self)

    @property
    def sms_voice(self) -> ServiceFactory[SMSVoiceClient]:
        return ServiceFactory("sms-voice", self)

    @property
    def snow_device_management(self) -> ServiceFactory[SnowDeviceManagementClient]:
        return ServiceFactory("snow-device-management", self)

    @property
    def snowball(self) -> ServiceFactory[SnowballClient]:
        return ServiceFactory("snowball", self)

    @property
    def sns(self) -> ServiceResourceFactory[SNSClient, SNSServiceResource]:
        return ServiceResourceFactory("sns", self)

    @property
    def socialmessaging(self) -> ServiceFactory[EndUserMessagingSocialClient]:
        return ServiceFactory("socialmessaging", self)

    @property
    def sqs(self) -> ServiceResourceFactory[SQSClient, SQSServiceResource]:
        return ServiceResourceFactory("sqs", self)

    @property
    def ssm(self) -> ServiceFactory[SSMClient]:
        return ServiceFactory("ssm", self)

    @property
    def ssm_contacts(self) -> ServiceFactory[SSMContactsClient]:
        return ServiceFactory("ssm-contacts", self)

    @property
    def ssm_incidents(self) -> ServiceFactory[SSMIncidentsClient]:
        return ServiceFactory("ssm-incidents", self)

    @property
    def ssm_quicksetup(self) -> ServiceFactory[SystemsManagerQuickSetupClient]:
        return ServiceFactory("ssm-quicksetup", self)

    @property
    def ssm_sap(self) -> ServiceFactory[SsmSapClient]:
        return ServiceFactory("ssm-sap", self)

    @property
    def sso(self) -> ServiceFactory[SSOClient]:
        return ServiceFactory("sso", self)

    @property
    def sso_admin(self) -> ServiceFactory[SSOAdminClient]:
        return ServiceFactory("sso-admin", self)

    @property
    def sso_oidc(self) -> ServiceFactory[SSOOIDCClient]:
        return ServiceFactory("sso-oidc", self)

    @property
    def stepfunctions(self) -> ServiceFactory[SFNClient]:
        return ServiceFactory("stepfunctions", self)

    @property
    def storagegateway(self) -> ServiceFactory[StorageGatewayClient]:
        return ServiceFactory("storagegateway", self)

    @property
    def sts(self) -> ServiceFactory[STSClient]:
        return ServiceFactory("sts", self)

    @property
    def supplychain(self) -> ServiceFactory[SupplyChainClient]:
        return ServiceFactory("supplychain", self)

    @property
    def support(self) -> ServiceFactory[SupportClient]:
        return ServiceFactory("support", self)

    @property
    def support_app(self) -> ServiceFactory[SupportAppClient]:
        return ServiceFactory("support-app", self)

    @property
    def swf(self) -> ServiceFactory[SWFClient]:
        return ServiceFactory("swf", self)

    @property
    def synthetics(self) -> ServiceFactory[SyntheticsClient]:
        return ServiceFactory("synthetics", self)

    @property
    def taxsettings(self) -> ServiceFactory[TaxSettingsClient]:
        return ServiceFactory("taxsettings", self)

    @property
    def textract(self) -> ServiceFactory[TextractClient]:
        return ServiceFactory("textract", self)

    @property
    def timestream_influxdb(self) -> ServiceFactory[TimestreamInfluxDBClient]:
        return ServiceFactory("timestream-influxdb", self)

    @property
    def timestream_query(self) -> ServiceFactory[TimestreamQueryClient]:
        return ServiceFactory("timestream-query", self)

    @property
    def timestream_write(self) -> ServiceFactory[TimestreamWriteClient]:
        return ServiceFactory("timestream-write", self)

    @property
    def tnb(self) -> ServiceFactory[TelcoNetworkBuilderClient]:
        return ServiceFactory("tnb", self)

    @property
    def transcribe(self) -> ServiceFactory[TranscribeServiceClient]:
        return ServiceFactory("transcribe", self)

    @property
    def transfer(self) -> ServiceFactory[TransferClient]:
        return ServiceFactory("transfer", self)

    @property
    def translate(self) -> ServiceFactory[TranslateClient]:
        return ServiceFactory("translate", self)

    @property
    def trustedadvisor(self) -> ServiceFactory[TrustedAdvisorPublicAPIClient]:
        return ServiceFactory("trustedadvisor", self)

    @property
    def verifiedpermissions(self) -> ServiceFactory[VerifiedPermissionsClient]:
        return ServiceFactory("verifiedpermissions", self)

    @property
    def voice_id(self) -> ServiceFactory[VoiceIDClient]:
        return ServiceFactory("voice-id", self)

    @property
    def vpc_lattice(self) -> ServiceFactory[VPCLatticeClient]:
        return ServiceFactory("vpc-lattice", self)

    @property
    def waf(self) -> ServiceFactory[WAFClient]:
        return ServiceFactory("waf", self)

    @property
    def waf_regional(self) -> ServiceFactory[WAFRegionalClient]:
        return ServiceFactory("waf-regional", self)

    @property
    def wafv2(self) -> ServiceFactory[WAFV2Client]:
        return ServiceFactory("wafv2", self)

    @property
    def wellarchitected(self) -> ServiceFactory[WellArchitectedClient]:
        return ServiceFactory("wellarchitected", self)

    @property
    def wisdom(self) -> ServiceFactory[ConnectWisdomServiceClient]:
        return ServiceFactory("wisdom", self)

    @property
    def workdocs(self) -> ServiceFactory[WorkDocsClient]:
        return ServiceFactory("workdocs", self)

    @property
    def workmail(self) -> ServiceFactory[WorkMailClient]:
        return ServiceFactory("workmail", self)

    @property
    def workmailmessageflow(self) -> ServiceFactory[WorkMailMessageFlowClient]:
        return ServiceFactory("workmailmessageflow", self)

    @property
    def workspaces(self) -> ServiceFactory[WorkSpacesClient]:
        return ServiceFactory("workspaces", self)

    @property
    def workspaces_thin_client(self) -> ServiceFactory[WorkSpacesThinClientClient]:
        return ServiceFactory("workspaces-thin-client", self)

    @property
    def workspaces_web(self) -> ServiceFactory[WorkSpacesWebClient]:
        return ServiceFactory("workspaces-web", self)

    @property
    def xray(self) -> ServiceFactory[XRayClient]:
        return ServiceFactory("xray", self)
