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

from boto34.aioboto3.services.accessanalyzer import AccessAnalyzerService
from boto34.aioboto3.services.account import AccountService
from boto34.aioboto3.services.acm import ACMService
from boto34.aioboto3.services.acm_pca import ACMPCAService
from boto34.aioboto3.services.amp import PrometheusServiceService
from boto34.aioboto3.services.amplify import AmplifyService
from boto34.aioboto3.services.amplifybackend import AmplifyBackendService
from boto34.aioboto3.services.amplifyuibuilder import AmplifyUIBuilderService
from boto34.aioboto3.services.apigateway import APIGatewayService
from boto34.aioboto3.services.apigatewaymanagementapi import ApiGatewayManagementApiService
from boto34.aioboto3.services.apigatewayv2 import ApiGatewayV2Service
from boto34.aioboto3.services.appconfig import AppConfigService
from boto34.aioboto3.services.appconfigdata import AppConfigDataService
from boto34.aioboto3.services.appfabric import AppFabricService
from boto34.aioboto3.services.appflow import AppflowService
from boto34.aioboto3.services.appintegrations import AppIntegrationsServiceService
from boto34.aioboto3.services.application_autoscaling import ApplicationAutoScalingService
from boto34.aioboto3.services.application_insights import ApplicationInsightsService
from boto34.aioboto3.services.application_signals import CloudWatchApplicationSignalsService
from boto34.aioboto3.services.applicationcostprofiler import ApplicationCostProfilerService
from boto34.aioboto3.services.appmesh import AppMeshService
from boto34.aioboto3.services.apprunner import AppRunnerService
from boto34.aioboto3.services.appstream import AppStreamService
from boto34.aioboto3.services.appsync import AppSyncService
from boto34.aioboto3.services.apptest import MainframeModernizationApplicationTestingService
from boto34.aioboto3.services.arc_zonal_shift import ARCZonalShiftService
from boto34.aioboto3.services.artifact import ArtifactService
from boto34.aioboto3.services.athena import AthenaService
from boto34.aioboto3.services.auditmanager import AuditManagerService
from boto34.aioboto3.services.autoscaling import AutoScalingService
from boto34.aioboto3.services.autoscaling_plans import AutoScalingPlansService
from boto34.aioboto3.services.b2bi import B2BIService
from boto34.aioboto3.services.backup import BackupService
from boto34.aioboto3.services.backup_gateway import BackupGatewayService
from boto34.aioboto3.services.backupsearch import BackupSearchService
from boto34.aioboto3.services.batch import BatchService
from boto34.aioboto3.services.bcm_data_exports import BillingandCostManagementDataExportsService
from boto34.aioboto3.services.bcm_pricing_calculator import (
    BillingandCostManagementPricingCalculatorService,
)
from boto34.aioboto3.services.bedrock import BedrockService
from boto34.aioboto3.services.bedrock_agent import AgentsforBedrockService
from boto34.aioboto3.services.bedrock_agent_runtime import AgentsforBedrockRuntimeService
from boto34.aioboto3.services.bedrock_data_automation import DataAutomationforBedrockService
from boto34.aioboto3.services.bedrock_data_automation_runtime import (
    RuntimeforBedrockDataAutomationService,
)
from boto34.aioboto3.services.bedrock_runtime import BedrockRuntimeService
from boto34.aioboto3.services.billing import BillingService
from boto34.aioboto3.services.billingconductor import BillingConductorService
from boto34.aioboto3.services.braket import BraketService
from boto34.aioboto3.services.budgets import BudgetsService
from boto34.aioboto3.services.ce import CostExplorerService
from boto34.aioboto3.services.chatbot import ChatbotService
from boto34.aioboto3.services.chime import ChimeService
from boto34.aioboto3.services.chime_sdk_identity import ChimeSDKIdentityService
from boto34.aioboto3.services.chime_sdk_media_pipelines import ChimeSDKMediaPipelinesService
from boto34.aioboto3.services.chime_sdk_meetings import ChimeSDKMeetingsService
from boto34.aioboto3.services.chime_sdk_messaging import ChimeSDKMessagingService
from boto34.aioboto3.services.chime_sdk_voice import ChimeSDKVoiceService
from boto34.aioboto3.services.cleanrooms import CleanRoomsServiceService
from boto34.aioboto3.services.cleanroomsml import CleanRoomsMLService
from boto34.aioboto3.services.cloud9 import Cloud9Service
from boto34.aioboto3.services.cloudcontrol import CloudControlApiService
from boto34.aioboto3.services.clouddirectory import CloudDirectoryService
from boto34.aioboto3.services.cloudformation import CloudFormationService
from boto34.aioboto3.services.cloudfront import CloudFrontService
from boto34.aioboto3.services.cloudfront_keyvaluestore import CloudFrontKeyValueStoreService
from boto34.aioboto3.services.cloudhsm import CloudHSMService
from boto34.aioboto3.services.cloudhsmv2 import CloudHSMV2Service
from boto34.aioboto3.services.cloudsearch import CloudSearchService
from boto34.aioboto3.services.cloudsearchdomain import CloudSearchDomainService
from boto34.aioboto3.services.cloudtrail import CloudTrailService
from boto34.aioboto3.services.cloudtrail_data import CloudTrailDataServiceService
from boto34.aioboto3.services.cloudwatch import CloudWatchService
from boto34.aioboto3.services.codeartifact import CodeArtifactService
from boto34.aioboto3.services.codebuild import CodeBuildService
from boto34.aioboto3.services.codecatalyst import CodeCatalystService
from boto34.aioboto3.services.codecommit import CodeCommitService
from boto34.aioboto3.services.codeconnections import CodeConnectionsService
from boto34.aioboto3.services.codedeploy import CodeDeployService
from boto34.aioboto3.services.codeguru_reviewer import CodeGuruReviewerService
from boto34.aioboto3.services.codeguru_security import CodeGuruSecurityService
from boto34.aioboto3.services.codeguruprofiler import CodeGuruProfilerService
from boto34.aioboto3.services.codepipeline import CodePipelineService
from boto34.aioboto3.services.codestar_connections import CodeStarconnectionsService
from boto34.aioboto3.services.codestar_notifications import CodeStarNotificationsService
from boto34.aioboto3.services.cognito_identity import CognitoIdentityService
from boto34.aioboto3.services.cognito_idp import CognitoIdentityProviderService
from boto34.aioboto3.services.cognito_sync import CognitoSyncService
from boto34.aioboto3.services.comprehend import ComprehendService
from boto34.aioboto3.services.comprehendmedical import ComprehendMedicalService
from boto34.aioboto3.services.compute_optimizer import ComputeOptimizerService
from boto34.aioboto3.services.config import ConfigServiceService
from boto34.aioboto3.services.connect import ConnectService
from boto34.aioboto3.services.connect_contact_lens import ConnectContactLensService
from boto34.aioboto3.services.connectcampaigns import ConnectCampaignServiceService
from boto34.aioboto3.services.connectcampaignsv2 import ConnectCampaignServiceV2Service
from boto34.aioboto3.services.connectcases import ConnectCasesService
from boto34.aioboto3.services.connectparticipant import ConnectParticipantService
from boto34.aioboto3.services.controlcatalog import ControlCatalogService
from boto34.aioboto3.services.controltower import ControlTowerService
from boto34.aioboto3.services.cost_optimization_hub import CostOptimizationHubService
from boto34.aioboto3.services.cur import CostandUsageReportServiceService
from boto34.aioboto3.services.customer_profiles import CustomerProfilesService
from boto34.aioboto3.services.databrew import GlueDataBrewService
from boto34.aioboto3.services.dataexchange import DataExchangeService
from boto34.aioboto3.services.datapipeline import DataPipelineService
from boto34.aioboto3.services.datasync import DataSyncService
from boto34.aioboto3.services.datazone import DataZoneService
from boto34.aioboto3.services.dax import DAXService
from boto34.aioboto3.services.deadline import DeadlineCloudService
from boto34.aioboto3.services.detective import DetectiveService
from boto34.aioboto3.services.devicefarm import DeviceFarmService
from boto34.aioboto3.services.devops_guru import DevOpsGuruService
from boto34.aioboto3.services.directconnect import DirectConnectService
from boto34.aioboto3.services.discovery import ApplicationDiscoveryServiceService
from boto34.aioboto3.services.dlm import DLMService
from boto34.aioboto3.services.dms import DatabaseMigrationServiceService
from boto34.aioboto3.services.docdb import DocDBService
from boto34.aioboto3.services.docdb_elastic import DocDBElasticService
from boto34.aioboto3.services.drs import DrsService
from boto34.aioboto3.services.ds import DirectoryServiceService
from boto34.aioboto3.services.ds_data import DirectoryServiceDataService
from boto34.aioboto3.services.dsql import AuroraDSQLService
from boto34.aioboto3.services.dynamodb import DynamoDBService
from boto34.aioboto3.services.dynamodbstreams import DynamoDBStreamsService
from boto34.aioboto3.services.ebs import EBSService
from boto34.aioboto3.services.ec2 import EC2Service
from boto34.aioboto3.services.ec2_instance_connect import EC2InstanceConnectService
from boto34.aioboto3.services.ecr import ECRService
from boto34.aioboto3.services.ecr_public import ECRPublicService
from boto34.aioboto3.services.ecs import ECSService
from boto34.aioboto3.services.efs import EFSService
from boto34.aioboto3.services.eks import EKSService
from boto34.aioboto3.services.eks_auth import EKSAuthService
from boto34.aioboto3.services.elasticache import ElastiCacheService
from boto34.aioboto3.services.elasticbeanstalk import ElasticBeanstalkService
from boto34.aioboto3.services.elastictranscoder import ElasticTranscoderService
from boto34.aioboto3.services.elb import ElasticLoadBalancingService
from boto34.aioboto3.services.elbv2 import ElasticLoadBalancingv2Service
from boto34.aioboto3.services.emr import EMRService
from boto34.aioboto3.services.emr_containers import EMRContainersService
from boto34.aioboto3.services.emr_serverless import EMRServerlessService
from boto34.aioboto3.services.entityresolution import EntityResolutionService
from boto34.aioboto3.services.es import ElasticsearchServiceService
from boto34.aioboto3.services.events import EventBridgeService
from boto34.aioboto3.services.evidently import CloudWatchEvidentlyService
from boto34.aioboto3.services.finspace import FinspaceService
from boto34.aioboto3.services.finspace_data import FinSpaceDataService
from boto34.aioboto3.services.firehose import FirehoseService
from boto34.aioboto3.services.fis import FISService
from boto34.aioboto3.services.fms import FMSService
from boto34.aioboto3.services.forecast import ForecastServiceService
from boto34.aioboto3.services.forecastquery import ForecastQueryServiceService
from boto34.aioboto3.services.frauddetector import FraudDetectorService
from boto34.aioboto3.services.freetier import FreeTierService
from boto34.aioboto3.services.fsx import FSxService
from boto34.aioboto3.services.gamelift import GameLiftService
from boto34.aioboto3.services.geo_maps import LocationServiceMapsV2Service
from boto34.aioboto3.services.geo_places import LocationServicePlacesV2Service
from boto34.aioboto3.services.geo_routes import LocationServiceRoutesV2Service
from boto34.aioboto3.services.glacier import GlacierService
from boto34.aioboto3.services.globalaccelerator import GlobalAcceleratorService
from boto34.aioboto3.services.glue import GlueService
from boto34.aioboto3.services.grafana import ManagedGrafanaService
from boto34.aioboto3.services.greengrass import GreengrassService
from boto34.aioboto3.services.greengrassv2 import GreengrassV2Service
from boto34.aioboto3.services.groundstation import GroundStationService
from boto34.aioboto3.services.guardduty import GuardDutyService
from boto34.aioboto3.services.health import HealthService
from boto34.aioboto3.services.healthlake import HealthLakeService
from boto34.aioboto3.services.iam import IAMService
from boto34.aioboto3.services.identitystore import IdentityStoreService
from boto34.aioboto3.services.imagebuilder import ImagebuilderService
from boto34.aioboto3.services.importexport import ImportExportService
from boto34.aioboto3.services.inspector import InspectorService
from boto34.aioboto3.services.inspector2 import Inspector2Service
from boto34.aioboto3.services.inspector_scan import InspectorscanService
from boto34.aioboto3.services.internetmonitor import CloudWatchInternetMonitorService
from boto34.aioboto3.services.invoicing import InvoicingService
from boto34.aioboto3.services.iot import IoTService
from boto34.aioboto3.services.iot_data import IoTDataPlaneService
from boto34.aioboto3.services.iot_jobs_data import IoTJobsDataPlaneService
from boto34.aioboto3.services.iotanalytics import IoTAnalyticsService
from boto34.aioboto3.services.iotdeviceadvisor import IoTDeviceAdvisorService
from boto34.aioboto3.services.iotevents import IoTEventsService
from boto34.aioboto3.services.iotevents_data import IoTEventsDataService
from boto34.aioboto3.services.iotfleethub import IoTFleetHubService
from boto34.aioboto3.services.iotfleetwise import IoTFleetWiseService
from boto34.aioboto3.services.iotsecuretunneling import IoTSecureTunnelingService
from boto34.aioboto3.services.iotsitewise import IoTSiteWiseService
from boto34.aioboto3.services.iotthingsgraph import IoTThingsGraphService
from boto34.aioboto3.services.iottwinmaker import IoTTwinMakerService
from boto34.aioboto3.services.iotwireless import IoTWirelessService
from boto34.aioboto3.services.ivs import IVSService
from boto34.aioboto3.services.ivs_realtime import IvsrealtimeService
from boto34.aioboto3.services.ivschat import IvschatService
from boto34.aioboto3.services.kafka import KafkaService
from boto34.aioboto3.services.kafkaconnect import KafkaConnectService
from boto34.aioboto3.services.kendra import KendraService
from boto34.aioboto3.services.kendra_ranking import KendraRankingService
from boto34.aioboto3.services.keyspaces import KeyspacesService
from boto34.aioboto3.services.kinesis import KinesisService
from boto34.aioboto3.services.kinesis_video_archived_media import KinesisVideoArchivedMediaService
from boto34.aioboto3.services.kinesis_video_media import KinesisVideoMediaService
from boto34.aioboto3.services.kinesis_video_signaling import KinesisVideoSignalingChannelsService
from boto34.aioboto3.services.kinesis_video_webrtc_storage import KinesisVideoWebRTCStorageService
from boto34.aioboto3.services.kinesisanalytics import KinesisAnalyticsService
from boto34.aioboto3.services.kinesisanalyticsv2 import KinesisAnalyticsV2Service
from boto34.aioboto3.services.kinesisvideo import KinesisVideoService
from boto34.aioboto3.services.kms import KMSService
from boto34.aioboto3.services.lakeformation import LakeFormationService
from boto34.aioboto3.services.lambda_ import LambdaService
from boto34.aioboto3.services.launch_wizard import LaunchWizardService
from boto34.aioboto3.services.lex_models import LexModelBuildingServiceService
from boto34.aioboto3.services.lex_runtime import LexRuntimeServiceService
from boto34.aioboto3.services.lexv2_models import LexModelsV2Service
from boto34.aioboto3.services.lexv2_runtime import LexRuntimeV2Service
from boto34.aioboto3.services.license_manager import LicenseManagerService
from boto34.aioboto3.services.license_manager_linux_subscriptions import (
    LicenseManagerLinuxSubscriptionsService,
)
from boto34.aioboto3.services.license_manager_user_subscriptions import (
    LicenseManagerUserSubscriptionsService,
)
from boto34.aioboto3.services.lightsail import LightsailService
from boto34.aioboto3.services.location import LocationServiceService
from boto34.aioboto3.services.logs import CloudWatchLogsService
from boto34.aioboto3.services.lookoutequipment import LookoutEquipmentService
from boto34.aioboto3.services.lookoutmetrics import LookoutMetricsService
from boto34.aioboto3.services.lookoutvision import LookoutforVisionService
from boto34.aioboto3.services.m2 import MainframeModernizationService
from boto34.aioboto3.services.machinelearning import MachineLearningService
from boto34.aioboto3.services.macie2 import Macie2Service
from boto34.aioboto3.services.mailmanager import MailManagerService
from boto34.aioboto3.services.managedblockchain import ManagedBlockchainService
from boto34.aioboto3.services.managedblockchain_query import ManagedBlockchainQueryService
from boto34.aioboto3.services.marketplace_agreement import AgreementServiceService
from boto34.aioboto3.services.marketplace_catalog import MarketplaceCatalogService
from boto34.aioboto3.services.marketplace_deployment import MarketplaceDeploymentServiceService
from boto34.aioboto3.services.marketplace_entitlement import MarketplaceEntitlementServiceService
from boto34.aioboto3.services.marketplace_reporting import MarketplaceReportingServiceService
from boto34.aioboto3.services.marketplacecommerceanalytics import (
    MarketplaceCommerceAnalyticsService,
)
from boto34.aioboto3.services.mediaconnect import MediaConnectService
from boto34.aioboto3.services.mediaconvert import MediaConvertService
from boto34.aioboto3.services.medialive import MediaLiveService
from boto34.aioboto3.services.mediapackage import MediaPackageService
from boto34.aioboto3.services.mediapackage_vod import MediaPackageVodService
from boto34.aioboto3.services.mediapackagev2 import Mediapackagev2Service
from boto34.aioboto3.services.mediastore import MediaStoreService
from boto34.aioboto3.services.mediastore_data import MediaStoreDataService
from boto34.aioboto3.services.mediatailor import MediaTailorService
from boto34.aioboto3.services.medical_imaging import HealthImagingService
from boto34.aioboto3.services.memorydb import MemoryDBService
from boto34.aioboto3.services.meteringmarketplace import MarketplaceMeteringService
from boto34.aioboto3.services.mgh import MigrationHubService
from boto34.aioboto3.services.mgn import MgnService
from boto34.aioboto3.services.migration_hub_refactor_spaces import MigrationHubRefactorSpacesService
from boto34.aioboto3.services.migrationhub_config import MigrationHubConfigService
from boto34.aioboto3.services.migrationhuborchestrator import MigrationHubOrchestratorService
from boto34.aioboto3.services.migrationhubstrategy import MigrationHubStrategyRecommendationsService
from boto34.aioboto3.services.mq import MQService
from boto34.aioboto3.services.mturk import MTurkService
from boto34.aioboto3.services.mwaa import MWAAService
from boto34.aioboto3.services.neptune import NeptuneService
from boto34.aioboto3.services.neptune_graph import NeptuneGraphService
from boto34.aioboto3.services.neptunedata import NeptuneDataService
from boto34.aioboto3.services.network_firewall import NetworkFirewallService
from boto34.aioboto3.services.networkflowmonitor import NetworkFlowMonitorService
from boto34.aioboto3.services.networkmanager import NetworkManagerService
from boto34.aioboto3.services.networkmonitor import CloudWatchNetworkMonitorService
from boto34.aioboto3.services.notifications import UserNotificationsService
from boto34.aioboto3.services.notificationscontacts import UserNotificationsContactsService
from boto34.aioboto3.services.oam import CloudWatchObservabilityAccessManagerService
from boto34.aioboto3.services.observabilityadmin import CloudWatchObservabilityAdminServiceService
from boto34.aioboto3.services.omics import OmicsService
from boto34.aioboto3.services.opensearch import OpenSearchServiceService
from boto34.aioboto3.services.opensearchserverless import OpenSearchServiceServerlessService
from boto34.aioboto3.services.opsworks import OpsWorksService
from boto34.aioboto3.services.opsworkscm import OpsWorksCMService
from boto34.aioboto3.services.organizations import OrganizationsService
from boto34.aioboto3.services.osis import OpenSearchIngestionService
from boto34.aioboto3.services.outposts import OutpostsService
from boto34.aioboto3.services.panorama import PanoramaService
from boto34.aioboto3.services.partnercentral_selling import PartnerCentralSellingAPIService
from boto34.aioboto3.services.payment_cryptography import PaymentCryptographyControlPlaneService
from boto34.aioboto3.services.payment_cryptography_data import PaymentCryptographyDataPlaneService
from boto34.aioboto3.services.pca_connector_ad import PcaConnectorAdService
from boto34.aioboto3.services.pca_connector_scep import PrivateCAConnectorforSCEPService
from boto34.aioboto3.services.pcs import ParallelComputingServiceService
from boto34.aioboto3.services.personalize import PersonalizeService
from boto34.aioboto3.services.personalize_events import PersonalizeEventsService
from boto34.aioboto3.services.personalize_runtime import PersonalizeRuntimeService
from boto34.aioboto3.services.pi import PIService
from boto34.aioboto3.services.pinpoint import PinpointService
from boto34.aioboto3.services.pinpoint_email import PinpointEmailService
from boto34.aioboto3.services.pinpoint_sms_voice import PinpointSMSVoiceService
from boto34.aioboto3.services.pinpoint_sms_voice_v2 import PinpointSMSVoiceV2Service
from boto34.aioboto3.services.pipes import EventBridgePipesService
from boto34.aioboto3.services.polly import PollyService
from boto34.aioboto3.services.pricing import PricingService
from boto34.aioboto3.services.privatenetworks import Private5GService
from boto34.aioboto3.services.proton import ProtonService
from boto34.aioboto3.services.qapps import QAppsService
from boto34.aioboto3.services.qbusiness import QBusinessService
from boto34.aioboto3.services.qconnect import QConnectService
from boto34.aioboto3.services.qldb import QLDBService
from boto34.aioboto3.services.qldb_session import QLDBSessionService
from boto34.aioboto3.services.quicksight import QuickSightService
from boto34.aioboto3.services.ram import RAMService
from boto34.aioboto3.services.rbin import RecycleBinService
from boto34.aioboto3.services.rds import RDSService
from boto34.aioboto3.services.rds_data import RDSDataServiceService
from boto34.aioboto3.services.redshift import RedshiftService
from boto34.aioboto3.services.redshift_data import RedshiftDataAPIServiceService
from boto34.aioboto3.services.redshift_serverless import RedshiftServerlessService
from boto34.aioboto3.services.rekognition import RekognitionService
from boto34.aioboto3.services.repostspace import RePostPrivateService
from boto34.aioboto3.services.resiliencehub import ResilienceHubService
from boto34.aioboto3.services.resource_explorer_2 import ResourceExplorerService
from boto34.aioboto3.services.resource_groups import ResourceGroupsService
from boto34.aioboto3.services.resourcegroupstaggingapi import ResourceGroupsTaggingAPIService
from boto34.aioboto3.services.robomaker import RoboMakerService
from boto34.aioboto3.services.rolesanywhere import IAMRolesAnywhereService
from boto34.aioboto3.services.route53 import Route53Service
from boto34.aioboto3.services.route53_recovery_cluster import Route53RecoveryClusterService
from boto34.aioboto3.services.route53_recovery_control_config import (
    Route53RecoveryControlConfigService,
)
from boto34.aioboto3.services.route53_recovery_readiness import Route53RecoveryReadinessService
from boto34.aioboto3.services.route53domains import Route53DomainsService
from boto34.aioboto3.services.route53profiles import Route53ProfilesService
from boto34.aioboto3.services.route53resolver import Route53ResolverService
from boto34.aioboto3.services.rum import CloudWatchRUMService
from boto34.aioboto3.services.s3 import S3Service
from boto34.aioboto3.services.s3control import S3ControlService
from boto34.aioboto3.services.s3outposts import S3OutpostsService
from boto34.aioboto3.services.s3tables import S3TablesService
from boto34.aioboto3.services.sagemaker import SageMakerService
from boto34.aioboto3.services.sagemaker_a2i_runtime import AugmentedAIRuntimeService
from boto34.aioboto3.services.sagemaker_edge import SagemakerEdgeManagerService
from boto34.aioboto3.services.sagemaker_featurestore_runtime import (
    SageMakerFeatureStoreRuntimeService,
)
from boto34.aioboto3.services.sagemaker_geospatial import SageMakergeospatialcapabilitiesService
from boto34.aioboto3.services.sagemaker_metrics import SageMakerMetricsService
from boto34.aioboto3.services.sagemaker_runtime import SageMakerRuntimeService
from boto34.aioboto3.services.savingsplans import SavingsPlansService
from boto34.aioboto3.services.scheduler import EventBridgeSchedulerService
from boto34.aioboto3.services.schemas import SchemasService
from boto34.aioboto3.services.sdb import SimpleDBService
from boto34.aioboto3.services.secretsmanager import SecretsManagerService
from boto34.aioboto3.services.security_ir import SecurityIncidentResponseService
from boto34.aioboto3.services.securityhub import SecurityHubService
from boto34.aioboto3.services.securitylake import SecurityLakeService
from boto34.aioboto3.services.serverlessrepo import ServerlessApplicationRepositoryService
from boto34.aioboto3.services.service_quotas import ServiceQuotasService
from boto34.aioboto3.services.servicecatalog import ServiceCatalogService
from boto34.aioboto3.services.servicecatalog_appregistry import AppRegistryService
from boto34.aioboto3.services.servicediscovery import ServiceDiscoveryService
from boto34.aioboto3.services.ses import SESService
from boto34.aioboto3.services.sesv2 import SESV2Service
from boto34.aioboto3.services.shield import ShieldService
from boto34.aioboto3.services.signer import SignerService
from boto34.aioboto3.services.simspaceweaver import SimSpaceWeaverService
from boto34.aioboto3.services.sms import SMSService
from boto34.aioboto3.services.sms_voice import SMSVoiceService
from boto34.aioboto3.services.snow_device_management import SnowDeviceManagementService
from boto34.aioboto3.services.snowball import SnowballService
from boto34.aioboto3.services.sns import SNSService
from boto34.aioboto3.services.socialmessaging import EndUserMessagingSocialService
from boto34.aioboto3.services.sqs import SQSService
from boto34.aioboto3.services.ssm import SSMService
from boto34.aioboto3.services.ssm_contacts import SSMContactsService
from boto34.aioboto3.services.ssm_incidents import SSMIncidentsService
from boto34.aioboto3.services.ssm_quicksetup import SystemsManagerQuickSetupService
from boto34.aioboto3.services.ssm_sap import SsmSapService
from boto34.aioboto3.services.sso import SSOService
from boto34.aioboto3.services.sso_admin import SSOAdminService
from boto34.aioboto3.services.sso_oidc import SSOOIDCService
from boto34.aioboto3.services.stepfunctions import SFNService
from boto34.aioboto3.services.storagegateway import StorageGatewayService
from boto34.aioboto3.services.sts import STSService
from boto34.aioboto3.services.supplychain import SupplyChainService
from boto34.aioboto3.services.support import SupportService
from boto34.aioboto3.services.support_app import SupportAppService
from boto34.aioboto3.services.swf import SWFService
from boto34.aioboto3.services.synthetics import SyntheticsService
from boto34.aioboto3.services.taxsettings import TaxSettingsService
from boto34.aioboto3.services.textract import TextractService
from boto34.aioboto3.services.timestream_influxdb import TimestreamInfluxDBService
from boto34.aioboto3.services.timestream_query import TimestreamQueryService
from boto34.aioboto3.services.timestream_write import TimestreamWriteService
from boto34.aioboto3.services.tnb import TelcoNetworkBuilderService
from boto34.aioboto3.services.transcribe import TranscribeServiceService
from boto34.aioboto3.services.transfer import TransferService
from boto34.aioboto3.services.translate import TranslateService
from boto34.aioboto3.services.trustedadvisor import TrustedAdvisorPublicAPIService
from boto34.aioboto3.services.verifiedpermissions import VerifiedPermissionsService
from boto34.aioboto3.services.voice_id import VoiceIDService
from boto34.aioboto3.services.vpc_lattice import VPCLatticeService
from boto34.aioboto3.services.waf import WAFService
from boto34.aioboto3.services.waf_regional import WAFRegionalService
from boto34.aioboto3.services.wafv2 import WAFV2Service
from boto34.aioboto3.services.wellarchitected import WellArchitectedService
from boto34.aioboto3.services.wisdom import ConnectWisdomServiceService
from boto34.aioboto3.services.workdocs import WorkDocsService
from boto34.aioboto3.services.workmail import WorkMailService
from boto34.aioboto3.services.workmailmessageflow import WorkMailMessageFlowService
from boto34.aioboto3.services.workspaces import WorkSpacesService
from boto34.aioboto3.services.workspaces_thin_client import WorkSpacesThinClientService
from boto34.aioboto3.services.workspaces_web import WorkSpacesWebService
from boto34.aioboto3.services.xray import XRayService


