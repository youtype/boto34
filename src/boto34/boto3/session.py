"""
Type annotated wrapper for boto3 Session.

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # s3_client is botocore.BaseClient
    # with type annotations only in type checking mode
    s3_client = session.s3.client()
    client.list_buckets()

    # s3_resource is boto3.ServiceResource
    # with type annotations only in type checking mode
    s3_resource = session.s3.resource()
    s3_resource.Bucket("bucket").objects.all()
    ```
"""

from boto3.session import Session as Boto3Session

from boto34.boto3.services.accessanalyzer import AccessAnalyzerService
from boto34.boto3.services.account import AccountService
from boto34.boto3.services.acm import ACMService
from boto34.boto3.services.acm_pca import ACMPCAService
from boto34.boto3.services.amp import PrometheusServiceService
from boto34.boto3.services.amplify import AmplifyService
from boto34.boto3.services.amplifybackend import AmplifyBackendService
from boto34.boto3.services.amplifyuibuilder import AmplifyUIBuilderService
from boto34.boto3.services.apigateway import APIGatewayService
from boto34.boto3.services.apigatewaymanagementapi import ApiGatewayManagementApiService
from boto34.boto3.services.apigatewayv2 import ApiGatewayV2Service
from boto34.boto3.services.appconfig import AppConfigService
from boto34.boto3.services.appconfigdata import AppConfigDataService
from boto34.boto3.services.appfabric import AppFabricService
from boto34.boto3.services.appflow import AppflowService
from boto34.boto3.services.appintegrations import AppIntegrationsServiceService
from boto34.boto3.services.application_autoscaling import ApplicationAutoScalingService
from boto34.boto3.services.application_insights import ApplicationInsightsService
from boto34.boto3.services.application_signals import CloudWatchApplicationSignalsService
from boto34.boto3.services.applicationcostprofiler import ApplicationCostProfilerService
from boto34.boto3.services.appmesh import AppMeshService
from boto34.boto3.services.apprunner import AppRunnerService
from boto34.boto3.services.appstream import AppStreamService
from boto34.boto3.services.appsync import AppSyncService
from boto34.boto3.services.apptest import MainframeModernizationApplicationTestingService
from boto34.boto3.services.arc_zonal_shift import ARCZonalShiftService
from boto34.boto3.services.artifact import ArtifactService
from boto34.boto3.services.athena import AthenaService
from boto34.boto3.services.auditmanager import AuditManagerService
from boto34.boto3.services.autoscaling import AutoScalingService
from boto34.boto3.services.autoscaling_plans import AutoScalingPlansService
from boto34.boto3.services.b2bi import B2BIService
from boto34.boto3.services.backup import BackupService
from boto34.boto3.services.backup_gateway import BackupGatewayService
from boto34.boto3.services.backupsearch import BackupSearchService
from boto34.boto3.services.batch import BatchService
from boto34.boto3.services.bcm_data_exports import BillingandCostManagementDataExportsService
from boto34.boto3.services.bcm_pricing_calculator import (
    BillingandCostManagementPricingCalculatorService,
)
from boto34.boto3.services.bedrock import BedrockService
from boto34.boto3.services.bedrock_agent import AgentsforBedrockService
from boto34.boto3.services.bedrock_agent_runtime import AgentsforBedrockRuntimeService
from boto34.boto3.services.bedrock_data_automation import DataAutomationforBedrockService
from boto34.boto3.services.bedrock_data_automation_runtime import (
    RuntimeforBedrockDataAutomationService,
)
from boto34.boto3.services.bedrock_runtime import BedrockRuntimeService
from boto34.boto3.services.billing import BillingService
from boto34.boto3.services.billingconductor import BillingConductorService
from boto34.boto3.services.braket import BraketService
from boto34.boto3.services.budgets import BudgetsService
from boto34.boto3.services.ce import CostExplorerService
from boto34.boto3.services.chatbot import ChatbotService
from boto34.boto3.services.chime import ChimeService
from boto34.boto3.services.chime_sdk_identity import ChimeSDKIdentityService
from boto34.boto3.services.chime_sdk_media_pipelines import ChimeSDKMediaPipelinesService
from boto34.boto3.services.chime_sdk_meetings import ChimeSDKMeetingsService
from boto34.boto3.services.chime_sdk_messaging import ChimeSDKMessagingService
from boto34.boto3.services.chime_sdk_voice import ChimeSDKVoiceService
from boto34.boto3.services.cleanrooms import CleanRoomsServiceService
from boto34.boto3.services.cleanroomsml import CleanRoomsMLService
from boto34.boto3.services.cloud9 import Cloud9Service
from boto34.boto3.services.cloudcontrol import CloudControlApiService
from boto34.boto3.services.clouddirectory import CloudDirectoryService
from boto34.boto3.services.cloudformation import CloudFormationService
from boto34.boto3.services.cloudfront import CloudFrontService
from boto34.boto3.services.cloudfront_keyvaluestore import CloudFrontKeyValueStoreService
from boto34.boto3.services.cloudhsm import CloudHSMService
from boto34.boto3.services.cloudhsmv2 import CloudHSMV2Service
from boto34.boto3.services.cloudsearch import CloudSearchService
from boto34.boto3.services.cloudsearchdomain import CloudSearchDomainService
from boto34.boto3.services.cloudtrail import CloudTrailService
from boto34.boto3.services.cloudtrail_data import CloudTrailDataServiceService
from boto34.boto3.services.cloudwatch import CloudWatchService
from boto34.boto3.services.codeartifact import CodeArtifactService
from boto34.boto3.services.codebuild import CodeBuildService
from boto34.boto3.services.codecatalyst import CodeCatalystService
from boto34.boto3.services.codecommit import CodeCommitService
from boto34.boto3.services.codeconnections import CodeConnectionsService
from boto34.boto3.services.codedeploy import CodeDeployService
from boto34.boto3.services.codeguru_reviewer import CodeGuruReviewerService
from boto34.boto3.services.codeguru_security import CodeGuruSecurityService
from boto34.boto3.services.codeguruprofiler import CodeGuruProfilerService
from boto34.boto3.services.codepipeline import CodePipelineService
from boto34.boto3.services.codestar_connections import CodeStarconnectionsService
from boto34.boto3.services.codestar_notifications import CodeStarNotificationsService
from boto34.boto3.services.cognito_identity import CognitoIdentityService
from boto34.boto3.services.cognito_idp import CognitoIdentityProviderService
from boto34.boto3.services.cognito_sync import CognitoSyncService
from boto34.boto3.services.comprehend import ComprehendService
from boto34.boto3.services.comprehendmedical import ComprehendMedicalService
from boto34.boto3.services.compute_optimizer import ComputeOptimizerService
from boto34.boto3.services.config import ConfigServiceService
from boto34.boto3.services.connect import ConnectService
from boto34.boto3.services.connect_contact_lens import ConnectContactLensService
from boto34.boto3.services.connectcampaigns import ConnectCampaignServiceService
from boto34.boto3.services.connectcampaignsv2 import ConnectCampaignServiceV2Service
from boto34.boto3.services.connectcases import ConnectCasesService
from boto34.boto3.services.connectparticipant import ConnectParticipantService
from boto34.boto3.services.controlcatalog import ControlCatalogService
from boto34.boto3.services.controltower import ControlTowerService
from boto34.boto3.services.cost_optimization_hub import CostOptimizationHubService
from boto34.boto3.services.cur import CostandUsageReportServiceService
from boto34.boto3.services.customer_profiles import CustomerProfilesService
from boto34.boto3.services.databrew import GlueDataBrewService
from boto34.boto3.services.dataexchange import DataExchangeService
from boto34.boto3.services.datapipeline import DataPipelineService
from boto34.boto3.services.datasync import DataSyncService
from boto34.boto3.services.datazone import DataZoneService
from boto34.boto3.services.dax import DAXService
from boto34.boto3.services.deadline import DeadlineCloudService
from boto34.boto3.services.detective import DetectiveService
from boto34.boto3.services.devicefarm import DeviceFarmService
from boto34.boto3.services.devops_guru import DevOpsGuruService
from boto34.boto3.services.directconnect import DirectConnectService
from boto34.boto3.services.discovery import ApplicationDiscoveryServiceService
from boto34.boto3.services.dlm import DLMService
from boto34.boto3.services.dms import DatabaseMigrationServiceService
from boto34.boto3.services.docdb import DocDBService
from boto34.boto3.services.docdb_elastic import DocDBElasticService
from boto34.boto3.services.drs import DrsService
from boto34.boto3.services.ds import DirectoryServiceService
from boto34.boto3.services.ds_data import DirectoryServiceDataService
from boto34.boto3.services.dsql import AuroraDSQLService
from boto34.boto3.services.dynamodb import DynamoDBService
from boto34.boto3.services.dynamodbstreams import DynamoDBStreamsService
from boto34.boto3.services.ebs import EBSService
from boto34.boto3.services.ec2 import EC2Service
from boto34.boto3.services.ec2_instance_connect import EC2InstanceConnectService
from boto34.boto3.services.ecr import ECRService
from boto34.boto3.services.ecr_public import ECRPublicService
from boto34.boto3.services.ecs import ECSService
from boto34.boto3.services.efs import EFSService
from boto34.boto3.services.eks import EKSService
from boto34.boto3.services.eks_auth import EKSAuthService
from boto34.boto3.services.elasticache import ElastiCacheService
from boto34.boto3.services.elasticbeanstalk import ElasticBeanstalkService
from boto34.boto3.services.elastictranscoder import ElasticTranscoderService
from boto34.boto3.services.elb import ElasticLoadBalancingService
from boto34.boto3.services.elbv2 import ElasticLoadBalancingv2Service
from boto34.boto3.services.emr import EMRService
from boto34.boto3.services.emr_containers import EMRContainersService
from boto34.boto3.services.emr_serverless import EMRServerlessService
from boto34.boto3.services.entityresolution import EntityResolutionService
from boto34.boto3.services.es import ElasticsearchServiceService
from boto34.boto3.services.events import EventBridgeService
from boto34.boto3.services.evidently import CloudWatchEvidentlyService
from boto34.boto3.services.finspace import FinspaceService
from boto34.boto3.services.finspace_data import FinSpaceDataService
from boto34.boto3.services.firehose import FirehoseService
from boto34.boto3.services.fis import FISService
from boto34.boto3.services.fms import FMSService
from boto34.boto3.services.forecast import ForecastServiceService
from boto34.boto3.services.forecastquery import ForecastQueryServiceService
from boto34.boto3.services.frauddetector import FraudDetectorService
from boto34.boto3.services.freetier import FreeTierService
from boto34.boto3.services.fsx import FSxService
from boto34.boto3.services.gamelift import GameLiftService
from boto34.boto3.services.geo_maps import LocationServiceMapsV2Service
from boto34.boto3.services.geo_places import LocationServicePlacesV2Service
from boto34.boto3.services.geo_routes import LocationServiceRoutesV2Service
from boto34.boto3.services.glacier import GlacierService
from boto34.boto3.services.globalaccelerator import GlobalAcceleratorService
from boto34.boto3.services.glue import GlueService
from boto34.boto3.services.grafana import ManagedGrafanaService
from boto34.boto3.services.greengrass import GreengrassService
from boto34.boto3.services.greengrassv2 import GreengrassV2Service
from boto34.boto3.services.groundstation import GroundStationService
from boto34.boto3.services.guardduty import GuardDutyService
from boto34.boto3.services.health import HealthService
from boto34.boto3.services.healthlake import HealthLakeService
from boto34.boto3.services.iam import IAMService
from boto34.boto3.services.identitystore import IdentityStoreService
from boto34.boto3.services.imagebuilder import ImagebuilderService
from boto34.boto3.services.importexport import ImportExportService
from boto34.boto3.services.inspector import InspectorService
from boto34.boto3.services.inspector2 import Inspector2Service
from boto34.boto3.services.inspector_scan import InspectorscanService
from boto34.boto3.services.internetmonitor import CloudWatchInternetMonitorService
from boto34.boto3.services.invoicing import InvoicingService
from boto34.boto3.services.iot import IoTService
from boto34.boto3.services.iot_data import IoTDataPlaneService
from boto34.boto3.services.iot_jobs_data import IoTJobsDataPlaneService
from boto34.boto3.services.iotanalytics import IoTAnalyticsService
from boto34.boto3.services.iotdeviceadvisor import IoTDeviceAdvisorService
from boto34.boto3.services.iotevents import IoTEventsService
from boto34.boto3.services.iotevents_data import IoTEventsDataService
from boto34.boto3.services.iotfleethub import IoTFleetHubService
from boto34.boto3.services.iotfleetwise import IoTFleetWiseService
from boto34.boto3.services.iotsecuretunneling import IoTSecureTunnelingService
from boto34.boto3.services.iotsitewise import IoTSiteWiseService
from boto34.boto3.services.iotthingsgraph import IoTThingsGraphService
from boto34.boto3.services.iottwinmaker import IoTTwinMakerService
from boto34.boto3.services.iotwireless import IoTWirelessService
from boto34.boto3.services.ivs import IVSService
from boto34.boto3.services.ivs_realtime import IvsrealtimeService
from boto34.boto3.services.ivschat import IvschatService
from boto34.boto3.services.kafka import KafkaService
from boto34.boto3.services.kafkaconnect import KafkaConnectService
from boto34.boto3.services.kendra import KendraService
from boto34.boto3.services.kendra_ranking import KendraRankingService
from boto34.boto3.services.keyspaces import KeyspacesService
from boto34.boto3.services.kinesis import KinesisService
from boto34.boto3.services.kinesis_video_archived_media import KinesisVideoArchivedMediaService
from boto34.boto3.services.kinesis_video_media import KinesisVideoMediaService
from boto34.boto3.services.kinesis_video_signaling import KinesisVideoSignalingChannelsService
from boto34.boto3.services.kinesis_video_webrtc_storage import KinesisVideoWebRTCStorageService
from boto34.boto3.services.kinesisanalytics import KinesisAnalyticsService
from boto34.boto3.services.kinesisanalyticsv2 import KinesisAnalyticsV2Service
from boto34.boto3.services.kinesisvideo import KinesisVideoService
from boto34.boto3.services.kms import KMSService
from boto34.boto3.services.lakeformation import LakeFormationService
from boto34.boto3.services.lambda_ import LambdaService
from boto34.boto3.services.launch_wizard import LaunchWizardService
from boto34.boto3.services.lex_models import LexModelBuildingServiceService
from boto34.boto3.services.lex_runtime import LexRuntimeServiceService
from boto34.boto3.services.lexv2_models import LexModelsV2Service
from boto34.boto3.services.lexv2_runtime import LexRuntimeV2Service
from boto34.boto3.services.license_manager import LicenseManagerService
from boto34.boto3.services.license_manager_linux_subscriptions import (
    LicenseManagerLinuxSubscriptionsService,
)
from boto34.boto3.services.license_manager_user_subscriptions import (
    LicenseManagerUserSubscriptionsService,
)
from boto34.boto3.services.lightsail import LightsailService
from boto34.boto3.services.location import LocationServiceService
from boto34.boto3.services.logs import CloudWatchLogsService
from boto34.boto3.services.lookoutequipment import LookoutEquipmentService
from boto34.boto3.services.lookoutmetrics import LookoutMetricsService
from boto34.boto3.services.lookoutvision import LookoutforVisionService
from boto34.boto3.services.m2 import MainframeModernizationService
from boto34.boto3.services.machinelearning import MachineLearningService
from boto34.boto3.services.macie2 import Macie2Service
from boto34.boto3.services.mailmanager import MailManagerService
from boto34.boto3.services.managedblockchain import ManagedBlockchainService
from boto34.boto3.services.managedblockchain_query import ManagedBlockchainQueryService
from boto34.boto3.services.marketplace_agreement import AgreementServiceService
from boto34.boto3.services.marketplace_catalog import MarketplaceCatalogService
from boto34.boto3.services.marketplace_deployment import MarketplaceDeploymentServiceService
from boto34.boto3.services.marketplace_entitlement import MarketplaceEntitlementServiceService
from boto34.boto3.services.marketplace_reporting import MarketplaceReportingServiceService
from boto34.boto3.services.marketplacecommerceanalytics import MarketplaceCommerceAnalyticsService
from boto34.boto3.services.mediaconnect import MediaConnectService
from boto34.boto3.services.mediaconvert import MediaConvertService
from boto34.boto3.services.medialive import MediaLiveService
from boto34.boto3.services.mediapackage import MediaPackageService
from boto34.boto3.services.mediapackage_vod import MediaPackageVodService
from boto34.boto3.services.mediapackagev2 import Mediapackagev2Service
from boto34.boto3.services.mediastore import MediaStoreService
from boto34.boto3.services.mediastore_data import MediaStoreDataService
from boto34.boto3.services.mediatailor import MediaTailorService
from boto34.boto3.services.medical_imaging import HealthImagingService
from boto34.boto3.services.memorydb import MemoryDBService
from boto34.boto3.services.meteringmarketplace import MarketplaceMeteringService
from boto34.boto3.services.mgh import MigrationHubService
from boto34.boto3.services.mgn import MgnService
from boto34.boto3.services.migration_hub_refactor_spaces import MigrationHubRefactorSpacesService
from boto34.boto3.services.migrationhub_config import MigrationHubConfigService
from boto34.boto3.services.migrationhuborchestrator import MigrationHubOrchestratorService
from boto34.boto3.services.migrationhubstrategy import MigrationHubStrategyRecommendationsService
from boto34.boto3.services.mq import MQService
from boto34.boto3.services.mturk import MTurkService
from boto34.boto3.services.mwaa import MWAAService
from boto34.boto3.services.neptune import NeptuneService
from boto34.boto3.services.neptune_graph import NeptuneGraphService
from boto34.boto3.services.neptunedata import NeptuneDataService
from boto34.boto3.services.network_firewall import NetworkFirewallService
from boto34.boto3.services.networkflowmonitor import NetworkFlowMonitorService
from boto34.boto3.services.networkmanager import NetworkManagerService
from boto34.boto3.services.networkmonitor import CloudWatchNetworkMonitorService
from boto34.boto3.services.notifications import UserNotificationsService
from boto34.boto3.services.notificationscontacts import UserNotificationsContactsService
from boto34.boto3.services.oam import CloudWatchObservabilityAccessManagerService
from boto34.boto3.services.observabilityadmin import CloudWatchObservabilityAdminServiceService
from boto34.boto3.services.omics import OmicsService
from boto34.boto3.services.opensearch import OpenSearchServiceService
from boto34.boto3.services.opensearchserverless import OpenSearchServiceServerlessService
from boto34.boto3.services.opsworks import OpsWorksService
from boto34.boto3.services.opsworkscm import OpsWorksCMService
from boto34.boto3.services.organizations import OrganizationsService
from boto34.boto3.services.osis import OpenSearchIngestionService
from boto34.boto3.services.outposts import OutpostsService
from boto34.boto3.services.panorama import PanoramaService
from boto34.boto3.services.partnercentral_selling import PartnerCentralSellingAPIService
from boto34.boto3.services.payment_cryptography import PaymentCryptographyControlPlaneService
from boto34.boto3.services.payment_cryptography_data import PaymentCryptographyDataPlaneService
from boto34.boto3.services.pca_connector_ad import PcaConnectorAdService
from boto34.boto3.services.pca_connector_scep import PrivateCAConnectorforSCEPService
from boto34.boto3.services.pcs import ParallelComputingServiceService
from boto34.boto3.services.personalize import PersonalizeService
from boto34.boto3.services.personalize_events import PersonalizeEventsService
from boto34.boto3.services.personalize_runtime import PersonalizeRuntimeService
from boto34.boto3.services.pi import PIService
from boto34.boto3.services.pinpoint import PinpointService
from boto34.boto3.services.pinpoint_email import PinpointEmailService
from boto34.boto3.services.pinpoint_sms_voice import PinpointSMSVoiceService
from boto34.boto3.services.pinpoint_sms_voice_v2 import PinpointSMSVoiceV2Service
from boto34.boto3.services.pipes import EventBridgePipesService
from boto34.boto3.services.polly import PollyService
from boto34.boto3.services.pricing import PricingService
from boto34.boto3.services.privatenetworks import Private5GService
from boto34.boto3.services.proton import ProtonService
from boto34.boto3.services.qapps import QAppsService
from boto34.boto3.services.qbusiness import QBusinessService
from boto34.boto3.services.qconnect import QConnectService
from boto34.boto3.services.qldb import QLDBService
from boto34.boto3.services.qldb_session import QLDBSessionService
from boto34.boto3.services.quicksight import QuickSightService
from boto34.boto3.services.ram import RAMService
from boto34.boto3.services.rbin import RecycleBinService
from boto34.boto3.services.rds import RDSService
from boto34.boto3.services.rds_data import RDSDataServiceService
from boto34.boto3.services.redshift import RedshiftService
from boto34.boto3.services.redshift_data import RedshiftDataAPIServiceService
from boto34.boto3.services.redshift_serverless import RedshiftServerlessService
from boto34.boto3.services.rekognition import RekognitionService
from boto34.boto3.services.repostspace import RePostPrivateService
from boto34.boto3.services.resiliencehub import ResilienceHubService
from boto34.boto3.services.resource_explorer_2 import ResourceExplorerService
from boto34.boto3.services.resource_groups import ResourceGroupsService
from boto34.boto3.services.resourcegroupstaggingapi import ResourceGroupsTaggingAPIService
from boto34.boto3.services.robomaker import RoboMakerService
from boto34.boto3.services.rolesanywhere import IAMRolesAnywhereService
from boto34.boto3.services.route53 import Route53Service
from boto34.boto3.services.route53_recovery_cluster import Route53RecoveryClusterService
from boto34.boto3.services.route53_recovery_control_config import (
    Route53RecoveryControlConfigService,
)
from boto34.boto3.services.route53_recovery_readiness import Route53RecoveryReadinessService
from boto34.boto3.services.route53domains import Route53DomainsService
from boto34.boto3.services.route53profiles import Route53ProfilesService
from boto34.boto3.services.route53resolver import Route53ResolverService
from boto34.boto3.services.rum import CloudWatchRUMService
from boto34.boto3.services.s3 import S3Service
from boto34.boto3.services.s3control import S3ControlService
from boto34.boto3.services.s3outposts import S3OutpostsService
from boto34.boto3.services.s3tables import S3TablesService
from boto34.boto3.services.sagemaker import SageMakerService
from boto34.boto3.services.sagemaker_a2i_runtime import AugmentedAIRuntimeService
from boto34.boto3.services.sagemaker_edge import SagemakerEdgeManagerService
from boto34.boto3.services.sagemaker_featurestore_runtime import SageMakerFeatureStoreRuntimeService
from boto34.boto3.services.sagemaker_geospatial import SageMakergeospatialcapabilitiesService
from boto34.boto3.services.sagemaker_metrics import SageMakerMetricsService
from boto34.boto3.services.sagemaker_runtime import SageMakerRuntimeService
from boto34.boto3.services.savingsplans import SavingsPlansService
from boto34.boto3.services.scheduler import EventBridgeSchedulerService
from boto34.boto3.services.schemas import SchemasService
from boto34.boto3.services.sdb import SimpleDBService
from boto34.boto3.services.secretsmanager import SecretsManagerService
from boto34.boto3.services.security_ir import SecurityIncidentResponseService
from boto34.boto3.services.securityhub import SecurityHubService
from boto34.boto3.services.securitylake import SecurityLakeService
from boto34.boto3.services.serverlessrepo import ServerlessApplicationRepositoryService
from boto34.boto3.services.service_quotas import ServiceQuotasService
from boto34.boto3.services.servicecatalog import ServiceCatalogService
from boto34.boto3.services.servicecatalog_appregistry import AppRegistryService
from boto34.boto3.services.servicediscovery import ServiceDiscoveryService
from boto34.boto3.services.ses import SESService
from boto34.boto3.services.sesv2 import SESV2Service
from boto34.boto3.services.shield import ShieldService
from boto34.boto3.services.signer import SignerService
from boto34.boto3.services.simspaceweaver import SimSpaceWeaverService
from boto34.boto3.services.sms import SMSService
from boto34.boto3.services.sms_voice import SMSVoiceService
from boto34.boto3.services.snow_device_management import SnowDeviceManagementService
from boto34.boto3.services.snowball import SnowballService
from boto34.boto3.services.sns import SNSService
from boto34.boto3.services.socialmessaging import EndUserMessagingSocialService
from boto34.boto3.services.sqs import SQSService
from boto34.boto3.services.ssm import SSMService
from boto34.boto3.services.ssm_contacts import SSMContactsService
from boto34.boto3.services.ssm_incidents import SSMIncidentsService
from boto34.boto3.services.ssm_quicksetup import SystemsManagerQuickSetupService
from boto34.boto3.services.ssm_sap import SsmSapService
from boto34.boto3.services.sso import SSOService
from boto34.boto3.services.sso_admin import SSOAdminService
from boto34.boto3.services.sso_oidc import SSOOIDCService
from boto34.boto3.services.stepfunctions import SFNService
from boto34.boto3.services.storagegateway import StorageGatewayService
from boto34.boto3.services.sts import STSService
from boto34.boto3.services.supplychain import SupplyChainService
from boto34.boto3.services.support import SupportService
from boto34.boto3.services.support_app import SupportAppService
from boto34.boto3.services.swf import SWFService
from boto34.boto3.services.synthetics import SyntheticsService
from boto34.boto3.services.taxsettings import TaxSettingsService
from boto34.boto3.services.textract import TextractService
from boto34.boto3.services.timestream_influxdb import TimestreamInfluxDBService
from boto34.boto3.services.timestream_query import TimestreamQueryService
from boto34.boto3.services.timestream_write import TimestreamWriteService
from boto34.boto3.services.tnb import TelcoNetworkBuilderService
from boto34.boto3.services.transcribe import TranscribeServiceService
from boto34.boto3.services.transfer import TransferService
from boto34.boto3.services.translate import TranslateService
from boto34.boto3.services.trustedadvisor import TrustedAdvisorPublicAPIService
from boto34.boto3.services.verifiedpermissions import VerifiedPermissionsService
from boto34.boto3.services.voice_id import VoiceIDService
from boto34.boto3.services.vpc_lattice import VPCLatticeService
from boto34.boto3.services.waf import WAFService
from boto34.boto3.services.waf_regional import WAFRegionalService
from boto34.boto3.services.wafv2 import WAFV2Service
from boto34.boto3.services.wellarchitected import WellArchitectedService
from boto34.boto3.services.wisdom import ConnectWisdomServiceService
from boto34.boto3.services.workdocs import WorkDocsService
from boto34.boto3.services.workmail import WorkMailService
from boto34.boto3.services.workmailmessageflow import WorkMailMessageFlowService
from boto34.boto3.services.workspaces import WorkSpacesService
from boto34.boto3.services.workspaces_thin_client import WorkSpacesThinClientService
from boto34.boto3.services.workspaces_web import WorkSpacesWebService
from boto34.boto3.services.xray import XRayService


