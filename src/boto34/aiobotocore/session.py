"""
Type annotated wrapper for aiobotocore Session.

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.Session constructor
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # s3_client is a regular aiobotocore.AioBaseClient
    # with type annotations only in type checking mode
    async with session.s3.create_client() as s3_client:
        s3_client.list_buckets()
    ```
"""

from __future__ import annotations

from typing import Mapping

from aiobotocore.session import AioSession

from boto34.aiobotocore.service_factory import ServiceFactory
from boto34.aiobotocore.services.accessanalyzer import AccessAnalyzerService
from boto34.aiobotocore.services.account import AccountService
from boto34.aiobotocore.services.acm import ACMService
from boto34.aiobotocore.services.acm_pca import ACMPCAService
from boto34.aiobotocore.services.amp import PrometheusServiceService
from boto34.aiobotocore.services.amplify import AmplifyService
from boto34.aiobotocore.services.amplifybackend import AmplifyBackendService
from boto34.aiobotocore.services.amplifyuibuilder import AmplifyUIBuilderService
from boto34.aiobotocore.services.apigateway import APIGatewayService
from boto34.aiobotocore.services.apigatewaymanagementapi import ApiGatewayManagementApiService
from boto34.aiobotocore.services.apigatewayv2 import ApiGatewayV2Service
from boto34.aiobotocore.services.appconfig import AppConfigService
from boto34.aiobotocore.services.appconfigdata import AppConfigDataService
from boto34.aiobotocore.services.appfabric import AppFabricService
from boto34.aiobotocore.services.appflow import AppflowService
from boto34.aiobotocore.services.appintegrations import AppIntegrationsServiceService
from boto34.aiobotocore.services.application_autoscaling import ApplicationAutoScalingService
from boto34.aiobotocore.services.application_insights import ApplicationInsightsService
from boto34.aiobotocore.services.application_signals import CloudWatchApplicationSignalsService
from boto34.aiobotocore.services.applicationcostprofiler import ApplicationCostProfilerService
from boto34.aiobotocore.services.appmesh import AppMeshService
from boto34.aiobotocore.services.apprunner import AppRunnerService
from boto34.aiobotocore.services.appstream import AppStreamService
from boto34.aiobotocore.services.appsync import AppSyncService
from boto34.aiobotocore.services.apptest import MainframeModernizationApplicationTestingService
from boto34.aiobotocore.services.arc_zonal_shift import ARCZonalShiftService
from boto34.aiobotocore.services.artifact import ArtifactService
from boto34.aiobotocore.services.athena import AthenaService
from boto34.aiobotocore.services.auditmanager import AuditManagerService
from boto34.aiobotocore.services.autoscaling import AutoScalingService
from boto34.aiobotocore.services.autoscaling_plans import AutoScalingPlansService
from boto34.aiobotocore.services.b2bi import B2BIService
from boto34.aiobotocore.services.backup import BackupService
from boto34.aiobotocore.services.backup_gateway import BackupGatewayService
from boto34.aiobotocore.services.backupsearch import BackupSearchService
from boto34.aiobotocore.services.batch import BatchService
from boto34.aiobotocore.services.bcm_data_exports import BillingandCostManagementDataExportsService
from boto34.aiobotocore.services.bcm_pricing_calculator import (
    BillingandCostManagementPricingCalculatorService,
)
from boto34.aiobotocore.services.bedrock import BedrockService
from boto34.aiobotocore.services.bedrock_agent import AgentsforBedrockService
from boto34.aiobotocore.services.bedrock_agent_runtime import AgentsforBedrockRuntimeService
from boto34.aiobotocore.services.bedrock_data_automation import DataAutomationforBedrockService
from boto34.aiobotocore.services.bedrock_data_automation_runtime import (
    RuntimeforBedrockDataAutomationService,
)
from boto34.aiobotocore.services.bedrock_runtime import BedrockRuntimeService
from boto34.aiobotocore.services.billing import BillingService
from boto34.aiobotocore.services.billingconductor import BillingConductorService
from boto34.aiobotocore.services.braket import BraketService
from boto34.aiobotocore.services.budgets import BudgetsService
from boto34.aiobotocore.services.ce import CostExplorerService
from boto34.aiobotocore.services.chatbot import ChatbotService
from boto34.aiobotocore.services.chime import ChimeService
from boto34.aiobotocore.services.chime_sdk_identity import ChimeSDKIdentityService
from boto34.aiobotocore.services.chime_sdk_media_pipelines import ChimeSDKMediaPipelinesService
from boto34.aiobotocore.services.chime_sdk_meetings import ChimeSDKMeetingsService
from boto34.aiobotocore.services.chime_sdk_messaging import ChimeSDKMessagingService
from boto34.aiobotocore.services.chime_sdk_voice import ChimeSDKVoiceService
from boto34.aiobotocore.services.cleanrooms import CleanRoomsServiceService
from boto34.aiobotocore.services.cleanroomsml import CleanRoomsMLService
from boto34.aiobotocore.services.cloud9 import Cloud9Service
from boto34.aiobotocore.services.cloudcontrol import CloudControlApiService
from boto34.aiobotocore.services.clouddirectory import CloudDirectoryService
from boto34.aiobotocore.services.cloudformation import CloudFormationService
from boto34.aiobotocore.services.cloudfront import CloudFrontService
from boto34.aiobotocore.services.cloudfront_keyvaluestore import CloudFrontKeyValueStoreService
from boto34.aiobotocore.services.cloudhsm import CloudHSMService
from boto34.aiobotocore.services.cloudhsmv2 import CloudHSMV2Service
from boto34.aiobotocore.services.cloudsearch import CloudSearchService
from boto34.aiobotocore.services.cloudsearchdomain import CloudSearchDomainService
from boto34.aiobotocore.services.cloudtrail import CloudTrailService
from boto34.aiobotocore.services.cloudtrail_data import CloudTrailDataServiceService
from boto34.aiobotocore.services.cloudwatch import CloudWatchService
from boto34.aiobotocore.services.codeartifact import CodeArtifactService
from boto34.aiobotocore.services.codebuild import CodeBuildService
from boto34.aiobotocore.services.codecatalyst import CodeCatalystService
from boto34.aiobotocore.services.codecommit import CodeCommitService
from boto34.aiobotocore.services.codeconnections import CodeConnectionsService
from boto34.aiobotocore.services.codedeploy import CodeDeployService
from boto34.aiobotocore.services.codeguru_reviewer import CodeGuruReviewerService
from boto34.aiobotocore.services.codeguru_security import CodeGuruSecurityService
from boto34.aiobotocore.services.codeguruprofiler import CodeGuruProfilerService
from boto34.aiobotocore.services.codepipeline import CodePipelineService
from boto34.aiobotocore.services.codestar_connections import CodeStarconnectionsService
from boto34.aiobotocore.services.codestar_notifications import CodeStarNotificationsService
from boto34.aiobotocore.services.cognito_identity import CognitoIdentityService
from boto34.aiobotocore.services.cognito_idp import CognitoIdentityProviderService
from boto34.aiobotocore.services.cognito_sync import CognitoSyncService
from boto34.aiobotocore.services.comprehend import ComprehendService
from boto34.aiobotocore.services.comprehendmedical import ComprehendMedicalService
from boto34.aiobotocore.services.compute_optimizer import ComputeOptimizerService
from boto34.aiobotocore.services.config import ConfigServiceService
from boto34.aiobotocore.services.connect import ConnectService
from boto34.aiobotocore.services.connect_contact_lens import ConnectContactLensService
from boto34.aiobotocore.services.connectcampaigns import ConnectCampaignServiceService
from boto34.aiobotocore.services.connectcampaignsv2 import ConnectCampaignServiceV2Service
from boto34.aiobotocore.services.connectcases import ConnectCasesService
from boto34.aiobotocore.services.connectparticipant import ConnectParticipantService
from boto34.aiobotocore.services.controlcatalog import ControlCatalogService
from boto34.aiobotocore.services.controltower import ControlTowerService
from boto34.aiobotocore.services.cost_optimization_hub import CostOptimizationHubService
from boto34.aiobotocore.services.cur import CostandUsageReportServiceService
from boto34.aiobotocore.services.customer_profiles import CustomerProfilesService
from boto34.aiobotocore.services.databrew import GlueDataBrewService
from boto34.aiobotocore.services.dataexchange import DataExchangeService
from boto34.aiobotocore.services.datapipeline import DataPipelineService
from boto34.aiobotocore.services.datasync import DataSyncService
from boto34.aiobotocore.services.datazone import DataZoneService
from boto34.aiobotocore.services.dax import DAXService
from boto34.aiobotocore.services.deadline import DeadlineCloudService
from boto34.aiobotocore.services.detective import DetectiveService
from boto34.aiobotocore.services.devicefarm import DeviceFarmService
from boto34.aiobotocore.services.devops_guru import DevOpsGuruService
from boto34.aiobotocore.services.directconnect import DirectConnectService
from boto34.aiobotocore.services.discovery import ApplicationDiscoveryServiceService
from boto34.aiobotocore.services.dlm import DLMService
from boto34.aiobotocore.services.dms import DatabaseMigrationServiceService
from boto34.aiobotocore.services.docdb import DocDBService
from boto34.aiobotocore.services.docdb_elastic import DocDBElasticService
from boto34.aiobotocore.services.drs import DrsService
from boto34.aiobotocore.services.ds import DirectoryServiceService
from boto34.aiobotocore.services.ds_data import DirectoryServiceDataService
from boto34.aiobotocore.services.dsql import AuroraDSQLService
from boto34.aiobotocore.services.dynamodb import DynamoDBService
from boto34.aiobotocore.services.dynamodbstreams import DynamoDBStreamsService
from boto34.aiobotocore.services.ebs import EBSService
from boto34.aiobotocore.services.ec2 import EC2Service
from boto34.aiobotocore.services.ec2_instance_connect import EC2InstanceConnectService
from boto34.aiobotocore.services.ecr import ECRService
from boto34.aiobotocore.services.ecr_public import ECRPublicService
from boto34.aiobotocore.services.ecs import ECSService
from boto34.aiobotocore.services.efs import EFSService
from boto34.aiobotocore.services.eks import EKSService
from boto34.aiobotocore.services.eks_auth import EKSAuthService
from boto34.aiobotocore.services.elasticache import ElastiCacheService
from boto34.aiobotocore.services.elasticbeanstalk import ElasticBeanstalkService
from boto34.aiobotocore.services.elastictranscoder import ElasticTranscoderService
from boto34.aiobotocore.services.elb import ElasticLoadBalancingService
from boto34.aiobotocore.services.elbv2 import ElasticLoadBalancingv2Service
from boto34.aiobotocore.services.emr import EMRService
from boto34.aiobotocore.services.emr_containers import EMRContainersService
from boto34.aiobotocore.services.emr_serverless import EMRServerlessService
from boto34.aiobotocore.services.entityresolution import EntityResolutionService
from boto34.aiobotocore.services.es import ElasticsearchServiceService
from boto34.aiobotocore.services.events import EventBridgeService
from boto34.aiobotocore.services.evidently import CloudWatchEvidentlyService
from boto34.aiobotocore.services.finspace import FinspaceService
from boto34.aiobotocore.services.finspace_data import FinSpaceDataService
from boto34.aiobotocore.services.firehose import FirehoseService
from boto34.aiobotocore.services.fis import FISService
from boto34.aiobotocore.services.fms import FMSService
from boto34.aiobotocore.services.forecast import ForecastServiceService
from boto34.aiobotocore.services.forecastquery import ForecastQueryServiceService
from boto34.aiobotocore.services.frauddetector import FraudDetectorService
from boto34.aiobotocore.services.freetier import FreeTierService
from boto34.aiobotocore.services.fsx import FSxService
from boto34.aiobotocore.services.gamelift import GameLiftService
from boto34.aiobotocore.services.geo_maps import LocationServiceMapsV2Service
from boto34.aiobotocore.services.geo_places import LocationServicePlacesV2Service
from boto34.aiobotocore.services.geo_routes import LocationServiceRoutesV2Service
from boto34.aiobotocore.services.glacier import GlacierService
from boto34.aiobotocore.services.globalaccelerator import GlobalAcceleratorService
from boto34.aiobotocore.services.glue import GlueService
from boto34.aiobotocore.services.grafana import ManagedGrafanaService
from boto34.aiobotocore.services.greengrass import GreengrassService
from boto34.aiobotocore.services.greengrassv2 import GreengrassV2Service
from boto34.aiobotocore.services.groundstation import GroundStationService
from boto34.aiobotocore.services.guardduty import GuardDutyService
from boto34.aiobotocore.services.health import HealthService
from boto34.aiobotocore.services.healthlake import HealthLakeService
from boto34.aiobotocore.services.iam import IAMService
from boto34.aiobotocore.services.identitystore import IdentityStoreService
from boto34.aiobotocore.services.imagebuilder import ImagebuilderService
from boto34.aiobotocore.services.importexport import ImportExportService
from boto34.aiobotocore.services.inspector import InspectorService
from boto34.aiobotocore.services.inspector2 import Inspector2Service
from boto34.aiobotocore.services.inspector_scan import InspectorscanService
from boto34.aiobotocore.services.internetmonitor import CloudWatchInternetMonitorService
from boto34.aiobotocore.services.invoicing import InvoicingService
from boto34.aiobotocore.services.iot import IoTService
from boto34.aiobotocore.services.iot_data import IoTDataPlaneService
from boto34.aiobotocore.services.iot_jobs_data import IoTJobsDataPlaneService
from boto34.aiobotocore.services.iotanalytics import IoTAnalyticsService
from boto34.aiobotocore.services.iotdeviceadvisor import IoTDeviceAdvisorService
from boto34.aiobotocore.services.iotevents import IoTEventsService
from boto34.aiobotocore.services.iotevents_data import IoTEventsDataService
from boto34.aiobotocore.services.iotfleethub import IoTFleetHubService
from boto34.aiobotocore.services.iotfleetwise import IoTFleetWiseService
from boto34.aiobotocore.services.iotsecuretunneling import IoTSecureTunnelingService
from boto34.aiobotocore.services.iotsitewise import IoTSiteWiseService
from boto34.aiobotocore.services.iotthingsgraph import IoTThingsGraphService
from boto34.aiobotocore.services.iottwinmaker import IoTTwinMakerService
from boto34.aiobotocore.services.iotwireless import IoTWirelessService
from boto34.aiobotocore.services.ivs import IVSService
from boto34.aiobotocore.services.ivs_realtime import IvsrealtimeService
from boto34.aiobotocore.services.ivschat import IvschatService
from boto34.aiobotocore.services.kafka import KafkaService
from boto34.aiobotocore.services.kafkaconnect import KafkaConnectService
from boto34.aiobotocore.services.kendra import KendraService
from boto34.aiobotocore.services.kendra_ranking import KendraRankingService
from boto34.aiobotocore.services.keyspaces import KeyspacesService
from boto34.aiobotocore.services.kinesis import KinesisService
from boto34.aiobotocore.services.kinesis_video_archived_media import (
    KinesisVideoArchivedMediaService,
)
from boto34.aiobotocore.services.kinesis_video_media import KinesisVideoMediaService
from boto34.aiobotocore.services.kinesis_video_signaling import KinesisVideoSignalingChannelsService
from boto34.aiobotocore.services.kinesis_video_webrtc_storage import (
    KinesisVideoWebRTCStorageService,
)
from boto34.aiobotocore.services.kinesisanalytics import KinesisAnalyticsService
from boto34.aiobotocore.services.kinesisanalyticsv2 import KinesisAnalyticsV2Service
from boto34.aiobotocore.services.kinesisvideo import KinesisVideoService
from boto34.aiobotocore.services.kms import KMSService
from boto34.aiobotocore.services.lakeformation import LakeFormationService
from boto34.aiobotocore.services.lambda_ import LambdaService
from boto34.aiobotocore.services.launch_wizard import LaunchWizardService
from boto34.aiobotocore.services.lex_models import LexModelBuildingServiceService
from boto34.aiobotocore.services.lex_runtime import LexRuntimeServiceService
from boto34.aiobotocore.services.lexv2_models import LexModelsV2Service
from boto34.aiobotocore.services.lexv2_runtime import LexRuntimeV2Service
from boto34.aiobotocore.services.license_manager import LicenseManagerService
from boto34.aiobotocore.services.license_manager_linux_subscriptions import (
    LicenseManagerLinuxSubscriptionsService,
)
from boto34.aiobotocore.services.license_manager_user_subscriptions import (
    LicenseManagerUserSubscriptionsService,
)
from boto34.aiobotocore.services.lightsail import LightsailService
from boto34.aiobotocore.services.location import LocationServiceService
from boto34.aiobotocore.services.logs import CloudWatchLogsService
from boto34.aiobotocore.services.lookoutequipment import LookoutEquipmentService
from boto34.aiobotocore.services.lookoutmetrics import LookoutMetricsService
from boto34.aiobotocore.services.lookoutvision import LookoutforVisionService
from boto34.aiobotocore.services.m2 import MainframeModernizationService
from boto34.aiobotocore.services.machinelearning import MachineLearningService
from boto34.aiobotocore.services.macie2 import Macie2Service
from boto34.aiobotocore.services.mailmanager import MailManagerService
from boto34.aiobotocore.services.managedblockchain import ManagedBlockchainService
from boto34.aiobotocore.services.managedblockchain_query import ManagedBlockchainQueryService
from boto34.aiobotocore.services.marketplace_agreement import AgreementServiceService
from boto34.aiobotocore.services.marketplace_catalog import MarketplaceCatalogService
from boto34.aiobotocore.services.marketplace_deployment import MarketplaceDeploymentServiceService
from boto34.aiobotocore.services.marketplace_entitlement import MarketplaceEntitlementServiceService
from boto34.aiobotocore.services.marketplace_reporting import MarketplaceReportingServiceService
from boto34.aiobotocore.services.marketplacecommerceanalytics import (
    MarketplaceCommerceAnalyticsService,
)
from boto34.aiobotocore.services.mediaconnect import MediaConnectService
from boto34.aiobotocore.services.mediaconvert import MediaConvertService
from boto34.aiobotocore.services.medialive import MediaLiveService
from boto34.aiobotocore.services.mediapackage import MediaPackageService
from boto34.aiobotocore.services.mediapackage_vod import MediaPackageVodService
from boto34.aiobotocore.services.mediapackagev2 import Mediapackagev2Service
from boto34.aiobotocore.services.mediastore import MediaStoreService
from boto34.aiobotocore.services.mediastore_data import MediaStoreDataService
from boto34.aiobotocore.services.mediatailor import MediaTailorService
from boto34.aiobotocore.services.medical_imaging import HealthImagingService
from boto34.aiobotocore.services.memorydb import MemoryDBService
from boto34.aiobotocore.services.meteringmarketplace import MarketplaceMeteringService
from boto34.aiobotocore.services.mgh import MigrationHubService
from boto34.aiobotocore.services.mgn import MgnService
from boto34.aiobotocore.services.migration_hub_refactor_spaces import (
    MigrationHubRefactorSpacesService,
)
from boto34.aiobotocore.services.migrationhub_config import MigrationHubConfigService
from boto34.aiobotocore.services.migrationhuborchestrator import MigrationHubOrchestratorService
from boto34.aiobotocore.services.migrationhubstrategy import (
    MigrationHubStrategyRecommendationsService,
)
from boto34.aiobotocore.services.mq import MQService
from boto34.aiobotocore.services.mturk import MTurkService
from boto34.aiobotocore.services.mwaa import MWAAService
from boto34.aiobotocore.services.neptune import NeptuneService
from boto34.aiobotocore.services.neptune_graph import NeptuneGraphService
from boto34.aiobotocore.services.neptunedata import NeptuneDataService
from boto34.aiobotocore.services.network_firewall import NetworkFirewallService
from boto34.aiobotocore.services.networkflowmonitor import NetworkFlowMonitorService
from boto34.aiobotocore.services.networkmanager import NetworkManagerService
from boto34.aiobotocore.services.networkmonitor import CloudWatchNetworkMonitorService
from boto34.aiobotocore.services.notifications import UserNotificationsService
from boto34.aiobotocore.services.notificationscontacts import UserNotificationsContactsService
from boto34.aiobotocore.services.oam import CloudWatchObservabilityAccessManagerService
from boto34.aiobotocore.services.observabilityadmin import (
    CloudWatchObservabilityAdminServiceService,
)
from boto34.aiobotocore.services.omics import OmicsService
from boto34.aiobotocore.services.opensearch import OpenSearchServiceService
from boto34.aiobotocore.services.opensearchserverless import OpenSearchServiceServerlessService
from boto34.aiobotocore.services.opsworks import OpsWorksService
from boto34.aiobotocore.services.opsworkscm import OpsWorksCMService
from boto34.aiobotocore.services.organizations import OrganizationsService
from boto34.aiobotocore.services.osis import OpenSearchIngestionService
from boto34.aiobotocore.services.outposts import OutpostsService
from boto34.aiobotocore.services.panorama import PanoramaService
from boto34.aiobotocore.services.partnercentral_selling import PartnerCentralSellingAPIService
from boto34.aiobotocore.services.payment_cryptography import PaymentCryptographyControlPlaneService
from boto34.aiobotocore.services.payment_cryptography_data import (
    PaymentCryptographyDataPlaneService,
)
from boto34.aiobotocore.services.pca_connector_ad import PcaConnectorAdService
from boto34.aiobotocore.services.pca_connector_scep import PrivateCAConnectorforSCEPService
from boto34.aiobotocore.services.pcs import ParallelComputingServiceService
from boto34.aiobotocore.services.personalize import PersonalizeService
from boto34.aiobotocore.services.personalize_events import PersonalizeEventsService
from boto34.aiobotocore.services.personalize_runtime import PersonalizeRuntimeService
from boto34.aiobotocore.services.pi import PIService
from boto34.aiobotocore.services.pinpoint import PinpointService
from boto34.aiobotocore.services.pinpoint_email import PinpointEmailService
from boto34.aiobotocore.services.pinpoint_sms_voice import PinpointSMSVoiceService
from boto34.aiobotocore.services.pinpoint_sms_voice_v2 import PinpointSMSVoiceV2Service
from boto34.aiobotocore.services.pipes import EventBridgePipesService
from boto34.aiobotocore.services.polly import PollyService
from boto34.aiobotocore.services.pricing import PricingService
from boto34.aiobotocore.services.privatenetworks import Private5GService
from boto34.aiobotocore.services.proton import ProtonService
from boto34.aiobotocore.services.qapps import QAppsService
from boto34.aiobotocore.services.qbusiness import QBusinessService
from boto34.aiobotocore.services.qconnect import QConnectService
from boto34.aiobotocore.services.qldb import QLDBService
from boto34.aiobotocore.services.qldb_session import QLDBSessionService
from boto34.aiobotocore.services.quicksight import QuickSightService
from boto34.aiobotocore.services.ram import RAMService
from boto34.aiobotocore.services.rbin import RecycleBinService
from boto34.aiobotocore.services.rds import RDSService
from boto34.aiobotocore.services.rds_data import RDSDataServiceService
from boto34.aiobotocore.services.redshift import RedshiftService
from boto34.aiobotocore.services.redshift_data import RedshiftDataAPIServiceService
from boto34.aiobotocore.services.redshift_serverless import RedshiftServerlessService
from boto34.aiobotocore.services.rekognition import RekognitionService
from boto34.aiobotocore.services.repostspace import RePostPrivateService
from boto34.aiobotocore.services.resiliencehub import ResilienceHubService
from boto34.aiobotocore.services.resource_explorer_2 import ResourceExplorerService
from boto34.aiobotocore.services.resource_groups import ResourceGroupsService
from boto34.aiobotocore.services.resourcegroupstaggingapi import ResourceGroupsTaggingAPIService
from boto34.aiobotocore.services.robomaker import RoboMakerService
from boto34.aiobotocore.services.rolesanywhere import IAMRolesAnywhereService
from boto34.aiobotocore.services.route53 import Route53Service
from boto34.aiobotocore.services.route53_recovery_cluster import Route53RecoveryClusterService
from boto34.aiobotocore.services.route53_recovery_control_config import (
    Route53RecoveryControlConfigService,
)
from boto34.aiobotocore.services.route53_recovery_readiness import Route53RecoveryReadinessService
from boto34.aiobotocore.services.route53domains import Route53DomainsService
from boto34.aiobotocore.services.route53profiles import Route53ProfilesService
from boto34.aiobotocore.services.route53resolver import Route53ResolverService
from boto34.aiobotocore.services.rum import CloudWatchRUMService
from boto34.aiobotocore.services.s3 import S3Service
from boto34.aiobotocore.services.s3control import S3ControlService
from boto34.aiobotocore.services.s3outposts import S3OutpostsService
from boto34.aiobotocore.services.s3tables import S3TablesService
from boto34.aiobotocore.services.sagemaker import SageMakerService
from boto34.aiobotocore.services.sagemaker_a2i_runtime import AugmentedAIRuntimeService
from boto34.aiobotocore.services.sagemaker_edge import SagemakerEdgeManagerService
from boto34.aiobotocore.services.sagemaker_featurestore_runtime import (
    SageMakerFeatureStoreRuntimeService,
)
from boto34.aiobotocore.services.sagemaker_geospatial import SageMakergeospatialcapabilitiesService
from boto34.aiobotocore.services.sagemaker_metrics import SageMakerMetricsService
from boto34.aiobotocore.services.sagemaker_runtime import SageMakerRuntimeService
from boto34.aiobotocore.services.savingsplans import SavingsPlansService
from boto34.aiobotocore.services.scheduler import EventBridgeSchedulerService
from boto34.aiobotocore.services.schemas import SchemasService
from boto34.aiobotocore.services.sdb import SimpleDBService
from boto34.aiobotocore.services.secretsmanager import SecretsManagerService
from boto34.aiobotocore.services.security_ir import SecurityIncidentResponseService
from boto34.aiobotocore.services.securityhub import SecurityHubService
from boto34.aiobotocore.services.securitylake import SecurityLakeService
from boto34.aiobotocore.services.serverlessrepo import ServerlessApplicationRepositoryService
from boto34.aiobotocore.services.service_quotas import ServiceQuotasService
from boto34.aiobotocore.services.servicecatalog import ServiceCatalogService
from boto34.aiobotocore.services.servicecatalog_appregistry import AppRegistryService
from boto34.aiobotocore.services.servicediscovery import ServiceDiscoveryService
from boto34.aiobotocore.services.ses import SESService
from boto34.aiobotocore.services.sesv2 import SESV2Service
from boto34.aiobotocore.services.shield import ShieldService
from boto34.aiobotocore.services.signer import SignerService
from boto34.aiobotocore.services.simspaceweaver import SimSpaceWeaverService
from boto34.aiobotocore.services.sms import SMSService
from boto34.aiobotocore.services.sms_voice import SMSVoiceService
from boto34.aiobotocore.services.snow_device_management import SnowDeviceManagementService
from boto34.aiobotocore.services.snowball import SnowballService
from boto34.aiobotocore.services.sns import SNSService
from boto34.aiobotocore.services.socialmessaging import EndUserMessagingSocialService
from boto34.aiobotocore.services.sqs import SQSService
from boto34.aiobotocore.services.ssm import SSMService
from boto34.aiobotocore.services.ssm_contacts import SSMContactsService
from boto34.aiobotocore.services.ssm_incidents import SSMIncidentsService
from boto34.aiobotocore.services.ssm_quicksetup import SystemsManagerQuickSetupService
from boto34.aiobotocore.services.ssm_sap import SsmSapService
from boto34.aiobotocore.services.sso import SSOService
from boto34.aiobotocore.services.sso_admin import SSOAdminService
from boto34.aiobotocore.services.sso_oidc import SSOOIDCService
from boto34.aiobotocore.services.stepfunctions import SFNService
from boto34.aiobotocore.services.storagegateway import StorageGatewayService
from boto34.aiobotocore.services.sts import STSService
from boto34.aiobotocore.services.supplychain import SupplyChainService
from boto34.aiobotocore.services.support import SupportService
from boto34.aiobotocore.services.support_app import SupportAppService
from boto34.aiobotocore.services.swf import SWFService
from boto34.aiobotocore.services.synthetics import SyntheticsService
from boto34.aiobotocore.services.taxsettings import TaxSettingsService
from boto34.aiobotocore.services.textract import TextractService
from boto34.aiobotocore.services.timestream_influxdb import TimestreamInfluxDBService
from boto34.aiobotocore.services.timestream_query import TimestreamQueryService
from boto34.aiobotocore.services.timestream_write import TimestreamWriteService
from boto34.aiobotocore.services.tnb import TelcoNetworkBuilderService
from boto34.aiobotocore.services.transcribe import TranscribeServiceService
from boto34.aiobotocore.services.transfer import TransferService
from boto34.aiobotocore.services.translate import TranslateService
from boto34.aiobotocore.services.trustedadvisor import TrustedAdvisorPublicAPIService
from boto34.aiobotocore.services.verifiedpermissions import VerifiedPermissionsService
from boto34.aiobotocore.services.voice_id import VoiceIDService
from boto34.aiobotocore.services.vpc_lattice import VPCLatticeService
from boto34.aiobotocore.services.waf import WAFService
from boto34.aiobotocore.services.waf_regional import WAFRegionalService
from boto34.aiobotocore.services.wafv2 import WAFV2Service
from boto34.aiobotocore.services.wellarchitected import WellArchitectedService
from boto34.aiobotocore.services.wisdom import ConnectWisdomServiceService
from boto34.aiobotocore.services.workdocs import WorkDocsService
from boto34.aiobotocore.services.workmail import WorkMailService
from boto34.aiobotocore.services.workmailmessageflow import WorkMailMessageFlowService
from boto34.aiobotocore.services.workspaces import WorkSpacesService
from boto34.aiobotocore.services.workspaces_thin_client import WorkSpacesThinClientService
from boto34.aiobotocore.services.workspaces_web import WorkSpacesWebService
from boto34.aiobotocore.services.xray import XRayService


