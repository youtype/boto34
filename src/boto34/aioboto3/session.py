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
    ```
"""

from aioboto3.session import Session as _Session

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
from boto34.aioboto3.services.sms_voice import PinpointSMSVoiceService
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


class Session(_Session):
    @property
    def accessanalyzer(self) -> AccessAnalyzerService:
        return AccessAnalyzerService(self)

    @property
    def account(self) -> AccountService:
        return AccountService(self)

    @property
    def acm(self) -> ACMService:
        return ACMService(self)

    @property
    def acm_pca(self) -> ACMPCAService:
        return ACMPCAService(self)

    @property
    def amp(self) -> PrometheusServiceService:
        return PrometheusServiceService(self)

    @property
    def amplify(self) -> AmplifyService:
        return AmplifyService(self)

    @property
    def amplifybackend(self) -> AmplifyBackendService:
        return AmplifyBackendService(self)

    @property
    def amplifyuibuilder(self) -> AmplifyUIBuilderService:
        return AmplifyUIBuilderService(self)

    @property
    def apigateway(self) -> APIGatewayService:
        return APIGatewayService(self)

    @property
    def apigatewaymanagementapi(self) -> ApiGatewayManagementApiService:
        return ApiGatewayManagementApiService(self)

    @property
    def apigatewayv2(self) -> ApiGatewayV2Service:
        return ApiGatewayV2Service(self)

    @property
    def appconfig(self) -> AppConfigService:
        return AppConfigService(self)

    @property
    def appconfigdata(self) -> AppConfigDataService:
        return AppConfigDataService(self)

    @property
    def appfabric(self) -> AppFabricService:
        return AppFabricService(self)

    @property
    def appflow(self) -> AppflowService:
        return AppflowService(self)

    @property
    def appintegrations(self) -> AppIntegrationsServiceService:
        return AppIntegrationsServiceService(self)

    @property
    def application_autoscaling(self) -> ApplicationAutoScalingService:
        return ApplicationAutoScalingService(self)

    @property
    def application_insights(self) -> ApplicationInsightsService:
        return ApplicationInsightsService(self)

    @property
    def application_signals(self) -> CloudWatchApplicationSignalsService:
        return CloudWatchApplicationSignalsService(self)

    @property
    def applicationcostprofiler(self) -> ApplicationCostProfilerService:
        return ApplicationCostProfilerService(self)

    @property
    def appmesh(self) -> AppMeshService:
        return AppMeshService(self)

    @property
    def apprunner(self) -> AppRunnerService:
        return AppRunnerService(self)

    @property
    def appstream(self) -> AppStreamService:
        return AppStreamService(self)

    @property
    def appsync(self) -> AppSyncService:
        return AppSyncService(self)

    @property
    def apptest(self) -> MainframeModernizationApplicationTestingService:
        return MainframeModernizationApplicationTestingService(self)

    @property
    def arc_zonal_shift(self) -> ARCZonalShiftService:
        return ARCZonalShiftService(self)

    @property
    def artifact(self) -> ArtifactService:
        return ArtifactService(self)

    @property
    def athena(self) -> AthenaService:
        return AthenaService(self)

    @property
    def auditmanager(self) -> AuditManagerService:
        return AuditManagerService(self)

    @property
    def autoscaling(self) -> AutoScalingService:
        return AutoScalingService(self)

    @property
    def autoscaling_plans(self) -> AutoScalingPlansService:
        return AutoScalingPlansService(self)

    @property
    def b2bi(self) -> B2BIService:
        return B2BIService(self)

    @property
    def backup(self) -> BackupService:
        return BackupService(self)

    @property
    def backup_gateway(self) -> BackupGatewayService:
        return BackupGatewayService(self)

    @property
    def backupsearch(self) -> BackupSearchService:
        return BackupSearchService(self)

    @property
    def batch(self) -> BatchService:
        return BatchService(self)

    @property
    def bcm_data_exports(self) -> BillingandCostManagementDataExportsService:
        return BillingandCostManagementDataExportsService(self)

    @property
    def bcm_pricing_calculator(self) -> BillingandCostManagementPricingCalculatorService:
        return BillingandCostManagementPricingCalculatorService(self)

    @property
    def bedrock(self) -> BedrockService:
        return BedrockService(self)

    @property
    def bedrock_agent(self) -> AgentsforBedrockService:
        return AgentsforBedrockService(self)

    @property
    def bedrock_agent_runtime(self) -> AgentsforBedrockRuntimeService:
        return AgentsforBedrockRuntimeService(self)

    @property
    def bedrock_data_automation(self) -> DataAutomationforBedrockService:
        return DataAutomationforBedrockService(self)

    @property
    def bedrock_data_automation_runtime(self) -> RuntimeforBedrockDataAutomationService:
        return RuntimeforBedrockDataAutomationService(self)

    @property
    def bedrock_runtime(self) -> BedrockRuntimeService:
        return BedrockRuntimeService(self)

    @property
    def billing(self) -> BillingService:
        return BillingService(self)

    @property
    def billingconductor(self) -> BillingConductorService:
        return BillingConductorService(self)

    @property
    def braket(self) -> BraketService:
        return BraketService(self)

    @property
    def budgets(self) -> BudgetsService:
        return BudgetsService(self)

    @property
    def ce(self) -> CostExplorerService:
        return CostExplorerService(self)

    @property
    def chatbot(self) -> ChatbotService:
        return ChatbotService(self)

    @property
    def chime(self) -> ChimeService:
        return ChimeService(self)

    @property
    def chime_sdk_identity(self) -> ChimeSDKIdentityService:
        return ChimeSDKIdentityService(self)

    @property
    def chime_sdk_media_pipelines(self) -> ChimeSDKMediaPipelinesService:
        return ChimeSDKMediaPipelinesService(self)

    @property
    def chime_sdk_meetings(self) -> ChimeSDKMeetingsService:
        return ChimeSDKMeetingsService(self)

    @property
    def chime_sdk_messaging(self) -> ChimeSDKMessagingService:
        return ChimeSDKMessagingService(self)

    @property
    def chime_sdk_voice(self) -> ChimeSDKVoiceService:
        return ChimeSDKVoiceService(self)

    @property
    def cleanrooms(self) -> CleanRoomsServiceService:
        return CleanRoomsServiceService(self)

    @property
    def cleanroomsml(self) -> CleanRoomsMLService:
        return CleanRoomsMLService(self)

    @property
    def cloud9(self) -> Cloud9Service:
        return Cloud9Service(self)

    @property
    def cloudcontrol(self) -> CloudControlApiService:
        return CloudControlApiService(self)

    @property
    def clouddirectory(self) -> CloudDirectoryService:
        return CloudDirectoryService(self)

    @property
    def cloudformation(self) -> CloudFormationService:
        return CloudFormationService(self)

    @property
    def cloudfront(self) -> CloudFrontService:
        return CloudFrontService(self)

    @property
    def cloudfront_keyvaluestore(self) -> CloudFrontKeyValueStoreService:
        return CloudFrontKeyValueStoreService(self)

    @property
    def cloudhsm(self) -> CloudHSMService:
        return CloudHSMService(self)

    @property
    def cloudhsmv2(self) -> CloudHSMV2Service:
        return CloudHSMV2Service(self)

    @property
    def cloudsearch(self) -> CloudSearchService:
        return CloudSearchService(self)

    @property
    def cloudsearchdomain(self) -> CloudSearchDomainService:
        return CloudSearchDomainService(self)

    @property
    def cloudtrail(self) -> CloudTrailService:
        return CloudTrailService(self)

    @property
    def cloudtrail_data(self) -> CloudTrailDataServiceService:
        return CloudTrailDataServiceService(self)

    @property
    def cloudwatch(self) -> CloudWatchService:
        return CloudWatchService(self)

    @property
    def codeartifact(self) -> CodeArtifactService:
        return CodeArtifactService(self)

    @property
    def codebuild(self) -> CodeBuildService:
        return CodeBuildService(self)

    @property
    def codecatalyst(self) -> CodeCatalystService:
        return CodeCatalystService(self)

    @property
    def codecommit(self) -> CodeCommitService:
        return CodeCommitService(self)

    @property
    def codeconnections(self) -> CodeConnectionsService:
        return CodeConnectionsService(self)

    @property
    def codedeploy(self) -> CodeDeployService:
        return CodeDeployService(self)

    @property
    def codeguru_reviewer(self) -> CodeGuruReviewerService:
        return CodeGuruReviewerService(self)

    @property
    def codeguru_security(self) -> CodeGuruSecurityService:
        return CodeGuruSecurityService(self)

    @property
    def codeguruprofiler(self) -> CodeGuruProfilerService:
        return CodeGuruProfilerService(self)

    @property
    def codepipeline(self) -> CodePipelineService:
        return CodePipelineService(self)

    @property
    def codestar_connections(self) -> CodeStarconnectionsService:
        return CodeStarconnectionsService(self)

    @property
    def codestar_notifications(self) -> CodeStarNotificationsService:
        return CodeStarNotificationsService(self)

    @property
    def cognito_identity(self) -> CognitoIdentityService:
        return CognitoIdentityService(self)

    @property
    def cognito_idp(self) -> CognitoIdentityProviderService:
        return CognitoIdentityProviderService(self)

    @property
    def cognito_sync(self) -> CognitoSyncService:
        return CognitoSyncService(self)

    @property
    def comprehend(self) -> ComprehendService:
        return ComprehendService(self)

    @property
    def comprehendmedical(self) -> ComprehendMedicalService:
        return ComprehendMedicalService(self)

    @property
    def compute_optimizer(self) -> ComputeOptimizerService:
        return ComputeOptimizerService(self)

    @property
    def config(self) -> ConfigServiceService:
        return ConfigServiceService(self)

    @property
    def connect(self) -> ConnectService:
        return ConnectService(self)

    @property
    def connect_contact_lens(self) -> ConnectContactLensService:
        return ConnectContactLensService(self)

    @property
    def connectcampaigns(self) -> ConnectCampaignServiceService:
        return ConnectCampaignServiceService(self)

    @property
    def connectcampaignsv2(self) -> ConnectCampaignServiceV2Service:
        return ConnectCampaignServiceV2Service(self)

    @property
    def connectcases(self) -> ConnectCasesService:
        return ConnectCasesService(self)

    @property
    def connectparticipant(self) -> ConnectParticipantService:
        return ConnectParticipantService(self)

    @property
    def controlcatalog(self) -> ControlCatalogService:
        return ControlCatalogService(self)

    @property
    def controltower(self) -> ControlTowerService:
        return ControlTowerService(self)

    @property
    def cost_optimization_hub(self) -> CostOptimizationHubService:
        return CostOptimizationHubService(self)

    @property
    def cur(self) -> CostandUsageReportServiceService:
        return CostandUsageReportServiceService(self)

    @property
    def customer_profiles(self) -> CustomerProfilesService:
        return CustomerProfilesService(self)

    @property
    def databrew(self) -> GlueDataBrewService:
        return GlueDataBrewService(self)

    @property
    def dataexchange(self) -> DataExchangeService:
        return DataExchangeService(self)

    @property
    def datapipeline(self) -> DataPipelineService:
        return DataPipelineService(self)

    @property
    def datasync(self) -> DataSyncService:
        return DataSyncService(self)

    @property
    def datazone(self) -> DataZoneService:
        return DataZoneService(self)

    @property
    def dax(self) -> DAXService:
        return DAXService(self)

    @property
    def deadline(self) -> DeadlineCloudService:
        return DeadlineCloudService(self)

    @property
    def detective(self) -> DetectiveService:
        return DetectiveService(self)

    @property
    def devicefarm(self) -> DeviceFarmService:
        return DeviceFarmService(self)

    @property
    def devops_guru(self) -> DevOpsGuruService:
        return DevOpsGuruService(self)

    @property
    def directconnect(self) -> DirectConnectService:
        return DirectConnectService(self)

    @property
    def discovery(self) -> ApplicationDiscoveryServiceService:
        return ApplicationDiscoveryServiceService(self)

    @property
    def dlm(self) -> DLMService:
        return DLMService(self)

    @property
    def dms(self) -> DatabaseMigrationServiceService:
        return DatabaseMigrationServiceService(self)

    @property
    def docdb(self) -> DocDBService:
        return DocDBService(self)

    @property
    def docdb_elastic(self) -> DocDBElasticService:
        return DocDBElasticService(self)

    @property
    def drs(self) -> DrsService:
        return DrsService(self)

    @property
    def ds(self) -> DirectoryServiceService:
        return DirectoryServiceService(self)

    @property
    def ds_data(self) -> DirectoryServiceDataService:
        return DirectoryServiceDataService(self)

    @property
    def dsql(self) -> AuroraDSQLService:
        return AuroraDSQLService(self)

    @property
    def dynamodb(self) -> DynamoDBService:
        return DynamoDBService(self)

    @property
    def dynamodbstreams(self) -> DynamoDBStreamsService:
        return DynamoDBStreamsService(self)

    @property
    def ebs(self) -> EBSService:
        return EBSService(self)

    @property
    def ec2(self) -> EC2Service:
        return EC2Service(self)

    @property
    def ec2_instance_connect(self) -> EC2InstanceConnectService:
        return EC2InstanceConnectService(self)

    @property
    def ecr(self) -> ECRService:
        return ECRService(self)

    @property
    def ecr_public(self) -> ECRPublicService:
        return ECRPublicService(self)

    @property
    def ecs(self) -> ECSService:
        return ECSService(self)

    @property
    def efs(self) -> EFSService:
        return EFSService(self)

    @property
    def eks(self) -> EKSService:
        return EKSService(self)

    @property
    def eks_auth(self) -> EKSAuthService:
        return EKSAuthService(self)

    @property
    def elasticache(self) -> ElastiCacheService:
        return ElastiCacheService(self)

    @property
    def elasticbeanstalk(self) -> ElasticBeanstalkService:
        return ElasticBeanstalkService(self)

    @property
    def elastictranscoder(self) -> ElasticTranscoderService:
        return ElasticTranscoderService(self)

    @property
    def elb(self) -> ElasticLoadBalancingService:
        return ElasticLoadBalancingService(self)

    @property
    def elbv2(self) -> ElasticLoadBalancingv2Service:
        return ElasticLoadBalancingv2Service(self)

    @property
    def emr(self) -> EMRService:
        return EMRService(self)

    @property
    def emr_containers(self) -> EMRContainersService:
        return EMRContainersService(self)

    @property
    def emr_serverless(self) -> EMRServerlessService:
        return EMRServerlessService(self)

    @property
    def entityresolution(self) -> EntityResolutionService:
        return EntityResolutionService(self)

    @property
    def es(self) -> ElasticsearchServiceService:
        return ElasticsearchServiceService(self)

    @property
    def events(self) -> EventBridgeService:
        return EventBridgeService(self)

    @property
    def evidently(self) -> CloudWatchEvidentlyService:
        return CloudWatchEvidentlyService(self)

    @property
    def finspace(self) -> FinspaceService:
        return FinspaceService(self)

    @property
    def finspace_data(self) -> FinSpaceDataService:
        return FinSpaceDataService(self)

    @property
    def firehose(self) -> FirehoseService:
        return FirehoseService(self)

    @property
    def fis(self) -> FISService:
        return FISService(self)

    @property
    def fms(self) -> FMSService:
        return FMSService(self)

    @property
    def forecast(self) -> ForecastServiceService:
        return ForecastServiceService(self)

    @property
    def forecastquery(self) -> ForecastQueryServiceService:
        return ForecastQueryServiceService(self)

    @property
    def frauddetector(self) -> FraudDetectorService:
        return FraudDetectorService(self)

    @property
    def freetier(self) -> FreeTierService:
        return FreeTierService(self)

    @property
    def fsx(self) -> FSxService:
        return FSxService(self)

    @property
    def gamelift(self) -> GameLiftService:
        return GameLiftService(self)

    @property
    def geo_maps(self) -> LocationServiceMapsV2Service:
        return LocationServiceMapsV2Service(self)

    @property
    def geo_places(self) -> LocationServicePlacesV2Service:
        return LocationServicePlacesV2Service(self)

    @property
    def geo_routes(self) -> LocationServiceRoutesV2Service:
        return LocationServiceRoutesV2Service(self)

    @property
    def glacier(self) -> GlacierService:
        return GlacierService(self)

    @property
    def globalaccelerator(self) -> GlobalAcceleratorService:
        return GlobalAcceleratorService(self)

    @property
    def glue(self) -> GlueService:
        return GlueService(self)

    @property
    def grafana(self) -> ManagedGrafanaService:
        return ManagedGrafanaService(self)

    @property
    def greengrass(self) -> GreengrassService:
        return GreengrassService(self)

    @property
    def greengrassv2(self) -> GreengrassV2Service:
        return GreengrassV2Service(self)

    @property
    def groundstation(self) -> GroundStationService:
        return GroundStationService(self)

    @property
    def guardduty(self) -> GuardDutyService:
        return GuardDutyService(self)

    @property
    def health(self) -> HealthService:
        return HealthService(self)

    @property
    def healthlake(self) -> HealthLakeService:
        return HealthLakeService(self)

    @property
    def iam(self) -> IAMService:
        return IAMService(self)

    @property
    def identitystore(self) -> IdentityStoreService:
        return IdentityStoreService(self)

    @property
    def imagebuilder(self) -> ImagebuilderService:
        return ImagebuilderService(self)

    @property
    def importexport(self) -> ImportExportService:
        return ImportExportService(self)

    @property
    def inspector(self) -> InspectorService:
        return InspectorService(self)

    @property
    def inspector_scan(self) -> InspectorscanService:
        return InspectorscanService(self)

    @property
    def inspector2(self) -> Inspector2Service:
        return Inspector2Service(self)

    @property
    def internetmonitor(self) -> CloudWatchInternetMonitorService:
        return CloudWatchInternetMonitorService(self)

    @property
    def invoicing(self) -> InvoicingService:
        return InvoicingService(self)

    @property
    def iot(self) -> IoTService:
        return IoTService(self)

    @property
    def iot_data(self) -> IoTDataPlaneService:
        return IoTDataPlaneService(self)

    @property
    def iot_jobs_data(self) -> IoTJobsDataPlaneService:
        return IoTJobsDataPlaneService(self)

    @property
    def iotanalytics(self) -> IoTAnalyticsService:
        return IoTAnalyticsService(self)

    @property
    def iotdeviceadvisor(self) -> IoTDeviceAdvisorService:
        return IoTDeviceAdvisorService(self)

    @property
    def iotevents(self) -> IoTEventsService:
        return IoTEventsService(self)

    @property
    def iotevents_data(self) -> IoTEventsDataService:
        return IoTEventsDataService(self)

    @property
    def iotfleethub(self) -> IoTFleetHubService:
        return IoTFleetHubService(self)

    @property
    def iotfleetwise(self) -> IoTFleetWiseService:
        return IoTFleetWiseService(self)

    @property
    def iotsecuretunneling(self) -> IoTSecureTunnelingService:
        return IoTSecureTunnelingService(self)

    @property
    def iotsitewise(self) -> IoTSiteWiseService:
        return IoTSiteWiseService(self)

    @property
    def iotthingsgraph(self) -> IoTThingsGraphService:
        return IoTThingsGraphService(self)

    @property
    def iottwinmaker(self) -> IoTTwinMakerService:
        return IoTTwinMakerService(self)

    @property
    def iotwireless(self) -> IoTWirelessService:
        return IoTWirelessService(self)

    @property
    def ivs(self) -> IVSService:
        return IVSService(self)

    @property
    def ivs_realtime(self) -> IvsrealtimeService:
        return IvsrealtimeService(self)

    @property
    def ivschat(self) -> IvschatService:
        return IvschatService(self)

    @property
    def kafka(self) -> KafkaService:
        return KafkaService(self)

    @property
    def kafkaconnect(self) -> KafkaConnectService:
        return KafkaConnectService(self)

    @property
    def kendra(self) -> KendraService:
        return KendraService(self)

    @property
    def kendra_ranking(self) -> KendraRankingService:
        return KendraRankingService(self)

    @property
    def keyspaces(self) -> KeyspacesService:
        return KeyspacesService(self)

    @property
    def kinesis(self) -> KinesisService:
        return KinesisService(self)

    @property
    def kinesis_video_archived_media(self) -> KinesisVideoArchivedMediaService:
        return KinesisVideoArchivedMediaService(self)

    @property
    def kinesis_video_media(self) -> KinesisVideoMediaService:
        return KinesisVideoMediaService(self)

    @property
    def kinesis_video_signaling(self) -> KinesisVideoSignalingChannelsService:
        return KinesisVideoSignalingChannelsService(self)

    @property
    def kinesis_video_webrtc_storage(self) -> KinesisVideoWebRTCStorageService:
        return KinesisVideoWebRTCStorageService(self)

    @property
    def kinesisanalytics(self) -> KinesisAnalyticsService:
        return KinesisAnalyticsService(self)

    @property
    def kinesisanalyticsv2(self) -> KinesisAnalyticsV2Service:
        return KinesisAnalyticsV2Service(self)

    @property
    def kinesisvideo(self) -> KinesisVideoService:
        return KinesisVideoService(self)

    @property
    def kms(self) -> KMSService:
        return KMSService(self)

    @property
    def lakeformation(self) -> LakeFormationService:
        return LakeFormationService(self)

    @property
    def lambda_(self) -> LambdaService:
        return LambdaService(self)

    @property
    def launch_wizard(self) -> LaunchWizardService:
        return LaunchWizardService(self)

    @property
    def lex_models(self) -> LexModelBuildingServiceService:
        return LexModelBuildingServiceService(self)

    @property
    def lex_runtime(self) -> LexRuntimeServiceService:
        return LexRuntimeServiceService(self)

    @property
    def lexv2_models(self) -> LexModelsV2Service:
        return LexModelsV2Service(self)

    @property
    def lexv2_runtime(self) -> LexRuntimeV2Service:
        return LexRuntimeV2Service(self)

    @property
    def license_manager(self) -> LicenseManagerService:
        return LicenseManagerService(self)

    @property
    def license_manager_linux_subscriptions(self) -> LicenseManagerLinuxSubscriptionsService:
        return LicenseManagerLinuxSubscriptionsService(self)

    @property
    def license_manager_user_subscriptions(self) -> LicenseManagerUserSubscriptionsService:
        return LicenseManagerUserSubscriptionsService(self)

    @property
    def lightsail(self) -> LightsailService:
        return LightsailService(self)

    @property
    def location(self) -> LocationServiceService:
        return LocationServiceService(self)

    @property
    def logs(self) -> CloudWatchLogsService:
        return CloudWatchLogsService(self)

    @property
    def lookoutequipment(self) -> LookoutEquipmentService:
        return LookoutEquipmentService(self)

    @property
    def lookoutmetrics(self) -> LookoutMetricsService:
        return LookoutMetricsService(self)

    @property
    def lookoutvision(self) -> LookoutforVisionService:
        return LookoutforVisionService(self)

    @property
    def m2(self) -> MainframeModernizationService:
        return MainframeModernizationService(self)

    @property
    def machinelearning(self) -> MachineLearningService:
        return MachineLearningService(self)

    @property
    def macie2(self) -> Macie2Service:
        return Macie2Service(self)

    @property
    def mailmanager(self) -> MailManagerService:
        return MailManagerService(self)

    @property
    def managedblockchain(self) -> ManagedBlockchainService:
        return ManagedBlockchainService(self)

    @property
    def managedblockchain_query(self) -> ManagedBlockchainQueryService:
        return ManagedBlockchainQueryService(self)

    @property
    def marketplace_agreement(self) -> AgreementServiceService:
        return AgreementServiceService(self)

    @property
    def marketplace_catalog(self) -> MarketplaceCatalogService:
        return MarketplaceCatalogService(self)

    @property
    def marketplace_deployment(self) -> MarketplaceDeploymentServiceService:
        return MarketplaceDeploymentServiceService(self)

    @property
    def marketplace_entitlement(self) -> MarketplaceEntitlementServiceService:
        return MarketplaceEntitlementServiceService(self)

    @property
    def marketplace_reporting(self) -> MarketplaceReportingServiceService:
        return MarketplaceReportingServiceService(self)

    @property
    def marketplacecommerceanalytics(self) -> MarketplaceCommerceAnalyticsService:
        return MarketplaceCommerceAnalyticsService(self)

    @property
    def mediaconnect(self) -> MediaConnectService:
        return MediaConnectService(self)

    @property
    def mediaconvert(self) -> MediaConvertService:
        return MediaConvertService(self)

    @property
    def medialive(self) -> MediaLiveService:
        return MediaLiveService(self)

    @property
    def mediapackage(self) -> MediaPackageService:
        return MediaPackageService(self)

    @property
    def mediapackage_vod(self) -> MediaPackageVodService:
        return MediaPackageVodService(self)

    @property
    def mediapackagev2(self) -> Mediapackagev2Service:
        return Mediapackagev2Service(self)

    @property
    def mediastore(self) -> MediaStoreService:
        return MediaStoreService(self)

    @property
    def mediastore_data(self) -> MediaStoreDataService:
        return MediaStoreDataService(self)

    @property
    def mediatailor(self) -> MediaTailorService:
        return MediaTailorService(self)

    @property
    def medical_imaging(self) -> HealthImagingService:
        return HealthImagingService(self)

    @property
    def memorydb(self) -> MemoryDBService:
        return MemoryDBService(self)

    @property
    def meteringmarketplace(self) -> MarketplaceMeteringService:
        return MarketplaceMeteringService(self)

    @property
    def mgh(self) -> MigrationHubService:
        return MigrationHubService(self)

    @property
    def mgn(self) -> MgnService:
        return MgnService(self)

    @property
    def migration_hub_refactor_spaces(self) -> MigrationHubRefactorSpacesService:
        return MigrationHubRefactorSpacesService(self)

    @property
    def migrationhub_config(self) -> MigrationHubConfigService:
        return MigrationHubConfigService(self)

    @property
    def migrationhuborchestrator(self) -> MigrationHubOrchestratorService:
        return MigrationHubOrchestratorService(self)

    @property
    def migrationhubstrategy(self) -> MigrationHubStrategyRecommendationsService:
        return MigrationHubStrategyRecommendationsService(self)

    @property
    def mq(self) -> MQService:
        return MQService(self)

    @property
    def mturk(self) -> MTurkService:
        return MTurkService(self)

    @property
    def mwaa(self) -> MWAAService:
        return MWAAService(self)

    @property
    def neptune(self) -> NeptuneService:
        return NeptuneService(self)

    @property
    def neptune_graph(self) -> NeptuneGraphService:
        return NeptuneGraphService(self)

    @property
    def neptunedata(self) -> NeptuneDataService:
        return NeptuneDataService(self)

    @property
    def network_firewall(self) -> NetworkFirewallService:
        return NetworkFirewallService(self)

    @property
    def networkflowmonitor(self) -> NetworkFlowMonitorService:
        return NetworkFlowMonitorService(self)

    @property
    def networkmanager(self) -> NetworkManagerService:
        return NetworkManagerService(self)

    @property
    def networkmonitor(self) -> CloudWatchNetworkMonitorService:
        return CloudWatchNetworkMonitorService(self)

    @property
    def notifications(self) -> UserNotificationsService:
        return UserNotificationsService(self)

    @property
    def notificationscontacts(self) -> UserNotificationsContactsService:
        return UserNotificationsContactsService(self)

    @property
    def oam(self) -> CloudWatchObservabilityAccessManagerService:
        return CloudWatchObservabilityAccessManagerService(self)

    @property
    def observabilityadmin(self) -> CloudWatchObservabilityAdminServiceService:
        return CloudWatchObservabilityAdminServiceService(self)

    @property
    def omics(self) -> OmicsService:
        return OmicsService(self)

    @property
    def opensearch(self) -> OpenSearchServiceService:
        return OpenSearchServiceService(self)

    @property
    def opensearchserverless(self) -> OpenSearchServiceServerlessService:
        return OpenSearchServiceServerlessService(self)

    @property
    def opsworks(self) -> OpsWorksService:
        return OpsWorksService(self)

    @property
    def opsworkscm(self) -> OpsWorksCMService:
        return OpsWorksCMService(self)

    @property
    def organizations(self) -> OrganizationsService:
        return OrganizationsService(self)

    @property
    def osis(self) -> OpenSearchIngestionService:
        return OpenSearchIngestionService(self)

    @property
    def outposts(self) -> OutpostsService:
        return OutpostsService(self)

    @property
    def panorama(self) -> PanoramaService:
        return PanoramaService(self)

    @property
    def partnercentral_selling(self) -> PartnerCentralSellingAPIService:
        return PartnerCentralSellingAPIService(self)

    @property
    def payment_cryptography(self) -> PaymentCryptographyControlPlaneService:
        return PaymentCryptographyControlPlaneService(self)

    @property
    def payment_cryptography_data(self) -> PaymentCryptographyDataPlaneService:
        return PaymentCryptographyDataPlaneService(self)

    @property
    def pca_connector_ad(self) -> PcaConnectorAdService:
        return PcaConnectorAdService(self)

    @property
    def pca_connector_scep(self) -> PrivateCAConnectorforSCEPService:
        return PrivateCAConnectorforSCEPService(self)

    @property
    def pcs(self) -> ParallelComputingServiceService:
        return ParallelComputingServiceService(self)

    @property
    def personalize(self) -> PersonalizeService:
        return PersonalizeService(self)

    @property
    def personalize_events(self) -> PersonalizeEventsService:
        return PersonalizeEventsService(self)

    @property
    def personalize_runtime(self) -> PersonalizeRuntimeService:
        return PersonalizeRuntimeService(self)

    @property
    def pi(self) -> PIService:
        return PIService(self)

    @property
    def pinpoint(self) -> PinpointService:
        return PinpointService(self)

    @property
    def pinpoint_email(self) -> PinpointEmailService:
        return PinpointEmailService(self)

    @property
    def pinpoint_sms_voice(self) -> PinpointSMSVoiceService:
        return PinpointSMSVoiceService(self)

    @property
    def pinpoint_sms_voice_v2(self) -> PinpointSMSVoiceV2Service:
        return PinpointSMSVoiceV2Service(self)

    @property
    def pipes(self) -> EventBridgePipesService:
        return EventBridgePipesService(self)

    @property
    def polly(self) -> PollyService:
        return PollyService(self)

    @property
    def pricing(self) -> PricingService:
        return PricingService(self)

    @property
    def privatenetworks(self) -> Private5GService:
        return Private5GService(self)

    @property
    def proton(self) -> ProtonService:
        return ProtonService(self)

    @property
    def qapps(self) -> QAppsService:
        return QAppsService(self)

    @property
    def qbusiness(self) -> QBusinessService:
        return QBusinessService(self)

    @property
    def qconnect(self) -> QConnectService:
        return QConnectService(self)

    @property
    def qldb(self) -> QLDBService:
        return QLDBService(self)

    @property
    def qldb_session(self) -> QLDBSessionService:
        return QLDBSessionService(self)

    @property
    def quicksight(self) -> QuickSightService:
        return QuickSightService(self)

    @property
    def ram(self) -> RAMService:
        return RAMService(self)

    @property
    def rbin(self) -> RecycleBinService:
        return RecycleBinService(self)

    @property
    def rds(self) -> RDSService:
        return RDSService(self)

    @property
    def rds_data(self) -> RDSDataServiceService:
        return RDSDataServiceService(self)

    @property
    def redshift(self) -> RedshiftService:
        return RedshiftService(self)

    @property
    def redshift_data(self) -> RedshiftDataAPIServiceService:
        return RedshiftDataAPIServiceService(self)

    @property
    def redshift_serverless(self) -> RedshiftServerlessService:
        return RedshiftServerlessService(self)

    @property
    def rekognition(self) -> RekognitionService:
        return RekognitionService(self)

    @property
    def repostspace(self) -> RePostPrivateService:
        return RePostPrivateService(self)

    @property
    def resiliencehub(self) -> ResilienceHubService:
        return ResilienceHubService(self)

    @property
    def resource_explorer_2(self) -> ResourceExplorerService:
        return ResourceExplorerService(self)

    @property
    def resource_groups(self) -> ResourceGroupsService:
        return ResourceGroupsService(self)

    @property
    def resourcegroupstaggingapi(self) -> ResourceGroupsTaggingAPIService:
        return ResourceGroupsTaggingAPIService(self)

    @property
    def robomaker(self) -> RoboMakerService:
        return RoboMakerService(self)

    @property
    def rolesanywhere(self) -> IAMRolesAnywhereService:
        return IAMRolesAnywhereService(self)

    @property
    def route53(self) -> Route53Service:
        return Route53Service(self)

    @property
    def route53_recovery_cluster(self) -> Route53RecoveryClusterService:
        return Route53RecoveryClusterService(self)

    @property
    def route53_recovery_control_config(self) -> Route53RecoveryControlConfigService:
        return Route53RecoveryControlConfigService(self)

    @property
    def route53_recovery_readiness(self) -> Route53RecoveryReadinessService:
        return Route53RecoveryReadinessService(self)

    @property
    def route53domains(self) -> Route53DomainsService:
        return Route53DomainsService(self)

    @property
    def route53profiles(self) -> Route53ProfilesService:
        return Route53ProfilesService(self)

    @property
    def route53resolver(self) -> Route53ResolverService:
        return Route53ResolverService(self)

    @property
    def rum(self) -> CloudWatchRUMService:
        return CloudWatchRUMService(self)

    @property
    def s3(self) -> S3Service:
        return S3Service(self)

    @property
    def s3control(self) -> S3ControlService:
        return S3ControlService(self)

    @property
    def s3outposts(self) -> S3OutpostsService:
        return S3OutpostsService(self)

    @property
    def s3tables(self) -> S3TablesService:
        return S3TablesService(self)

    @property
    def sagemaker(self) -> SageMakerService:
        return SageMakerService(self)

    @property
    def sagemaker_a2i_runtime(self) -> AugmentedAIRuntimeService:
        return AugmentedAIRuntimeService(self)

    @property
    def sagemaker_edge(self) -> SagemakerEdgeManagerService:
        return SagemakerEdgeManagerService(self)

    @property
    def sagemaker_featurestore_runtime(self) -> SageMakerFeatureStoreRuntimeService:
        return SageMakerFeatureStoreRuntimeService(self)

    @property
    def sagemaker_geospatial(self) -> SageMakergeospatialcapabilitiesService:
        return SageMakergeospatialcapabilitiesService(self)

    @property
    def sagemaker_metrics(self) -> SageMakerMetricsService:
        return SageMakerMetricsService(self)

    @property
    def sagemaker_runtime(self) -> SageMakerRuntimeService:
        return SageMakerRuntimeService(self)

    @property
    def savingsplans(self) -> SavingsPlansService:
        return SavingsPlansService(self)

    @property
    def scheduler(self) -> EventBridgeSchedulerService:
        return EventBridgeSchedulerService(self)

    @property
    def schemas(self) -> SchemasService:
        return SchemasService(self)

    @property
    def sdb(self) -> SimpleDBService:
        return SimpleDBService(self)

    @property
    def secretsmanager(self) -> SecretsManagerService:
        return SecretsManagerService(self)

    @property
    def security_ir(self) -> SecurityIncidentResponseService:
        return SecurityIncidentResponseService(self)

    @property
    def securityhub(self) -> SecurityHubService:
        return SecurityHubService(self)

    @property
    def securitylake(self) -> SecurityLakeService:
        return SecurityLakeService(self)

    @property
    def serverlessrepo(self) -> ServerlessApplicationRepositoryService:
        return ServerlessApplicationRepositoryService(self)

    @property
    def service_quotas(self) -> ServiceQuotasService:
        return ServiceQuotasService(self)

    @property
    def servicecatalog(self) -> ServiceCatalogService:
        return ServiceCatalogService(self)

    @property
    def servicecatalog_appregistry(self) -> AppRegistryService:
        return AppRegistryService(self)

    @property
    def servicediscovery(self) -> ServiceDiscoveryService:
        return ServiceDiscoveryService(self)

    @property
    def ses(self) -> SESService:
        return SESService(self)

    @property
    def sesv2(self) -> SESV2Service:
        return SESV2Service(self)

    @property
    def shield(self) -> ShieldService:
        return ShieldService(self)

    @property
    def signer(self) -> SignerService:
        return SignerService(self)

    @property
    def simspaceweaver(self) -> SimSpaceWeaverService:
        return SimSpaceWeaverService(self)

    @property
    def sms(self) -> SMSService:
        return SMSService(self)

    @property
    def sms_voice(self) -> PinpointSMSVoiceService:
        return PinpointSMSVoiceService(self)

    @property
    def snow_device_management(self) -> SnowDeviceManagementService:
        return SnowDeviceManagementService(self)

    @property
    def snowball(self) -> SnowballService:
        return SnowballService(self)

    @property
    def sns(self) -> SNSService:
        return SNSService(self)

    @property
    def socialmessaging(self) -> EndUserMessagingSocialService:
        return EndUserMessagingSocialService(self)

    @property
    def sqs(self) -> SQSService:
        return SQSService(self)

    @property
    def ssm(self) -> SSMService:
        return SSMService(self)

    @property
    def ssm_contacts(self) -> SSMContactsService:
        return SSMContactsService(self)

    @property
    def ssm_incidents(self) -> SSMIncidentsService:
        return SSMIncidentsService(self)

    @property
    def ssm_quicksetup(self) -> SystemsManagerQuickSetupService:
        return SystemsManagerQuickSetupService(self)

    @property
    def ssm_sap(self) -> SsmSapService:
        return SsmSapService(self)

    @property
    def sso(self) -> SSOService:
        return SSOService(self)

    @property
    def sso_admin(self) -> SSOAdminService:
        return SSOAdminService(self)

    @property
    def sso_oidc(self) -> SSOOIDCService:
        return SSOOIDCService(self)

    @property
    def stepfunctions(self) -> SFNService:
        return SFNService(self)

    @property
    def storagegateway(self) -> StorageGatewayService:
        return StorageGatewayService(self)

    @property
    def sts(self) -> STSService:
        return STSService(self)

    @property
    def supplychain(self) -> SupplyChainService:
        return SupplyChainService(self)

    @property
    def support(self) -> SupportService:
        return SupportService(self)

    @property
    def support_app(self) -> SupportAppService:
        return SupportAppService(self)

    @property
    def swf(self) -> SWFService:
        return SWFService(self)

    @property
    def synthetics(self) -> SyntheticsService:
        return SyntheticsService(self)

    @property
    def taxsettings(self) -> TaxSettingsService:
        return TaxSettingsService(self)

    @property
    def textract(self) -> TextractService:
        return TextractService(self)

    @property
    def timestream_influxdb(self) -> TimestreamInfluxDBService:
        return TimestreamInfluxDBService(self)

    @property
    def timestream_query(self) -> TimestreamQueryService:
        return TimestreamQueryService(self)

    @property
    def timestream_write(self) -> TimestreamWriteService:
        return TimestreamWriteService(self)

    @property
    def tnb(self) -> TelcoNetworkBuilderService:
        return TelcoNetworkBuilderService(self)

    @property
    def transcribe(self) -> TranscribeServiceService:
        return TranscribeServiceService(self)

    @property
    def transfer(self) -> TransferService:
        return TransferService(self)

    @property
    def translate(self) -> TranslateService:
        return TranslateService(self)

    @property
    def trustedadvisor(self) -> TrustedAdvisorPublicAPIService:
        return TrustedAdvisorPublicAPIService(self)

    @property
    def verifiedpermissions(self) -> VerifiedPermissionsService:
        return VerifiedPermissionsService(self)

    @property
    def voice_id(self) -> VoiceIDService:
        return VoiceIDService(self)

    @property
    def vpc_lattice(self) -> VPCLatticeService:
        return VPCLatticeService(self)

    @property
    def waf(self) -> WAFService:
        return WAFService(self)

    @property
    def waf_regional(self) -> WAFRegionalService:
        return WAFRegionalService(self)

    @property
    def wafv2(self) -> WAFV2Service:
        return WAFV2Service(self)

    @property
    def wellarchitected(self) -> WellArchitectedService:
        return WellArchitectedService(self)

    @property
    def wisdom(self) -> ConnectWisdomServiceService:
        return ConnectWisdomServiceService(self)

    @property
    def workdocs(self) -> WorkDocsService:
        return WorkDocsService(self)

    @property
    def workmail(self) -> WorkMailService:
        return WorkMailService(self)

    @property
    def workmailmessageflow(self) -> WorkMailMessageFlowService:
        return WorkMailMessageFlowService(self)

    @property
    def workspaces(self) -> WorkSpacesService:
        return WorkSpacesService(self)

    @property
    def workspaces_thin_client(self) -> WorkSpacesThinClientService:
        return WorkSpacesThinClientService(self)

    @property
    def workspaces_web(self) -> WorkSpacesWebService:
        return WorkSpacesWebService(self)

    @property
    def xray(self) -> XRayService:
        return XRayService(self)