class Session(Boto3Session):
    @property
    def accessanalyzer(self) -> AccessAnalyzerService:
        """
        boto3 Session for AccessAnalyzer service.
        """
        return AccessAnalyzerService("accessanalyzer", self)

    @property
    def account(self) -> AccountService:
        """
        boto3 Session for Account service.
        """
        return AccountService("account", self)

    @property
    def acm(self) -> ACMService:
        """
        boto3 Session for ACM service.
        """
        return ACMService("acm", self)

    @property
    def acm_pca(self) -> ACMPCAService:
        """
        boto3 Session for ACMPCA service.
        """
        return ACMPCAService("acm-pca", self)

    @property
    def amp(self) -> PrometheusServiceService:
        """
        boto3 Session for PrometheusService service.
        """
        return PrometheusServiceService("amp", self)

    @property
    def amplify(self) -> AmplifyService:
        """
        boto3 Session for Amplify service.
        """
        return AmplifyService("amplify", self)

    @property
    def amplifybackend(self) -> AmplifyBackendService:
        """
        boto3 Session for AmplifyBackend service.
        """
        return AmplifyBackendService("amplifybackend", self)

    @property
    def amplifyuibuilder(self) -> AmplifyUIBuilderService:
        """
        boto3 Session for AmplifyUIBuilder service.
        """
        return AmplifyUIBuilderService("amplifyuibuilder", self)

    @property
    def apigateway(self) -> APIGatewayService:
        """
        boto3 Session for APIGateway service.
        """
        return APIGatewayService("apigateway", self)

    @property
    def apigatewaymanagementapi(self) -> ApiGatewayManagementApiService:
        """
        boto3 Session for ApiGatewayManagementApi service.
        """
        return ApiGatewayManagementApiService("apigatewaymanagementapi", self)

    @property
    def apigatewayv2(self) -> ApiGatewayV2Service:
        """
        boto3 Session for ApiGatewayV2 service.
        """
        return ApiGatewayV2Service("apigatewayv2", self)

    @property
    def appconfig(self) -> AppConfigService:
        """
        boto3 Session for AppConfig service.
        """
        return AppConfigService("appconfig", self)

    @property
    def appconfigdata(self) -> AppConfigDataService:
        """
        boto3 Session for AppConfigData service.
        """
        return AppConfigDataService("appconfigdata", self)

    @property
    def appfabric(self) -> AppFabricService:
        """
        boto3 Session for AppFabric service.
        """
        return AppFabricService("appfabric", self)

    @property
    def appflow(self) -> AppflowService:
        """
        boto3 Session for Appflow service.
        """
        return AppflowService("appflow", self)

    @property
    def appintegrations(self) -> AppIntegrationsServiceService:
        """
        boto3 Session for AppIntegrationsService service.
        """
        return AppIntegrationsServiceService("appintegrations", self)

    @property
    def application_autoscaling(self) -> ApplicationAutoScalingService:
        """
        boto3 Session for ApplicationAutoScaling service.
        """
        return ApplicationAutoScalingService("application-autoscaling", self)

    @property
    def application_insights(self) -> ApplicationInsightsService:
        """
        boto3 Session for ApplicationInsights service.
        """
        return ApplicationInsightsService("application-insights", self)

    @property
    def application_signals(self) -> CloudWatchApplicationSignalsService:
        """
        boto3 Session for CloudWatchApplicationSignals service.
        """
        return CloudWatchApplicationSignalsService("application-signals", self)

    @property
    def applicationcostprofiler(self) -> ApplicationCostProfilerService:
        """
        boto3 Session for ApplicationCostProfiler service.
        """
        return ApplicationCostProfilerService("applicationcostprofiler", self)

    @property
    def appmesh(self) -> AppMeshService:
        """
        boto3 Session for AppMesh service.
        """
        return AppMeshService("appmesh", self)

    @property
    def apprunner(self) -> AppRunnerService:
        """
        boto3 Session for AppRunner service.
        """
        return AppRunnerService("apprunner", self)

    @property
    def appstream(self) -> AppStreamService:
        """
        boto3 Session for AppStream service.
        """
        return AppStreamService("appstream", self)

    @property
    def appsync(self) -> AppSyncService:
        """
        boto3 Session for AppSync service.
        """
        return AppSyncService("appsync", self)

    @property
    def apptest(self) -> MainframeModernizationApplicationTestingService:
        """
        boto3 Session for MainframeModernizationApplicationTesting service.
        """
        return MainframeModernizationApplicationTestingService("apptest", self)

    @property
    def arc_zonal_shift(self) -> ARCZonalShiftService:
        """
        boto3 Session for ARCZonalShift service.
        """
        return ARCZonalShiftService("arc-zonal-shift", self)

    @property
    def artifact(self) -> ArtifactService:
        """
        boto3 Session for Artifact service.
        """
        return ArtifactService("artifact", self)

    @property
    def athena(self) -> AthenaService:
        """
        boto3 Session for Athena service.
        """
        return AthenaService("athena", self)

    @property
    def auditmanager(self) -> AuditManagerService:
        """
        boto3 Session for AuditManager service.
        """
        return AuditManagerService("auditmanager", self)

    @property
    def autoscaling(self) -> AutoScalingService:
        """
        boto3 Session for AutoScaling service.
        """
        return AutoScalingService("autoscaling", self)

    @property
    def autoscaling_plans(self) -> AutoScalingPlansService:
        """
        boto3 Session for AutoScalingPlans service.
        """
        return AutoScalingPlansService("autoscaling-plans", self)

    @property
    def b2bi(self) -> B2BIService:
        """
        boto3 Session for B2BI service.
        """
        return B2BIService("b2bi", self)

    @property
    def backup(self) -> BackupService:
        """
        boto3 Session for Backup service.
        """
        return BackupService("backup", self)

    @property
    def backup_gateway(self) -> BackupGatewayService:
        """
        boto3 Session for BackupGateway service.
        """
        return BackupGatewayService("backup-gateway", self)

    @property
    def backupsearch(self) -> BackupSearchService:
        """
        boto3 Session for BackupSearch service.
        """
        return BackupSearchService("backupsearch", self)

    @property
    def batch(self) -> BatchService:
        """
        boto3 Session for Batch service.
        """
        return BatchService("batch", self)

    @property
    def bcm_data_exports(self) -> BillingandCostManagementDataExportsService:
        """
        boto3 Session for BillingandCostManagementDataExports service.
        """
        return BillingandCostManagementDataExportsService("bcm-data-exports", self)

    @property
    def bcm_pricing_calculator(self) -> BillingandCostManagementPricingCalculatorService:
        """
        boto3 Session for BillingandCostManagementPricingCalculator service.
        """
        return BillingandCostManagementPricingCalculatorService("bcm-pricing-calculator", self)

    @property
    def bedrock(self) -> BedrockService:
        """
        boto3 Session for Bedrock service.
        """
        return BedrockService("bedrock", self)

    @property
    def bedrock_agent(self) -> AgentsforBedrockService:
        """
        boto3 Session for AgentsforBedrock service.
        """
        return AgentsforBedrockService("bedrock-agent", self)

    @property
    def bedrock_agent_runtime(self) -> AgentsforBedrockRuntimeService:
        """
        boto3 Session for AgentsforBedrockRuntime service.
        """
        return AgentsforBedrockRuntimeService("bedrock-agent-runtime", self)

    @property
    def bedrock_data_automation(self) -> DataAutomationforBedrockService:
        """
        boto3 Session for DataAutomationforBedrock service.
        """
        return DataAutomationforBedrockService("bedrock-data-automation", self)

    @property
    def bedrock_data_automation_runtime(self) -> RuntimeforBedrockDataAutomationService:
        """
        boto3 Session for RuntimeforBedrockDataAutomation service.
        """
        return RuntimeforBedrockDataAutomationService("bedrock-data-automation-runtime", self)

    @property
    def bedrock_runtime(self) -> BedrockRuntimeService:
        """
        boto3 Session for BedrockRuntime service.
        """
        return BedrockRuntimeService("bedrock-runtime", self)

    @property
    def billing(self) -> BillingService:
        """
        boto3 Session for Billing service.
        """
        return BillingService("billing", self)

    @property
    def billingconductor(self) -> BillingConductorService:
        """
        boto3 Session for BillingConductor service.
        """
        return BillingConductorService("billingconductor", self)

    @property
    def braket(self) -> BraketService:
        """
        boto3 Session for Braket service.
        """
        return BraketService("braket", self)

    @property
    def budgets(self) -> BudgetsService:
        """
        boto3 Session for Budgets service.
        """
        return BudgetsService("budgets", self)

    @property
    def ce(self) -> CostExplorerService:
        """
        boto3 Session for CostExplorer service.
        """
        return CostExplorerService("ce", self)

    @property
    def chatbot(self) -> ChatbotService:
        """
        boto3 Session for Chatbot service.
        """
        return ChatbotService("chatbot", self)

    @property
    def chime(self) -> ChimeService:
        """
        boto3 Session for Chime service.
        """
        return ChimeService("chime", self)

    @property
    def chime_sdk_identity(self) -> ChimeSDKIdentityService:
        """
        boto3 Session for ChimeSDKIdentity service.
        """
        return ChimeSDKIdentityService("chime-sdk-identity", self)

    @property
    def chime_sdk_media_pipelines(self) -> ChimeSDKMediaPipelinesService:
        """
        boto3 Session for ChimeSDKMediaPipelines service.
        """
        return ChimeSDKMediaPipelinesService("chime-sdk-media-pipelines", self)

    @property
    def chime_sdk_meetings(self) -> ChimeSDKMeetingsService:
        """
        boto3 Session for ChimeSDKMeetings service.
        """
        return ChimeSDKMeetingsService("chime-sdk-meetings", self)

    @property
    def chime_sdk_messaging(self) -> ChimeSDKMessagingService:
        """
        boto3 Session for ChimeSDKMessaging service.
        """
        return ChimeSDKMessagingService("chime-sdk-messaging", self)

    @property
    def chime_sdk_voice(self) -> ChimeSDKVoiceService:
        """
        boto3 Session for ChimeSDKVoice service.
        """
        return ChimeSDKVoiceService("chime-sdk-voice", self)

    @property
    def cleanrooms(self) -> CleanRoomsServiceService:
        """
        boto3 Session for CleanRoomsService service.
        """
        return CleanRoomsServiceService("cleanrooms", self)

    @property
    def cleanroomsml(self) -> CleanRoomsMLService:
        """
        boto3 Session for CleanRoomsML service.
        """
        return CleanRoomsMLService("cleanroomsml", self)

    @property
    def cloud9(self) -> Cloud9Service:
        """
        boto3 Session for Cloud9 service.
        """
        return Cloud9Service("cloud9", self)

    @property
    def cloudcontrol(self) -> CloudControlApiService:
        """
        boto3 Session for CloudControlApi service.
        """
        return CloudControlApiService("cloudcontrol", self)

    @property
    def clouddirectory(self) -> CloudDirectoryService:
        """
        boto3 Session for CloudDirectory service.
        """
        return CloudDirectoryService("clouddirectory", self)

    @property
    def cloudformation(self) -> CloudFormationService:
        """
        boto3 Session for CloudFormation service.
        """
        return CloudFormationService("cloudformation", self)

    @property
    def cloudfront(self) -> CloudFrontService:
        """
        boto3 Session for CloudFront service.
        """
        return CloudFrontService("cloudfront", self)

    @property
    def cloudfront_keyvaluestore(self) -> CloudFrontKeyValueStoreService:
        """
        boto3 Session for CloudFrontKeyValueStore service.
        """
        return CloudFrontKeyValueStoreService("cloudfront-keyvaluestore", self)

    @property
    def cloudhsm(self) -> CloudHSMService:
        """
        boto3 Session for CloudHSM service.
        """
        return CloudHSMService("cloudhsm", self)

    @property
    def cloudhsmv2(self) -> CloudHSMV2Service:
        """
        boto3 Session for CloudHSMV2 service.
        """
        return CloudHSMV2Service("cloudhsmv2", self)

    @property
    def cloudsearch(self) -> CloudSearchService:
        """
        boto3 Session for CloudSearch service.
        """
        return CloudSearchService("cloudsearch", self)

    @property
    def cloudsearchdomain(self) -> CloudSearchDomainService:
        """
        boto3 Session for CloudSearchDomain service.
        """
        return CloudSearchDomainService("cloudsearchdomain", self)

    @property
    def cloudtrail(self) -> CloudTrailService:
        """
        boto3 Session for CloudTrail service.
        """
        return CloudTrailService("cloudtrail", self)

    @property
    def cloudtrail_data(self) -> CloudTrailDataServiceService:
        """
        boto3 Session for CloudTrailDataService service.
        """
        return CloudTrailDataServiceService("cloudtrail-data", self)

    @property
    def cloudwatch(self) -> CloudWatchService:
        """
        boto3 Session for CloudWatch service.
        """
        return CloudWatchService("cloudwatch", self)

    @property
    def codeartifact(self) -> CodeArtifactService:
        """
        boto3 Session for CodeArtifact service.
        """
        return CodeArtifactService("codeartifact", self)

    @property
    def codebuild(self) -> CodeBuildService:
        """
        boto3 Session for CodeBuild service.
        """
        return CodeBuildService("codebuild", self)

    @property
    def codecatalyst(self) -> CodeCatalystService:
        """
        boto3 Session for CodeCatalyst service.
        """
        return CodeCatalystService("codecatalyst", self)

    @property
    def codecommit(self) -> CodeCommitService:
        """
        boto3 Session for CodeCommit service.
        """
        return CodeCommitService("codecommit", self)

    @property
    def codeconnections(self) -> CodeConnectionsService:
        """
        boto3 Session for CodeConnections service.
        """
        return CodeConnectionsService("codeconnections", self)

    @property
    def codedeploy(self) -> CodeDeployService:
        """
        boto3 Session for CodeDeploy service.
        """
        return CodeDeployService("codedeploy", self)

    @property
    def codeguru_reviewer(self) -> CodeGuruReviewerService:
        """
        boto3 Session for CodeGuruReviewer service.
        """
        return CodeGuruReviewerService("codeguru-reviewer", self)

    @property
    def codeguru_security(self) -> CodeGuruSecurityService:
        """
        boto3 Session for CodeGuruSecurity service.
        """
        return CodeGuruSecurityService("codeguru-security", self)

    @property
    def codeguruprofiler(self) -> CodeGuruProfilerService:
        """
        boto3 Session for CodeGuruProfiler service.
        """
        return CodeGuruProfilerService("codeguruprofiler", self)

    @property
    def codepipeline(self) -> CodePipelineService:
        """
        boto3 Session for CodePipeline service.
        """
        return CodePipelineService("codepipeline", self)

    @property
    def codestar_connections(self) -> CodeStarconnectionsService:
        """
        boto3 Session for CodeStarconnections service.
        """
        return CodeStarconnectionsService("codestar-connections", self)

    @property
    def codestar_notifications(self) -> CodeStarNotificationsService:
        """
        boto3 Session for CodeStarNotifications service.
        """
        return CodeStarNotificationsService("codestar-notifications", self)

    @property
    def cognito_identity(self) -> CognitoIdentityService:
        """
        boto3 Session for CognitoIdentity service.
        """
        return CognitoIdentityService("cognito-identity", self)

    @property
    def cognito_idp(self) -> CognitoIdentityProviderService:
        """
        boto3 Session for CognitoIdentityProvider service.
        """
        return CognitoIdentityProviderService("cognito-idp", self)

    @property
    def cognito_sync(self) -> CognitoSyncService:
        """
        boto3 Session for CognitoSync service.
        """
        return CognitoSyncService("cognito-sync", self)

    @property
    def comprehend(self) -> ComprehendService:
        """
        boto3 Session for Comprehend service.
        """
        return ComprehendService("comprehend", self)

    @property
    def comprehendmedical(self) -> ComprehendMedicalService:
        """
        boto3 Session for ComprehendMedical service.
        """
        return ComprehendMedicalService("comprehendmedical", self)

    @property
    def compute_optimizer(self) -> ComputeOptimizerService:
        """
        boto3 Session for ComputeOptimizer service.
        """
        return ComputeOptimizerService("compute-optimizer", self)

    @property
    def config(self) -> ConfigServiceService:
        """
        boto3 Session for ConfigService service.
        """
        return ConfigServiceService("config", self)

    @property
    def connect(self) -> ConnectService:
        """
        boto3 Session for Connect service.
        """
        return ConnectService("connect", self)

    @property
    def connect_contact_lens(self) -> ConnectContactLensService:
        """
        boto3 Session for ConnectContactLens service.
        """
        return ConnectContactLensService("connect-contact-lens", self)

    @property
    def connectcampaigns(self) -> ConnectCampaignServiceService:
        """
        boto3 Session for ConnectCampaignService service.
        """
        return ConnectCampaignServiceService("connectcampaigns", self)

    @property
    def connectcampaignsv2(self) -> ConnectCampaignServiceV2Service:
        """
        boto3 Session for ConnectCampaignServiceV2 service.
        """
        return ConnectCampaignServiceV2Service("connectcampaignsv2", self)

    @property
    def connectcases(self) -> ConnectCasesService:
        """
        boto3 Session for ConnectCases service.
        """
        return ConnectCasesService("connectcases", self)

    @property
    def connectparticipant(self) -> ConnectParticipantService:
        """
        boto3 Session for ConnectParticipant service.
        """
        return ConnectParticipantService("connectparticipant", self)

    @property
    def controlcatalog(self) -> ControlCatalogService:
        """
        boto3 Session for ControlCatalog service.
        """
        return ControlCatalogService("controlcatalog", self)

    @property
    def controltower(self) -> ControlTowerService:
        """
        boto3 Session for ControlTower service.
        """
        return ControlTowerService("controltower", self)

    @property
    def cost_optimization_hub(self) -> CostOptimizationHubService:
        """
        boto3 Session for CostOptimizationHub service.
        """
        return CostOptimizationHubService("cost-optimization-hub", self)

    @property
    def cur(self) -> CostandUsageReportServiceService:
        """
        boto3 Session for CostandUsageReportService service.
        """
        return CostandUsageReportServiceService("cur", self)

    @property
    def customer_profiles(self) -> CustomerProfilesService:
        """
        boto3 Session for CustomerProfiles service.
        """
        return CustomerProfilesService("customer-profiles", self)

    @property
    def databrew(self) -> GlueDataBrewService:
        """
        boto3 Session for GlueDataBrew service.
        """
        return GlueDataBrewService("databrew", self)

    @property
    def dataexchange(self) -> DataExchangeService:
        """
        boto3 Session for DataExchange service.
        """
        return DataExchangeService("dataexchange", self)

    @property
    def datapipeline(self) -> DataPipelineService:
        """
        boto3 Session for DataPipeline service.
        """
        return DataPipelineService("datapipeline", self)

    @property
    def datasync(self) -> DataSyncService:
        """
        boto3 Session for DataSync service.
        """
        return DataSyncService("datasync", self)

    @property
    def datazone(self) -> DataZoneService:
        """
        boto3 Session for DataZone service.
        """
        return DataZoneService("datazone", self)

    @property
    def dax(self) -> DAXService:
        """
        boto3 Session for DAX service.
        """
        return DAXService("dax", self)

    @property
    def deadline(self) -> DeadlineCloudService:
        """
        boto3 Session for DeadlineCloud service.
        """
        return DeadlineCloudService("deadline", self)

    @property
    def detective(self) -> DetectiveService:
        """
        boto3 Session for Detective service.
        """
        return DetectiveService("detective", self)

    @property
    def devicefarm(self) -> DeviceFarmService:
        """
        boto3 Session for DeviceFarm service.
        """
        return DeviceFarmService("devicefarm", self)

    @property
    def devops_guru(self) -> DevOpsGuruService:
        """
        boto3 Session for DevOpsGuru service.
        """
        return DevOpsGuruService("devops-guru", self)

    @property
    def directconnect(self) -> DirectConnectService:
        """
        boto3 Session for DirectConnect service.
        """
        return DirectConnectService("directconnect", self)

    @property
    def discovery(self) -> ApplicationDiscoveryServiceService:
        """
        boto3 Session for ApplicationDiscoveryService service.
        """
        return ApplicationDiscoveryServiceService("discovery", self)

    @property
    def dlm(self) -> DLMService:
        """
        boto3 Session for DLM service.
        """
        return DLMService("dlm", self)

    @property
    def dms(self) -> DatabaseMigrationServiceService:
        """
        boto3 Session for DatabaseMigrationService service.
        """
        return DatabaseMigrationServiceService("dms", self)

    @property
    def docdb(self) -> DocDBService:
        """
        boto3 Session for DocDB service.
        """
        return DocDBService("docdb", self)

    @property
    def docdb_elastic(self) -> DocDBElasticService:
        """
        boto3 Session for DocDBElastic service.
        """
        return DocDBElasticService("docdb-elastic", self)

    @property
    def drs(self) -> DrsService:
        """
        boto3 Session for Drs service.
        """
        return DrsService("drs", self)

    @property
    def ds(self) -> DirectoryServiceService:
        """
        boto3 Session for DirectoryService service.
        """
        return DirectoryServiceService("ds", self)

    @property
    def ds_data(self) -> DirectoryServiceDataService:
        """
        boto3 Session for DirectoryServiceData service.
        """
        return DirectoryServiceDataService("ds-data", self)

    @property
    def dsql(self) -> AuroraDSQLService:
        """
        boto3 Session for AuroraDSQL service.
        """
        return AuroraDSQLService("dsql", self)

    @property
    def dynamodb(self) -> DynamoDBService:
        """
        boto3 Session for DynamoDB service.
        """
        return DynamoDBService("dynamodb", self)

    @property
    def dynamodbstreams(self) -> DynamoDBStreamsService:
        """
        boto3 Session for DynamoDBStreams service.
        """
        return DynamoDBStreamsService("dynamodbstreams", self)

    @property
    def ebs(self) -> EBSService:
        """
        boto3 Session for EBS service.
        """
        return EBSService("ebs", self)

    @property
    def ec2(self) -> EC2Service:
        """
        boto3 Session for EC2 service.
        """
        return EC2Service("ec2", self)

    @property
    def ec2_instance_connect(self) -> EC2InstanceConnectService:
        """
        boto3 Session for EC2InstanceConnect service.
        """
        return EC2InstanceConnectService("ec2-instance-connect", self)

    @property
    def ecr(self) -> ECRService:
        """
        boto3 Session for ECR service.
        """
        return ECRService("ecr", self)

    @property
    def ecr_public(self) -> ECRPublicService:
        """
        boto3 Session for ECRPublic service.
        """
        return ECRPublicService("ecr-public", self)

    @property
    def ecs(self) -> ECSService:
        """
        boto3 Session for ECS service.
        """
        return ECSService("ecs", self)

    @property
    def efs(self) -> EFSService:
        """
        boto3 Session for EFS service.
        """
        return EFSService("efs", self)

    @property
    def eks(self) -> EKSService:
        """
        boto3 Session for EKS service.
        """
        return EKSService("eks", self)

    @property
    def eks_auth(self) -> EKSAuthService:
        """
        boto3 Session for EKSAuth service.
        """
        return EKSAuthService("eks-auth", self)

    @property
    def elasticache(self) -> ElastiCacheService:
        """
        boto3 Session for ElastiCache service.
        """
        return ElastiCacheService("elasticache", self)

    @property
    def elasticbeanstalk(self) -> ElasticBeanstalkService:
        """
        boto3 Session for ElasticBeanstalk service.
        """
        return ElasticBeanstalkService("elasticbeanstalk", self)

    @property
    def elastictranscoder(self) -> ElasticTranscoderService:
        """
        boto3 Session for ElasticTranscoder service.
        """
        return ElasticTranscoderService("elastictranscoder", self)

    @property
    def elb(self) -> ElasticLoadBalancingService:
        """
        boto3 Session for ElasticLoadBalancing service.
        """
        return ElasticLoadBalancingService("elb", self)

    @property
    def elbv2(self) -> ElasticLoadBalancingv2Service:
        """
        boto3 Session for ElasticLoadBalancingv2 service.
        """
        return ElasticLoadBalancingv2Service("elbv2", self)

    @property
    def emr(self) -> EMRService:
        """
        boto3 Session for EMR service.
        """
        return EMRService("emr", self)

    @property
    def emr_containers(self) -> EMRContainersService:
        """
        boto3 Session for EMRContainers service.
        """
        return EMRContainersService("emr-containers", self)

    @property
    def emr_serverless(self) -> EMRServerlessService:
        """
        boto3 Session for EMRServerless service.
        """
        return EMRServerlessService("emr-serverless", self)

    @property
    def entityresolution(self) -> EntityResolutionService:
        """
        boto3 Session for EntityResolution service.
        """
        return EntityResolutionService("entityresolution", self)

    @property
    def es(self) -> ElasticsearchServiceService:
        """
        boto3 Session for ElasticsearchService service.
        """
        return ElasticsearchServiceService("es", self)

    @property
    def eventbridge(self) -> EventBridgeService:
        """
        boto3 Session for EventBridge service.
        """
        return EventBridgeService("events", self)

    @property
    def evidently(self) -> CloudWatchEvidentlyService:
        """
        boto3 Session for CloudWatchEvidently service.
        """
        return CloudWatchEvidentlyService("evidently", self)

    @property
    def finspace(self) -> FinspaceService:
        """
        boto3 Session for Finspace service.
        """
        return FinspaceService("finspace", self)

    @property
    def finspace_data(self) -> FinSpaceDataService:
        """
        boto3 Session for FinSpaceData service.
        """
        return FinSpaceDataService("finspace-data", self)

    @property
    def firehose(self) -> FirehoseService:
        """
        boto3 Session for Firehose service.
        """
        return FirehoseService("firehose", self)

    @property
    def fis(self) -> FISService:
        """
        boto3 Session for FIS service.
        """
        return FISService("fis", self)

    @property
    def fms(self) -> FMSService:
        """
        boto3 Session for FMS service.
        """
        return FMSService("fms", self)

    @property
    def forecast(self) -> ForecastServiceService:
        """
        boto3 Session for ForecastService service.
        """
        return ForecastServiceService("forecast", self)

    @property
    def forecastquery(self) -> ForecastQueryServiceService:
        """
        boto3 Session for ForecastQueryService service.
        """
        return ForecastQueryServiceService("forecastquery", self)

    @property
    def frauddetector(self) -> FraudDetectorService:
        """
        boto3 Session for FraudDetector service.
        """
        return FraudDetectorService("frauddetector", self)

    @property
    def freetier(self) -> FreeTierService:
        """
        boto3 Session for FreeTier service.
        """
        return FreeTierService("freetier", self)

    @property
    def fsx(self) -> FSxService:
        """
        boto3 Session for FSx service.
        """
        return FSxService("fsx", self)

    @property
    def gamelift(self) -> GameLiftService:
        """
        boto3 Session for GameLift service.
        """
        return GameLiftService("gamelift", self)

    @property
    def geo_maps(self) -> LocationServiceMapsV2Service:
        """
        boto3 Session for LocationServiceMapsV2 service.
        """
        return LocationServiceMapsV2Service("geo-maps", self)

    @property
    def geo_places(self) -> LocationServicePlacesV2Service:
        """
        boto3 Session for LocationServicePlacesV2 service.
        """
        return LocationServicePlacesV2Service("geo-places", self)

    @property
    def geo_routes(self) -> LocationServiceRoutesV2Service:
        """
        boto3 Session for LocationServiceRoutesV2 service.
        """
        return LocationServiceRoutesV2Service("geo-routes", self)

    @property
    def glacier(self) -> GlacierService:
        """
        boto3 Session for Glacier service.
        """
        return GlacierService("glacier", self)

    @property
    def globalaccelerator(self) -> GlobalAcceleratorService:
        """
        boto3 Session for GlobalAccelerator service.
        """
        return GlobalAcceleratorService("globalaccelerator", self)

    @property
    def glue(self) -> GlueService:
        """
        boto3 Session for Glue service.
        """
        return GlueService("glue", self)

    @property
    def grafana(self) -> ManagedGrafanaService:
        """
        boto3 Session for ManagedGrafana service.
        """
        return ManagedGrafanaService("grafana", self)

    @property
    def greengrass(self) -> GreengrassService:
        """
        boto3 Session for Greengrass service.
        """
        return GreengrassService("greengrass", self)

    @property
    def greengrassv2(self) -> GreengrassV2Service:
        """
        boto3 Session for GreengrassV2 service.
        """
        return GreengrassV2Service("greengrassv2", self)

    @property
    def groundstation(self) -> GroundStationService:
        """
        boto3 Session for GroundStation service.
        """
        return GroundStationService("groundstation", self)

    @property
    def guardduty(self) -> GuardDutyService:
        """
        boto3 Session for GuardDuty service.
        """
        return GuardDutyService("guardduty", self)

    @property
    def health(self) -> HealthService:
        """
        boto3 Session for Health service.
        """
        return HealthService("health", self)

    @property
    def healthlake(self) -> HealthLakeService:
        """
        boto3 Session for HealthLake service.
        """
        return HealthLakeService("healthlake", self)

    @property
    def iam(self) -> IAMService:
        """
        boto3 Session for IAM service.
        """
        return IAMService("iam", self)

    @property
    def identitystore(self) -> IdentityStoreService:
        """
        boto3 Session for IdentityStore service.
        """
        return IdentityStoreService("identitystore", self)

    @property
    def imagebuilder(self) -> ImagebuilderService:
        """
        boto3 Session for Imagebuilder service.
        """
        return ImagebuilderService("imagebuilder", self)

    @property
    def importexport(self) -> ImportExportService:
        """
        boto3 Session for ImportExport service.
        """
        return ImportExportService("importexport", self)

    @property
    def inspector(self) -> InspectorService:
        """
        boto3 Session for Inspector service.
        """
        return InspectorService("inspector", self)

    @property
    def inspector_scan(self) -> InspectorscanService:
        """
        boto3 Session for Inspectorscan service.
        """
        return InspectorscanService("inspector-scan", self)

    @property
    def inspector2(self) -> Inspector2Service:
        """
        boto3 Session for Inspector2 service.
        """
        return Inspector2Service("inspector2", self)

    @property
    def internetmonitor(self) -> CloudWatchInternetMonitorService:
        """
        boto3 Session for CloudWatchInternetMonitor service.
        """
        return CloudWatchInternetMonitorService("internetmonitor", self)

    @property
    def invoicing(self) -> InvoicingService:
        """
        boto3 Session for Invoicing service.
        """
        return InvoicingService("invoicing", self)

    @property
    def iot(self) -> IoTService:
        """
        boto3 Session for IoT service.
        """
        return IoTService("iot", self)

    @property
    def iot_data(self) -> IoTDataPlaneService:
        """
        boto3 Session for IoTDataPlane service.
        """
        return IoTDataPlaneService("iot-data", self)

    @property
    def iot_jobs_data(self) -> IoTJobsDataPlaneService:
        """
        boto3 Session for IoTJobsDataPlane service.
        """
        return IoTJobsDataPlaneService("iot-jobs-data", self)

    @property
    def iotanalytics(self) -> IoTAnalyticsService:
        """
        boto3 Session for IoTAnalytics service.
        """
        return IoTAnalyticsService("iotanalytics", self)

    @property
    def iotdeviceadvisor(self) -> IoTDeviceAdvisorService:
        """
        boto3 Session for IoTDeviceAdvisor service.
        """
        return IoTDeviceAdvisorService("iotdeviceadvisor", self)

    @property
    def iotevents(self) -> IoTEventsService:
        """
        boto3 Session for IoTEvents service.
        """
        return IoTEventsService("iotevents", self)

    @property
    def iotevents_data(self) -> IoTEventsDataService:
        """
        boto3 Session for IoTEventsData service.
        """
        return IoTEventsDataService("iotevents-data", self)

    @property
    def iotfleethub(self) -> IoTFleetHubService:
        """
        boto3 Session for IoTFleetHub service.
        """
        return IoTFleetHubService("iotfleethub", self)

    @property
    def iotfleetwise(self) -> IoTFleetWiseService:
        """
        boto3 Session for IoTFleetWise service.
        """
        return IoTFleetWiseService("iotfleetwise", self)

    @property
    def iotsecuretunneling(self) -> IoTSecureTunnelingService:
        """
        boto3 Session for IoTSecureTunneling service.
        """
        return IoTSecureTunnelingService("iotsecuretunneling", self)

    @property
    def iotsitewise(self) -> IoTSiteWiseService:
        """
        boto3 Session for IoTSiteWise service.
        """
        return IoTSiteWiseService("iotsitewise", self)

    @property
    def iotthingsgraph(self) -> IoTThingsGraphService:
        """
        boto3 Session for IoTThingsGraph service.
        """
        return IoTThingsGraphService("iotthingsgraph", self)

    @property
    def iottwinmaker(self) -> IoTTwinMakerService:
        """
        boto3 Session for IoTTwinMaker service.
        """
        return IoTTwinMakerService("iottwinmaker", self)

    @property
    def iotwireless(self) -> IoTWirelessService:
        """
        boto3 Session for IoTWireless service.
        """
        return IoTWirelessService("iotwireless", self)

    @property
    def ivs(self) -> IVSService:
        """
        boto3 Session for IVS service.
        """
        return IVSService("ivs", self)

    @property
    def ivs_realtime(self) -> IvsrealtimeService:
        """
        boto3 Session for Ivsrealtime service.
        """
        return IvsrealtimeService("ivs-realtime", self)

    @property
    def ivschat(self) -> IvschatService:
        """
        boto3 Session for Ivschat service.
        """
        return IvschatService("ivschat", self)

    @property
    def kafka(self) -> KafkaService:
        """
        boto3 Session for Kafka service.
        """
        return KafkaService("kafka", self)

    @property
    def kafkaconnect(self) -> KafkaConnectService:
        """
        boto3 Session for KafkaConnect service.
        """
        return KafkaConnectService("kafkaconnect", self)

    @property
    def kendra(self) -> KendraService:
        """
        boto3 Session for Kendra service.
        """
        return KendraService("kendra", self)

    @property
    def kendra_ranking(self) -> KendraRankingService:
        """
        boto3 Session for KendraRanking service.
        """
        return KendraRankingService("kendra-ranking", self)

    @property
    def keyspaces(self) -> KeyspacesService:
        """
        boto3 Session for Keyspaces service.
        """
        return KeyspacesService("keyspaces", self)

    @property
    def kinesis(self) -> KinesisService:
        """
        boto3 Session for Kinesis service.
        """
        return KinesisService("kinesis", self)

    @property
    def kinesis_video_archived_media(self) -> KinesisVideoArchivedMediaService:
        """
        boto3 Session for KinesisVideoArchivedMedia service.
        """
        return KinesisVideoArchivedMediaService("kinesis-video-archived-media", self)

    @property
    def kinesis_video_media(self) -> KinesisVideoMediaService:
        """
        boto3 Session for KinesisVideoMedia service.
        """
        return KinesisVideoMediaService("kinesis-video-media", self)

    @property
    def kinesis_video_signaling(self) -> KinesisVideoSignalingChannelsService:
        """
        boto3 Session for KinesisVideoSignalingChannels service.
        """
        return KinesisVideoSignalingChannelsService("kinesis-video-signaling", self)

    @property
    def kinesis_video_webrtc_storage(self) -> KinesisVideoWebRTCStorageService:
        """
        boto3 Session for KinesisVideoWebRTCStorage service.
        """
        return KinesisVideoWebRTCStorageService("kinesis-video-webrtc-storage", self)

    @property
    def kinesisanalytics(self) -> KinesisAnalyticsService:
        """
        boto3 Session for KinesisAnalytics service.
        """
        return KinesisAnalyticsService("kinesisanalytics", self)

    @property
    def kinesisanalyticsv2(self) -> KinesisAnalyticsV2Service:
        """
        boto3 Session for KinesisAnalyticsV2 service.
        """
        return KinesisAnalyticsV2Service("kinesisanalyticsv2", self)

    @property
    def kinesisvideo(self) -> KinesisVideoService:
        """
        boto3 Session for KinesisVideo service.
        """
        return KinesisVideoService("kinesisvideo", self)

    @property
    def kms(self) -> KMSService:
        """
        boto3 Session for KMS service.
        """
        return KMSService("kms", self)

    @property
    def lakeformation(self) -> LakeFormationService:
        """
        boto3 Session for LakeFormation service.
        """
        return LakeFormationService("lakeformation", self)

    @property
    def lambda_(self) -> LambdaService:
        """
        boto3 Session for Lambda service.
        """
        return LambdaService("lambda", self)

    @property
    def launch_wizard(self) -> LaunchWizardService:
        """
        boto3 Session for LaunchWizard service.
        """
        return LaunchWizardService("launch-wizard", self)

    @property
    def lex_models(self) -> LexModelBuildingServiceService:
        """
        boto3 Session for LexModelBuildingService service.
        """
        return LexModelBuildingServiceService("lex-models", self)

    @property
    def lex_runtime(self) -> LexRuntimeServiceService:
        """
        boto3 Session for LexRuntimeService service.
        """
        return LexRuntimeServiceService("lex-runtime", self)

    @property
    def lexv2_models(self) -> LexModelsV2Service:
        """
        boto3 Session for LexModelsV2 service.
        """
        return LexModelsV2Service("lexv2-models", self)

    @property
    def lexv2_runtime(self) -> LexRuntimeV2Service:
        """
        boto3 Session for LexRuntimeV2 service.
        """
        return LexRuntimeV2Service("lexv2-runtime", self)

    @property
    def license_manager(self) -> LicenseManagerService:
        """
        boto3 Session for LicenseManager service.
        """
        return LicenseManagerService("license-manager", self)

    @property
    def license_manager_linux_subscriptions(self) -> LicenseManagerLinuxSubscriptionsService:
        """
        boto3 Session for LicenseManagerLinuxSubscriptions service.
        """
        return LicenseManagerLinuxSubscriptionsService("license-manager-linux-subscriptions", self)

    @property
    def license_manager_user_subscriptions(self) -> LicenseManagerUserSubscriptionsService:
        """
        boto3 Session for LicenseManagerUserSubscriptions service.
        """
        return LicenseManagerUserSubscriptionsService("license-manager-user-subscriptions", self)

    @property
    def lightsail(self) -> LightsailService:
        """
        boto3 Session for Lightsail service.
        """
        return LightsailService("lightsail", self)

    @property
    def location(self) -> LocationServiceService:
        """
        boto3 Session for LocationService service.
        """
        return LocationServiceService("location", self)

    @property
    def logs(self) -> CloudWatchLogsService:
        """
        boto3 Session for CloudWatchLogs service.
        """
        return CloudWatchLogsService("logs", self)

    @property
    def lookoutequipment(self) -> LookoutEquipmentService:
        """
        boto3 Session for LookoutEquipment service.
        """
        return LookoutEquipmentService("lookoutequipment", self)

    @property
    def lookoutmetrics(self) -> LookoutMetricsService:
        """
        boto3 Session for LookoutMetrics service.
        """
        return LookoutMetricsService("lookoutmetrics", self)

    @property
    def lookoutvision(self) -> LookoutforVisionService:
        """
        boto3 Session for LookoutforVision service.
        """
        return LookoutforVisionService("lookoutvision", self)

    @property
    def m2(self) -> MainframeModernizationService:
        """
        boto3 Session for MainframeModernization service.
        """
        return MainframeModernizationService("m2", self)

    @property
    def machinelearning(self) -> MachineLearningService:
        """
        boto3 Session for MachineLearning service.
        """
        return MachineLearningService("machinelearning", self)

    @property
    def macie2(self) -> Macie2Service:
        """
        boto3 Session for Macie2 service.
        """
        return Macie2Service("macie2", self)

    @property
    def mailmanager(self) -> MailManagerService:
        """
        boto3 Session for MailManager service.
        """
        return MailManagerService("mailmanager", self)

    @property
    def managedblockchain(self) -> ManagedBlockchainService:
        """
        boto3 Session for ManagedBlockchain service.
        """
        return ManagedBlockchainService("managedblockchain", self)

    @property
    def managedblockchain_query(self) -> ManagedBlockchainQueryService:
        """
        boto3 Session for ManagedBlockchainQuery service.
        """
        return ManagedBlockchainQueryService("managedblockchain-query", self)

    @property
    def marketplace_agreement(self) -> AgreementServiceService:
        """
        boto3 Session for AgreementService service.
        """
        return AgreementServiceService("marketplace-agreement", self)

    @property
    def marketplace_catalog(self) -> MarketplaceCatalogService:
        """
        boto3 Session for MarketplaceCatalog service.
        """
        return MarketplaceCatalogService("marketplace-catalog", self)

    @property
    def marketplace_deployment(self) -> MarketplaceDeploymentServiceService:
        """
        boto3 Session for MarketplaceDeploymentService service.
        """
        return MarketplaceDeploymentServiceService("marketplace-deployment", self)

    @property
    def marketplace_entitlement(self) -> MarketplaceEntitlementServiceService:
        """
        boto3 Session for MarketplaceEntitlementService service.
        """
        return MarketplaceEntitlementServiceService("marketplace-entitlement", self)

    @property
    def marketplace_reporting(self) -> MarketplaceReportingServiceService:
        """
        boto3 Session for MarketplaceReportingService service.
        """
        return MarketplaceReportingServiceService("marketplace-reporting", self)

    @property
    def marketplacecommerceanalytics(self) -> MarketplaceCommerceAnalyticsService:
        """
        boto3 Session for MarketplaceCommerceAnalytics service.
        """
        return MarketplaceCommerceAnalyticsService("marketplacecommerceanalytics", self)

    @property
    def mediaconnect(self) -> MediaConnectService:
        """
        boto3 Session for MediaConnect service.
        """
        return MediaConnectService("mediaconnect", self)

    @property
    def mediaconvert(self) -> MediaConvertService:
        """
        boto3 Session for MediaConvert service.
        """
        return MediaConvertService("mediaconvert", self)

    @property
    def medialive(self) -> MediaLiveService:
        """
        boto3 Session for MediaLive service.
        """
        return MediaLiveService("medialive", self)

    @property
    def mediapackage(self) -> MediaPackageService:
        """
        boto3 Session for MediaPackage service.
        """
        return MediaPackageService("mediapackage", self)

    @property
    def mediapackage_vod(self) -> MediaPackageVodService:
        """
        boto3 Session for MediaPackageVod service.
        """
        return MediaPackageVodService("mediapackage-vod", self)

    @property
    def mediapackagev2(self) -> Mediapackagev2Service:
        """
        boto3 Session for Mediapackagev2 service.
        """
        return Mediapackagev2Service("mediapackagev2", self)

    @property
    def mediastore(self) -> MediaStoreService:
        """
        boto3 Session for MediaStore service.
        """
        return MediaStoreService("mediastore", self)

    @property
    def mediastore_data(self) -> MediaStoreDataService:
        """
        boto3 Session for MediaStoreData service.
        """
        return MediaStoreDataService("mediastore-data", self)

    @property
    def mediatailor(self) -> MediaTailorService:
        """
        boto3 Session for MediaTailor service.
        """
        return MediaTailorService("mediatailor", self)

    @property
    def medical_imaging(self) -> HealthImagingService:
        """
        boto3 Session for HealthImaging service.
        """
        return HealthImagingService("medical-imaging", self)

    @property
    def memorydb(self) -> MemoryDBService:
        """
        boto3 Session for MemoryDB service.
        """
        return MemoryDBService("memorydb", self)

    @property
    def meteringmarketplace(self) -> MarketplaceMeteringService:
        """
        boto3 Session for MarketplaceMetering service.
        """
        return MarketplaceMeteringService("meteringmarketplace", self)

    @property
    def mgh(self) -> MigrationHubService:
        """
        boto3 Session for MigrationHub service.
        """
        return MigrationHubService("mgh", self)

    @property
    def mgn(self) -> MgnService:
        """
        boto3 Session for Mgn service.
        """
        return MgnService("mgn", self)

    @property
    def migration_hub_refactor_spaces(self) -> MigrationHubRefactorSpacesService:
        """
        boto3 Session for MigrationHubRefactorSpaces service.
        """
        return MigrationHubRefactorSpacesService("migration-hub-refactor-spaces", self)

    @property
    def migrationhub_config(self) -> MigrationHubConfigService:
        """
        boto3 Session for MigrationHubConfig service.
        """
        return MigrationHubConfigService("migrationhub-config", self)

    @property
    def migrationhuborchestrator(self) -> MigrationHubOrchestratorService:
        """
        boto3 Session for MigrationHubOrchestrator service.
        """
        return MigrationHubOrchestratorService("migrationhuborchestrator", self)

    @property
    def migrationhubstrategy(self) -> MigrationHubStrategyRecommendationsService:
        """
        boto3 Session for MigrationHubStrategyRecommendations service.
        """
        return MigrationHubStrategyRecommendationsService("migrationhubstrategy", self)

    @property
    def mq(self) -> MQService:
        """
        boto3 Session for MQ service.
        """
        return MQService("mq", self)

    @property
    def mturk(self) -> MTurkService:
        """
        boto3 Session for MTurk service.
        """
        return MTurkService("mturk", self)

    @property
    def mwaa(self) -> MWAAService:
        """
        boto3 Session for MWAA service.
        """
        return MWAAService("mwaa", self)

    @property
    def neptune(self) -> NeptuneService:
        """
        boto3 Session for Neptune service.
        """
        return NeptuneService("neptune", self)

    @property
    def neptune_graph(self) -> NeptuneGraphService:
        """
        boto3 Session for NeptuneGraph service.
        """
        return NeptuneGraphService("neptune-graph", self)

    @property
    def neptunedata(self) -> NeptuneDataService:
        """
        boto3 Session for NeptuneData service.
        """
        return NeptuneDataService("neptunedata", self)

    @property
    def network_firewall(self) -> NetworkFirewallService:
        """
        boto3 Session for NetworkFirewall service.
        """
        return NetworkFirewallService("network-firewall", self)

    @property
    def networkflowmonitor(self) -> NetworkFlowMonitorService:
        """
        boto3 Session for NetworkFlowMonitor service.
        """
        return NetworkFlowMonitorService("networkflowmonitor", self)

    @property
    def networkmanager(self) -> NetworkManagerService:
        """
        boto3 Session for NetworkManager service.
        """
        return NetworkManagerService("networkmanager", self)

    @property
    def networkmonitor(self) -> CloudWatchNetworkMonitorService:
        """
        boto3 Session for CloudWatchNetworkMonitor service.
        """
        return CloudWatchNetworkMonitorService("networkmonitor", self)

    @property
    def notifications(self) -> UserNotificationsService:
        """
        boto3 Session for UserNotifications service.
        """
        return UserNotificationsService("notifications", self)

    @property
    def notificationscontacts(self) -> UserNotificationsContactsService:
        """
        boto3 Session for UserNotificationsContacts service.
        """
        return UserNotificationsContactsService("notificationscontacts", self)

    @property
    def oam(self) -> CloudWatchObservabilityAccessManagerService:
        """
        boto3 Session for CloudWatchObservabilityAccessManager service.
        """
        return CloudWatchObservabilityAccessManagerService("oam", self)

    @property
    def observabilityadmin(self) -> CloudWatchObservabilityAdminServiceService:
        """
        boto3 Session for CloudWatchObservabilityAdminService service.
        """
        return CloudWatchObservabilityAdminServiceService("observabilityadmin", self)

    @property
    def omics(self) -> OmicsService:
        """
        boto3 Session for Omics service.
        """
        return OmicsService("omics", self)

    @property
    def opensearch(self) -> OpenSearchServiceService:
        """
        boto3 Session for OpenSearchService service.
        """
        return OpenSearchServiceService("opensearch", self)

    @property
    def opensearchserverless(self) -> OpenSearchServiceServerlessService:
        """
        boto3 Session for OpenSearchServiceServerless service.
        """
        return OpenSearchServiceServerlessService("opensearchserverless", self)

    @property
    def opsworks(self) -> OpsWorksService:
        """
        boto3 Session for OpsWorks service.
        """
        return OpsWorksService("opsworks", self)

    @property
    def opsworkscm(self) -> OpsWorksCMService:
        """
        boto3 Session for OpsWorksCM service.
        """
        return OpsWorksCMService("opsworkscm", self)

    @property
    def organizations(self) -> OrganizationsService:
        """
        boto3 Session for Organizations service.
        """
        return OrganizationsService("organizations", self)

    @property
    def osis(self) -> OpenSearchIngestionService:
        """
        boto3 Session for OpenSearchIngestion service.
        """
        return OpenSearchIngestionService("osis", self)

    @property
    def outposts(self) -> OutpostsService:
        """
        boto3 Session for Outposts service.
        """
        return OutpostsService("outposts", self)

    @property
    def panorama(self) -> PanoramaService:
        """
        boto3 Session for Panorama service.
        """
        return PanoramaService("panorama", self)

    @property
    def partnercentral_selling(self) -> PartnerCentralSellingAPIService:
        """
        boto3 Session for PartnerCentralSellingAPI service.
        """
        return PartnerCentralSellingAPIService("partnercentral-selling", self)

    @property
    def payment_cryptography(self) -> PaymentCryptographyControlPlaneService:
        """
        boto3 Session for PaymentCryptographyControlPlane service.
        """
        return PaymentCryptographyControlPlaneService("payment-cryptography", self)

    @property
    def payment_cryptography_data(self) -> PaymentCryptographyDataPlaneService:
        """
        boto3 Session for PaymentCryptographyDataPlane service.
        """
        return PaymentCryptographyDataPlaneService("payment-cryptography-data", self)

    @property
    def pca_connector_ad(self) -> PcaConnectorAdService:
        """
        boto3 Session for PcaConnectorAd service.
        """
        return PcaConnectorAdService("pca-connector-ad", self)

    @property
    def pca_connector_scep(self) -> PrivateCAConnectorforSCEPService:
        """
        boto3 Session for PrivateCAConnectorforSCEP service.
        """
        return PrivateCAConnectorforSCEPService("pca-connector-scep", self)

    @property
    def pcs(self) -> ParallelComputingServiceService:
        """
        boto3 Session for ParallelComputingService service.
        """
        return ParallelComputingServiceService("pcs", self)

    @property
    def personalize(self) -> PersonalizeService:
        """
        boto3 Session for Personalize service.
        """
        return PersonalizeService("personalize", self)

    @property
    def personalize_events(self) -> PersonalizeEventsService:
        """
        boto3 Session for PersonalizeEvents service.
        """
        return PersonalizeEventsService("personalize-events", self)

    @property
    def personalize_runtime(self) -> PersonalizeRuntimeService:
        """
        boto3 Session for PersonalizeRuntime service.
        """
        return PersonalizeRuntimeService("personalize-runtime", self)

    @property
    def pi(self) -> PIService:
        """
        boto3 Session for PI service.
        """
        return PIService("pi", self)

    @property
    def pinpoint(self) -> PinpointService:
        """
        boto3 Session for Pinpoint service.
        """
        return PinpointService("pinpoint", self)

    @property
    def pinpoint_email(self) -> PinpointEmailService:
        """
        boto3 Session for PinpointEmail service.
        """
        return PinpointEmailService("pinpoint-email", self)

    @property
    def pinpoint_sms_voice(self) -> PinpointSMSVoiceService:
        """
        boto3 Session for PinpointSMSVoice service.
        """
        return PinpointSMSVoiceService("pinpoint-sms-voice", self)

    @property
    def pinpoint_sms_voice_v2(self) -> PinpointSMSVoiceV2Service:
        """
        boto3 Session for PinpointSMSVoiceV2 service.
        """
        return PinpointSMSVoiceV2Service("pinpoint-sms-voice-v2", self)

    @property
    def pipes(self) -> EventBridgePipesService:
        """
        boto3 Session for EventBridgePipes service.
        """
        return EventBridgePipesService("pipes", self)

    @property
    def polly(self) -> PollyService:
        """
        boto3 Session for Polly service.
        """
        return PollyService("polly", self)

    @property
    def pricing(self) -> PricingService:
        """
        boto3 Session for Pricing service.
        """
        return PricingService("pricing", self)

    @property
    def privatenetworks(self) -> Private5GService:
        """
        boto3 Session for Private5G service.
        """
        return Private5GService("privatenetworks", self)

    @property
    def proton(self) -> ProtonService:
        """
        boto3 Session for Proton service.
        """
        return ProtonService("proton", self)

    @property
    def qapps(self) -> QAppsService:
        """
        boto3 Session for QApps service.
        """
        return QAppsService("qapps", self)

    @property
    def qbusiness(self) -> QBusinessService:
        """
        boto3 Session for QBusiness service.
        """
        return QBusinessService("qbusiness", self)

    @property
    def qconnect(self) -> QConnectService:
        """
        boto3 Session for QConnect service.
        """
        return QConnectService("qconnect", self)

    @property
    def qldb(self) -> QLDBService:
        """
        boto3 Session for QLDB service.
        """
        return QLDBService("qldb", self)

    @property
    def qldb_session(self) -> QLDBSessionService:
        """
        boto3 Session for QLDBSession service.
        """
        return QLDBSessionService("qldb-session", self)

    @property
    def quicksight(self) -> QuickSightService:
        """
        boto3 Session for QuickSight service.
        """
        return QuickSightService("quicksight", self)

    @property
    def ram(self) -> RAMService:
        """
        boto3 Session for RAM service.
        """
        return RAMService("ram", self)

    @property
    def rbin(self) -> RecycleBinService:
        """
        boto3 Session for RecycleBin service.
        """
        return RecycleBinService("rbin", self)

    @property
    def rds(self) -> RDSService:
        """
        boto3 Session for RDS service.
        """
        return RDSService("rds", self)

    @property
    def rds_data(self) -> RDSDataServiceService:
        """
        boto3 Session for RDSDataService service.
        """
        return RDSDataServiceService("rds-data", self)

    @property
    def redshift(self) -> RedshiftService:
        """
        boto3 Session for Redshift service.
        """
        return RedshiftService("redshift", self)

    @property
    def redshift_data(self) -> RedshiftDataAPIServiceService:
        """
        boto3 Session for RedshiftDataAPIService service.
        """
        return RedshiftDataAPIServiceService("redshift-data", self)

    @property
    def redshift_serverless(self) -> RedshiftServerlessService:
        """
        boto3 Session for RedshiftServerless service.
        """
        return RedshiftServerlessService("redshift-serverless", self)

    @property
    def rekognition(self) -> RekognitionService:
        """
        boto3 Session for Rekognition service.
        """
        return RekognitionService("rekognition", self)

    @property
    def repostspace(self) -> RePostPrivateService:
        """
        boto3 Session for RePostPrivate service.
        """
        return RePostPrivateService("repostspace", self)

    @property
    def resiliencehub(self) -> ResilienceHubService:
        """
        boto3 Session for ResilienceHub service.
        """
        return ResilienceHubService("resiliencehub", self)

    @property
    def resource_explorer_2(self) -> ResourceExplorerService:
        """
        boto3 Session for ResourceExplorer service.
        """
        return ResourceExplorerService("resource-explorer-2", self)

    @property
    def resource_groups(self) -> ResourceGroupsService:
        """
        boto3 Session for ResourceGroups service.
        """
        return ResourceGroupsService("resource-groups", self)

    @property
    def resourcegroupstaggingapi(self) -> ResourceGroupsTaggingAPIService:
        """
        boto3 Session for ResourceGroupsTaggingAPI service.
        """
        return ResourceGroupsTaggingAPIService("resourcegroupstaggingapi", self)

    @property
    def robomaker(self) -> RoboMakerService:
        """
        boto3 Session for RoboMaker service.
        """
        return RoboMakerService("robomaker", self)

    @property
    def rolesanywhere(self) -> IAMRolesAnywhereService:
        """
        boto3 Session for IAMRolesAnywhere service.
        """
        return IAMRolesAnywhereService("rolesanywhere", self)

    @property
    def route53(self) -> Route53Service:
        """
        boto3 Session for Route53 service.
        """
        return Route53Service("route53", self)

    @property
    def route53_recovery_cluster(self) -> Route53RecoveryClusterService:
        """
        boto3 Session for Route53RecoveryCluster service.
        """
        return Route53RecoveryClusterService("route53-recovery-cluster", self)

    @property
    def route53_recovery_control_config(self) -> Route53RecoveryControlConfigService:
        """
        boto3 Session for Route53RecoveryControlConfig service.
        """
        return Route53RecoveryControlConfigService("route53-recovery-control-config", self)

    @property
    def route53_recovery_readiness(self) -> Route53RecoveryReadinessService:
        """
        boto3 Session for Route53RecoveryReadiness service.
        """
        return Route53RecoveryReadinessService("route53-recovery-readiness", self)

    @property
    def route53domains(self) -> Route53DomainsService:
        """
        boto3 Session for Route53Domains service.
        """
        return Route53DomainsService("route53domains", self)

    @property
    def route53profiles(self) -> Route53ProfilesService:
        """
        boto3 Session for Route53Profiles service.
        """
        return Route53ProfilesService("route53profiles", self)

    @property
    def route53resolver(self) -> Route53ResolverService:
        """
        boto3 Session for Route53Resolver service.
        """
        return Route53ResolverService("route53resolver", self)

    @property
    def rum(self) -> CloudWatchRUMService:
        """
        boto3 Session for CloudWatchRUM service.
        """
        return CloudWatchRUMService("rum", self)

    @property
    def s3(self) -> S3Service:
        """
        boto3 Session for S3 service.
        """
        return S3Service("s3", self)

    @property
    def s3control(self) -> S3ControlService:
        """
        boto3 Session for S3Control service.
        """
        return S3ControlService("s3control", self)

    @property
    def s3outposts(self) -> S3OutpostsService:
        """
        boto3 Session for S3Outposts service.
        """
        return S3OutpostsService("s3outposts", self)

    @property
    def s3tables(self) -> S3TablesService:
        """
        boto3 Session for S3Tables service.
        """
        return S3TablesService("s3tables", self)

    @property
    def sagemaker(self) -> SageMakerService:
        """
        boto3 Session for SageMaker service.
        """
        return SageMakerService("sagemaker", self)

    @property
    def sagemaker_a2i_runtime(self) -> AugmentedAIRuntimeService:
        """
        boto3 Session for AugmentedAIRuntime service.
        """
        return AugmentedAIRuntimeService("sagemaker-a2i-runtime", self)

    @property
    def sagemaker_edge(self) -> SagemakerEdgeManagerService:
        """
        boto3 Session for SagemakerEdgeManager service.
        """
        return SagemakerEdgeManagerService("sagemaker-edge", self)

    @property
    def sagemaker_featurestore_runtime(self) -> SageMakerFeatureStoreRuntimeService:
        """
        boto3 Session for SageMakerFeatureStoreRuntime service.
        """
        return SageMakerFeatureStoreRuntimeService("sagemaker-featurestore-runtime", self)

    @property
    def sagemaker_geospatial(self) -> SageMakergeospatialcapabilitiesService:
        """
        boto3 Session for SageMakergeospatialcapabilities service.
        """
        return SageMakergeospatialcapabilitiesService("sagemaker-geospatial", self)

    @property
    def sagemaker_metrics(self) -> SageMakerMetricsService:
        """
        boto3 Session for SageMakerMetrics service.
        """
        return SageMakerMetricsService("sagemaker-metrics", self)

    @property
    def sagemaker_runtime(self) -> SageMakerRuntimeService:
        """
        boto3 Session for SageMakerRuntime service.
        """
        return SageMakerRuntimeService("sagemaker-runtime", self)

    @property
    def savingsplans(self) -> SavingsPlansService:
        """
        boto3 Session for SavingsPlans service.
        """
        return SavingsPlansService("savingsplans", self)

    @property
    def scheduler(self) -> EventBridgeSchedulerService:
        """
        boto3 Session for EventBridgeScheduler service.
        """
        return EventBridgeSchedulerService("scheduler", self)

    @property
    def schemas(self) -> SchemasService:
        """
        boto3 Session for Schemas service.
        """
        return SchemasService("schemas", self)

    @property
    def sdb(self) -> SimpleDBService:
        """
        boto3 Session for SimpleDB service.
        """
        return SimpleDBService("sdb", self)

    @property
    def secretsmanager(self) -> SecretsManagerService:
        """
        boto3 Session for SecretsManager service.
        """
        return SecretsManagerService("secretsmanager", self)

    @property
    def security_ir(self) -> SecurityIncidentResponseService:
        """
        boto3 Session for SecurityIncidentResponse service.
        """
        return SecurityIncidentResponseService("security-ir", self)

    @property
    def securityhub(self) -> SecurityHubService:
        """
        boto3 Session for SecurityHub service.
        """
        return SecurityHubService("securityhub", self)

    @property
    def securitylake(self) -> SecurityLakeService:
        """
        boto3 Session for SecurityLake service.
        """
        return SecurityLakeService("securitylake", self)

    @property
    def serverlessrepo(self) -> ServerlessApplicationRepositoryService:
        """
        boto3 Session for ServerlessApplicationRepository service.
        """
        return ServerlessApplicationRepositoryService("serverlessrepo", self)

    @property
    def service_quotas(self) -> ServiceQuotasService:
        """
        boto3 Session for ServiceQuotas service.
        """
        return ServiceQuotasService("service-quotas", self)

    @property
    def servicecatalog(self) -> ServiceCatalogService:
        """
        boto3 Session for ServiceCatalog service.
        """
        return ServiceCatalogService("servicecatalog", self)

    @property
    def servicecatalog_appregistry(self) -> AppRegistryService:
        """
        boto3 Session for AppRegistry service.
        """
        return AppRegistryService("servicecatalog-appregistry", self)

    @property
    def servicediscovery(self) -> ServiceDiscoveryService:
        """
        boto3 Session for ServiceDiscovery service.
        """
        return ServiceDiscoveryService("servicediscovery", self)

    @property
    def ses(self) -> SESService:
        """
        boto3 Session for SES service.
        """
        return SESService("ses", self)

    @property
    def sesv2(self) -> SESV2Service:
        """
        boto3 Session for SESV2 service.
        """
        return SESV2Service("sesv2", self)

    @property
    def shield(self) -> ShieldService:
        """
        boto3 Session for Shield service.
        """
        return ShieldService("shield", self)

    @property
    def signer(self) -> SignerService:
        """
        boto3 Session for Signer service.
        """
        return SignerService("signer", self)

    @property
    def simspaceweaver(self) -> SimSpaceWeaverService:
        """
        boto3 Session for SimSpaceWeaver service.
        """
        return SimSpaceWeaverService("simspaceweaver", self)

    @property
    def sms(self) -> SMSService:
        """
        boto3 Session for SMS service.
        """
        return SMSService("sms", self)

    @property
    def sms_voice(self) -> SMSVoiceService:
        """
        boto3 Session for SMSVoice service.
        """
        return SMSVoiceService("sms-voice", self)

    @property
    def snow_device_management(self) -> SnowDeviceManagementService:
        """
        boto3 Session for SnowDeviceManagement service.
        """
        return SnowDeviceManagementService("snow-device-management", self)

    @property
    def snowball(self) -> SnowballService:
        """
        boto3 Session for Snowball service.
        """
        return SnowballService("snowball", self)

    @property
    def sns(self) -> SNSService:
        """
        boto3 Session for SNS service.
        """
        return SNSService("sns", self)

    @property
    def socialmessaging(self) -> EndUserMessagingSocialService:
        """
        boto3 Session for EndUserMessagingSocial service.
        """
        return EndUserMessagingSocialService("socialmessaging", self)

    @property
    def sqs(self) -> SQSService:
        """
        boto3 Session for SQS service.
        """
        return SQSService("sqs", self)

    @property
    def ssm(self) -> SSMService:
        """
        boto3 Session for SSM service.
        """
        return SSMService("ssm", self)

    @property
    def ssm_contacts(self) -> SSMContactsService:
        """
        boto3 Session for SSMContacts service.
        """
        return SSMContactsService("ssm-contacts", self)

    @property
    def ssm_incidents(self) -> SSMIncidentsService:
        """
        boto3 Session for SSMIncidents service.
        """
        return SSMIncidentsService("ssm-incidents", self)

    @property
    def ssm_quicksetup(self) -> SystemsManagerQuickSetupService:
        """
        boto3 Session for SystemsManagerQuickSetup service.
        """
        return SystemsManagerQuickSetupService("ssm-quicksetup", self)

    @property
    def ssm_sap(self) -> SsmSapService:
        """
        boto3 Session for SsmSap service.
        """
        return SsmSapService("ssm-sap", self)

    @property
    def sso(self) -> SSOService:
        """
        boto3 Session for SSO service.
        """
        return SSOService("sso", self)

    @property
    def sso_admin(self) -> SSOAdminService:
        """
        boto3 Session for SSOAdmin service.
        """
        return SSOAdminService("sso-admin", self)

    @property
    def sso_oidc(self) -> SSOOIDCService:
        """
        boto3 Session for SSOOIDC service.
        """
        return SSOOIDCService("sso-oidc", self)

    @property
    def stepfunctions(self) -> SFNService:
        """
        boto3 Session for SFN service.
        """
        return SFNService("stepfunctions", self)

    @property
    def storagegateway(self) -> StorageGatewayService:
        """
        boto3 Session for StorageGateway service.
        """
        return StorageGatewayService("storagegateway", self)

    @property
    def sts(self) -> STSService:
        """
        boto3 Session for STS service.
        """
        return STSService("sts", self)

    @property
    def supplychain(self) -> SupplyChainService:
        """
        boto3 Session for SupplyChain service.
        """
        return SupplyChainService("supplychain", self)

    @property
    def support(self) -> SupportService:
        """
        boto3 Session for Support service.
        """
        return SupportService("support", self)

    @property
    def support_app(self) -> SupportAppService:
        """
        boto3 Session for SupportApp service.
        """
        return SupportAppService("support-app", self)

    @property
    def swf(self) -> SWFService:
        """
        boto3 Session for SWF service.
        """
        return SWFService("swf", self)

    @property
    def synthetics(self) -> SyntheticsService:
        """
        boto3 Session for Synthetics service.
        """
        return SyntheticsService("synthetics", self)

    @property
    def taxsettings(self) -> TaxSettingsService:
        """
        boto3 Session for TaxSettings service.
        """
        return TaxSettingsService("taxsettings", self)

    @property
    def textract(self) -> TextractService:
        """
        boto3 Session for Textract service.
        """
        return TextractService("textract", self)

    @property
    def timestream_influxdb(self) -> TimestreamInfluxDBService:
        """
        boto3 Session for TimestreamInfluxDB service.
        """
        return TimestreamInfluxDBService("timestream-influxdb", self)

    @property
    def timestream_query(self) -> TimestreamQueryService:
        """
        boto3 Session for TimestreamQuery service.
        """
        return TimestreamQueryService("timestream-query", self)

    @property
    def timestream_write(self) -> TimestreamWriteService:
        """
        boto3 Session for TimestreamWrite service.
        """
        return TimestreamWriteService("timestream-write", self)

    @property
    def tnb(self) -> TelcoNetworkBuilderService:
        """
        boto3 Session for TelcoNetworkBuilder service.
        """
        return TelcoNetworkBuilderService("tnb", self)

    @property
    def transcribe(self) -> TranscribeServiceService:
        """
        boto3 Session for TranscribeService service.
        """
        return TranscribeServiceService("transcribe", self)

    @property
    def transfer(self) -> TransferService:
        """
        boto3 Session for Transfer service.
        """
        return TransferService("transfer", self)

    @property
    def translate(self) -> TranslateService:
        """
        boto3 Session for Translate service.
        """
        return TranslateService("translate", self)

    @property
    def trustedadvisor(self) -> TrustedAdvisorPublicAPIService:
        """
        boto3 Session for TrustedAdvisorPublicAPI service.
        """
        return TrustedAdvisorPublicAPIService("trustedadvisor", self)

    @property
    def verifiedpermissions(self) -> VerifiedPermissionsService:
        """
        boto3 Session for VerifiedPermissions service.
        """
        return VerifiedPermissionsService("verifiedpermissions", self)

    @property
    def voice_id(self) -> VoiceIDService:
        """
        boto3 Session for VoiceID service.
        """
        return VoiceIDService("voice-id", self)

    @property
    def vpc_lattice(self) -> VPCLatticeService:
        """
        boto3 Session for VPCLattice service.
        """
        return VPCLatticeService("vpc-lattice", self)

    @property
    def waf(self) -> WAFService:
        """
        boto3 Session for WAF service.
        """
        return WAFService("waf", self)

    @property
    def waf_regional(self) -> WAFRegionalService:
        """
        boto3 Session for WAFRegional service.
        """
        return WAFRegionalService("waf-regional", self)

    @property
    def wafv2(self) -> WAFV2Service:
        """
        boto3 Session for WAFV2 service.
        """
        return WAFV2Service("wafv2", self)

    @property
    def wellarchitected(self) -> WellArchitectedService:
        """
        boto3 Session for WellArchitected service.
        """
        return WellArchitectedService("wellarchitected", self)

    @property
    def wisdom(self) -> ConnectWisdomServiceService:
        """
        boto3 Session for ConnectWisdomService service.
        """
        return ConnectWisdomServiceService("wisdom", self)

    @property
    def workdocs(self) -> WorkDocsService:
        """
        boto3 Session for WorkDocs service.
        """
        return WorkDocsService("workdocs", self)

    @property
    def workmail(self) -> WorkMailService:
        """
        boto3 Session for WorkMail service.
        """
        return WorkMailService("workmail", self)

    @property
    def workmailmessageflow(self) -> WorkMailMessageFlowService:
        """
        boto3 Session for WorkMailMessageFlow service.
        """
        return WorkMailMessageFlowService("workmailmessageflow", self)

    @property
    def workspaces(self) -> WorkSpacesService:
        """
        boto3 Session for WorkSpaces service.
        """
        return WorkSpacesService("workspaces", self)

    @property
    def workspaces_thin_client(self) -> WorkSpacesThinClientService:
        """
        boto3 Session for WorkSpacesThinClient service.
        """
        return WorkSpacesThinClientService("workspaces-thin-client", self)

    @property
    def workspaces_web(self) -> WorkSpacesWebService:
        """
        boto3 Session for WorkSpacesWeb service.
        """
        return WorkSpacesWebService("workspaces-web", self)

    @property
    def xray(self) -> XRayService:
        """
        boto3 Session for XRay service.
        """
        return XRayService("xray", self)