class Session(AioSession):
    @property
    def accessanalyzer(self) -> AccessAnalyzerService:
        """
        aiobotocore Session for AccessAnalyzer service.
        """
        return AccessAnalyzerService("accessanalyzer", self)

    @property
    def account(self) -> AccountService:
        """
        aiobotocore Session for Account service.
        """
        return AccountService("account", self)

    @property
    def acm(self) -> ACMService:
        """
        aiobotocore Session for ACM service.
        """
        return ACMService("acm", self)

    @property
    def acm_pca(self) -> ACMPCAService:
        """
        aiobotocore Session for ACMPCA service.
        """
        return ACMPCAService("acm-pca", self)

    @property
    def amp(self) -> PrometheusServiceService:
        """
        aiobotocore Session for PrometheusService service.
        """
        return PrometheusServiceService("amp", self)

    @property
    def amplify(self) -> AmplifyService:
        """
        aiobotocore Session for Amplify service.
        """
        return AmplifyService("amplify", self)

    @property
    def amplifybackend(self) -> AmplifyBackendService:
        """
        aiobotocore Session for AmplifyBackend service.
        """
        return AmplifyBackendService("amplifybackend", self)

    @property
    def amplifyuibuilder(self) -> AmplifyUIBuilderService:
        """
        aiobotocore Session for AmplifyUIBuilder service.
        """
        return AmplifyUIBuilderService("amplifyuibuilder", self)

    @property
    def apigateway(self) -> APIGatewayService:
        """
        aiobotocore Session for APIGateway service.
        """
        return APIGatewayService("apigateway", self)

    @property
    def apigatewaymanagementapi(self) -> ApiGatewayManagementApiService:
        """
        aiobotocore Session for ApiGatewayManagementApi service.
        """
        return ApiGatewayManagementApiService("apigatewaymanagementapi", self)

    @property
    def apigatewayv2(self) -> ApiGatewayV2Service:
        """
        aiobotocore Session for ApiGatewayV2 service.
        """
        return ApiGatewayV2Service("apigatewayv2", self)

    @property
    def appconfig(self) -> AppConfigService:
        """
        aiobotocore Session for AppConfig service.
        """
        return AppConfigService("appconfig", self)

    @property
    def appconfigdata(self) -> AppConfigDataService:
        """
        aiobotocore Session for AppConfigData service.
        """
        return AppConfigDataService("appconfigdata", self)

    @property
    def appfabric(self) -> AppFabricService:
        """
        aiobotocore Session for AppFabric service.
        """
        return AppFabricService("appfabric", self)

    @property
    def appflow(self) -> AppflowService:
        """
        aiobotocore Session for Appflow service.
        """
        return AppflowService("appflow", self)

    @property
    def appintegrations(self) -> AppIntegrationsServiceService:
        """
        aiobotocore Session for AppIntegrationsService service.
        """
        return AppIntegrationsServiceService("appintegrations", self)

    @property
    def application_autoscaling(self) -> ApplicationAutoScalingService:
        """
        aiobotocore Session for ApplicationAutoScaling service.
        """
        return ApplicationAutoScalingService("application-autoscaling", self)

    @property
    def application_insights(self) -> ApplicationInsightsService:
        """
        aiobotocore Session for ApplicationInsights service.
        """
        return ApplicationInsightsService("application-insights", self)

    @property
    def application_signals(self) -> CloudWatchApplicationSignalsService:
        """
        aiobotocore Session for CloudWatchApplicationSignals service.
        """
        return CloudWatchApplicationSignalsService("application-signals", self)

    @property
    def applicationcostprofiler(self) -> ApplicationCostProfilerService:
        """
        aiobotocore Session for ApplicationCostProfiler service.
        """
        return ApplicationCostProfilerService("applicationcostprofiler", self)

    @property
    def appmesh(self) -> AppMeshService:
        """
        aiobotocore Session for AppMesh service.
        """
        return AppMeshService("appmesh", self)

    @property
    def apprunner(self) -> AppRunnerService:
        """
        aiobotocore Session for AppRunner service.
        """
        return AppRunnerService("apprunner", self)

    @property
    def appstream(self) -> AppStreamService:
        """
        aiobotocore Session for AppStream service.
        """
        return AppStreamService("appstream", self)

    @property
    def appsync(self) -> AppSyncService:
        """
        aiobotocore Session for AppSync service.
        """
        return AppSyncService("appsync", self)

    @property
    def apptest(self) -> MainframeModernizationApplicationTestingService:
        """
        aiobotocore Session for MainframeModernizationApplicationTesting service.
        """
        return MainframeModernizationApplicationTestingService("apptest", self)

    @property
    def arc_zonal_shift(self) -> ARCZonalShiftService:
        """
        aiobotocore Session for ARCZonalShift service.
        """
        return ARCZonalShiftService("arc-zonal-shift", self)

    @property
    def artifact(self) -> ArtifactService:
        """
        aiobotocore Session for Artifact service.
        """
        return ArtifactService("artifact", self)

    @property
    def athena(self) -> AthenaService:
        """
        aiobotocore Session for Athena service.
        """
        return AthenaService("athena", self)

    @property
    def auditmanager(self) -> AuditManagerService:
        """
        aiobotocore Session for AuditManager service.
        """
        return AuditManagerService("auditmanager", self)

    @property
    def autoscaling(self) -> AutoScalingService:
        """
        aiobotocore Session for AutoScaling service.
        """
        return AutoScalingService("autoscaling", self)

    @property
    def autoscaling_plans(self) -> AutoScalingPlansService:
        """
        aiobotocore Session for AutoScalingPlans service.
        """
        return AutoScalingPlansService("autoscaling-plans", self)

    @property
    def b2bi(self) -> B2BIService:
        """
        aiobotocore Session for B2BI service.
        """
        return B2BIService("b2bi", self)

    @property
    def backup(self) -> BackupService:
        """
        aiobotocore Session for Backup service.
        """
        return BackupService("backup", self)

    @property
    def backup_gateway(self) -> BackupGatewayService:
        """
        aiobotocore Session for BackupGateway service.
        """
        return BackupGatewayService("backup-gateway", self)

    @property
    def backupsearch(self) -> BackupSearchService:
        """
        aiobotocore Session for BackupSearch service.
        """
        return BackupSearchService("backupsearch", self)

    @property
    def batch(self) -> BatchService:
        """
        aiobotocore Session for Batch service.
        """
        return BatchService("batch", self)

    @property
    def bcm_data_exports(self) -> BillingandCostManagementDataExportsService:
        """
        aiobotocore Session for BillingandCostManagementDataExports service.
        """
        return BillingandCostManagementDataExportsService("bcm-data-exports", self)

    @property
    def bcm_pricing_calculator(self) -> BillingandCostManagementPricingCalculatorService:
        """
        aiobotocore Session for BillingandCostManagementPricingCalculator service.
        """
        return BillingandCostManagementPricingCalculatorService("bcm-pricing-calculator", self)

    @property
    def bedrock(self) -> BedrockService:
        """
        aiobotocore Session for Bedrock service.
        """
        return BedrockService("bedrock", self)

    @property
    def bedrock_agent(self) -> AgentsforBedrockService:
        """
        aiobotocore Session for AgentsforBedrock service.
        """
        return AgentsforBedrockService("bedrock-agent", self)

    @property
    def bedrock_agent_runtime(self) -> AgentsforBedrockRuntimeService:
        """
        aiobotocore Session for AgentsforBedrockRuntime service.
        """
        return AgentsforBedrockRuntimeService("bedrock-agent-runtime", self)

    @property
    def bedrock_data_automation(self) -> DataAutomationforBedrockService:
        """
        aiobotocore Session for DataAutomationforBedrock service.
        """
        return DataAutomationforBedrockService("bedrock-data-automation", self)

    @property
    def bedrock_data_automation_runtime(self) -> RuntimeforBedrockDataAutomationService:
        """
        aiobotocore Session for RuntimeforBedrockDataAutomation service.
        """
        return RuntimeforBedrockDataAutomationService("bedrock-data-automation-runtime", self)

    @property
    def bedrock_runtime(self) -> BedrockRuntimeService:
        """
        aiobotocore Session for BedrockRuntime service.
        """
        return BedrockRuntimeService("bedrock-runtime", self)

    @property
    def billing(self) -> BillingService:
        """
        aiobotocore Session for Billing service.
        """
        return BillingService("billing", self)

    @property
    def billingconductor(self) -> BillingConductorService:
        """
        aiobotocore Session for BillingConductor service.
        """
        return BillingConductorService("billingconductor", self)

    @property
    def braket(self) -> BraketService:
        """
        aiobotocore Session for Braket service.
        """
        return BraketService("braket", self)

    @property
    def budgets(self) -> BudgetsService:
        """
        aiobotocore Session for Budgets service.
        """
        return BudgetsService("budgets", self)

    @property
    def ce(self) -> CostExplorerService:
        """
        aiobotocore Session for CostExplorer service.
        """
        return CostExplorerService("ce", self)

    @property
    def chatbot(self) -> ChatbotService:
        """
        aiobotocore Session for Chatbot service.
        """
        return ChatbotService("chatbot", self)

    @property
    def chime(self) -> ChimeService:
        """
        aiobotocore Session for Chime service.
        """
        return ChimeService("chime", self)

    @property
    def chime_sdk_identity(self) -> ChimeSDKIdentityService:
        """
        aiobotocore Session for ChimeSDKIdentity service.
        """
        return ChimeSDKIdentityService("chime-sdk-identity", self)

    @property
    def chime_sdk_media_pipelines(self) -> ChimeSDKMediaPipelinesService:
        """
        aiobotocore Session for ChimeSDKMediaPipelines service.
        """
        return ChimeSDKMediaPipelinesService("chime-sdk-media-pipelines", self)

    @property
    def chime_sdk_meetings(self) -> ChimeSDKMeetingsService:
        """
        aiobotocore Session for ChimeSDKMeetings service.
        """
        return ChimeSDKMeetingsService("chime-sdk-meetings", self)

    @property
    def chime_sdk_messaging(self) -> ChimeSDKMessagingService:
        """
        aiobotocore Session for ChimeSDKMessaging service.
        """
        return ChimeSDKMessagingService("chime-sdk-messaging", self)

    @property
    def chime_sdk_voice(self) -> ChimeSDKVoiceService:
        """
        aiobotocore Session for ChimeSDKVoice service.
        """
        return ChimeSDKVoiceService("chime-sdk-voice", self)

    @property
    def cleanrooms(self) -> CleanRoomsServiceService:
        """
        aiobotocore Session for CleanRoomsService service.
        """
        return CleanRoomsServiceService("cleanrooms", self)

    @property
    def cleanroomsml(self) -> CleanRoomsMLService:
        """
        aiobotocore Session for CleanRoomsML service.
        """
        return CleanRoomsMLService("cleanroomsml", self)

    @property
    def cloud9(self) -> Cloud9Service:
        """
        aiobotocore Session for Cloud9 service.
        """
        return Cloud9Service("cloud9", self)

    @property
    def cloudcontrol(self) -> CloudControlApiService:
        """
        aiobotocore Session for CloudControlApi service.
        """
        return CloudControlApiService("cloudcontrol", self)

    @property
    def clouddirectory(self) -> CloudDirectoryService:
        """
        aiobotocore Session for CloudDirectory service.
        """
        return CloudDirectoryService("clouddirectory", self)

    @property
    def cloudformation(self) -> CloudFormationService:
        """
        aiobotocore Session for CloudFormation service.
        """
        return CloudFormationService("cloudformation", self)

    @property
    def cloudfront(self) -> CloudFrontService:
        """
        aiobotocore Session for CloudFront service.
        """
        return CloudFrontService("cloudfront", self)

    @property
    def cloudfront_keyvaluestore(self) -> CloudFrontKeyValueStoreService:
        """
        aiobotocore Session for CloudFrontKeyValueStore service.
        """
        return CloudFrontKeyValueStoreService("cloudfront-keyvaluestore", self)

    @property
    def cloudhsm(self) -> CloudHSMService:
        """
        aiobotocore Session for CloudHSM service.
        """
        return CloudHSMService("cloudhsm", self)

    @property
    def cloudhsmv2(self) -> CloudHSMV2Service:
        """
        aiobotocore Session for CloudHSMV2 service.
        """
        return CloudHSMV2Service("cloudhsmv2", self)

    @property
    def cloudsearch(self) -> CloudSearchService:
        """
        aiobotocore Session for CloudSearch service.
        """
        return CloudSearchService("cloudsearch", self)

    @property
    def cloudsearchdomain(self) -> CloudSearchDomainService:
        """
        aiobotocore Session for CloudSearchDomain service.
        """
        return CloudSearchDomainService("cloudsearchdomain", self)

    @property
    def cloudtrail(self) -> CloudTrailService:
        """
        aiobotocore Session for CloudTrail service.
        """
        return CloudTrailService("cloudtrail", self)

    @property
    def cloudtrail_data(self) -> CloudTrailDataServiceService:
        """
        aiobotocore Session for CloudTrailDataService service.
        """
        return CloudTrailDataServiceService("cloudtrail-data", self)

    @property
    def cloudwatch(self) -> CloudWatchService:
        """
        aiobotocore Session for CloudWatch service.
        """
        return CloudWatchService("cloudwatch", self)

    @property
    def codeartifact(self) -> CodeArtifactService:
        """
        aiobotocore Session for CodeArtifact service.
        """
        return CodeArtifactService("codeartifact", self)

    @property
    def codebuild(self) -> CodeBuildService:
        """
        aiobotocore Session for CodeBuild service.
        """
        return CodeBuildService("codebuild", self)

    @property
    def codecatalyst(self) -> CodeCatalystService:
        """
        aiobotocore Session for CodeCatalyst service.
        """
        return CodeCatalystService("codecatalyst", self)

    @property
    def codecommit(self) -> CodeCommitService:
        """
        aiobotocore Session for CodeCommit service.
        """
        return CodeCommitService("codecommit", self)

    @property
    def codeconnections(self) -> CodeConnectionsService:
        """
        aiobotocore Session for CodeConnections service.
        """
        return CodeConnectionsService("codeconnections", self)

    @property
    def codedeploy(self) -> CodeDeployService:
        """
        aiobotocore Session for CodeDeploy service.
        """
        return CodeDeployService("codedeploy", self)

    @property
    def codeguru_reviewer(self) -> CodeGuruReviewerService:
        """
        aiobotocore Session for CodeGuruReviewer service.
        """
        return CodeGuruReviewerService("codeguru-reviewer", self)

    @property
    def codeguru_security(self) -> CodeGuruSecurityService:
        """
        aiobotocore Session for CodeGuruSecurity service.
        """
        return CodeGuruSecurityService("codeguru-security", self)

    @property
    def codeguruprofiler(self) -> CodeGuruProfilerService:
        """
        aiobotocore Session for CodeGuruProfiler service.
        """
        return CodeGuruProfilerService("codeguruprofiler", self)

    @property
    def codepipeline(self) -> CodePipelineService:
        """
        aiobotocore Session for CodePipeline service.
        """
        return CodePipelineService("codepipeline", self)

    @property
    def codestar_connections(self) -> CodeStarconnectionsService:
        """
        aiobotocore Session for CodeStarconnections service.
        """
        return CodeStarconnectionsService("codestar-connections", self)

    @property
    def codestar_notifications(self) -> CodeStarNotificationsService:
        """
        aiobotocore Session for CodeStarNotifications service.
        """
        return CodeStarNotificationsService("codestar-notifications", self)

    @property
    def cognito_identity(self) -> CognitoIdentityService:
        """
        aiobotocore Session for CognitoIdentity service.
        """
        return CognitoIdentityService("cognito-identity", self)

    @property
    def cognito_idp(self) -> CognitoIdentityProviderService:
        """
        aiobotocore Session for CognitoIdentityProvider service.
        """
        return CognitoIdentityProviderService("cognito-idp", self)

    @property
    def cognito_sync(self) -> CognitoSyncService:
        """
        aiobotocore Session for CognitoSync service.
        """
        return CognitoSyncService("cognito-sync", self)

    @property
    def comprehend(self) -> ComprehendService:
        """
        aiobotocore Session for Comprehend service.
        """
        return ComprehendService("comprehend", self)

    @property
    def comprehendmedical(self) -> ComprehendMedicalService:
        """
        aiobotocore Session for ComprehendMedical service.
        """
        return ComprehendMedicalService("comprehendmedical", self)

    @property
    def compute_optimizer(self) -> ComputeOptimizerService:
        """
        aiobotocore Session for ComputeOptimizer service.
        """
        return ComputeOptimizerService("compute-optimizer", self)

    @property
    def config(self) -> ConfigServiceService:
        """
        aiobotocore Session for ConfigService service.
        """
        return ConfigServiceService("config", self)

    @property
    def connect(self) -> ConnectService:
        """
        aiobotocore Session for Connect service.
        """
        return ConnectService("connect", self)

    @property
    def connect_contact_lens(self) -> ConnectContactLensService:
        """
        aiobotocore Session for ConnectContactLens service.
        """
        return ConnectContactLensService("connect-contact-lens", self)

    @property
    def connectcampaigns(self) -> ConnectCampaignServiceService:
        """
        aiobotocore Session for ConnectCampaignService service.
        """
        return ConnectCampaignServiceService("connectcampaigns", self)

    @property
    def connectcampaignsv2(self) -> ConnectCampaignServiceV2Service:
        """
        aiobotocore Session for ConnectCampaignServiceV2 service.
        """
        return ConnectCampaignServiceV2Service("connectcampaignsv2", self)

    @property
    def connectcases(self) -> ConnectCasesService:
        """
        aiobotocore Session for ConnectCases service.
        """
        return ConnectCasesService("connectcases", self)

    @property
    def connectparticipant(self) -> ConnectParticipantService:
        """
        aiobotocore Session for ConnectParticipant service.
        """
        return ConnectParticipantService("connectparticipant", self)

    @property
    def controlcatalog(self) -> ControlCatalogService:
        """
        aiobotocore Session for ControlCatalog service.
        """
        return ControlCatalogService("controlcatalog", self)

    @property
    def controltower(self) -> ControlTowerService:
        """
        aiobotocore Session for ControlTower service.
        """
        return ControlTowerService("controltower", self)

    @property
    def cost_optimization_hub(self) -> CostOptimizationHubService:
        """
        aiobotocore Session for CostOptimizationHub service.
        """
        return CostOptimizationHubService("cost-optimization-hub", self)

    @property
    def cur(self) -> CostandUsageReportServiceService:
        """
        aiobotocore Session for CostandUsageReportService service.
        """
        return CostandUsageReportServiceService("cur", self)

    @property
    def customer_profiles(self) -> CustomerProfilesService:
        """
        aiobotocore Session for CustomerProfiles service.
        """
        return CustomerProfilesService("customer-profiles", self)

    @property
    def databrew(self) -> GlueDataBrewService:
        """
        aiobotocore Session for GlueDataBrew service.
        """
        return GlueDataBrewService("databrew", self)

    @property
    def dataexchange(self) -> DataExchangeService:
        """
        aiobotocore Session for DataExchange service.
        """
        return DataExchangeService("dataexchange", self)

    @property
    def datapipeline(self) -> DataPipelineService:
        """
        aiobotocore Session for DataPipeline service.
        """
        return DataPipelineService("datapipeline", self)

    @property
    def datasync(self) -> DataSyncService:
        """
        aiobotocore Session for DataSync service.
        """
        return DataSyncService("datasync", self)

    @property
    def datazone(self) -> DataZoneService:
        """
        aiobotocore Session for DataZone service.
        """
        return DataZoneService("datazone", self)

    @property
    def dax(self) -> DAXService:
        """
        aiobotocore Session for DAX service.
        """
        return DAXService("dax", self)

    @property
    def deadline(self) -> DeadlineCloudService:
        """
        aiobotocore Session for DeadlineCloud service.
        """
        return DeadlineCloudService("deadline", self)

    @property
    def detective(self) -> DetectiveService:
        """
        aiobotocore Session for Detective service.
        """
        return DetectiveService("detective", self)

    @property
    def devicefarm(self) -> DeviceFarmService:
        """
        aiobotocore Session for DeviceFarm service.
        """
        return DeviceFarmService("devicefarm", self)

    @property
    def devops_guru(self) -> DevOpsGuruService:
        """
        aiobotocore Session for DevOpsGuru service.
        """
        return DevOpsGuruService("devops-guru", self)

    @property
    def directconnect(self) -> DirectConnectService:
        """
        aiobotocore Session for DirectConnect service.
        """
        return DirectConnectService("directconnect", self)

    @property
    def discovery(self) -> ApplicationDiscoveryServiceService:
        """
        aiobotocore Session for ApplicationDiscoveryService service.
        """
        return ApplicationDiscoveryServiceService("discovery", self)

    @property
    def dlm(self) -> DLMService:
        """
        aiobotocore Session for DLM service.
        """
        return DLMService("dlm", self)

    @property
    def dms(self) -> DatabaseMigrationServiceService:
        """
        aiobotocore Session for DatabaseMigrationService service.
        """
        return DatabaseMigrationServiceService("dms", self)

    @property
    def docdb(self) -> DocDBService:
        """
        aiobotocore Session for DocDB service.
        """
        return DocDBService("docdb", self)

    @property
    def docdb_elastic(self) -> DocDBElasticService:
        """
        aiobotocore Session for DocDBElastic service.
        """
        return DocDBElasticService("docdb-elastic", self)

    @property
    def drs(self) -> DrsService:
        """
        aiobotocore Session for Drs service.
        """
        return DrsService("drs", self)

    @property
    def ds(self) -> DirectoryServiceService:
        """
        aiobotocore Session for DirectoryService service.
        """
        return DirectoryServiceService("ds", self)

    @property
    def ds_data(self) -> DirectoryServiceDataService:
        """
        aiobotocore Session for DirectoryServiceData service.
        """
        return DirectoryServiceDataService("ds-data", self)

    @property
    def dsql(self) -> AuroraDSQLService:
        """
        aiobotocore Session for AuroraDSQL service.
        """
        return AuroraDSQLService("dsql", self)

    @property
    def dynamodb(self) -> DynamoDBService:
        """
        aiobotocore Session for DynamoDB service.
        """
        return DynamoDBService("dynamodb", self)

    @property
    def dynamodbstreams(self) -> DynamoDBStreamsService:
        """
        aiobotocore Session for DynamoDBStreams service.
        """
        return DynamoDBStreamsService("dynamodbstreams", self)

    @property
    def ebs(self) -> EBSService:
        """
        aiobotocore Session for EBS service.
        """
        return EBSService("ebs", self)

    @property
    def ec2(self) -> EC2Service:
        """
        aiobotocore Session for EC2 service.
        """
        return EC2Service("ec2", self)

    @property
    def ec2_instance_connect(self) -> EC2InstanceConnectService:
        """
        aiobotocore Session for EC2InstanceConnect service.
        """
        return EC2InstanceConnectService("ec2-instance-connect", self)

    @property
    def ecr(self) -> ECRService:
        """
        aiobotocore Session for ECR service.
        """
        return ECRService("ecr", self)

    @property
    def ecr_public(self) -> ECRPublicService:
        """
        aiobotocore Session for ECRPublic service.
        """
        return ECRPublicService("ecr-public", self)

    @property
    def ecs(self) -> ECSService:
        """
        aiobotocore Session for ECS service.
        """
        return ECSService("ecs", self)

    @property
    def efs(self) -> EFSService:
        """
        aiobotocore Session for EFS service.
        """
        return EFSService("efs", self)

    @property
    def eks(self) -> EKSService:
        """
        aiobotocore Session for EKS service.
        """
        return EKSService("eks", self)

    @property
    def eks_auth(self) -> EKSAuthService:
        """
        aiobotocore Session for EKSAuth service.
        """
        return EKSAuthService("eks-auth", self)

    @property
    def elasticache(self) -> ElastiCacheService:
        """
        aiobotocore Session for ElastiCache service.
        """
        return ElastiCacheService("elasticache", self)

    @property
    def elasticbeanstalk(self) -> ElasticBeanstalkService:
        """
        aiobotocore Session for ElasticBeanstalk service.
        """
        return ElasticBeanstalkService("elasticbeanstalk", self)

    @property
    def elastictranscoder(self) -> ElasticTranscoderService:
        """
        aiobotocore Session for ElasticTranscoder service.
        """
        return ElasticTranscoderService("elastictranscoder", self)

    @property
    def elb(self) -> ElasticLoadBalancingService:
        """
        aiobotocore Session for ElasticLoadBalancing service.
        """
        return ElasticLoadBalancingService("elb", self)

    @property
    def elbv2(self) -> ElasticLoadBalancingv2Service:
        """
        aiobotocore Session for ElasticLoadBalancingv2 service.
        """
        return ElasticLoadBalancingv2Service("elbv2", self)

    @property
    def emr(self) -> EMRService:
        """
        aiobotocore Session for EMR service.
        """
        return EMRService("emr", self)

    @property
    def emr_containers(self) -> EMRContainersService:
        """
        aiobotocore Session for EMRContainers service.
        """
        return EMRContainersService("emr-containers", self)

    @property
    def emr_serverless(self) -> EMRServerlessService:
        """
        aiobotocore Session for EMRServerless service.
        """
        return EMRServerlessService("emr-serverless", self)

    @property
    def entityresolution(self) -> EntityResolutionService:
        """
        aiobotocore Session for EntityResolution service.
        """
        return EntityResolutionService("entityresolution", self)

    @property
    def es(self) -> ElasticsearchServiceService:
        """
        aiobotocore Session for ElasticsearchService service.
        """
        return ElasticsearchServiceService("es", self)

    @property
    def eventbridge(self) -> EventBridgeService:
        """
        aiobotocore Session for EventBridge service.
        """
        return EventBridgeService("events", self)

    @property
    def evidently(self) -> CloudWatchEvidentlyService:
        """
        aiobotocore Session for CloudWatchEvidently service.
        """
        return CloudWatchEvidentlyService("evidently", self)

    @property
    def finspace(self) -> FinspaceService:
        """
        aiobotocore Session for Finspace service.
        """
        return FinspaceService("finspace", self)

    @property
    def finspace_data(self) -> FinSpaceDataService:
        """
        aiobotocore Session for FinSpaceData service.
        """
        return FinSpaceDataService("finspace-data", self)

    @property
    def firehose(self) -> FirehoseService:
        """
        aiobotocore Session for Firehose service.
        """
        return FirehoseService("firehose", self)

    @property
    def fis(self) -> FISService:
        """
        aiobotocore Session for FIS service.
        """
        return FISService("fis", self)

    @property
    def fms(self) -> FMSService:
        """
        aiobotocore Session for FMS service.
        """
        return FMSService("fms", self)

    @property
    def forecast(self) -> ForecastServiceService:
        """
        aiobotocore Session for ForecastService service.
        """
        return ForecastServiceService("forecast", self)

    @property
    def forecastquery(self) -> ForecastQueryServiceService:
        """
        aiobotocore Session for ForecastQueryService service.
        """
        return ForecastQueryServiceService("forecastquery", self)

    @property
    def frauddetector(self) -> FraudDetectorService:
        """
        aiobotocore Session for FraudDetector service.
        """
        return FraudDetectorService("frauddetector", self)

    @property
    def freetier(self) -> FreeTierService:
        """
        aiobotocore Session for FreeTier service.
        """
        return FreeTierService("freetier", self)

    @property
    def fsx(self) -> FSxService:
        """
        aiobotocore Session for FSx service.
        """
        return FSxService("fsx", self)

    @property
    def gamelift(self) -> GameLiftService:
        """
        aiobotocore Session for GameLift service.
        """
        return GameLiftService("gamelift", self)

    @property
    def geo_maps(self) -> LocationServiceMapsV2Service:
        """
        aiobotocore Session for LocationServiceMapsV2 service.
        """
        return LocationServiceMapsV2Service("geo-maps", self)

    @property
    def geo_places(self) -> LocationServicePlacesV2Service:
        """
        aiobotocore Session for LocationServicePlacesV2 service.
        """
        return LocationServicePlacesV2Service("geo-places", self)

    @property
    def geo_routes(self) -> LocationServiceRoutesV2Service:
        """
        aiobotocore Session for LocationServiceRoutesV2 service.
        """
        return LocationServiceRoutesV2Service("geo-routes", self)

    @property
    def glacier(self) -> GlacierService:
        """
        aiobotocore Session for Glacier service.
        """
        return GlacierService("glacier", self)

    @property
    def globalaccelerator(self) -> GlobalAcceleratorService:
        """
        aiobotocore Session for GlobalAccelerator service.
        """
        return GlobalAcceleratorService("globalaccelerator", self)

    @property
    def glue(self) -> GlueService:
        """
        aiobotocore Session for Glue service.
        """
        return GlueService("glue", self)

    @property
    def grafana(self) -> ManagedGrafanaService:
        """
        aiobotocore Session for ManagedGrafana service.
        """
        return ManagedGrafanaService("grafana", self)

    @property
    def greengrass(self) -> GreengrassService:
        """
        aiobotocore Session for Greengrass service.
        """
        return GreengrassService("greengrass", self)

    @property
    def greengrassv2(self) -> GreengrassV2Service:
        """
        aiobotocore Session for GreengrassV2 service.
        """
        return GreengrassV2Service("greengrassv2", self)

    @property
    def groundstation(self) -> GroundStationService:
        """
        aiobotocore Session for GroundStation service.
        """
        return GroundStationService("groundstation", self)

    @property
    def guardduty(self) -> GuardDutyService:
        """
        aiobotocore Session for GuardDuty service.
        """
        return GuardDutyService("guardduty", self)

    @property
    def health(self) -> HealthService:
        """
        aiobotocore Session for Health service.
        """
        return HealthService("health", self)

    @property
    def healthlake(self) -> HealthLakeService:
        """
        aiobotocore Session for HealthLake service.
        """
        return HealthLakeService("healthlake", self)

    @property
    def iam(self) -> IAMService:
        """
        aiobotocore Session for IAM service.
        """
        return IAMService("iam", self)

    @property
    def identitystore(self) -> IdentityStoreService:
        """
        aiobotocore Session for IdentityStore service.
        """
        return IdentityStoreService("identitystore", self)

    @property
    def imagebuilder(self) -> ImagebuilderService:
        """
        aiobotocore Session for Imagebuilder service.
        """
        return ImagebuilderService("imagebuilder", self)

    @property
    def importexport(self) -> ImportExportService:
        """
        aiobotocore Session for ImportExport service.
        """
        return ImportExportService("importexport", self)

    @property
    def inspector(self) -> InspectorService:
        """
        aiobotocore Session for Inspector service.
        """
        return InspectorService("inspector", self)

    @property
    def inspector_scan(self) -> InspectorscanService:
        """
        aiobotocore Session for Inspectorscan service.
        """
        return InspectorscanService("inspector-scan", self)

    @property
    def inspector2(self) -> Inspector2Service:
        """
        aiobotocore Session for Inspector2 service.
        """
        return Inspector2Service("inspector2", self)

    @property
    def internetmonitor(self) -> CloudWatchInternetMonitorService:
        """
        aiobotocore Session for CloudWatchInternetMonitor service.
        """
        return CloudWatchInternetMonitorService("internetmonitor", self)

    @property
    def invoicing(self) -> InvoicingService:
        """
        aiobotocore Session for Invoicing service.
        """
        return InvoicingService("invoicing", self)

    @property
    def iot(self) -> IoTService:
        """
        aiobotocore Session for IoT service.
        """
        return IoTService("iot", self)

    @property
    def iot_data(self) -> IoTDataPlaneService:
        """
        aiobotocore Session for IoTDataPlane service.
        """
        return IoTDataPlaneService("iot-data", self)

    @property
    def iot_jobs_data(self) -> IoTJobsDataPlaneService:
        """
        aiobotocore Session for IoTJobsDataPlane service.
        """
        return IoTJobsDataPlaneService("iot-jobs-data", self)

    @property
    def iotanalytics(self) -> IoTAnalyticsService:
        """
        aiobotocore Session for IoTAnalytics service.
        """
        return IoTAnalyticsService("iotanalytics", self)

    @property
    def iotdeviceadvisor(self) -> IoTDeviceAdvisorService:
        """
        aiobotocore Session for IoTDeviceAdvisor service.
        """
        return IoTDeviceAdvisorService("iotdeviceadvisor", self)

    @property
    def iotevents(self) -> IoTEventsService:
        """
        aiobotocore Session for IoTEvents service.
        """
        return IoTEventsService("iotevents", self)

    @property
    def iotevents_data(self) -> IoTEventsDataService:
        """
        aiobotocore Session for IoTEventsData service.
        """
        return IoTEventsDataService("iotevents-data", self)

    @property
    def iotfleethub(self) -> IoTFleetHubService:
        """
        aiobotocore Session for IoTFleetHub service.
        """
        return IoTFleetHubService("iotfleethub", self)

    @property
    def iotfleetwise(self) -> IoTFleetWiseService:
        """
        aiobotocore Session for IoTFleetWise service.
        """
        return IoTFleetWiseService("iotfleetwise", self)

    @property
    def iotsecuretunneling(self) -> IoTSecureTunnelingService:
        """
        aiobotocore Session for IoTSecureTunneling service.
        """
        return IoTSecureTunnelingService("iotsecuretunneling", self)

    @property
    def iotsitewise(self) -> IoTSiteWiseService:
        """
        aiobotocore Session for IoTSiteWise service.
        """
        return IoTSiteWiseService("iotsitewise", self)

    @property
    def iotthingsgraph(self) -> IoTThingsGraphService:
        """
        aiobotocore Session for IoTThingsGraph service.
        """
        return IoTThingsGraphService("iotthingsgraph", self)

    @property
    def iottwinmaker(self) -> IoTTwinMakerService:
        """
        aiobotocore Session for IoTTwinMaker service.
        """
        return IoTTwinMakerService("iottwinmaker", self)

    @property
    def iotwireless(self) -> IoTWirelessService:
        """
        aiobotocore Session for IoTWireless service.
        """
        return IoTWirelessService("iotwireless", self)

    @property
    def ivs(self) -> IVSService:
        """
        aiobotocore Session for IVS service.
        """
        return IVSService("ivs", self)

    @property
    def ivs_realtime(self) -> IvsrealtimeService:
        """
        aiobotocore Session for Ivsrealtime service.
        """
        return IvsrealtimeService("ivs-realtime", self)

    @property
    def ivschat(self) -> IvschatService:
        """
        aiobotocore Session for Ivschat service.
        """
        return IvschatService("ivschat", self)

    @property
    def kafka(self) -> KafkaService:
        """
        aiobotocore Session for Kafka service.
        """
        return KafkaService("kafka", self)

    @property
    def kafkaconnect(self) -> KafkaConnectService:
        """
        aiobotocore Session for KafkaConnect service.
        """
        return KafkaConnectService("kafkaconnect", self)

    @property
    def kendra(self) -> KendraService:
        """
        aiobotocore Session for Kendra service.
        """
        return KendraService("kendra", self)

    @property
    def kendra_ranking(self) -> KendraRankingService:
        """
        aiobotocore Session for KendraRanking service.
        """
        return KendraRankingService("kendra-ranking", self)

    @property
    def keyspaces(self) -> KeyspacesService:
        """
        aiobotocore Session for Keyspaces service.
        """
        return KeyspacesService("keyspaces", self)

    @property
    def kinesis(self) -> KinesisService:
        """
        aiobotocore Session for Kinesis service.
        """
        return KinesisService("kinesis", self)

    @property
    def kinesis_video_archived_media(self) -> KinesisVideoArchivedMediaService:
        """
        aiobotocore Session for KinesisVideoArchivedMedia service.
        """
        return KinesisVideoArchivedMediaService("kinesis-video-archived-media", self)

    @property
    def kinesis_video_media(self) -> KinesisVideoMediaService:
        """
        aiobotocore Session for KinesisVideoMedia service.
        """
        return KinesisVideoMediaService("kinesis-video-media", self)

    @property
    def kinesis_video_signaling(self) -> KinesisVideoSignalingChannelsService:
        """
        aiobotocore Session for KinesisVideoSignalingChannels service.
        """
        return KinesisVideoSignalingChannelsService("kinesis-video-signaling", self)

    @property
    def kinesis_video_webrtc_storage(self) -> KinesisVideoWebRTCStorageService:
        """
        aiobotocore Session for KinesisVideoWebRTCStorage service.
        """
        return KinesisVideoWebRTCStorageService("kinesis-video-webrtc-storage", self)

    @property
    def kinesisanalytics(self) -> KinesisAnalyticsService:
        """
        aiobotocore Session for KinesisAnalytics service.
        """
        return KinesisAnalyticsService("kinesisanalytics", self)

    @property
    def kinesisanalyticsv2(self) -> KinesisAnalyticsV2Service:
        """
        aiobotocore Session for KinesisAnalyticsV2 service.
        """
        return KinesisAnalyticsV2Service("kinesisanalyticsv2", self)

    @property
    def kinesisvideo(self) -> KinesisVideoService:
        """
        aiobotocore Session for KinesisVideo service.
        """
        return KinesisVideoService("kinesisvideo", self)

    @property
    def kms(self) -> KMSService:
        """
        aiobotocore Session for KMS service.
        """
        return KMSService("kms", self)

    @property
    def lakeformation(self) -> LakeFormationService:
        """
        aiobotocore Session for LakeFormation service.
        """
        return LakeFormationService("lakeformation", self)

    @property
    def lambda_(self) -> LambdaService:
        """
        aiobotocore Session for Lambda service.
        """
        return LambdaService("lambda", self)

    @property
    def launch_wizard(self) -> LaunchWizardService:
        """
        aiobotocore Session for LaunchWizard service.
        """
        return LaunchWizardService("launch-wizard", self)

    @property
    def lex_models(self) -> LexModelBuildingServiceService:
        """
        aiobotocore Session for LexModelBuildingService service.
        """
        return LexModelBuildingServiceService("lex-models", self)

    @property
    def lex_runtime(self) -> LexRuntimeServiceService:
        """
        aiobotocore Session for LexRuntimeService service.
        """
        return LexRuntimeServiceService("lex-runtime", self)

    @property
    def lexv2_models(self) -> LexModelsV2Service:
        """
        aiobotocore Session for LexModelsV2 service.
        """
        return LexModelsV2Service("lexv2-models", self)

    @property
    def lexv2_runtime(self) -> LexRuntimeV2Service:
        """
        aiobotocore Session for LexRuntimeV2 service.
        """
        return LexRuntimeV2Service("lexv2-runtime", self)

    @property
    def license_manager(self) -> LicenseManagerService:
        """
        aiobotocore Session for LicenseManager service.
        """
        return LicenseManagerService("license-manager", self)

    @property
    def license_manager_linux_subscriptions(self) -> LicenseManagerLinuxSubscriptionsService:
        """
        aiobotocore Session for LicenseManagerLinuxSubscriptions service.
        """
        return LicenseManagerLinuxSubscriptionsService("license-manager-linux-subscriptions", self)

    @property
    def license_manager_user_subscriptions(self) -> LicenseManagerUserSubscriptionsService:
        """
        aiobotocore Session for LicenseManagerUserSubscriptions service.
        """
        return LicenseManagerUserSubscriptionsService("license-manager-user-subscriptions", self)

    @property
    def lightsail(self) -> LightsailService:
        """
        aiobotocore Session for Lightsail service.
        """
        return LightsailService("lightsail", self)

    @property
    def location(self) -> LocationServiceService:
        """
        aiobotocore Session for LocationService service.
        """
        return LocationServiceService("location", self)

    @property
    def logs(self) -> CloudWatchLogsService:
        """
        aiobotocore Session for CloudWatchLogs service.
        """
        return CloudWatchLogsService("logs", self)

    @property
    def lookoutequipment(self) -> LookoutEquipmentService:
        """
        aiobotocore Session for LookoutEquipment service.
        """
        return LookoutEquipmentService("lookoutequipment", self)

    @property
    def lookoutmetrics(self) -> LookoutMetricsService:
        """
        aiobotocore Session for LookoutMetrics service.
        """
        return LookoutMetricsService("lookoutmetrics", self)

    @property
    def lookoutvision(self) -> LookoutforVisionService:
        """
        aiobotocore Session for LookoutforVision service.
        """
        return LookoutforVisionService("lookoutvision", self)

    @property
    def m2(self) -> MainframeModernizationService:
        """
        aiobotocore Session for MainframeModernization service.
        """
        return MainframeModernizationService("m2", self)

    @property
    def machinelearning(self) -> MachineLearningService:
        """
        aiobotocore Session for MachineLearning service.
        """
        return MachineLearningService("machinelearning", self)

    @property
    def macie2(self) -> Macie2Service:
        """
        aiobotocore Session for Macie2 service.
        """
        return Macie2Service("macie2", self)

    @property
    def mailmanager(self) -> MailManagerService:
        """
        aiobotocore Session for MailManager service.
        """
        return MailManagerService("mailmanager", self)

    @property
    def managedblockchain(self) -> ManagedBlockchainService:
        """
        aiobotocore Session for ManagedBlockchain service.
        """
        return ManagedBlockchainService("managedblockchain", self)

    @property
    def managedblockchain_query(self) -> ManagedBlockchainQueryService:
        """
        aiobotocore Session for ManagedBlockchainQuery service.
        """
        return ManagedBlockchainQueryService("managedblockchain-query", self)

    @property
    def marketplace_agreement(self) -> AgreementServiceService:
        """
        aiobotocore Session for AgreementService service.
        """
        return AgreementServiceService("marketplace-agreement", self)

    @property
    def marketplace_catalog(self) -> MarketplaceCatalogService:
        """
        aiobotocore Session for MarketplaceCatalog service.
        """
        return MarketplaceCatalogService("marketplace-catalog", self)

    @property
    def marketplace_deployment(self) -> MarketplaceDeploymentServiceService:
        """
        aiobotocore Session for MarketplaceDeploymentService service.
        """
        return MarketplaceDeploymentServiceService("marketplace-deployment", self)

    @property
    def marketplace_entitlement(self) -> MarketplaceEntitlementServiceService:
        """
        aiobotocore Session for MarketplaceEntitlementService service.
        """
        return MarketplaceEntitlementServiceService("marketplace-entitlement", self)

    @property
    def marketplace_reporting(self) -> MarketplaceReportingServiceService:
        """
        aiobotocore Session for MarketplaceReportingService service.
        """
        return MarketplaceReportingServiceService("marketplace-reporting", self)

    @property
    def marketplacecommerceanalytics(self) -> MarketplaceCommerceAnalyticsService:
        """
        aiobotocore Session for MarketplaceCommerceAnalytics service.
        """
        return MarketplaceCommerceAnalyticsService("marketplacecommerceanalytics", self)

    @property
    def mediaconnect(self) -> MediaConnectService:
        """
        aiobotocore Session for MediaConnect service.
        """
        return MediaConnectService("mediaconnect", self)

    @property
    def mediaconvert(self) -> MediaConvertService:
        """
        aiobotocore Session for MediaConvert service.
        """
        return MediaConvertService("mediaconvert", self)

    @property
    def medialive(self) -> MediaLiveService:
        """
        aiobotocore Session for MediaLive service.
        """
        return MediaLiveService("medialive", self)

    @property
    def mediapackage(self) -> MediaPackageService:
        """
        aiobotocore Session for MediaPackage service.
        """
        return MediaPackageService("mediapackage", self)

    @property
    def mediapackage_vod(self) -> MediaPackageVodService:
        """
        aiobotocore Session for MediaPackageVod service.
        """
        return MediaPackageVodService("mediapackage-vod", self)

    @property
    def mediapackagev2(self) -> Mediapackagev2Service:
        """
        aiobotocore Session for Mediapackagev2 service.
        """
        return Mediapackagev2Service("mediapackagev2", self)

    @property
    def mediastore(self) -> MediaStoreService:
        """
        aiobotocore Session for MediaStore service.
        """
        return MediaStoreService("mediastore", self)

    @property
    def mediastore_data(self) -> MediaStoreDataService:
        """
        aiobotocore Session for MediaStoreData service.
        """
        return MediaStoreDataService("mediastore-data", self)

    @property
    def mediatailor(self) -> MediaTailorService:
        """
        aiobotocore Session for MediaTailor service.
        """
        return MediaTailorService("mediatailor", self)

    @property
    def medical_imaging(self) -> HealthImagingService:
        """
        aiobotocore Session for HealthImaging service.
        """
        return HealthImagingService("medical-imaging", self)

    @property
    def memorydb(self) -> MemoryDBService:
        """
        aiobotocore Session for MemoryDB service.
        """
        return MemoryDBService("memorydb", self)

    @property
    def meteringmarketplace(self) -> MarketplaceMeteringService:
        """
        aiobotocore Session for MarketplaceMetering service.
        """
        return MarketplaceMeteringService("meteringmarketplace", self)

    @property
    def mgh(self) -> MigrationHubService:
        """
        aiobotocore Session for MigrationHub service.
        """
        return MigrationHubService("mgh", self)

    @property
    def mgn(self) -> MgnService:
        """
        aiobotocore Session for Mgn service.
        """
        return MgnService("mgn", self)

    @property
    def migration_hub_refactor_spaces(self) -> MigrationHubRefactorSpacesService:
        """
        aiobotocore Session for MigrationHubRefactorSpaces service.
        """
        return MigrationHubRefactorSpacesService("migration-hub-refactor-spaces", self)

    @property
    def migrationhub_config(self) -> MigrationHubConfigService:
        """
        aiobotocore Session for MigrationHubConfig service.
        """
        return MigrationHubConfigService("migrationhub-config", self)

    @property
    def migrationhuborchestrator(self) -> MigrationHubOrchestratorService:
        """
        aiobotocore Session for MigrationHubOrchestrator service.
        """
        return MigrationHubOrchestratorService("migrationhuborchestrator", self)

    @property
    def migrationhubstrategy(self) -> MigrationHubStrategyRecommendationsService:
        """
        aiobotocore Session for MigrationHubStrategyRecommendations service.
        """
        return MigrationHubStrategyRecommendationsService("migrationhubstrategy", self)

    @property
    def mq(self) -> MQService:
        """
        aiobotocore Session for MQ service.
        """
        return MQService("mq", self)

    @property
    def mturk(self) -> MTurkService:
        """
        aiobotocore Session for MTurk service.
        """
        return MTurkService("mturk", self)

    @property
    def mwaa(self) -> MWAAService:
        """
        aiobotocore Session for MWAA service.
        """
        return MWAAService("mwaa", self)

    @property
    def neptune(self) -> NeptuneService:
        """
        aiobotocore Session for Neptune service.
        """
        return NeptuneService("neptune", self)

    @property
    def neptune_graph(self) -> NeptuneGraphService:
        """
        aiobotocore Session for NeptuneGraph service.
        """
        return NeptuneGraphService("neptune-graph", self)

    @property
    def neptunedata(self) -> NeptuneDataService:
        """
        aiobotocore Session for NeptuneData service.
        """
        return NeptuneDataService("neptunedata", self)

    @property
    def network_firewall(self) -> NetworkFirewallService:
        """
        aiobotocore Session for NetworkFirewall service.
        """
        return NetworkFirewallService("network-firewall", self)

    @property
    def networkflowmonitor(self) -> NetworkFlowMonitorService:
        """
        aiobotocore Session for NetworkFlowMonitor service.
        """
        return NetworkFlowMonitorService("networkflowmonitor", self)

    @property
    def networkmanager(self) -> NetworkManagerService:
        """
        aiobotocore Session for NetworkManager service.
        """
        return NetworkManagerService("networkmanager", self)

    @property
    def networkmonitor(self) -> CloudWatchNetworkMonitorService:
        """
        aiobotocore Session for CloudWatchNetworkMonitor service.
        """
        return CloudWatchNetworkMonitorService("networkmonitor", self)

    @property
    def notifications(self) -> UserNotificationsService:
        """
        aiobotocore Session for UserNotifications service.
        """
        return UserNotificationsService("notifications", self)

    @property
    def notificationscontacts(self) -> UserNotificationsContactsService:
        """
        aiobotocore Session for UserNotificationsContacts service.
        """
        return UserNotificationsContactsService("notificationscontacts", self)

    @property
    def oam(self) -> CloudWatchObservabilityAccessManagerService:
        """
        aiobotocore Session for CloudWatchObservabilityAccessManager service.
        """
        return CloudWatchObservabilityAccessManagerService("oam", self)

    @property
    def observabilityadmin(self) -> CloudWatchObservabilityAdminServiceService:
        """
        aiobotocore Session for CloudWatchObservabilityAdminService service.
        """
        return CloudWatchObservabilityAdminServiceService("observabilityadmin", self)

    @property
    def omics(self) -> OmicsService:
        """
        aiobotocore Session for Omics service.
        """
        return OmicsService("omics", self)

    @property
    def opensearch(self) -> OpenSearchServiceService:
        """
        aiobotocore Session for OpenSearchService service.
        """
        return OpenSearchServiceService("opensearch", self)

    @property
    def opensearchserverless(self) -> OpenSearchServiceServerlessService:
        """
        aiobotocore Session for OpenSearchServiceServerless service.
        """
        return OpenSearchServiceServerlessService("opensearchserverless", self)

    @property
    def opsworks(self) -> OpsWorksService:
        """
        aiobotocore Session for OpsWorks service.
        """
        return OpsWorksService("opsworks", self)

    @property
    def opsworkscm(self) -> OpsWorksCMService:
        """
        aiobotocore Session for OpsWorksCM service.
        """
        return OpsWorksCMService("opsworkscm", self)

    @property
    def organizations(self) -> OrganizationsService:
        """
        aiobotocore Session for Organizations service.
        """
        return OrganizationsService("organizations", self)

    @property
    def osis(self) -> OpenSearchIngestionService:
        """
        aiobotocore Session for OpenSearchIngestion service.
        """
        return OpenSearchIngestionService("osis", self)

    @property
    def outposts(self) -> OutpostsService:
        """
        aiobotocore Session for Outposts service.
        """
        return OutpostsService("outposts", self)

    @property
    def panorama(self) -> PanoramaService:
        """
        aiobotocore Session for Panorama service.
        """
        return PanoramaService("panorama", self)

    @property
    def partnercentral_selling(self) -> PartnerCentralSellingAPIService:
        """
        aiobotocore Session for PartnerCentralSellingAPI service.
        """
        return PartnerCentralSellingAPIService("partnercentral-selling", self)

    @property
    def payment_cryptography(self) -> PaymentCryptographyControlPlaneService:
        """
        aiobotocore Session for PaymentCryptographyControlPlane service.
        """
        return PaymentCryptographyControlPlaneService("payment-cryptography", self)

    @property
    def payment_cryptography_data(self) -> PaymentCryptographyDataPlaneService:
        """
        aiobotocore Session for PaymentCryptographyDataPlane service.
        """
        return PaymentCryptographyDataPlaneService("payment-cryptography-data", self)

    @property
    def pca_connector_ad(self) -> PcaConnectorAdService:
        """
        aiobotocore Session for PcaConnectorAd service.
        """
        return PcaConnectorAdService("pca-connector-ad", self)

    @property
    def pca_connector_scep(self) -> PrivateCAConnectorforSCEPService:
        """
        aiobotocore Session for PrivateCAConnectorforSCEP service.
        """
        return PrivateCAConnectorforSCEPService("pca-connector-scep", self)

    @property
    def pcs(self) -> ParallelComputingServiceService:
        """
        aiobotocore Session for ParallelComputingService service.
        """
        return ParallelComputingServiceService("pcs", self)

    @property
    def personalize(self) -> PersonalizeService:
        """
        aiobotocore Session for Personalize service.
        """
        return PersonalizeService("personalize", self)

    @property
    def personalize_events(self) -> PersonalizeEventsService:
        """
        aiobotocore Session for PersonalizeEvents service.
        """
        return PersonalizeEventsService("personalize-events", self)

    @property
    def personalize_runtime(self) -> PersonalizeRuntimeService:
        """
        aiobotocore Session for PersonalizeRuntime service.
        """
        return PersonalizeRuntimeService("personalize-runtime", self)

    @property
    def pi(self) -> PIService:
        """
        aiobotocore Session for PI service.
        """
        return PIService("pi", self)

    @property
    def pinpoint(self) -> PinpointService:
        """
        aiobotocore Session for Pinpoint service.
        """
        return PinpointService("pinpoint", self)

    @property
    def pinpoint_email(self) -> PinpointEmailService:
        """
        aiobotocore Session for PinpointEmail service.
        """
        return PinpointEmailService("pinpoint-email", self)

    @property
    def pinpoint_sms_voice(self) -> PinpointSMSVoiceService:
        """
        aiobotocore Session for PinpointSMSVoice service.
        """
        return PinpointSMSVoiceService("pinpoint-sms-voice", self)

    @property
    def pinpoint_sms_voice_v2(self) -> PinpointSMSVoiceV2Service:
        """
        aiobotocore Session for PinpointSMSVoiceV2 service.
        """
        return PinpointSMSVoiceV2Service("pinpoint-sms-voice-v2", self)

    @property
    def pipes(self) -> EventBridgePipesService:
        """
        aiobotocore Session for EventBridgePipes service.
        """
        return EventBridgePipesService("pipes", self)

    @property
    def polly(self) -> PollyService:
        """
        aiobotocore Session for Polly service.
        """
        return PollyService("polly", self)

    @property
    def pricing(self) -> PricingService:
        """
        aiobotocore Session for Pricing service.
        """
        return PricingService("pricing", self)

    @property
    def privatenetworks(self) -> Private5GService:
        """
        aiobotocore Session for Private5G service.
        """
        return Private5GService("privatenetworks", self)

    @property
    def proton(self) -> ProtonService:
        """
        aiobotocore Session for Proton service.
        """
        return ProtonService("proton", self)

    @property
    def qapps(self) -> QAppsService:
        """
        aiobotocore Session for QApps service.
        """
        return QAppsService("qapps", self)

    @property
    def qbusiness(self) -> QBusinessService:
        """
        aiobotocore Session for QBusiness service.
        """
        return QBusinessService("qbusiness", self)

    @property
    def qconnect(self) -> QConnectService:
        """
        aiobotocore Session for QConnect service.
        """
        return QConnectService("qconnect", self)

    @property
    def qldb(self) -> QLDBService:
        """
        aiobotocore Session for QLDB service.
        """
        return QLDBService("qldb", self)

    @property
    def qldb_session(self) -> QLDBSessionService:
        """
        aiobotocore Session for QLDBSession service.
        """
        return QLDBSessionService("qldb-session", self)

    @property
    def quicksight(self) -> QuickSightService:
        """
        aiobotocore Session for QuickSight service.
        """
        return QuickSightService("quicksight", self)

    @property
    def ram(self) -> RAMService:
        """
        aiobotocore Session for RAM service.
        """
        return RAMService("ram", self)

    @property
    def rbin(self) -> RecycleBinService:
        """
        aiobotocore Session for RecycleBin service.
        """
        return RecycleBinService("rbin", self)

    @property
    def rds(self) -> RDSService:
        """
        aiobotocore Session for RDS service.
        """
        return RDSService("rds", self)

    @property
    def rds_data(self) -> RDSDataServiceService:
        """
        aiobotocore Session for RDSDataService service.
        """
        return RDSDataServiceService("rds-data", self)

    @property
    def redshift(self) -> RedshiftService:
        """
        aiobotocore Session for Redshift service.
        """
        return RedshiftService("redshift", self)

    @property
    def redshift_data(self) -> RedshiftDataAPIServiceService:
        """
        aiobotocore Session for RedshiftDataAPIService service.
        """
        return RedshiftDataAPIServiceService("redshift-data", self)

    @property
    def redshift_serverless(self) -> RedshiftServerlessService:
        """
        aiobotocore Session for RedshiftServerless service.
        """
        return RedshiftServerlessService("redshift-serverless", self)

    @property
    def rekognition(self) -> RekognitionService:
        """
        aiobotocore Session for Rekognition service.
        """
        return RekognitionService("rekognition", self)

    @property
    def repostspace(self) -> RePostPrivateService:
        """
        aiobotocore Session for RePostPrivate service.
        """
        return RePostPrivateService("repostspace", self)

    @property
    def resiliencehub(self) -> ResilienceHubService:
        """
        aiobotocore Session for ResilienceHub service.
        """
        return ResilienceHubService("resiliencehub", self)

    @property
    def resource_explorer_2(self) -> ResourceExplorerService:
        """
        aiobotocore Session for ResourceExplorer service.
        """
        return ResourceExplorerService("resource-explorer-2", self)

    @property
    def resource_groups(self) -> ResourceGroupsService:
        """
        aiobotocore Session for ResourceGroups service.
        """
        return ResourceGroupsService("resource-groups", self)

    @property
    def resourcegroupstaggingapi(self) -> ResourceGroupsTaggingAPIService:
        """
        aiobotocore Session for ResourceGroupsTaggingAPI service.
        """
        return ResourceGroupsTaggingAPIService("resourcegroupstaggingapi", self)

    @property
    def robomaker(self) -> RoboMakerService:
        """
        aiobotocore Session for RoboMaker service.
        """
        return RoboMakerService("robomaker", self)

    @property
    def rolesanywhere(self) -> IAMRolesAnywhereService:
        """
        aiobotocore Session for IAMRolesAnywhere service.
        """
        return IAMRolesAnywhereService("rolesanywhere", self)

    @property
    def route53(self) -> Route53Service:
        """
        aiobotocore Session for Route53 service.
        """
        return Route53Service("route53", self)

    @property
    def route53_recovery_cluster(self) -> Route53RecoveryClusterService:
        """
        aiobotocore Session for Route53RecoveryCluster service.
        """
        return Route53RecoveryClusterService("route53-recovery-cluster", self)

    @property
    def route53_recovery_control_config(self) -> Route53RecoveryControlConfigService:
        """
        aiobotocore Session for Route53RecoveryControlConfig service.
        """
        return Route53RecoveryControlConfigService("route53-recovery-control-config", self)

    @property
    def route53_recovery_readiness(self) -> Route53RecoveryReadinessService:
        """
        aiobotocore Session for Route53RecoveryReadiness service.
        """
        return Route53RecoveryReadinessService("route53-recovery-readiness", self)

    @property
    def route53domains(self) -> Route53DomainsService:
        """
        aiobotocore Session for Route53Domains service.
        """
        return Route53DomainsService("route53domains", self)

    @property
    def route53profiles(self) -> Route53ProfilesService:
        """
        aiobotocore Session for Route53Profiles service.
        """
        return Route53ProfilesService("route53profiles", self)

    @property
    def route53resolver(self) -> Route53ResolverService:
        """
        aiobotocore Session for Route53Resolver service.
        """
        return Route53ResolverService("route53resolver", self)

    @property
    def rum(self) -> CloudWatchRUMService:
        """
        aiobotocore Session for CloudWatchRUM service.
        """
        return CloudWatchRUMService("rum", self)

    @property
    def s3(self) -> S3Service:
        """
        aiobotocore Session for S3 service.
        """
        return S3Service("s3", self)

    @property
    def s3control(self) -> S3ControlService:
        """
        aiobotocore Session for S3Control service.
        """
        return S3ControlService("s3control", self)

    @property
    def s3outposts(self) -> S3OutpostsService:
        """
        aiobotocore Session for S3Outposts service.
        """
        return S3OutpostsService("s3outposts", self)

    @property
    def s3tables(self) -> S3TablesService:
        """
        aiobotocore Session for S3Tables service.
        """
        return S3TablesService("s3tables", self)

    @property
    def sagemaker(self) -> SageMakerService:
        """
        aiobotocore Session for SageMaker service.
        """
        return SageMakerService("sagemaker", self)

    @property
    def sagemaker_a2i_runtime(self) -> AugmentedAIRuntimeService:
        """
        aiobotocore Session for AugmentedAIRuntime service.
        """
        return AugmentedAIRuntimeService("sagemaker-a2i-runtime", self)

    @property
    def sagemaker_edge(self) -> SagemakerEdgeManagerService:
        """
        aiobotocore Session for SagemakerEdgeManager service.
        """
        return SagemakerEdgeManagerService("sagemaker-edge", self)

    @property
    def sagemaker_featurestore_runtime(self) -> SageMakerFeatureStoreRuntimeService:
        """
        aiobotocore Session for SageMakerFeatureStoreRuntime service.
        """
        return SageMakerFeatureStoreRuntimeService("sagemaker-featurestore-runtime", self)

    @property
    def sagemaker_geospatial(self) -> SageMakergeospatialcapabilitiesService:
        """
        aiobotocore Session for SageMakergeospatialcapabilities service.
        """
        return SageMakergeospatialcapabilitiesService("sagemaker-geospatial", self)

    @property
    def sagemaker_metrics(self) -> SageMakerMetricsService:
        """
        aiobotocore Session for SageMakerMetrics service.
        """
        return SageMakerMetricsService("sagemaker-metrics", self)

    @property
    def sagemaker_runtime(self) -> SageMakerRuntimeService:
        """
        aiobotocore Session for SageMakerRuntime service.
        """
        return SageMakerRuntimeService("sagemaker-runtime", self)

    @property
    def savingsplans(self) -> SavingsPlansService:
        """
        aiobotocore Session for SavingsPlans service.
        """
        return SavingsPlansService("savingsplans", self)

    @property
    def scheduler(self) -> EventBridgeSchedulerService:
        """
        aiobotocore Session for EventBridgeScheduler service.
        """
        return EventBridgeSchedulerService("scheduler", self)

    @property
    def schemas(self) -> SchemasService:
        """
        aiobotocore Session for Schemas service.
        """
        return SchemasService("schemas", self)

    @property
    def sdb(self) -> SimpleDBService:
        """
        aiobotocore Session for SimpleDB service.
        """
        return SimpleDBService("sdb", self)

    @property
    def secretsmanager(self) -> SecretsManagerService:
        """
        aiobotocore Session for SecretsManager service.
        """
        return SecretsManagerService("secretsmanager", self)

    @property
    def security_ir(self) -> SecurityIncidentResponseService:
        """
        aiobotocore Session for SecurityIncidentResponse service.
        """
        return SecurityIncidentResponseService("security-ir", self)

    @property
    def securityhub(self) -> SecurityHubService:
        """
        aiobotocore Session for SecurityHub service.
        """
        return SecurityHubService("securityhub", self)

    @property
    def securitylake(self) -> SecurityLakeService:
        """
        aiobotocore Session for SecurityLake service.
        """
        return SecurityLakeService("securitylake", self)

    @property
    def serverlessrepo(self) -> ServerlessApplicationRepositoryService:
        """
        aiobotocore Session for ServerlessApplicationRepository service.
        """
        return ServerlessApplicationRepositoryService("serverlessrepo", self)

    @property
    def service_quotas(self) -> ServiceQuotasService:
        """
        aiobotocore Session for ServiceQuotas service.
        """
        return ServiceQuotasService("service-quotas", self)

    @property
    def servicecatalog(self) -> ServiceCatalogService:
        """
        aiobotocore Session for ServiceCatalog service.
        """
        return ServiceCatalogService("servicecatalog", self)

    @property
    def servicecatalog_appregistry(self) -> AppRegistryService:
        """
        aiobotocore Session for AppRegistry service.
        """
        return AppRegistryService("servicecatalog-appregistry", self)

    @property
    def servicediscovery(self) -> ServiceDiscoveryService:
        """
        aiobotocore Session for ServiceDiscovery service.
        """
        return ServiceDiscoveryService("servicediscovery", self)

    @property
    def ses(self) -> SESService:
        """
        aiobotocore Session for SES service.
        """
        return SESService("ses", self)

    @property
    def sesv2(self) -> SESV2Service:
        """
        aiobotocore Session for SESV2 service.
        """
        return SESV2Service("sesv2", self)

    @property
    def shield(self) -> ShieldService:
        """
        aiobotocore Session for Shield service.
        """
        return ShieldService("shield", self)

    @property
    def signer(self) -> SignerService:
        """
        aiobotocore Session for Signer service.
        """
        return SignerService("signer", self)

    @property
    def simspaceweaver(self) -> SimSpaceWeaverService:
        """
        aiobotocore Session for SimSpaceWeaver service.
        """
        return SimSpaceWeaverService("simspaceweaver", self)

    @property
    def sms(self) -> SMSService:
        """
        aiobotocore Session for SMS service.
        """
        return SMSService("sms", self)

    @property
    def sms_voice(self) -> SMSVoiceService:
        """
        aiobotocore Session for SMSVoice service.
        """
        return SMSVoiceService("sms-voice", self)

    @property
    def snow_device_management(self) -> SnowDeviceManagementService:
        """
        aiobotocore Session for SnowDeviceManagement service.
        """
        return SnowDeviceManagementService("snow-device-management", self)

    @property
    def snowball(self) -> SnowballService:
        """
        aiobotocore Session for Snowball service.
        """
        return SnowballService("snowball", self)

    @property
    def sns(self) -> SNSService:
        """
        aiobotocore Session for SNS service.
        """
        return SNSService("sns", self)

    @property
    def socialmessaging(self) -> EndUserMessagingSocialService:
        """
        aiobotocore Session for EndUserMessagingSocial service.
        """
        return EndUserMessagingSocialService("socialmessaging", self)

    @property
    def sqs(self) -> SQSService:
        """
        aiobotocore Session for SQS service.
        """
        return SQSService("sqs", self)

    @property
    def ssm(self) -> SSMService:
        """
        aiobotocore Session for SSM service.
        """
        return SSMService("ssm", self)

    @property
    def ssm_contacts(self) -> SSMContactsService:
        """
        aiobotocore Session for SSMContacts service.
        """
        return SSMContactsService("ssm-contacts", self)

    @property
    def ssm_incidents(self) -> SSMIncidentsService:
        """
        aiobotocore Session for SSMIncidents service.
        """
        return SSMIncidentsService("ssm-incidents", self)

    @property
    def ssm_quicksetup(self) -> SystemsManagerQuickSetupService:
        """
        aiobotocore Session for SystemsManagerQuickSetup service.
        """
        return SystemsManagerQuickSetupService("ssm-quicksetup", self)

    @property
    def ssm_sap(self) -> SsmSapService:
        """
        aiobotocore Session for SsmSap service.
        """
        return SsmSapService("ssm-sap", self)

    @property
    def sso(self) -> SSOService:
        """
        aiobotocore Session for SSO service.
        """
        return SSOService("sso", self)

    @property
    def sso_admin(self) -> SSOAdminService:
        """
        aiobotocore Session for SSOAdmin service.
        """
        return SSOAdminService("sso-admin", self)

    @property
    def sso_oidc(self) -> SSOOIDCService:
        """
        aiobotocore Session for SSOOIDC service.
        """
        return SSOOIDCService("sso-oidc", self)

    @property
    def stepfunctions(self) -> SFNService:
        """
        aiobotocore Session for SFN service.
        """
        return SFNService("stepfunctions", self)

    @property
    def storagegateway(self) -> StorageGatewayService:
        """
        aiobotocore Session for StorageGateway service.
        """
        return StorageGatewayService("storagegateway", self)

    @property
    def sts(self) -> STSService:
        """
        aiobotocore Session for STS service.
        """
        return STSService("sts", self)

    @property
    def supplychain(self) -> SupplyChainService:
        """
        aiobotocore Session for SupplyChain service.
        """
        return SupplyChainService("supplychain", self)

    @property
    def support(self) -> SupportService:
        """
        aiobotocore Session for Support service.
        """
        return SupportService("support", self)

    @property
    def support_app(self) -> SupportAppService:
        """
        aiobotocore Session for SupportApp service.
        """
        return SupportAppService("support-app", self)

    @property
    def swf(self) -> SWFService:
        """
        aiobotocore Session for SWF service.
        """
        return SWFService("swf", self)

    @property
    def synthetics(self) -> SyntheticsService:
        """
        aiobotocore Session for Synthetics service.
        """
        return SyntheticsService("synthetics", self)

    @property
    def taxsettings(self) -> TaxSettingsService:
        """
        aiobotocore Session for TaxSettings service.
        """
        return TaxSettingsService("taxsettings", self)

    @property
    def textract(self) -> TextractService:
        """
        aiobotocore Session for Textract service.
        """
        return TextractService("textract", self)

    @property
    def timestream_influxdb(self) -> TimestreamInfluxDBService:
        """
        aiobotocore Session for TimestreamInfluxDB service.
        """
        return TimestreamInfluxDBService("timestream-influxdb", self)

    @property
    def timestream_query(self) -> TimestreamQueryService:
        """
        aiobotocore Session for TimestreamQuery service.
        """
        return TimestreamQueryService("timestream-query", self)

    @property
    def timestream_write(self) -> TimestreamWriteService:
        """
        aiobotocore Session for TimestreamWrite service.
        """
        return TimestreamWriteService("timestream-write", self)

    @property
    def tnb(self) -> TelcoNetworkBuilderService:
        """
        aiobotocore Session for TelcoNetworkBuilder service.
        """
        return TelcoNetworkBuilderService("tnb", self)

    @property
    def transcribe(self) -> TranscribeServiceService:
        """
        aiobotocore Session for TranscribeService service.
        """
        return TranscribeServiceService("transcribe", self)

    @property
    def transfer(self) -> TransferService:
        """
        aiobotocore Session for Transfer service.
        """
        return TransferService("transfer", self)

    @property
    def translate(self) -> TranslateService:
        """
        aiobotocore Session for Translate service.
        """
        return TranslateService("translate", self)

    @property
    def trustedadvisor(self) -> TrustedAdvisorPublicAPIService:
        """
        aiobotocore Session for TrustedAdvisorPublicAPI service.
        """
        return TrustedAdvisorPublicAPIService("trustedadvisor", self)

    @property
    def verifiedpermissions(self) -> VerifiedPermissionsService:
        """
        aiobotocore Session for VerifiedPermissions service.
        """
        return VerifiedPermissionsService("verifiedpermissions", self)

    @property
    def voice_id(self) -> VoiceIDService:
        """
        aiobotocore Session for VoiceID service.
        """
        return VoiceIDService("voice-id", self)

    @property
    def vpc_lattice(self) -> VPCLatticeService:
        """
        aiobotocore Session for VPCLattice service.
        """
        return VPCLatticeService("vpc-lattice", self)

    @property
    def waf(self) -> WAFService:
        """
        aiobotocore Session for WAF service.
        """
        return WAFService("waf", self)

    @property
    def waf_regional(self) -> WAFRegionalService:
        """
        aiobotocore Session for WAFRegional service.
        """
        return WAFRegionalService("waf-regional", self)

    @property
    def wafv2(self) -> WAFV2Service:
        """
        aiobotocore Session for WAFV2 service.
        """
        return WAFV2Service("wafv2", self)

    @property
    def wellarchitected(self) -> WellArchitectedService:
        """
        aiobotocore Session for WellArchitected service.
        """
        return WellArchitectedService("wellarchitected", self)

    @property
    def wisdom(self) -> ConnectWisdomServiceService:
        """
        aiobotocore Session for ConnectWisdomService service.
        """
        return ConnectWisdomServiceService("wisdom", self)

    @property
    def workdocs(self) -> WorkDocsService:
        """
        aiobotocore Session for WorkDocs service.
        """
        return WorkDocsService("workdocs", self)

    @property
    def workmail(self) -> WorkMailService:
        """
        aiobotocore Session for WorkMail service.
        """
        return WorkMailService("workmail", self)

    @property
    def workmailmessageflow(self) -> WorkMailMessageFlowService:
        """
        aiobotocore Session for WorkMailMessageFlow service.
        """
        return WorkMailMessageFlowService("workmailmessageflow", self)

    @property
    def workspaces(self) -> WorkSpacesService:
        """
        aiobotocore Session for WorkSpaces service.
        """
        return WorkSpacesService("workspaces", self)

    @property
    def workspaces_thin_client(self) -> WorkSpacesThinClientService:
        """
        aiobotocore Session for WorkSpacesThinClient service.
        """
        return WorkSpacesThinClientService("workspaces-thin-client", self)

    @property
    def workspaces_web(self) -> WorkSpacesWebService:
        """
        aiobotocore Session for WorkSpacesWeb service.
        """
        return WorkSpacesWebService("workspaces-web", self)

    @property
    def xray(self) -> XRayService:
        """
        aiobotocore Session for XRay service.
        """
        return XRayService("xray", self)


def get_session(env_vars: Mapping[str, str] | None = None) -> Session:
    return Session(session_vars=env_vars)