class Session(Aioboto3Session):
    @property
    def accessanalyzer(self) -> AccessAnalyzerService:
        """
        aioboto3 Session for AccessAnalyzer service.
        """
        return AccessAnalyzerService("accessanalyzer", self)

    @property
    def account(self) -> AccountService:
        """
        aioboto3 Session for Account service.
        """
        return AccountService("account", self)

    @property
    def acm(self) -> ACMService:
        """
        aioboto3 Session for ACM service.
        """
        return ACMService("acm", self)

    @property
    def acm_pca(self) -> ACMPCAService:
        """
        aioboto3 Session for ACMPCA service.
        """
        return ACMPCAService("acm-pca", self)

    @property
    def amp(self) -> PrometheusServiceService:
        """
        aioboto3 Session for PrometheusService service.
        """
        return PrometheusServiceService("amp", self)

    @property
    def amplify(self) -> AmplifyService:
        """
        aioboto3 Session for Amplify service.
        """
        return AmplifyService("amplify", self)

    @property
    def amplifybackend(self) -> AmplifyBackendService:
        """
        aioboto3 Session for AmplifyBackend service.
        """
        return AmplifyBackendService("amplifybackend", self)

    @property
    def amplifyuibuilder(self) -> AmplifyUIBuilderService:
        """
        aioboto3 Session for AmplifyUIBuilder service.
        """
        return AmplifyUIBuilderService("amplifyuibuilder", self)

    @property
    def apigateway(self) -> APIGatewayService:
        """
        aioboto3 Session for APIGateway service.
        """
        return APIGatewayService("apigateway", self)

    @property
    def apigatewaymanagementapi(self) -> ApiGatewayManagementApiService:
        """
        aioboto3 Session for ApiGatewayManagementApi service.
        """
        return ApiGatewayManagementApiService("apigatewaymanagementapi", self)

    @property
    def apigatewayv2(self) -> ApiGatewayV2Service:
        """
        aioboto3 Session for ApiGatewayV2 service.
        """
        return ApiGatewayV2Service("apigatewayv2", self)

    @property
    def appconfig(self) -> AppConfigService:
        """
        aioboto3 Session for AppConfig service.
        """
        return AppConfigService("appconfig", self)

    @property
    def appconfigdata(self) -> AppConfigDataService:
        """
        aioboto3 Session for AppConfigData service.
        """
        return AppConfigDataService("appconfigdata", self)

    @property
    def appfabric(self) -> AppFabricService:
        """
        aioboto3 Session for AppFabric service.
        """
        return AppFabricService("appfabric", self)

    @property
    def appflow(self) -> AppflowService:
        """
        aioboto3 Session for Appflow service.
        """
        return AppflowService("appflow", self)

    @property
    def appintegrations(self) -> AppIntegrationsServiceService:
        """
        aioboto3 Session for AppIntegrationsService service.
        """
        return AppIntegrationsServiceService("appintegrations", self)

    @property
    def application_autoscaling(self) -> ApplicationAutoScalingService:
        """
        aioboto3 Session for ApplicationAutoScaling service.
        """
        return ApplicationAutoScalingService("application-autoscaling", self)

    @property
    def application_insights(self) -> ApplicationInsightsService:
        """
        aioboto3 Session for ApplicationInsights service.
        """
        return ApplicationInsightsService("application-insights", self)

    @property
    def application_signals(self) -> CloudWatchApplicationSignalsService:
        """
        aioboto3 Session for CloudWatchApplicationSignals service.
        """
        return CloudWatchApplicationSignalsService("application-signals", self)

    @property
    def applicationcostprofiler(self) -> ApplicationCostProfilerService:
        """
        aioboto3 Session for ApplicationCostProfiler service.
        """
        return ApplicationCostProfilerService("applicationcostprofiler", self)

    @property
    def appmesh(self) -> AppMeshService:
        """
        aioboto3 Session for AppMesh service.
        """
        return AppMeshService("appmesh", self)

    @property
    def apprunner(self) -> AppRunnerService:
        """
        aioboto3 Session for AppRunner service.
        """
        return AppRunnerService("apprunner", self)

    @property
    def appstream(self) -> AppStreamService:
        """
        aioboto3 Session for AppStream service.
        """
        return AppStreamService("appstream", self)

    @property
    def appsync(self) -> AppSyncService:
        """
        aioboto3 Session for AppSync service.
        """
        return AppSyncService("appsync", self)

    @property
    def apptest(self) -> MainframeModernizationApplicationTestingService:
        """
        aioboto3 Session for MainframeModernizationApplicationTesting service.
        """
        return MainframeModernizationApplicationTestingService("apptest", self)

    @property
    def arc_zonal_shift(self) -> ARCZonalShiftService:
        """
        aioboto3 Session for ARCZonalShift service.
        """
        return ARCZonalShiftService("arc-zonal-shift", self)

    @property
    def artifact(self) -> ArtifactService:
        """
        aioboto3 Session for Artifact service.
        """
        return ArtifactService("artifact", self)

    @property
    def athena(self) -> AthenaService:
        """
        aioboto3 Session for Athena service.
        """
        return AthenaService("athena", self)

    @property
    def auditmanager(self) -> AuditManagerService:
        """
        aioboto3 Session for AuditManager service.
        """
        return AuditManagerService("auditmanager", self)

    @property
    def autoscaling(self) -> AutoScalingService:
        """
        aioboto3 Session for AutoScaling service.
        """
        return AutoScalingService("autoscaling", self)

    @property
    def autoscaling_plans(self) -> AutoScalingPlansService:
        """
        aioboto3 Session for AutoScalingPlans service.
        """
        return AutoScalingPlansService("autoscaling-plans", self)

    @property
    def b2bi(self) -> B2BIService:
        """
        aioboto3 Session for B2BI service.
        """
        return B2BIService("b2bi", self)

    @property
    def backup(self) -> BackupService:
        """
        aioboto3 Session for Backup service.
        """
        return BackupService("backup", self)

    @property
    def backup_gateway(self) -> BackupGatewayService:
        """
        aioboto3 Session for BackupGateway service.
        """
        return BackupGatewayService("backup-gateway", self)

    @property
    def backupsearch(self) -> BackupSearchService:
        """
        aioboto3 Session for BackupSearch service.
        """
        return BackupSearchService("backupsearch", self)

    @property
    def batch(self) -> BatchService:
        """
        aioboto3 Session for Batch service.
        """
        return BatchService("batch", self)

    @property
    def bcm_data_exports(self) -> BillingandCostManagementDataExportsService:
        """
        aioboto3 Session for BillingandCostManagementDataExports service.
        """
        return BillingandCostManagementDataExportsService("bcm-data-exports", self)

    @property
    def bcm_pricing_calculator(self) -> BillingandCostManagementPricingCalculatorService:
        """
        aioboto3 Session for BillingandCostManagementPricingCalculator service.
        """
        return BillingandCostManagementPricingCalculatorService("bcm-pricing-calculator", self)

    @property
    def bedrock(self) -> BedrockService:
        """
        aioboto3 Session for Bedrock service.
        """
        return BedrockService("bedrock", self)

    @property
    def bedrock_agent(self) -> AgentsforBedrockService:
        """
        aioboto3 Session for AgentsforBedrock service.
        """
        return AgentsforBedrockService("bedrock-agent", self)

    @property
    def bedrock_agent_runtime(self) -> AgentsforBedrockRuntimeService:
        """
        aioboto3 Session for AgentsforBedrockRuntime service.
        """
        return AgentsforBedrockRuntimeService("bedrock-agent-runtime", self)

    @property
    def bedrock_data_automation(self) -> DataAutomationforBedrockService:
        """
        aioboto3 Session for DataAutomationforBedrock service.
        """
        return DataAutomationforBedrockService("bedrock-data-automation", self)

    @property
    def bedrock_data_automation_runtime(self) -> RuntimeforBedrockDataAutomationService:
        """
        aioboto3 Session for RuntimeforBedrockDataAutomation service.
        """
        return RuntimeforBedrockDataAutomationService("bedrock-data-automation-runtime", self)

    @property
    def bedrock_runtime(self) -> BedrockRuntimeService:
        """
        aioboto3 Session for BedrockRuntime service.
        """
        return BedrockRuntimeService("bedrock-runtime", self)

    @property
    def billing(self) -> BillingService:
        """
        aioboto3 Session for Billing service.
        """
        return BillingService("billing", self)

    @property
    def billingconductor(self) -> BillingConductorService:
        """
        aioboto3 Session for BillingConductor service.
        """
        return BillingConductorService("billingconductor", self)

    @property
    def braket(self) -> BraketService:
        """
        aioboto3 Session for Braket service.
        """
        return BraketService("braket", self)

    @property
    def budgets(self) -> BudgetsService:
        """
        aioboto3 Session for Budgets service.
        """
        return BudgetsService("budgets", self)

    @property
    def ce(self) -> CostExplorerService:
        """
        aioboto3 Session for CostExplorer service.
        """
        return CostExplorerService("ce", self)

    @property
    def chatbot(self) -> ChatbotService:
        """
        aioboto3 Session for Chatbot service.
        """
        return ChatbotService("chatbot", self)

    @property
    def chime(self) -> ChimeService:
        """
        aioboto3 Session for Chime service.
        """
        return ChimeService("chime", self)

    @property
    def chime_sdk_identity(self) -> ChimeSDKIdentityService:
        """
        aioboto3 Session for ChimeSDKIdentity service.
        """
        return ChimeSDKIdentityService("chime-sdk-identity", self)

    @property
    def chime_sdk_media_pipelines(self) -> ChimeSDKMediaPipelinesService:
        """
        aioboto3 Session for ChimeSDKMediaPipelines service.
        """
        return ChimeSDKMediaPipelinesService("chime-sdk-media-pipelines", self)

    @property
    def chime_sdk_meetings(self) -> ChimeSDKMeetingsService:
        """
        aioboto3 Session for ChimeSDKMeetings service.
        """
        return ChimeSDKMeetingsService("chime-sdk-meetings", self)

    @property
    def chime_sdk_messaging(self) -> ChimeSDKMessagingService:
        """
        aioboto3 Session for ChimeSDKMessaging service.
        """
        return ChimeSDKMessagingService("chime-sdk-messaging", self)

    @property
    def chime_sdk_voice(self) -> ChimeSDKVoiceService:
        """
        aioboto3 Session for ChimeSDKVoice service.
        """
        return ChimeSDKVoiceService("chime-sdk-voice", self)

    @property
    def cleanrooms(self) -> CleanRoomsServiceService:
        """
        aioboto3 Session for CleanRoomsService service.
        """
        return CleanRoomsServiceService("cleanrooms", self)

    @property
    def cleanroomsml(self) -> CleanRoomsMLService:
        """
        aioboto3 Session for CleanRoomsML service.
        """
        return CleanRoomsMLService("cleanroomsml", self)

    @property
    def cloud9(self) -> Cloud9Service:
        """
        aioboto3 Session for Cloud9 service.
        """
        return Cloud9Service("cloud9", self)

    @property
    def cloudcontrol(self) -> CloudControlApiService:
        """
        aioboto3 Session for CloudControlApi service.
        """
        return CloudControlApiService("cloudcontrol", self)

    @property
    def clouddirectory(self) -> CloudDirectoryService:
        """
        aioboto3 Session for CloudDirectory service.
        """
        return CloudDirectoryService("clouddirectory", self)

    @property
    def cloudformation(self) -> CloudFormationService:
        """
        aioboto3 Session for CloudFormation service.
        """
        return CloudFormationService("cloudformation", self)

    @property
    def cloudfront(self) -> CloudFrontService:
        """
        aioboto3 Session for CloudFront service.
        """
        return CloudFrontService("cloudfront", self)

    @property
    def cloudfront_keyvaluestore(self) -> CloudFrontKeyValueStoreService:
        """
        aioboto3 Session for CloudFrontKeyValueStore service.
        """
        return CloudFrontKeyValueStoreService("cloudfront-keyvaluestore", self)

    @property
    def cloudhsm(self) -> CloudHSMService:
        """
        aioboto3 Session for CloudHSM service.
        """
        return CloudHSMService("cloudhsm", self)

    @property
    def cloudhsmv2(self) -> CloudHSMV2Service:
        """
        aioboto3 Session for CloudHSMV2 service.
        """
        return CloudHSMV2Service("cloudhsmv2", self)

    @property
    def cloudsearch(self) -> CloudSearchService:
        """
        aioboto3 Session for CloudSearch service.
        """
        return CloudSearchService("cloudsearch", self)

    @property
    def cloudsearchdomain(self) -> CloudSearchDomainService:
        """
        aioboto3 Session for CloudSearchDomain service.
        """
        return CloudSearchDomainService("cloudsearchdomain", self)

    @property
    def cloudtrail(self) -> CloudTrailService:
        """
        aioboto3 Session for CloudTrail service.
        """
        return CloudTrailService("cloudtrail", self)

    @property
    def cloudtrail_data(self) -> CloudTrailDataServiceService:
        """
        aioboto3 Session for CloudTrailDataService service.
        """
        return CloudTrailDataServiceService("cloudtrail-data", self)

    @property
    def cloudwatch(self) -> CloudWatchService:
        """
        aioboto3 Session for CloudWatch service.
        """
        return CloudWatchService("cloudwatch", self)

    @property
    def codeartifact(self) -> CodeArtifactService:
        """
        aioboto3 Session for CodeArtifact service.
        """
        return CodeArtifactService("codeartifact", self)

    @property
    def codebuild(self) -> CodeBuildService:
        """
        aioboto3 Session for CodeBuild service.
        """
        return CodeBuildService("codebuild", self)

    @property
    def codecatalyst(self) -> CodeCatalystService:
        """
        aioboto3 Session for CodeCatalyst service.
        """
        return CodeCatalystService("codecatalyst", self)

    @property
    def codecommit(self) -> CodeCommitService:
        """
        aioboto3 Session for CodeCommit service.
        """
        return CodeCommitService("codecommit", self)

    @property
    def codeconnections(self) -> CodeConnectionsService:
        """
        aioboto3 Session for CodeConnections service.
        """
        return CodeConnectionsService("codeconnections", self)

    @property
    def codedeploy(self) -> CodeDeployService:
        """
        aioboto3 Session for CodeDeploy service.
        """
        return CodeDeployService("codedeploy", self)

    @property
    def codeguru_reviewer(self) -> CodeGuruReviewerService:
        """
        aioboto3 Session for CodeGuruReviewer service.
        """
        return CodeGuruReviewerService("codeguru-reviewer", self)

    @property
    def codeguru_security(self) -> CodeGuruSecurityService:
        """
        aioboto3 Session for CodeGuruSecurity service.
        """
        return CodeGuruSecurityService("codeguru-security", self)

    @property
    def codeguruprofiler(self) -> CodeGuruProfilerService:
        """
        aioboto3 Session for CodeGuruProfiler service.
        """
        return CodeGuruProfilerService("codeguruprofiler", self)

    @property
    def codepipeline(self) -> CodePipelineService:
        """
        aioboto3 Session for CodePipeline service.
        """
        return CodePipelineService("codepipeline", self)

    @property
    def codestar_connections(self) -> CodeStarconnectionsService:
        """
        aioboto3 Session for CodeStarconnections service.
        """
        return CodeStarconnectionsService("codestar-connections", self)

    @property
    def codestar_notifications(self) -> CodeStarNotificationsService:
        """
        aioboto3 Session for CodeStarNotifications service.
        """
        return CodeStarNotificationsService("codestar-notifications", self)

    @property
    def cognito_identity(self) -> CognitoIdentityService:
        """
        aioboto3 Session for CognitoIdentity service.
        """
        return CognitoIdentityService("cognito-identity", self)

    @property
    def cognito_idp(self) -> CognitoIdentityProviderService:
        """
        aioboto3 Session for CognitoIdentityProvider service.
        """
        return CognitoIdentityProviderService("cognito-idp", self)

    @property
    def cognito_sync(self) -> CognitoSyncService:
        """
        aioboto3 Session for CognitoSync service.
        """
        return CognitoSyncService("cognito-sync", self)

    @property
    def comprehend(self) -> ComprehendService:
        """
        aioboto3 Session for Comprehend service.
        """
        return ComprehendService("comprehend", self)

    @property
    def comprehendmedical(self) -> ComprehendMedicalService:
        """
        aioboto3 Session for ComprehendMedical service.
        """
        return ComprehendMedicalService("comprehendmedical", self)

    @property
    def compute_optimizer(self) -> ComputeOptimizerService:
        """
        aioboto3 Session for ComputeOptimizer service.
        """
        return ComputeOptimizerService("compute-optimizer", self)

    @property
    def config(self) -> ConfigServiceService:
        """
        aioboto3 Session for ConfigService service.
        """
        return ConfigServiceService("config", self)

    @property
    def connect(self) -> ConnectService:
        """
        aioboto3 Session for Connect service.
        """
        return ConnectService("connect", self)

    @property
    def connect_contact_lens(self) -> ConnectContactLensService:
        """
        aioboto3 Session for ConnectContactLens service.
        """
        return ConnectContactLensService("connect-contact-lens", self)

    @property
    def connectcampaigns(self) -> ConnectCampaignServiceService:
        """
        aioboto3 Session for ConnectCampaignService service.
        """
        return ConnectCampaignServiceService("connectcampaigns", self)

    @property
    def connectcampaignsv2(self) -> ConnectCampaignServiceV2Service:
        """
        aioboto3 Session for ConnectCampaignServiceV2 service.
        """
        return ConnectCampaignServiceV2Service("connectcampaignsv2", self)

    @property
    def connectcases(self) -> ConnectCasesService:
        """
        aioboto3 Session for ConnectCases service.
        """
        return ConnectCasesService("connectcases", self)

    @property
    def connectparticipant(self) -> ConnectParticipantService:
        """
        aioboto3 Session for ConnectParticipant service.
        """
        return ConnectParticipantService("connectparticipant", self)

    @property
    def controlcatalog(self) -> ControlCatalogService:
        """
        aioboto3 Session for ControlCatalog service.
        """
        return ControlCatalogService("controlcatalog", self)

    @property
    def controltower(self) -> ControlTowerService:
        """
        aioboto3 Session for ControlTower service.
        """
        return ControlTowerService("controltower", self)

    @property
    def cost_optimization_hub(self) -> CostOptimizationHubService:
        """
        aioboto3 Session for CostOptimizationHub service.
        """
        return CostOptimizationHubService("cost-optimization-hub", self)

    @property
    def cur(self) -> CostandUsageReportServiceService:
        """
        aioboto3 Session for CostandUsageReportService service.
        """
        return CostandUsageReportServiceService("cur", self)

    @property
    def customer_profiles(self) -> CustomerProfilesService:
        """
        aioboto3 Session for CustomerProfiles service.
        """
        return CustomerProfilesService("customer-profiles", self)

    @property
    def databrew(self) -> GlueDataBrewService:
        """
        aioboto3 Session for GlueDataBrew service.
        """
        return GlueDataBrewService("databrew", self)

    @property
    def dataexchange(self) -> DataExchangeService:
        """
        aioboto3 Session for DataExchange service.
        """
        return DataExchangeService("dataexchange", self)

    @property
    def datapipeline(self) -> DataPipelineService:
        """
        aioboto3 Session for DataPipeline service.
        """
        return DataPipelineService("datapipeline", self)

    @property
    def datasync(self) -> DataSyncService:
        """
        aioboto3 Session for DataSync service.
        """
        return DataSyncService("datasync", self)

    @property
    def datazone(self) -> DataZoneService:
        """
        aioboto3 Session for DataZone service.
        """
        return DataZoneService("datazone", self)

    @property
    def dax(self) -> DAXService:
        """
        aioboto3 Session for DAX service.
        """
        return DAXService("dax", self)

    @property
    def deadline(self) -> DeadlineCloudService:
        """
        aioboto3 Session for DeadlineCloud service.
        """
        return DeadlineCloudService("deadline", self)

    @property
    def detective(self) -> DetectiveService:
        """
        aioboto3 Session for Detective service.
        """
        return DetectiveService("detective", self)

    @property
    def devicefarm(self) -> DeviceFarmService:
        """
        aioboto3 Session for DeviceFarm service.
        """
        return DeviceFarmService("devicefarm", self)

    @property
    def devops_guru(self) -> DevOpsGuruService:
        """
        aioboto3 Session for DevOpsGuru service.
        """
        return DevOpsGuruService("devops-guru", self)

    @property
    def directconnect(self) -> DirectConnectService:
        """
        aioboto3 Session for DirectConnect service.
        """
        return DirectConnectService("directconnect", self)

    @property
    def discovery(self) -> ApplicationDiscoveryServiceService:
        """
        aioboto3 Session for ApplicationDiscoveryService service.
        """
        return ApplicationDiscoveryServiceService("discovery", self)

    @property
    def dlm(self) -> DLMService:
        """
        aioboto3 Session for DLM service.
        """
        return DLMService("dlm", self)

    @property
    def dms(self) -> DatabaseMigrationServiceService:
        """
        aioboto3 Session for DatabaseMigrationService service.
        """
        return DatabaseMigrationServiceService("dms", self)

    @property
    def docdb(self) -> DocDBService:
        """
        aioboto3 Session for DocDB service.
        """
        return DocDBService("docdb", self)

    @property
    def docdb_elastic(self) -> DocDBElasticService:
        """
        aioboto3 Session for DocDBElastic service.
        """
        return DocDBElasticService("docdb-elastic", self)

    @property
    def drs(self) -> DrsService:
        """
        aioboto3 Session for Drs service.
        """
        return DrsService("drs", self)

    @property
    def ds(self) -> DirectoryServiceService:
        """
        aioboto3 Session for DirectoryService service.
        """
        return DirectoryServiceService("ds", self)

    @property
    def ds_data(self) -> DirectoryServiceDataService:
        """
        aioboto3 Session for DirectoryServiceData service.
        """
        return DirectoryServiceDataService("ds-data", self)

    @property
    def dsql(self) -> AuroraDSQLService:
        """
        aioboto3 Session for AuroraDSQL service.
        """
        return AuroraDSQLService("dsql", self)

    @property
    def dynamodb(self) -> DynamoDBService:
        """
        aioboto3 Session for DynamoDB service.
        """
        return DynamoDBService("dynamodb", self)

    @property
    def dynamodbstreams(self) -> DynamoDBStreamsService:
        """
        aioboto3 Session for DynamoDBStreams service.
        """
        return DynamoDBStreamsService("dynamodbstreams", self)

    @property
    def ebs(self) -> EBSService:
        """
        aioboto3 Session for EBS service.
        """
        return EBSService("ebs", self)

    @property
    def ec2(self) -> EC2Service:
        """
        aioboto3 Session for EC2 service.
        """
        return EC2Service("ec2", self)

    @property
    def ec2_instance_connect(self) -> EC2InstanceConnectService:
        """
        aioboto3 Session for EC2InstanceConnect service.
        """
        return EC2InstanceConnectService("ec2-instance-connect", self)

    @property
    def ecr(self) -> ECRService:
        """
        aioboto3 Session for ECR service.
        """
        return ECRService("ecr", self)

    @property
    def ecr_public(self) -> ECRPublicService:
        """
        aioboto3 Session for ECRPublic service.
        """
        return ECRPublicService("ecr-public", self)

    @property
    def ecs(self) -> ECSService:
        """
        aioboto3 Session for ECS service.
        """
        return ECSService("ecs", self)

    @property
    def efs(self) -> EFSService:
        """
        aioboto3 Session for EFS service.
        """
        return EFSService("efs", self)

    @property
    def eks(self) -> EKSService:
        """
        aioboto3 Session for EKS service.
        """
        return EKSService("eks", self)

    @property
    def eks_auth(self) -> EKSAuthService:
        """
        aioboto3 Session for EKSAuth service.
        """
        return EKSAuthService("eks-auth", self)

    @property
    def elasticache(self) -> ElastiCacheService:
        """
        aioboto3 Session for ElastiCache service.
        """
        return ElastiCacheService("elasticache", self)

    @property
    def elasticbeanstalk(self) -> ElasticBeanstalkService:
        """
        aioboto3 Session for ElasticBeanstalk service.
        """
        return ElasticBeanstalkService("elasticbeanstalk", self)

    @property
    def elastictranscoder(self) -> ElasticTranscoderService:
        """
        aioboto3 Session for ElasticTranscoder service.
        """
        return ElasticTranscoderService("elastictranscoder", self)

    @property
    def elb(self) -> ElasticLoadBalancingService:
        """
        aioboto3 Session for ElasticLoadBalancing service.
        """
        return ElasticLoadBalancingService("elb", self)

    @property
    def elbv2(self) -> ElasticLoadBalancingv2Service:
        """
        aioboto3 Session for ElasticLoadBalancingv2 service.
        """
        return ElasticLoadBalancingv2Service("elbv2", self)

    @property
    def emr(self) -> EMRService:
        """
        aioboto3 Session for EMR service.
        """
        return EMRService("emr", self)

    @property
    def emr_containers(self) -> EMRContainersService:
        """
        aioboto3 Session for EMRContainers service.
        """
        return EMRContainersService("emr-containers", self)

    @property
    def emr_serverless(self) -> EMRServerlessService:
        """
        aioboto3 Session for EMRServerless service.
        """
        return EMRServerlessService("emr-serverless", self)

    @property
    def entityresolution(self) -> EntityResolutionService:
        """
        aioboto3 Session for EntityResolution service.
        """
        return EntityResolutionService("entityresolution", self)

    @property
    def es(self) -> ElasticsearchServiceService:
        """
        aioboto3 Session for ElasticsearchService service.
        """
        return ElasticsearchServiceService("es", self)

    @property
    def eventbridge(self) -> EventBridgeService:
        """
        aioboto3 Session for EventBridge service.
        """
        return EventBridgeService("events", self)

    @property
    def evidently(self) -> CloudWatchEvidentlyService:
        """
        aioboto3 Session for CloudWatchEvidently service.
        """
        return CloudWatchEvidentlyService("evidently", self)

    @property
    def finspace(self) -> FinspaceService:
        """
        aioboto3 Session for Finspace service.
        """
        return FinspaceService("finspace", self)

    @property
    def finspace_data(self) -> FinSpaceDataService:
        """
        aioboto3 Session for FinSpaceData service.
        """
        return FinSpaceDataService("finspace-data", self)

    @property
    def firehose(self) -> FirehoseService:
        """
        aioboto3 Session for Firehose service.
        """
        return FirehoseService("firehose", self)

    @property
    def fis(self) -> FISService:
        """
        aioboto3 Session for FIS service.
        """
        return FISService("fis", self)

    @property
    def fms(self) -> FMSService:
        """
        aioboto3 Session for FMS service.
        """
        return FMSService("fms", self)

    @property
    def forecast(self) -> ForecastServiceService:
        """
        aioboto3 Session for ForecastService service.
        """
        return ForecastServiceService("forecast", self)

    @property
    def forecastquery(self) -> ForecastQueryServiceService:
        """
        aioboto3 Session for ForecastQueryService service.
        """
        return ForecastQueryServiceService("forecastquery", self)

    @property
    def frauddetector(self) -> FraudDetectorService:
        """
        aioboto3 Session for FraudDetector service.
        """
        return FraudDetectorService("frauddetector", self)

    @property
    def freetier(self) -> FreeTierService:
        """
        aioboto3 Session for FreeTier service.
        """
        return FreeTierService("freetier", self)

    @property
    def fsx(self) -> FSxService:
        """
        aioboto3 Session for FSx service.
        """
        return FSxService("fsx", self)

    @property
    def gamelift(self) -> GameLiftService:
        """
        aioboto3 Session for GameLift service.
        """
        return GameLiftService("gamelift", self)

    @property
    def geo_maps(self) -> LocationServiceMapsV2Service:
        """
        aioboto3 Session for LocationServiceMapsV2 service.
        """
        return LocationServiceMapsV2Service("geo-maps", self)

    @property
    def geo_places(self) -> LocationServicePlacesV2Service:
        """
        aioboto3 Session for LocationServicePlacesV2 service.
        """
        return LocationServicePlacesV2Service("geo-places", self)

    @property
    def geo_routes(self) -> LocationServiceRoutesV2Service:
        """
        aioboto3 Session for LocationServiceRoutesV2 service.
        """
        return LocationServiceRoutesV2Service("geo-routes", self)

    @property
    def glacier(self) -> GlacierService:
        """
        aioboto3 Session for Glacier service.
        """
        return GlacierService("glacier", self)

    @property
    def globalaccelerator(self) -> GlobalAcceleratorService:
        """
        aioboto3 Session for GlobalAccelerator service.
        """
        return GlobalAcceleratorService("globalaccelerator", self)

    @property
    def glue(self) -> GlueService:
        """
        aioboto3 Session for Glue service.
        """
        return GlueService("glue", self)

    @property
    def grafana(self) -> ManagedGrafanaService:
        """
        aioboto3 Session for ManagedGrafana service.
        """
        return ManagedGrafanaService("grafana", self)

    @property
    def greengrass(self) -> GreengrassService:
        """
        aioboto3 Session for Greengrass service.
        """
        return GreengrassService("greengrass", self)

    @property
    def greengrassv2(self) -> GreengrassV2Service:
        """
        aioboto3 Session for GreengrassV2 service.
        """
        return GreengrassV2Service("greengrassv2", self)

    @property
    def groundstation(self) -> GroundStationService:
        """
        aioboto3 Session for GroundStation service.
        """
        return GroundStationService("groundstation", self)

    @property
    def guardduty(self) -> GuardDutyService:
        """
        aioboto3 Session for GuardDuty service.
        """
        return GuardDutyService("guardduty", self)

    @property
    def health(self) -> HealthService:
        """
        aioboto3 Session for Health service.
        """
        return HealthService("health", self)

    @property
    def healthlake(self) -> HealthLakeService:
        """
        aioboto3 Session for HealthLake service.
        """
        return HealthLakeService("healthlake", self)

    @property
    def iam(self) -> IAMService:
        """
        aioboto3 Session for IAM service.
        """
        return IAMService("iam", self)

    @property
    def identitystore(self) -> IdentityStoreService:
        """
        aioboto3 Session for IdentityStore service.
        """
        return IdentityStoreService("identitystore", self)

    @property
    def imagebuilder(self) -> ImagebuilderService:
        """
        aioboto3 Session for Imagebuilder service.
        """
        return ImagebuilderService("imagebuilder", self)

    @property
    def importexport(self) -> ImportExportService:
        """
        aioboto3 Session for ImportExport service.
        """
        return ImportExportService("importexport", self)

    @property
    def inspector(self) -> InspectorService:
        """
        aioboto3 Session for Inspector service.
        """
        return InspectorService("inspector", self)

    @property
    def inspector_scan(self) -> InspectorscanService:
        """
        aioboto3 Session for Inspectorscan service.
        """
        return InspectorscanService("inspector-scan", self)

    @property
    def inspector2(self) -> Inspector2Service:
        """
        aioboto3 Session for Inspector2 service.
        """
        return Inspector2Service("inspector2", self)

    @property
    def internetmonitor(self) -> CloudWatchInternetMonitorService:
        """
        aioboto3 Session for CloudWatchInternetMonitor service.
        """
        return CloudWatchInternetMonitorService("internetmonitor", self)

    @property
    def invoicing(self) -> InvoicingService:
        """
        aioboto3 Session for Invoicing service.
        """
        return InvoicingService("invoicing", self)

    @property
    def iot(self) -> IoTService:
        """
        aioboto3 Session for IoT service.
        """
        return IoTService("iot", self)

    @property
    def iot_data(self) -> IoTDataPlaneService:
        """
        aioboto3 Session for IoTDataPlane service.
        """
        return IoTDataPlaneService("iot-data", self)

    @property
    def iot_jobs_data(self) -> IoTJobsDataPlaneService:
        """
        aioboto3 Session for IoTJobsDataPlane service.
        """
        return IoTJobsDataPlaneService("iot-jobs-data", self)

    @property
    def iotanalytics(self) -> IoTAnalyticsService:
        """
        aioboto3 Session for IoTAnalytics service.
        """
        return IoTAnalyticsService("iotanalytics", self)

    @property
    def iotdeviceadvisor(self) -> IoTDeviceAdvisorService:
        """
        aioboto3 Session for IoTDeviceAdvisor service.
        """
        return IoTDeviceAdvisorService("iotdeviceadvisor", self)

    @property
    def iotevents(self) -> IoTEventsService:
        """
        aioboto3 Session for IoTEvents service.
        """
        return IoTEventsService("iotevents", self)

    @property
    def iotevents_data(self) -> IoTEventsDataService:
        """
        aioboto3 Session for IoTEventsData service.
        """
        return IoTEventsDataService("iotevents-data", self)

    @property
    def iotfleethub(self) -> IoTFleetHubService:
        """
        aioboto3 Session for IoTFleetHub service.
        """
        return IoTFleetHubService("iotfleethub", self)

    @property
    def iotfleetwise(self) -> IoTFleetWiseService:
        """
        aioboto3 Session for IoTFleetWise service.
        """
        return IoTFleetWiseService("iotfleetwise", self)

    @property
    def iotsecuretunneling(self) -> IoTSecureTunnelingService:
        """
        aioboto3 Session for IoTSecureTunneling service.
        """
        return IoTSecureTunnelingService("iotsecuretunneling", self)

    @property
    def iotsitewise(self) -> IoTSiteWiseService:
        """
        aioboto3 Session for IoTSiteWise service.
        """
        return IoTSiteWiseService("iotsitewise", self)

    @property
    def iotthingsgraph(self) -> IoTThingsGraphService:
        """
        aioboto3 Session for IoTThingsGraph service.
        """
        return IoTThingsGraphService("iotthingsgraph", self)

    @property
    def iottwinmaker(self) -> IoTTwinMakerService:
        """
        aioboto3 Session for IoTTwinMaker service.
        """
        return IoTTwinMakerService("iottwinmaker", self)

    @property
    def iotwireless(self) -> IoTWirelessService:
        """
        aioboto3 Session for IoTWireless service.
        """
        return IoTWirelessService("iotwireless", self)

    @property
    def ivs(self) -> IVSService:
        """
        aioboto3 Session for IVS service.
        """
        return IVSService("ivs", self)

    @property
    def ivs_realtime(self) -> IvsrealtimeService:
        """
        aioboto3 Session for Ivsrealtime service.
        """
        return IvsrealtimeService("ivs-realtime", self)

    @property
    def ivschat(self) -> IvschatService:
        """
        aioboto3 Session for Ivschat service.
        """
        return IvschatService("ivschat", self)

    @property
    def kafka(self) -> KafkaService:
        """
        aioboto3 Session for Kafka service.
        """
        return KafkaService("kafka", self)

    @property
    def kafkaconnect(self) -> KafkaConnectService:
        """
        aioboto3 Session for KafkaConnect service.
        """
        return KafkaConnectService("kafkaconnect", self)

    @property
    def kendra(self) -> KendraService:
        """
        aioboto3 Session for Kendra service.
        """
        return KendraService("kendra", self)

    @property
    def kendra_ranking(self) -> KendraRankingService:
        """
        aioboto3 Session for KendraRanking service.
        """
        return KendraRankingService("kendra-ranking", self)

    @property
    def keyspaces(self) -> KeyspacesService:
        """
        aioboto3 Session for Keyspaces service.
        """
        return KeyspacesService("keyspaces", self)

    @property
    def kinesis(self) -> KinesisService:
        """
        aioboto3 Session for Kinesis service.
        """
        return KinesisService("kinesis", self)

    @property
    def kinesis_video_archived_media(self) -> KinesisVideoArchivedMediaService:
        """
        aioboto3 Session for KinesisVideoArchivedMedia service.
        """
        return KinesisVideoArchivedMediaService("kinesis-video-archived-media", self)

    @property
    def kinesis_video_media(self) -> KinesisVideoMediaService:
        """
        aioboto3 Session for KinesisVideoMedia service.
        """
        return KinesisVideoMediaService("kinesis-video-media", self)

    @property
    def kinesis_video_signaling(self) -> KinesisVideoSignalingChannelsService:
        """
        aioboto3 Session for KinesisVideoSignalingChannels service.
        """
        return KinesisVideoSignalingChannelsService("kinesis-video-signaling", self)

    @property
    def kinesis_video_webrtc_storage(self) -> KinesisVideoWebRTCStorageService:
        """
        aioboto3 Session for KinesisVideoWebRTCStorage service.
        """
        return KinesisVideoWebRTCStorageService("kinesis-video-webrtc-storage", self)

    @property
    def kinesisanalytics(self) -> KinesisAnalyticsService:
        """
        aioboto3 Session for KinesisAnalytics service.
        """
        return KinesisAnalyticsService("kinesisanalytics", self)

    @property
    def kinesisanalyticsv2(self) -> KinesisAnalyticsV2Service:
        """
        aioboto3 Session for KinesisAnalyticsV2 service.
        """
        return KinesisAnalyticsV2Service("kinesisanalyticsv2", self)

    @property
    def kinesisvideo(self) -> KinesisVideoService:
        """
        aioboto3 Session for KinesisVideo service.
        """
        return KinesisVideoService("kinesisvideo", self)

    @property
    def kms(self) -> KMSService:
        """
        aioboto3 Session for KMS service.
        """
        return KMSService("kms", self)

    @property
    def lakeformation(self) -> LakeFormationService:
        """
        aioboto3 Session for LakeFormation service.
        """
        return LakeFormationService("lakeformation", self)

    @property
    def lambda_(self) -> LambdaService:
        """
        aioboto3 Session for Lambda service.
        """
        return LambdaService("lambda", self)

    @property
    def launch_wizard(self) -> LaunchWizardService:
        """
        aioboto3 Session for LaunchWizard service.
        """
        return LaunchWizardService("launch-wizard", self)

    @property
    def lex_models(self) -> LexModelBuildingServiceService:
        """
        aioboto3 Session for LexModelBuildingService service.
        """
        return LexModelBuildingServiceService("lex-models", self)

    @property
    def lex_runtime(self) -> LexRuntimeServiceService:
        """
        aioboto3 Session for LexRuntimeService service.
        """
        return LexRuntimeServiceService("lex-runtime", self)

    @property
    def lexv2_models(self) -> LexModelsV2Service:
        """
        aioboto3 Session for LexModelsV2 service.
        """
        return LexModelsV2Service("lexv2-models", self)

    @property
    def lexv2_runtime(self) -> LexRuntimeV2Service:
        """
        aioboto3 Session for LexRuntimeV2 service.
        """
        return LexRuntimeV2Service("lexv2-runtime", self)

    @property
    def license_manager(self) -> LicenseManagerService:
        """
        aioboto3 Session for LicenseManager service.
        """
        return LicenseManagerService("license-manager", self)

    @property
    def license_manager_linux_subscriptions(self) -> LicenseManagerLinuxSubscriptionsService:
        """
        aioboto3 Session for LicenseManagerLinuxSubscriptions service.
        """
        return LicenseManagerLinuxSubscriptionsService("license-manager-linux-subscriptions", self)

    @property
    def license_manager_user_subscriptions(self) -> LicenseManagerUserSubscriptionsService:
        """
        aioboto3 Session for LicenseManagerUserSubscriptions service.
        """
        return LicenseManagerUserSubscriptionsService("license-manager-user-subscriptions", self)

    @property
    def lightsail(self) -> LightsailService:
        """
        aioboto3 Session for Lightsail service.
        """
        return LightsailService("lightsail", self)

    @property
    def location(self) -> LocationServiceService:
        """
        aioboto3 Session for LocationService service.
        """
        return LocationServiceService("location", self)

    @property
    def logs(self) -> CloudWatchLogsService:
        """
        aioboto3 Session for CloudWatchLogs service.
        """
        return CloudWatchLogsService("logs", self)

    @property
    def lookoutequipment(self) -> LookoutEquipmentService:
        """
        aioboto3 Session for LookoutEquipment service.
        """
        return LookoutEquipmentService("lookoutequipment", self)

    @property
    def lookoutmetrics(self) -> LookoutMetricsService:
        """
        aioboto3 Session for LookoutMetrics service.
        """
        return LookoutMetricsService("lookoutmetrics", self)

    @property
    def lookoutvision(self) -> LookoutforVisionService:
        """
        aioboto3 Session for LookoutforVision service.
        """
        return LookoutforVisionService("lookoutvision", self)

    @property
    def m2(self) -> MainframeModernizationService:
        """
        aioboto3 Session for MainframeModernization service.
        """
        return MainframeModernizationService("m2", self)

    @property
    def machinelearning(self) -> MachineLearningService:
        """
        aioboto3 Session for MachineLearning service.
        """
        return MachineLearningService("machinelearning", self)

    @property
    def macie2(self) -> Macie2Service:
        """
        aioboto3 Session for Macie2 service.
        """
        return Macie2Service("macie2", self)

    @property
    def mailmanager(self) -> MailManagerService:
        """
        aioboto3 Session for MailManager service.
        """
        return MailManagerService("mailmanager", self)

    @property
    def managedblockchain(self) -> ManagedBlockchainService:
        """
        aioboto3 Session for ManagedBlockchain service.
        """
        return ManagedBlockchainService("managedblockchain", self)

    @property
    def managedblockchain_query(self) -> ManagedBlockchainQueryService:
        """
        aioboto3 Session for ManagedBlockchainQuery service.
        """
        return ManagedBlockchainQueryService("managedblockchain-query", self)

    @property
    def marketplace_agreement(self) -> AgreementServiceService:
        """
        aioboto3 Session for AgreementService service.
        """
        return AgreementServiceService("marketplace-agreement", self)

    @property
    def marketplace_catalog(self) -> MarketplaceCatalogService:
        """
        aioboto3 Session for MarketplaceCatalog service.
        """
        return MarketplaceCatalogService("marketplace-catalog", self)

    @property
    def marketplace_deployment(self) -> MarketplaceDeploymentServiceService:
        """
        aioboto3 Session for MarketplaceDeploymentService service.
        """
        return MarketplaceDeploymentServiceService("marketplace-deployment", self)

    @property
    def marketplace_entitlement(self) -> MarketplaceEntitlementServiceService:
        """
        aioboto3 Session for MarketplaceEntitlementService service.
        """
        return MarketplaceEntitlementServiceService("marketplace-entitlement", self)

    @property
    def marketplace_reporting(self) -> MarketplaceReportingServiceService:
        """
        aioboto3 Session for MarketplaceReportingService service.
        """
        return MarketplaceReportingServiceService("marketplace-reporting", self)

    @property
    def marketplacecommerceanalytics(self) -> MarketplaceCommerceAnalyticsService:
        """
        aioboto3 Session for MarketplaceCommerceAnalytics service.
        """
        return MarketplaceCommerceAnalyticsService("marketplacecommerceanalytics", self)

    @property
    def mediaconnect(self) -> MediaConnectService:
        """
        aioboto3 Session for MediaConnect service.
        """
        return MediaConnectService("mediaconnect", self)

    @property
    def mediaconvert(self) -> MediaConvertService:
        """
        aioboto3 Session for MediaConvert service.
        """
        return MediaConvertService("mediaconvert", self)

    @property
    def medialive(self) -> MediaLiveService:
        """
        aioboto3 Session for MediaLive service.
        """
        return MediaLiveService("medialive", self)

    @property
    def mediapackage(self) -> MediaPackageService:
        """
        aioboto3 Session for MediaPackage service.
        """
        return MediaPackageService("mediapackage", self)

    @property
    def mediapackage_vod(self) -> MediaPackageVodService:
        """
        aioboto3 Session for MediaPackageVod service.
        """
        return MediaPackageVodService("mediapackage-vod", self)

    @property
    def mediapackagev2(self) -> Mediapackagev2Service:
        """
        aioboto3 Session for Mediapackagev2 service.
        """
        return Mediapackagev2Service("mediapackagev2", self)

    @property
    def mediastore(self) -> MediaStoreService:
        """
        aioboto3 Session for MediaStore service.
        """
        return MediaStoreService("mediastore", self)

    @property
    def mediastore_data(self) -> MediaStoreDataService:
        """
        aioboto3 Session for MediaStoreData service.
        """
        return MediaStoreDataService("mediastore-data", self)

    @property
    def mediatailor(self) -> MediaTailorService:
        """
        aioboto3 Session for MediaTailor service.
        """
        return MediaTailorService("mediatailor", self)

    @property
    def medical_imaging(self) -> HealthImagingService:
        """
        aioboto3 Session for HealthImaging service.
        """
        return HealthImagingService("medical-imaging", self)

    @property
    def memorydb(self) -> MemoryDBService:
        """
        aioboto3 Session for MemoryDB service.
        """
        return MemoryDBService("memorydb", self)

    @property
    def meteringmarketplace(self) -> MarketplaceMeteringService:
        """
        aioboto3 Session for MarketplaceMetering service.
        """
        return MarketplaceMeteringService("meteringmarketplace", self)

    @property
    def mgh(self) -> MigrationHubService:
        """
        aioboto3 Session for MigrationHub service.
        """
        return MigrationHubService("mgh", self)

    @property
    def mgn(self) -> MgnService:
        """
        aioboto3 Session for Mgn service.
        """
        return MgnService("mgn", self)

    @property
    def migration_hub_refactor_spaces(self) -> MigrationHubRefactorSpacesService:
        """
        aioboto3 Session for MigrationHubRefactorSpaces service.
        """
        return MigrationHubRefactorSpacesService("migration-hub-refactor-spaces", self)

    @property
    def migrationhub_config(self) -> MigrationHubConfigService:
        """
        aioboto3 Session for MigrationHubConfig service.
        """
        return MigrationHubConfigService("migrationhub-config", self)

    @property
    def migrationhuborchestrator(self) -> MigrationHubOrchestratorService:
        """
        aioboto3 Session for MigrationHubOrchestrator service.
        """
        return MigrationHubOrchestratorService("migrationhuborchestrator", self)

    @property
    def migrationhubstrategy(self) -> MigrationHubStrategyRecommendationsService:
        """
        aioboto3 Session for MigrationHubStrategyRecommendations service.
        """
        return MigrationHubStrategyRecommendationsService("migrationhubstrategy", self)

    @property
    def mq(self) -> MQService:
        """
        aioboto3 Session for MQ service.
        """
        return MQService("mq", self)

    @property
    def mturk(self) -> MTurkService:
        """
        aioboto3 Session for MTurk service.
        """
        return MTurkService("mturk", self)

    @property
    def mwaa(self) -> MWAAService:
        """
        aioboto3 Session for MWAA service.
        """
        return MWAAService("mwaa", self)

    @property
    def neptune(self) -> NeptuneService:
        """
        aioboto3 Session for Neptune service.
        """
        return NeptuneService("neptune", self)

    @property
    def neptune_graph(self) -> NeptuneGraphService:
        """
        aioboto3 Session for NeptuneGraph service.
        """
        return NeptuneGraphService("neptune-graph", self)

    @property
    def neptunedata(self) -> NeptuneDataService:
        """
        aioboto3 Session for NeptuneData service.
        """
        return NeptuneDataService("neptunedata", self)

    @property
    def network_firewall(self) -> NetworkFirewallService:
        """
        aioboto3 Session for NetworkFirewall service.
        """
        return NetworkFirewallService("network-firewall", self)

    @property
    def networkflowmonitor(self) -> NetworkFlowMonitorService:
        """
        aioboto3 Session for NetworkFlowMonitor service.
        """
        return NetworkFlowMonitorService("networkflowmonitor", self)

    @property
    def networkmanager(self) -> NetworkManagerService:
        """
        aioboto3 Session for NetworkManager service.
        """
        return NetworkManagerService("networkmanager", self)

    @property
    def networkmonitor(self) -> CloudWatchNetworkMonitorService:
        """
        aioboto3 Session for CloudWatchNetworkMonitor service.
        """
        return CloudWatchNetworkMonitorService("networkmonitor", self)

    @property
    def notifications(self) -> UserNotificationsService:
        """
        aioboto3 Session for UserNotifications service.
        """
        return UserNotificationsService("notifications", self)

    @property
    def notificationscontacts(self) -> UserNotificationsContactsService:
        """
        aioboto3 Session for UserNotificationsContacts service.
        """
        return UserNotificationsContactsService("notificationscontacts", self)

    @property
    def oam(self) -> CloudWatchObservabilityAccessManagerService:
        """
        aioboto3 Session for CloudWatchObservabilityAccessManager service.
        """
        return CloudWatchObservabilityAccessManagerService("oam", self)

    @property
    def observabilityadmin(self) -> CloudWatchObservabilityAdminServiceService:
        """
        aioboto3 Session for CloudWatchObservabilityAdminService service.
        """
        return CloudWatchObservabilityAdminServiceService("observabilityadmin", self)

    @property
    def omics(self) -> OmicsService:
        """
        aioboto3 Session for Omics service.
        """
        return OmicsService("omics", self)

    @property
    def opensearch(self) -> OpenSearchServiceService:
        """
        aioboto3 Session for OpenSearchService service.
        """
        return OpenSearchServiceService("opensearch", self)

    @property
    def opensearchserverless(self) -> OpenSearchServiceServerlessService:
        """
        aioboto3 Session for OpenSearchServiceServerless service.
        """
        return OpenSearchServiceServerlessService("opensearchserverless", self)

    @property
    def opsworks(self) -> OpsWorksService:
        """
        aioboto3 Session for OpsWorks service.
        """
        return OpsWorksService("opsworks", self)

    @property
    def opsworkscm(self) -> OpsWorksCMService:
        """
        aioboto3 Session for OpsWorksCM service.
        """
        return OpsWorksCMService("opsworkscm", self)

    @property
    def organizations(self) -> OrganizationsService:
        """
        aioboto3 Session for Organizations service.
        """
        return OrganizationsService("organizations", self)

    @property
    def osis(self) -> OpenSearchIngestionService:
        """
        aioboto3 Session for OpenSearchIngestion service.
        """
        return OpenSearchIngestionService("osis", self)

    @property
    def outposts(self) -> OutpostsService:
        """
        aioboto3 Session for Outposts service.
        """
        return OutpostsService("outposts", self)

    @property
    def panorama(self) -> PanoramaService:
        """
        aioboto3 Session for Panorama service.
        """
        return PanoramaService("panorama", self)

    @property
    def partnercentral_selling(self) -> PartnerCentralSellingAPIService:
        """
        aioboto3 Session for PartnerCentralSellingAPI service.
        """
        return PartnerCentralSellingAPIService("partnercentral-selling", self)

    @property
    def payment_cryptography(self) -> PaymentCryptographyControlPlaneService:
        """
        aioboto3 Session for PaymentCryptographyControlPlane service.
        """
        return PaymentCryptographyControlPlaneService("payment-cryptography", self)

    @property
    def payment_cryptography_data(self) -> PaymentCryptographyDataPlaneService:
        """
        aioboto3 Session for PaymentCryptographyDataPlane service.
        """
        return PaymentCryptographyDataPlaneService("payment-cryptography-data", self)

    @property
    def pca_connector_ad(self) -> PcaConnectorAdService:
        """
        aioboto3 Session for PcaConnectorAd service.
        """
        return PcaConnectorAdService("pca-connector-ad", self)

    @property
    def pca_connector_scep(self) -> PrivateCAConnectorforSCEPService:
        """
        aioboto3 Session for PrivateCAConnectorforSCEP service.
        """
        return PrivateCAConnectorforSCEPService("pca-connector-scep", self)

    @property
    def pcs(self) -> ParallelComputingServiceService:
        """
        aioboto3 Session for ParallelComputingService service.
        """
        return ParallelComputingServiceService("pcs", self)

    @property
    def personalize(self) -> PersonalizeService:
        """
        aioboto3 Session for Personalize service.
        """
        return PersonalizeService("personalize", self)

    @property
    def personalize_events(self) -> PersonalizeEventsService:
        """
        aioboto3 Session for PersonalizeEvents service.
        """
        return PersonalizeEventsService("personalize-events", self)

    @property
    def personalize_runtime(self) -> PersonalizeRuntimeService:
        """
        aioboto3 Session for PersonalizeRuntime service.
        """
        return PersonalizeRuntimeService("personalize-runtime", self)

    @property
    def pi(self) -> PIService:
        """
        aioboto3 Session for PI service.
        """
        return PIService("pi", self)

    @property
    def pinpoint(self) -> PinpointService:
        """
        aioboto3 Session for Pinpoint service.
        """
        return PinpointService("pinpoint", self)

    @property
    def pinpoint_email(self) -> PinpointEmailService:
        """
        aioboto3 Session for PinpointEmail service.
        """
        return PinpointEmailService("pinpoint-email", self)

    @property
    def pinpoint_sms_voice(self) -> PinpointSMSVoiceService:
        """
        aioboto3 Session for PinpointSMSVoice service.
        """
        return PinpointSMSVoiceService("pinpoint-sms-voice", self)

    @property
    def pinpoint_sms_voice_v2(self) -> PinpointSMSVoiceV2Service:
        """
        aioboto3 Session for PinpointSMSVoiceV2 service.
        """
        return PinpointSMSVoiceV2Service("pinpoint-sms-voice-v2", self)

    @property
    def pipes(self) -> EventBridgePipesService:
        """
        aioboto3 Session for EventBridgePipes service.
        """
        return EventBridgePipesService("pipes", self)

    @property
    def polly(self) -> PollyService:
        """
        aioboto3 Session for Polly service.
        """
        return PollyService("polly", self)

    @property
    def pricing(self) -> PricingService:
        """
        aioboto3 Session for Pricing service.
        """
        return PricingService("pricing", self)

    @property
    def privatenetworks(self) -> Private5GService:
        """
        aioboto3 Session for Private5G service.
        """
        return Private5GService("privatenetworks", self)

    @property
    def proton(self) -> ProtonService:
        """
        aioboto3 Session for Proton service.
        """
        return ProtonService("proton", self)

    @property
    def qapps(self) -> QAppsService:
        """
        aioboto3 Session for QApps service.
        """
        return QAppsService("qapps", self)

    @property
    def qbusiness(self) -> QBusinessService:
        """
        aioboto3 Session for QBusiness service.
        """
        return QBusinessService("qbusiness", self)

    @property
    def qconnect(self) -> QConnectService:
        """
        aioboto3 Session for QConnect service.
        """
        return QConnectService("qconnect", self)

    @property
    def qldb(self) -> QLDBService:
        """
        aioboto3 Session for QLDB service.
        """
        return QLDBService("qldb", self)

    @property
    def qldb_session(self) -> QLDBSessionService:
        """
        aioboto3 Session for QLDBSession service.
        """
        return QLDBSessionService("qldb-session", self)

    @property
    def quicksight(self) -> QuickSightService:
        """
        aioboto3 Session for QuickSight service.
        """
        return QuickSightService("quicksight", self)

    @property
    def ram(self) -> RAMService:
        """
        aioboto3 Session for RAM service.
        """
        return RAMService("ram", self)

    @property
    def rbin(self) -> RecycleBinService:
        """
        aioboto3 Session for RecycleBin service.
        """
        return RecycleBinService("rbin", self)

    @property
    def rds(self) -> RDSService:
        """
        aioboto3 Session for RDS service.
        """
        return RDSService("rds", self)

    @property
    def rds_data(self) -> RDSDataServiceService:
        """
        aioboto3 Session for RDSDataService service.
        """
        return RDSDataServiceService("rds-data", self)

    @property
    def redshift(self) -> RedshiftService:
        """
        aioboto3 Session for Redshift service.
        """
        return RedshiftService("redshift", self)

    @property
    def redshift_data(self) -> RedshiftDataAPIServiceService:
        """
        aioboto3 Session for RedshiftDataAPIService service.
        """
        return RedshiftDataAPIServiceService("redshift-data", self)

    @property
    def redshift_serverless(self) -> RedshiftServerlessService:
        """
        aioboto3 Session for RedshiftServerless service.
        """
        return RedshiftServerlessService("redshift-serverless", self)

    @property
    def rekognition(self) -> RekognitionService:
        """
        aioboto3 Session for Rekognition service.
        """
        return RekognitionService("rekognition", self)

    @property
    def repostspace(self) -> RePostPrivateService:
        """
        aioboto3 Session for RePostPrivate service.
        """
        return RePostPrivateService("repostspace", self)

    @property
    def resiliencehub(self) -> ResilienceHubService:
        """
        aioboto3 Session for ResilienceHub service.
        """
        return ResilienceHubService("resiliencehub", self)

    @property
    def resource_explorer_2(self) -> ResourceExplorerService:
        """
        aioboto3 Session for ResourceExplorer service.
        """
        return ResourceExplorerService("resource-explorer-2", self)

    @property
    def resource_groups(self) -> ResourceGroupsService:
        """
        aioboto3 Session for ResourceGroups service.
        """
        return ResourceGroupsService("resource-groups", self)

    @property
    def resourcegroupstaggingapi(self) -> ResourceGroupsTaggingAPIService:
        """
        aioboto3 Session for ResourceGroupsTaggingAPI service.
        """
        return ResourceGroupsTaggingAPIService("resourcegroupstaggingapi", self)

    @property
    def robomaker(self) -> RoboMakerService:
        """
        aioboto3 Session for RoboMaker service.
        """
        return RoboMakerService("robomaker", self)

    @property
    def rolesanywhere(self) -> IAMRolesAnywhereService:
        """
        aioboto3 Session for IAMRolesAnywhere service.
        """
        return IAMRolesAnywhereService("rolesanywhere", self)

    @property
    def route53(self) -> Route53Service:
        """
        aioboto3 Session for Route53 service.
        """
        return Route53Service("route53", self)

    @property
    def route53_recovery_cluster(self) -> Route53RecoveryClusterService:
        """
        aioboto3 Session for Route53RecoveryCluster service.
        """
        return Route53RecoveryClusterService("route53-recovery-cluster", self)

    @property
    def route53_recovery_control_config(self) -> Route53RecoveryControlConfigService:
        """
        aioboto3 Session for Route53RecoveryControlConfig service.
        """
        return Route53RecoveryControlConfigService("route53-recovery-control-config", self)

    @property
    def route53_recovery_readiness(self) -> Route53RecoveryReadinessService:
        """
        aioboto3 Session for Route53RecoveryReadiness service.
        """
        return Route53RecoveryReadinessService("route53-recovery-readiness", self)

    @property
    def route53domains(self) -> Route53DomainsService:
        """
        aioboto3 Session for Route53Domains service.
        """
        return Route53DomainsService("route53domains", self)

    @property
    def route53profiles(self) -> Route53ProfilesService:
        """
        aioboto3 Session for Route53Profiles service.
        """
        return Route53ProfilesService("route53profiles", self)

    @property
    def route53resolver(self) -> Route53ResolverService:
        """
        aioboto3 Session for Route53Resolver service.
        """
        return Route53ResolverService("route53resolver", self)

    @property
    def rum(self) -> CloudWatchRUMService:
        """
        aioboto3 Session for CloudWatchRUM service.
        """
        return CloudWatchRUMService("rum", self)

    @property
    def s3(self) -> S3Service:
        """
        aioboto3 Session for S3 service.
        """
        return S3Service("s3", self)

    @property
    def s3control(self) -> S3ControlService:
        """
        aioboto3 Session for S3Control service.
        """
        return S3ControlService("s3control", self)

    @property
    def s3outposts(self) -> S3OutpostsService:
        """
        aioboto3 Session for S3Outposts service.
        """
        return S3OutpostsService("s3outposts", self)

    @property
    def s3tables(self) -> S3TablesService:
        """
        aioboto3 Session for S3Tables service.
        """
        return S3TablesService("s3tables", self)

    @property
    def sagemaker(self) -> SageMakerService:
        """
        aioboto3 Session for SageMaker service.
        """
        return SageMakerService("sagemaker", self)

    @property
    def sagemaker_a2i_runtime(self) -> AugmentedAIRuntimeService:
        """
        aioboto3 Session for AugmentedAIRuntime service.
        """
        return AugmentedAIRuntimeService("sagemaker-a2i-runtime", self)

    @property
    def sagemaker_edge(self) -> SagemakerEdgeManagerService:
        """
        aioboto3 Session for SagemakerEdgeManager service.
        """
        return SagemakerEdgeManagerService("sagemaker-edge", self)

    @property
    def sagemaker_featurestore_runtime(self) -> SageMakerFeatureStoreRuntimeService:
        """
        aioboto3 Session for SageMakerFeatureStoreRuntime service.
        """
        return SageMakerFeatureStoreRuntimeService("sagemaker-featurestore-runtime", self)

    @property
    def sagemaker_geospatial(self) -> SageMakergeospatialcapabilitiesService:
        """
        aioboto3 Session for SageMakergeospatialcapabilities service.
        """
        return SageMakergeospatialcapabilitiesService("sagemaker-geospatial", self)

    @property
    def sagemaker_metrics(self) -> SageMakerMetricsService:
        """
        aioboto3 Session for SageMakerMetrics service.
        """
        return SageMakerMetricsService("sagemaker-metrics", self)

    @property
    def sagemaker_runtime(self) -> SageMakerRuntimeService:
        """
        aioboto3 Session for SageMakerRuntime service.
        """
        return SageMakerRuntimeService("sagemaker-runtime", self)

    @property
    def savingsplans(self) -> SavingsPlansService:
        """
        aioboto3 Session for SavingsPlans service.
        """
        return SavingsPlansService("savingsplans", self)

    @property
    def scheduler(self) -> EventBridgeSchedulerService:
        """
        aioboto3 Session for EventBridgeScheduler service.
        """
        return EventBridgeSchedulerService("scheduler", self)

    @property
    def schemas(self) -> SchemasService:
        """
        aioboto3 Session for Schemas service.
        """
        return SchemasService("schemas", self)

    @property
    def sdb(self) -> SimpleDBService:
        """
        aioboto3 Session for SimpleDB service.
        """
        return SimpleDBService("sdb", self)

    @property
    def secretsmanager(self) -> SecretsManagerService:
        """
        aioboto3 Session for SecretsManager service.
        """
        return SecretsManagerService("secretsmanager", self)

    @property
    def security_ir(self) -> SecurityIncidentResponseService:
        """
        aioboto3 Session for SecurityIncidentResponse service.
        """
        return SecurityIncidentResponseService("security-ir", self)

    @property
    def securityhub(self) -> SecurityHubService:
        """
        aioboto3 Session for SecurityHub service.
        """
        return SecurityHubService("securityhub", self)

    @property
    def securitylake(self) -> SecurityLakeService:
        """
        aioboto3 Session for SecurityLake service.
        """
        return SecurityLakeService("securitylake", self)

    @property
    def serverlessrepo(self) -> ServerlessApplicationRepositoryService:
        """
        aioboto3 Session for ServerlessApplicationRepository service.
        """
        return ServerlessApplicationRepositoryService("serverlessrepo", self)

    @property
    def service_quotas(self) -> ServiceQuotasService:
        """
        aioboto3 Session for ServiceQuotas service.
        """
        return ServiceQuotasService("service-quotas", self)

    @property
    def servicecatalog(self) -> ServiceCatalogService:
        """
        aioboto3 Session for ServiceCatalog service.
        """
        return ServiceCatalogService("servicecatalog", self)

    @property
    def servicecatalog_appregistry(self) -> AppRegistryService:
        """
        aioboto3 Session for AppRegistry service.
        """
        return AppRegistryService("servicecatalog-appregistry", self)

    @property
    def servicediscovery(self) -> ServiceDiscoveryService:
        """
        aioboto3 Session for ServiceDiscovery service.
        """
        return ServiceDiscoveryService("servicediscovery", self)

    @property
    def ses(self) -> SESService:
        """
        aioboto3 Session for SES service.
        """
        return SESService("ses", self)

    @property
    def sesv2(self) -> SESV2Service:
        """
        aioboto3 Session for SESV2 service.
        """
        return SESV2Service("sesv2", self)

    @property
    def shield(self) -> ShieldService:
        """
        aioboto3 Session for Shield service.
        """
        return ShieldService("shield", self)

    @property
    def signer(self) -> SignerService:
        """
        aioboto3 Session for Signer service.
        """
        return SignerService("signer", self)

    @property
    def simspaceweaver(self) -> SimSpaceWeaverService:
        """
        aioboto3 Session for SimSpaceWeaver service.
        """
        return SimSpaceWeaverService("simspaceweaver", self)

    @property
    def sms(self) -> SMSService:
        """
        aioboto3 Session for SMS service.
        """
        return SMSService("sms", self)

    @property
    def sms_voice(self) -> SMSVoiceService:
        """
        aioboto3 Session for SMSVoice service.
        """
        return SMSVoiceService("sms-voice", self)

    @property
    def snow_device_management(self) -> SnowDeviceManagementService:
        """
        aioboto3 Session for SnowDeviceManagement service.
        """
        return SnowDeviceManagementService("snow-device-management", self)

    @property
    def snowball(self) -> SnowballService:
        """
        aioboto3 Session for Snowball service.
        """
        return SnowballService("snowball", self)

    @property
    def sns(self) -> SNSService:
        """
        aioboto3 Session for SNS service.
        """
        return SNSService("sns", self)

    @property
    def socialmessaging(self) -> EndUserMessagingSocialService:
        """
        aioboto3 Session for EndUserMessagingSocial service.
        """
        return EndUserMessagingSocialService("socialmessaging", self)

    @property
    def sqs(self) -> SQSService:
        """
        aioboto3 Session for SQS service.
        """
        return SQSService("sqs", self)

    @property
    def ssm(self) -> SSMService:
        """
        aioboto3 Session for SSM service.
        """
        return SSMService("ssm", self)

    @property
    def ssm_contacts(self) -> SSMContactsService:
        """
        aioboto3 Session for SSMContacts service.
        """
        return SSMContactsService("ssm-contacts", self)

    @property
    def ssm_incidents(self) -> SSMIncidentsService:
        """
        aioboto3 Session for SSMIncidents service.
        """
        return SSMIncidentsService("ssm-incidents", self)

    @property
    def ssm_quicksetup(self) -> SystemsManagerQuickSetupService:
        """
        aioboto3 Session for SystemsManagerQuickSetup service.
        """
        return SystemsManagerQuickSetupService("ssm-quicksetup", self)

    @property
    def ssm_sap(self) -> SsmSapService:
        """
        aioboto3 Session for SsmSap service.
        """
        return SsmSapService("ssm-sap", self)

    @property
    def sso(self) -> SSOService:
        """
        aioboto3 Session for SSO service.
        """
        return SSOService("sso", self)

    @property
    def sso_admin(self) -> SSOAdminService:
        """
        aioboto3 Session for SSOAdmin service.
        """
        return SSOAdminService("sso-admin", self)

    @property
    def sso_oidc(self) -> SSOOIDCService:
        """
        aioboto3 Session for SSOOIDC service.
        """
        return SSOOIDCService("sso-oidc", self)

    @property
    def stepfunctions(self) -> SFNService:
        """
        aioboto3 Session for SFN service.
        """
        return SFNService("stepfunctions", self)

    @property
    def storagegateway(self) -> StorageGatewayService:
        """
        aioboto3 Session for StorageGateway service.
        """
        return StorageGatewayService("storagegateway", self)

    @property
    def sts(self) -> STSService:
        """
        aioboto3 Session for STS service.
        """
        return STSService("sts", self)

    @property
    def supplychain(self) -> SupplyChainService:
        """
        aioboto3 Session for SupplyChain service.
        """
        return SupplyChainService("supplychain", self)

    @property
    def support(self) -> SupportService:
        """
        aioboto3 Session for Support service.
        """
        return SupportService("support", self)

    @property
    def support_app(self) -> SupportAppService:
        """
        aioboto3 Session for SupportApp service.
        """
        return SupportAppService("support-app", self)

    @property
    def swf(self) -> SWFService:
        """
        aioboto3 Session for SWF service.
        """
        return SWFService("swf", self)

    @property
    def synthetics(self) -> SyntheticsService:
        """
        aioboto3 Session for Synthetics service.
        """
        return SyntheticsService("synthetics", self)

    @property
    def taxsettings(self) -> TaxSettingsService:
        """
        aioboto3 Session for TaxSettings service.
        """
        return TaxSettingsService("taxsettings", self)

    @property
    def textract(self) -> TextractService:
        """
        aioboto3 Session for Textract service.
        """
        return TextractService("textract", self)

    @property
    def timestream_influxdb(self) -> TimestreamInfluxDBService:
        """
        aioboto3 Session for TimestreamInfluxDB service.
        """
        return TimestreamInfluxDBService("timestream-influxdb", self)

    @property
    def timestream_query(self) -> TimestreamQueryService:
        """
        aioboto3 Session for TimestreamQuery service.
        """
        return TimestreamQueryService("timestream-query", self)

    @property
    def timestream_write(self) -> TimestreamWriteService:
        """
        aioboto3 Session for TimestreamWrite service.
        """
        return TimestreamWriteService("timestream-write", self)

    @property
    def tnb(self) -> TelcoNetworkBuilderService:
        """
        aioboto3 Session for TelcoNetworkBuilder service.
        """
        return TelcoNetworkBuilderService("tnb", self)

    @property
    def transcribe(self) -> TranscribeServiceService:
        """
        aioboto3 Session for TranscribeService service.
        """
        return TranscribeServiceService("transcribe", self)

    @property
    def transfer(self) -> TransferService:
        """
        aioboto3 Session for Transfer service.
        """
        return TransferService("transfer", self)

    @property
    def translate(self) -> TranslateService:
        """
        aioboto3 Session for Translate service.
        """
        return TranslateService("translate", self)

    @property
    def trustedadvisor(self) -> TrustedAdvisorPublicAPIService:
        """
        aioboto3 Session for TrustedAdvisorPublicAPI service.
        """
        return TrustedAdvisorPublicAPIService("trustedadvisor", self)

    @property
    def verifiedpermissions(self) -> VerifiedPermissionsService:
        """
        aioboto3 Session for VerifiedPermissions service.
        """
        return VerifiedPermissionsService("verifiedpermissions", self)

    @property
    def voice_id(self) -> VoiceIDService:
        """
        aioboto3 Session for VoiceID service.
        """
        return VoiceIDService("voice-id", self)

    @property
    def vpc_lattice(self) -> VPCLatticeService:
        """
        aioboto3 Session for VPCLattice service.
        """
        return VPCLatticeService("vpc-lattice", self)

    @property
    def waf(self) -> WAFService:
        """
        aioboto3 Session for WAF service.
        """
        return WAFService("waf", self)

    @property
    def waf_regional(self) -> WAFRegionalService:
        """
        aioboto3 Session for WAFRegional service.
        """
        return WAFRegionalService("waf-regional", self)

    @property
    def wafv2(self) -> WAFV2Service:
        """
        aioboto3 Session for WAFV2 service.
        """
        return WAFV2Service("wafv2", self)

    @property
    def wellarchitected(self) -> WellArchitectedService:
        """
        aioboto3 Session for WellArchitected service.
        """
        return WellArchitectedService("wellarchitected", self)

    @property
    def wisdom(self) -> ConnectWisdomServiceService:
        """
        aioboto3 Session for ConnectWisdomService service.
        """
        return ConnectWisdomServiceService("wisdom", self)

    @property
    def workdocs(self) -> WorkDocsService:
        """
        aioboto3 Session for WorkDocs service.
        """
        return WorkDocsService("workdocs", self)

    @property
    def workmail(self) -> WorkMailService:
        """
        aioboto3 Session for WorkMail service.
        """
        return WorkMailService("workmail", self)

    @property
    def workmailmessageflow(self) -> WorkMailMessageFlowService:
        """
        aioboto3 Session for WorkMailMessageFlow service.
        """
        return WorkMailMessageFlowService("workmailmessageflow", self)

    @property
    def workspaces(self) -> WorkSpacesService:
        """
        aioboto3 Session for WorkSpaces service.
        """
        return WorkSpacesService("workspaces", self)

    @property
    def workspaces_thin_client(self) -> WorkSpacesThinClientService:
        """
        aioboto3 Session for WorkSpacesThinClient service.
        """
        return WorkSpacesThinClientService("workspaces-thin-client", self)

    @property
    def workspaces_web(self) -> WorkSpacesWebService:
        """
        aioboto3 Session for WorkSpacesWeb service.
        """
        return WorkSpacesWebService("workspaces-web", self)

    @property
    def xray(self) -> XRayService:
        """
        aioboto3 Session for XRay service.
        """
        return XRayService("xray", self)
