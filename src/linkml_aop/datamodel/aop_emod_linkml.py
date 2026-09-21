# Auto generated from aop_emod_linkml.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-09-21T18:31:35
# Schema: aopwiki-emod
#
# id: http://example.org/aopwiki-emod
# description: A LinkML schema for the AOP-Wiki data model, extended with the EMOD (Evidence Model) concepts of Assays, Observations, Evidence, and Biological Target Families. It serves two purposes: validating content already curated in the AOP-Wiki, and providing a structure for Adverse Outcome Pathways derived by automated approaches, including analysis of multimodal data and text mining. Both purposes depend on being able to tell what evidence supports from what has been inferred, so the classes and slots are defined to keep an observation, the method that produced it, and the mechanism inferred from it distinct from one another.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Datetime, Float, Integer, String
from linkml_runtime.utils.metamodelcore import XSDDateTime

metamodel_version = "1.7.0"
version = None

# Namespaces
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CurieNamespace('', 'http://example.org/aopwiki-emod/')


# Types

# Class references
class AopId(extended_int):
    pass


class EventId(extended_int):
    pass


class KeRelationshipId(extended_int):
    pass


class AssayId(extended_int):
    pass


class ObservationId(extended_int):
    pass


class EvidenceId(extended_int):
    pass


class StressorId(extended_int):
    pass


class CitationId(extended_int):
    pass


class BiologicalActionId(extended_int):
    pass


class BiologicalObjectId(extended_int):
    pass


class BiologicalProcessId(extended_int):
    pass


class LevelOfBiologicalOrganizationId(extended_int):
    pass


class AopToEventId(extended_int):
    pass


class AopToLifeStageId(extended_int):
    pass


class AopToKeRelationshipId(extended_int):
    pass


class AopToSexId(extended_int):
    pass


class AopToPrototypicalStressorId(extended_int):
    pass


class AopToTaxonId(extended_int):
    pass


class AssignedLicenseId(extended_int):
    pass


class BioTargetFamilyId(extended_int):
    pass


class CellTermId(extended_int):
    pass


class ConfidenceLevelId(extended_int):
    pass


class DirectnessId(extended_int):
    pass


class EventToLifeStageId(extended_int):
    pass


class EventToSexId(extended_int):
    pass


class EventToTaxonId(extended_int):
    pass


class ExperimentSetupId(extended_int):
    pass


class ExperimentTypeId(extended_int):
    pass


class HandbookId(extended_int):
    pass


class HarmonizedAopId(extended_int):
    pass


class HarmonizedEventId(extended_int):
    pass


class LicenseId(extended_int):
    pass


class LifeStageTermId(extended_int):
    pass


class OecdStatusId(extended_int):
    pass


class OrganTermId(extended_int):
    pass


class KeRelationshipToLifeStageId(extended_int):
    pass


class KeRelationshipToSexId(extended_int):
    pass


class KeRelationshipToTaxonId(extended_int):
    pass


class SexTermId(extended_int):
    pass


class EventComponentId(extended_int):
    pass


class TaxonTermId(extended_int):
    pass


class TestGuidelineId(extended_int):
    pass


class UserId(extended_int):
    pass


@dataclass(repr=False)
class Aop(YAMLRoot):
    """
    An AOP describes a sequence of events commencing with initial interaction(s) of a stressor with a biomolecule
    within an organism that causes a perturbation in its biology (i.e., molecular initiating event, MIE), which can
    progress through a dependent series of intermediate key events (KEs) and culminate in an adverse outcome (AO)
    considered relevant to risk assessment or regulatory decision-making. AOPs are composed of a causal sequence of
    upstream to downstream KEs, representing a cascading series of measurable biological changes that can be expected
    to occur if the perturbation is sufficiently severe (i.e., in terms of potency, duration, frequency) to drive the
    pathway all the way to the AO. Importantly, AOPs do not describe every detail of the biology but instead focus on
    describing critical steps or check-points along the path to adversity, which are both measurable and have
    potential predictive value for regulatory application.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/Aop")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Aop"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/Aop")

    id: Union[int, AopId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    title: Optional[str] = None
    short_name: Optional[str] = None
    corresponding_author_id: Optional[Union[dict, "User"]] = None
    abstract: Optional[str] = None
    authors: Optional[str] = None
    applicability_of_the_aop: Optional[str] = None
    key_event_essentiality: Optional[str] = None
    weight_of_evidence_summary: Optional[str] = None
    quantitative_considerations: Optional[str] = None
    optional_considerations: Optional[str] = None
    overall_assessment: Optional[str] = None
    background: Optional[str] = None
    oecd_project: Optional[str] = None
    oecd_status_id: Optional[Union[dict, "OecdStatus"]] = None
    graphical_representation_image_uid: Optional[str] = None
    legacy: Optional[int] = None
    overall_assessment_file_uid: Optional[str] = None
    changed_at: Optional[str] = None
    development_strategy: Optional[str] = None
    known_modulating_factors: Optional[str] = None
    assigned_license_id: Optional[Union[dict, "AssignedLicense"]] = None
    handbook_id: Optional[Union[dict, "Handbook"]] = None
    completion_score: Optional[str] = None
    mean_ker_score: Optional[str] = None
    mean_event_score: Optional[str] = None
    has_references: Optional[str] = None
    project_129: Optional[str] = None
    has_structured_methods: Optional[str] = None
    assays: Optional[Union[dict[Union[int, AssayId], Union[dict, "Assay"]], list[Union[dict, "Assay"]]]] = empty_dict()
    prototypical_stressors: Optional[Union[dict[Union[int, AopToPrototypicalStressorId], Union[dict, "AopToPrototypicalStressor"]], list[Union[dict, "AopToPrototypicalStressor"]]]] = empty_dict()
    events: Optional[Union[dict[Union[int, AopToEventId], Union[dict, "AopToEvent"]], list[Union[dict, "AopToEvent"]]]] = empty_dict()
    ke_relationships: Optional[Union[dict[Union[int, AopToKeRelationshipId], Union[dict, "AopToKeRelationship"]], list[Union[dict, "AopToKeRelationship"]]]] = empty_dict()
    life_stages: Optional[Union[dict[Union[int, AopToLifeStageId], Union[dict, "AopToLifeStage"]], list[Union[dict, "AopToLifeStage"]]]] = empty_dict()
    sexes: Optional[Union[dict[Union[int, AopToSexId], Union[dict, "AopToSex"]], list[Union[dict, "AopToSex"]]]] = empty_dict()
    taxons: Optional[Union[dict[Union[int, AopToTaxonId], Union[dict, "AopToTaxon"]], list[Union[dict, "AopToTaxon"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AopId):
            self.id = AopId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.short_name is not None and not isinstance(self.short_name, str):
            self.short_name = str(self.short_name)

        if self.corresponding_author_id is not None and not isinstance(self.corresponding_author_id, User):
            self.corresponding_author_id = User(**as_dict(self.corresponding_author_id))

        if self.abstract is not None and not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if self.authors is not None and not isinstance(self.authors, str):
            self.authors = str(self.authors)

        if self.applicability_of_the_aop is not None and not isinstance(self.applicability_of_the_aop, str):
            self.applicability_of_the_aop = str(self.applicability_of_the_aop)

        if self.key_event_essentiality is not None and not isinstance(self.key_event_essentiality, str):
            self.key_event_essentiality = str(self.key_event_essentiality)

        if self.weight_of_evidence_summary is not None and not isinstance(self.weight_of_evidence_summary, str):
            self.weight_of_evidence_summary = str(self.weight_of_evidence_summary)

        if self.quantitative_considerations is not None and not isinstance(self.quantitative_considerations, str):
            self.quantitative_considerations = str(self.quantitative_considerations)

        if self.optional_considerations is not None and not isinstance(self.optional_considerations, str):
            self.optional_considerations = str(self.optional_considerations)

        if self.overall_assessment is not None and not isinstance(self.overall_assessment, str):
            self.overall_assessment = str(self.overall_assessment)

        if self.background is not None and not isinstance(self.background, str):
            self.background = str(self.background)

        if self.oecd_project is not None and not isinstance(self.oecd_project, str):
            self.oecd_project = str(self.oecd_project)

        if self.oecd_status_id is not None and not isinstance(self.oecd_status_id, OecdStatus):
            self.oecd_status_id = OecdStatus(**as_dict(self.oecd_status_id))

        if self.graphical_representation_image_uid is not None and not isinstance(self.graphical_representation_image_uid, str):
            self.graphical_representation_image_uid = str(self.graphical_representation_image_uid)

        if self.legacy is not None and not isinstance(self.legacy, int):
            self.legacy = int(self.legacy)

        if self.overall_assessment_file_uid is not None and not isinstance(self.overall_assessment_file_uid, str):
            self.overall_assessment_file_uid = str(self.overall_assessment_file_uid)

        if self.changed_at is not None and not isinstance(self.changed_at, str):
            self.changed_at = str(self.changed_at)

        if self.development_strategy is not None and not isinstance(self.development_strategy, str):
            self.development_strategy = str(self.development_strategy)

        if self.known_modulating_factors is not None and not isinstance(self.known_modulating_factors, str):
            self.known_modulating_factors = str(self.known_modulating_factors)

        if self.assigned_license_id is not None and not isinstance(self.assigned_license_id, AssignedLicense):
            self.assigned_license_id = AssignedLicense(**as_dict(self.assigned_license_id))

        if self.handbook_id is not None and not isinstance(self.handbook_id, Handbook):
            self.handbook_id = Handbook(**as_dict(self.handbook_id))

        if self.completion_score is not None and not isinstance(self.completion_score, str):
            self.completion_score = str(self.completion_score)

        if self.mean_ker_score is not None and not isinstance(self.mean_ker_score, str):
            self.mean_ker_score = str(self.mean_ker_score)

        if self.mean_event_score is not None and not isinstance(self.mean_event_score, str):
            self.mean_event_score = str(self.mean_event_score)

        if self.has_references is not None and not isinstance(self.has_references, str):
            self.has_references = str(self.has_references)

        if self.project_129 is not None and not isinstance(self.project_129, str):
            self.project_129 = str(self.project_129)

        if self.has_structured_methods is not None and not isinstance(self.has_structured_methods, str):
            self.has_structured_methods = str(self.has_structured_methods)

        self._normalize_inlined_as_list(slot_name="assays", slot_type=Assay, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="prototypical_stressors", slot_type=AopToPrototypicalStressor, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="events", slot_type=AopToEvent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ke_relationships", slot_type=AopToKeRelationship, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="life_stages", slot_type=AopToLifeStage, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sexes", slot_type=AopToSex, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="taxons", slot_type=AopToTaxon, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Event(YAMLRoot):
    """
    An Event is a measurable biological change at a defined level of biological organization, described in the
    abstract so that it can be measured and supported by evidence. An Event may be described in the AOP-Wiki before it
    is used anywhere, and becomes a Key Event when it is incorporated into an Adverse Outcome Pathway. The AOP-Wiki
    defines a Key Event as "a change in biological or physiological state that is both measurable and essential to the
    progression of a defined biological perturbation leading to a specific adverse outcome." Within a pathway, the Key
    Events at the starting and ending positions are Molecular Initiating Events and Adverse Outcomes, and those
    between them are intermediate Key Events. These positions are recorded per pathway and rest on the mechanistic
    evidence available to the authors of that pathway, so one Event may serve as a Molecular Initiating Event in one
    Adverse Outcome Pathway and as an intermediate Key Event in another.

    Whether an Event's change can be measured experimentally depends on factors such as the level of biological
    organization and the species. Molecular and cellular changes can be tested and measured in model organisms in a
    laboratory context. Changes up to the population level can be observed in model organisms in a lab and in
    ecological indicator species. Changes at the individual or population level in humans are observed through
    epidemiological and clinical studies rather than tested.

    An Event is a type of change rather than a particular occurrence of one, and is therefore not an exposure event in
    an open system: the exposure of a population to a pollutant in air or water is not an Event. Such real-world
    exposures can rarely be observed at the molecular level, so the Molecular Initiating Event that follows one is not
    usually observable at the time of the exposure event. Describing Events in the abstract keeps supporting evidence
    separate from what is inferred.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/Event")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/Event")

    id: Union[int, EventId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    title: Optional[str] = None
    short_name: Optional[str] = None
    biological_organization_id: Optional[Union[dict, "LevelOfBiologicalOrganization"]] = None
    how_it_works: Optional[str] = None
    measured_or_detected: Optional[str] = None
    supporting_tax_evidence: Optional[str] = None
    evidence_for_chemical_initiation: Optional[str] = None
    examples_using_ao: Optional[str] = None
    references: Optional[str] = None
    definition: Optional[str] = None
    organ_term_id: Optional[Union[dict, "OrganTerm"]] = None
    cell_term_id: Optional[Union[dict, "CellTerm"]] = None
    completion_score: Optional[str] = None
    integration_score: Optional[str] = None
    has_method_text: Optional[str] = None
    aop_open_for_adoption_count: Optional[str] = None
    aop_oecd_program_count: Optional[str] = None
    aop_oecd_endorsed_count: Optional[str] = None
    event_components: Optional[Union[dict[Union[int, EventComponentId], Union[dict, "EventComponent"]], list[Union[dict, "EventComponent"]]]] = empty_dict()
    assays: Optional[Union[dict[Union[int, AssayId], Union[dict, "Assay"]], list[Union[dict, "Assay"]]]] = empty_dict()
    observations: Optional[Union[dict[Union[int, ObservationId], Union[dict, "Observation"]], list[Union[dict, "Observation"]]]] = empty_dict()
    bio_target_families: Optional[Union[dict[Union[int, BioTargetFamilyId], Union[dict, "BioTargetFamily"]], list[Union[dict, "BioTargetFamily"]]]] = empty_dict()
    test_guidelines: Optional[Union[dict[Union[int, TestGuidelineId], Union[dict, "TestGuideline"]], list[Union[dict, "TestGuideline"]]]] = empty_dict()
    aops: Optional[Union[dict[Union[int, AopToEventId], Union[dict, "AopToEvent"]], list[Union[dict, "AopToEvent"]]]] = empty_dict()
    life_stages: Optional[Union[dict[Union[int, EventToLifeStageId], Union[dict, "EventToLifeStage"]], list[Union[dict, "EventToLifeStage"]]]] = empty_dict()
    sexes: Optional[Union[dict[Union[int, EventToSexId], Union[dict, "EventToSex"]], list[Union[dict, "EventToSex"]]]] = empty_dict()
    taxons: Optional[Union[dict[Union[int, EventToTaxonId], Union[dict, "EventToTaxon"]], list[Union[dict, "EventToTaxon"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventId):
            self.id = EventId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.short_name is not None and not isinstance(self.short_name, str):
            self.short_name = str(self.short_name)

        if self.biological_organization_id is not None and not isinstance(self.biological_organization_id, LevelOfBiologicalOrganization):
            self.biological_organization_id = LevelOfBiologicalOrganization(**as_dict(self.biological_organization_id))

        if self.how_it_works is not None and not isinstance(self.how_it_works, str):
            self.how_it_works = str(self.how_it_works)

        if self.measured_or_detected is not None and not isinstance(self.measured_or_detected, str):
            self.measured_or_detected = str(self.measured_or_detected)

        if self.supporting_tax_evidence is not None and not isinstance(self.supporting_tax_evidence, str):
            self.supporting_tax_evidence = str(self.supporting_tax_evidence)

        if self.evidence_for_chemical_initiation is not None and not isinstance(self.evidence_for_chemical_initiation, str):
            self.evidence_for_chemical_initiation = str(self.evidence_for_chemical_initiation)

        if self.examples_using_ao is not None and not isinstance(self.examples_using_ao, str):
            self.examples_using_ao = str(self.examples_using_ao)

        if self.references is not None and not isinstance(self.references, str):
            self.references = str(self.references)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.organ_term_id is not None and not isinstance(self.organ_term_id, OrganTerm):
            self.organ_term_id = OrganTerm(**as_dict(self.organ_term_id))

        if self.cell_term_id is not None and not isinstance(self.cell_term_id, CellTerm):
            self.cell_term_id = CellTerm(**as_dict(self.cell_term_id))

        if self.completion_score is not None and not isinstance(self.completion_score, str):
            self.completion_score = str(self.completion_score)

        if self.integration_score is not None and not isinstance(self.integration_score, str):
            self.integration_score = str(self.integration_score)

        if self.has_method_text is not None and not isinstance(self.has_method_text, str):
            self.has_method_text = str(self.has_method_text)

        if self.aop_open_for_adoption_count is not None and not isinstance(self.aop_open_for_adoption_count, str):
            self.aop_open_for_adoption_count = str(self.aop_open_for_adoption_count)

        if self.aop_oecd_program_count is not None and not isinstance(self.aop_oecd_program_count, str):
            self.aop_oecd_program_count = str(self.aop_oecd_program_count)

        if self.aop_oecd_endorsed_count is not None and not isinstance(self.aop_oecd_endorsed_count, str):
            self.aop_oecd_endorsed_count = str(self.aop_oecd_endorsed_count)

        self._normalize_inlined_as_list(slot_name="event_components", slot_type=EventComponent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="assays", slot_type=Assay, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="observations", slot_type=Observation, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="bio_target_families", slot_type=BioTargetFamily, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="test_guidelines", slot_type=TestGuideline, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aops", slot_type=AopToEvent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="life_stages", slot_type=EventToLifeStage, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sexes", slot_type=EventToSex, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="taxons", slot_type=EventToTaxon, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KeRelationship(YAMLRoot):
    """
    A scientifically-based relationship that connects one key event to another, defines a causal and predictive
    relationship between the upstream and downstream event, and thereby facilitates inference or extrapolation of the
    state of the downstream key event from the known, measured, or predicted state of the upstream key event.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/KeRelationship")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "KeRelationship"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/KeRelationship")

    id: Union[int, KeRelationshipId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    upstream_event_id: Optional[Union[dict, Event]] = None
    downstream_event_id: Optional[Union[dict, Event]] = None
    how_it_works: Optional[str] = None
    biological_plausibility: Optional[str] = None
    empirical_support: Optional[str] = None
    uncertainties: Optional[str] = None
    quantitative_understanding: Optional[str] = None
    taxon_evidence: Optional[str] = None
    weight_of_evidence: Optional[str] = None
    response_relationship: Optional[str] = None
    time_scale: Optional[str] = None
    modulating_factors: Optional[str] = None
    known_loops: Optional[str] = None
    evidence_collection_strategy: Optional[str] = None
    references: Optional[str] = None
    completion_score: Optional[str] = None
    has_tabulated_evidence: Optional[str] = None
    aops: Optional[Union[dict[Union[int, AopToKeRelationshipId], Union[dict, "AopToKeRelationship"]], list[Union[dict, "AopToKeRelationship"]]]] = empty_dict()
    taxons: Optional[Union[dict[Union[int, KeRelationshipToTaxonId], Union[dict, "KeRelationshipToTaxon"]], list[Union[dict, "KeRelationshipToTaxon"]]]] = empty_dict()
    sexes: Optional[Union[dict[Union[int, KeRelationshipToSexId], Union[dict, "KeRelationshipToSex"]], list[Union[dict, "KeRelationshipToSex"]]]] = empty_dict()
    life_stages: Optional[Union[dict[Union[int, KeRelationshipToLifeStageId], Union[dict, "KeRelationshipToLifeStage"]], list[Union[dict, "KeRelationshipToLifeStage"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KeRelationshipId):
            self.id = KeRelationshipId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.upstream_event_id is not None and not isinstance(self.upstream_event_id, Event):
            self.upstream_event_id = Event(**as_dict(self.upstream_event_id))

        if self.downstream_event_id is not None and not isinstance(self.downstream_event_id, Event):
            self.downstream_event_id = Event(**as_dict(self.downstream_event_id))

        if self.how_it_works is not None and not isinstance(self.how_it_works, str):
            self.how_it_works = str(self.how_it_works)

        if self.biological_plausibility is not None and not isinstance(self.biological_plausibility, str):
            self.biological_plausibility = str(self.biological_plausibility)

        if self.empirical_support is not None and not isinstance(self.empirical_support, str):
            self.empirical_support = str(self.empirical_support)

        if self.uncertainties is not None and not isinstance(self.uncertainties, str):
            self.uncertainties = str(self.uncertainties)

        if self.quantitative_understanding is not None and not isinstance(self.quantitative_understanding, str):
            self.quantitative_understanding = str(self.quantitative_understanding)

        if self.taxon_evidence is not None and not isinstance(self.taxon_evidence, str):
            self.taxon_evidence = str(self.taxon_evidence)

        if self.weight_of_evidence is not None and not isinstance(self.weight_of_evidence, str):
            self.weight_of_evidence = str(self.weight_of_evidence)

        if self.response_relationship is not None and not isinstance(self.response_relationship, str):
            self.response_relationship = str(self.response_relationship)

        if self.time_scale is not None and not isinstance(self.time_scale, str):
            self.time_scale = str(self.time_scale)

        if self.modulating_factors is not None and not isinstance(self.modulating_factors, str):
            self.modulating_factors = str(self.modulating_factors)

        if self.known_loops is not None and not isinstance(self.known_loops, str):
            self.known_loops = str(self.known_loops)

        if self.evidence_collection_strategy is not None and not isinstance(self.evidence_collection_strategy, str):
            self.evidence_collection_strategy = str(self.evidence_collection_strategy)

        if self.references is not None and not isinstance(self.references, str):
            self.references = str(self.references)

        if self.completion_score is not None and not isinstance(self.completion_score, str):
            self.completion_score = str(self.completion_score)

        if self.has_tabulated_evidence is not None and not isinstance(self.has_tabulated_evidence, str):
            self.has_tabulated_evidence = str(self.has_tabulated_evidence)

        self._normalize_inlined_as_list(slot_name="aops", slot_type=AopToKeRelationship, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="taxons", slot_type=KeRelationshipToTaxon, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sexes", slot_type=KeRelationshipToSex, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="life_stages", slot_type=KeRelationshipToLifeStage, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Assay(YAMLRoot):
    """
    A defined experimental method for measuring a biological change, structured so that its elements - the biological
    object measured, the process it takes part in, the detection technology, and the taxa and biological target
    families it applies to - can be matched against the Key Events the assay can inform. Assays are how New Approach
    Methodologies (NAMs) connect to Adverse Outcome Pathways, and an assay may be specified by one or more test
    guidelines. Some assays have an inherent directionality, meaning they are designed to detect change in a specific
    direction, such as an agonist or an antagonist effect on a specific molecular target.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/Assay")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Assay"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/Assay")

    id: Union[int, AssayId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    title: Optional[str] = None
    description: Optional[str] = None
    detection_technology: Optional[str] = None
    biological_action_id: Optional[Union[dict, "BiologicalAction"]] = None
    external_assay_id: Optional[str] = None
    classification: Optional[str] = None
    objects: Optional[Union[dict[Union[int, BiologicalObjectId], Union[dict, "BiologicalObject"]], list[Union[dict, "BiologicalObject"]]]] = empty_dict()
    processes: Optional[Union[dict[Union[int, BiologicalProcessId], Union[dict, "BiologicalProcess"]], list[Union[dict, "BiologicalProcess"]]]] = empty_dict()
    taxon_terms: Optional[Union[dict[Union[int, TaxonTermId], Union[dict, "TaxonTerm"]], list[Union[dict, "TaxonTerm"]]]] = empty_dict()
    events: Optional[Union[dict[Union[int, EventId], Union[dict, Event]], list[Union[dict, Event]]]] = empty_dict()
    bio_target_families: Optional[Union[dict[Union[int, BioTargetFamilyId], Union[dict, "BioTargetFamily"]], list[Union[dict, "BioTargetFamily"]]]] = empty_dict()
    aops: Optional[Union[dict[Union[int, AopId], Union[dict, Aop]], list[Union[dict, Aop]]]] = empty_dict()
    citations: Optional[Union[dict[Union[int, CitationId], Union[dict, "Citation"]], list[Union[dict, "Citation"]]]] = empty_dict()
    test_guidelines: Optional[Union[dict[Union[int, TestGuidelineId], Union[dict, "TestGuideline"]], list[Union[dict, "TestGuideline"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssayId):
            self.id = AssayId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.detection_technology is not None and not isinstance(self.detection_technology, str):
            self.detection_technology = str(self.detection_technology)

        if self.biological_action_id is not None and not isinstance(self.biological_action_id, BiologicalAction):
            self.biological_action_id = BiologicalAction(**as_dict(self.biological_action_id))

        if self.external_assay_id is not None and not isinstance(self.external_assay_id, str):
            self.external_assay_id = str(self.external_assay_id)

        if self.classification is not None and not isinstance(self.classification, str):
            self.classification = str(self.classification)

        self._normalize_inlined_as_list(slot_name="objects", slot_type=BiologicalObject, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="processes", slot_type=BiologicalProcess, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="taxon_terms", slot_type=TaxonTerm, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="events", slot_type=Event, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="bio_target_families", slot_type=BioTargetFamily, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="aops", slot_type=Aop, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="citations", slot_type=Citation, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="test_guidelines", slot_type=TestGuideline, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Observation(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/Observation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Observation"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/Observation")

    id: Union[int, ObservationId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    biological_action_id: Optional[Union[dict, "BiologicalAction"]] = None
    biological_process_id: Optional[Union[dict, "BiologicalProcess"]] = None
    biological_object_id: Optional[Union[dict, "BiologicalObject"]] = None
    assay_id: Optional[Union[dict, Assay]] = None
    stressor_id: Optional[Union[dict, "Stressor"]] = None
    phenotype: Optional[str] = None
    experiment_setup_id: Optional[Union[dict, "ExperimentSetup"]] = None
    biological_object_str: Optional[str] = None
    events: Optional[Union[dict[Union[int, EventId], Union[dict, Event]], list[Union[dict, Event]]]] = empty_dict()
    citations: Optional[Union[dict[Union[int, CitationId], Union[dict, "Citation"]], list[Union[dict, "Citation"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObservationId):
            self.id = ObservationId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.biological_action_id is not None and not isinstance(self.biological_action_id, BiologicalAction):
            self.biological_action_id = BiologicalAction(**as_dict(self.biological_action_id))

        if self.biological_process_id is not None and not isinstance(self.biological_process_id, BiologicalProcess):
            self.biological_process_id = BiologicalProcess(**as_dict(self.biological_process_id))

        if self.biological_object_id is not None and not isinstance(self.biological_object_id, BiologicalObject):
            self.biological_object_id = BiologicalObject(**as_dict(self.biological_object_id))

        if self.assay_id is not None and not isinstance(self.assay_id, Assay):
            self.assay_id = Assay(**as_dict(self.assay_id))

        if self.stressor_id is not None and not isinstance(self.stressor_id, Stressor):
            self.stressor_id = Stressor(**as_dict(self.stressor_id))

        if self.phenotype is not None and not isinstance(self.phenotype, str):
            self.phenotype = str(self.phenotype)

        if self.experiment_setup_id is not None and not isinstance(self.experiment_setup_id, ExperimentSetup):
            self.experiment_setup_id = ExperimentSetup(**as_dict(self.experiment_setup_id))

        if self.biological_object_str is not None and not isinstance(self.biological_object_str, str):
            self.biological_object_str = str(self.biological_object_str)

        self._normalize_inlined_as_list(slot_name="events", slot_type=Event, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="citations", slot_type=Citation, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Evidence(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/Evidence")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Evidence"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/Evidence")

    id: Union[int, EvidenceId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    upstream_observation_id: Optional[Union[dict, Observation]] = None
    downstream_observation_id: Optional[Union[dict, Observation]] = None
    citation_id: Optional[Union[dict, "Citation"]] = None
    taxon_term_id: Optional[Union[dict, "TaxonTerm"]] = None
    sex_term_id: Optional[Union[dict, "SexTerm"]] = None
    life_stage_term_id: Optional[Union[dict, "LifeStageTerm"]] = None
    relationship_id: Optional[Union[dict, KeRelationship]] = None
    experimental_design: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvidenceId):
            self.id = EvidenceId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.upstream_observation_id is not None and not isinstance(self.upstream_observation_id, Observation):
            self.upstream_observation_id = Observation(**as_dict(self.upstream_observation_id))

        if self.downstream_observation_id is not None and not isinstance(self.downstream_observation_id, Observation):
            self.downstream_observation_id = Observation(**as_dict(self.downstream_observation_id))

        if self.citation_id is not None and not isinstance(self.citation_id, Citation):
            self.citation_id = Citation(**as_dict(self.citation_id))

        if self.taxon_term_id is not None and not isinstance(self.taxon_term_id, TaxonTerm):
            self.taxon_term_id = TaxonTerm(**as_dict(self.taxon_term_id))

        if self.sex_term_id is not None and not isinstance(self.sex_term_id, SexTerm):
            self.sex_term_id = SexTerm(**as_dict(self.sex_term_id))

        if self.life_stage_term_id is not None and not isinstance(self.life_stage_term_id, LifeStageTerm):
            self.life_stage_term_id = LifeStageTerm(**as_dict(self.life_stage_term_id))

        if self.relationship_id is not None and not isinstance(self.relationship_id, KeRelationship):
            self.relationship_id = KeRelationship(**as_dict(self.relationship_id))

        if self.experimental_design is not None and not isinstance(self.experimental_design, str):
            self.experimental_design = str(self.experimental_design)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Stressor(YAMLRoot):
    """
    An external or internal factor that induces a perturbation to a biological system, potentially initiating a
    molecular initiating event (MIE) but could also impact a biological process represented by a key event. Stressors
    may include chemical, physical, or biological agents capable of eliciting measurable changes in the biological
    system relevant to the AOP.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/Stressor")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Stressor"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/Stressor")

    id: Union[int, StressorId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    name: Optional[str] = None
    aops: Optional[Union[dict[Union[int, AopToPrototypicalStressorId], Union[dict, "AopToPrototypicalStressor"]], list[Union[dict, "AopToPrototypicalStressor"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StressorId):
            self.id = StressorId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        self._normalize_inlined_as_list(slot_name="aops", slot_type=AopToPrototypicalStressor, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Citation(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/Citation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Citation"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/Citation")

    id: Union[int, CitationId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    doi: Optional[str] = None
    title: Optional[str] = None
    authors: Optional[str] = None
    journal: Optional[str] = None
    year: Optional[str] = None
    publisher: Optional[str] = None
    bio_target_families: Optional[Union[dict[Union[int, BioTargetFamilyId], Union[dict, "BioTargetFamily"]], list[Union[dict, "BioTargetFamily"]]]] = empty_dict()
    observations: Optional[Union[dict[Union[int, ObservationId], Union[dict, Observation]], list[Union[dict, Observation]]]] = empty_dict()
    assays: Optional[Union[dict[Union[int, AssayId], Union[dict, Assay]], list[Union[dict, Assay]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CitationId):
            self.id = CitationId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.doi is not None and not isinstance(self.doi, str):
            self.doi = str(self.doi)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.authors is not None and not isinstance(self.authors, str):
            self.authors = str(self.authors)

        if self.journal is not None and not isinstance(self.journal, str):
            self.journal = str(self.journal)

        if self.year is not None and not isinstance(self.year, str):
            self.year = str(self.year)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        self._normalize_inlined_as_list(slot_name="bio_target_families", slot_type=BioTargetFamily, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="observations", slot_type=Observation, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="assays", slot_type=Assay, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalAction(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/BiologicalAction")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "BiologicalAction"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/BiologicalAction")

    id: Union[int, BiologicalActionId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    term: Optional[Union[str, "BiologicalActionEnum"]] = None
    source: Optional[str] = None
    source_id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiologicalActionId):
            self.id = BiologicalActionId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.term is not None and not isinstance(self.term, BiologicalActionEnum):
            self.term = BiologicalActionEnum(self.term)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.source_id is not None and not isinstance(self.source_id, str):
            self.source_id = str(self.source_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalObject(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/BiologicalObject")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "BiologicalObject"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/BiologicalObject")

    id: Union[int, BiologicalObjectId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    term: Optional[str] = None
    source: Optional[Union[str, "BiologicalObjectSourceEnum"]] = None
    source_id: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiologicalObjectId):
            self.id = BiologicalObjectId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.term is not None and not isinstance(self.term, str):
            self.term = str(self.term)

        if self.source is not None and not isinstance(self.source, BiologicalObjectSourceEnum):
            self.source = BiologicalObjectSourceEnum(self.source)

        if self.source_id is not None and not isinstance(self.source_id, str):
            self.source_id = str(self.source_id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalProcess(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/BiologicalProcess")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "BiologicalProcess"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/BiologicalProcess")

    id: Union[int, BiologicalProcessId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    term: Optional[str] = None
    source: Optional[Union[str, "BiologicalProcessSourceEnum"]] = None
    source_id: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiologicalProcessId):
            self.id = BiologicalProcessId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.term is not None and not isinstance(self.term, str):
            self.term = str(self.term)

        if self.source is not None and not isinstance(self.source, BiologicalProcessSourceEnum):
            self.source = BiologicalProcessSourceEnum(self.source)

        if self.source_id is not None and not isinstance(self.source_id, str):
            self.source_id = str(self.source_id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LevelOfBiologicalOrganization(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/LevelOfBiologicalOrganization")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "LevelOfBiologicalOrganization"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/LevelOfBiologicalOrganization")

    id: Union[int, LevelOfBiologicalOrganizationId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    term: Optional[Union[str, "BiologicalOrganizationEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LevelOfBiologicalOrganizationId):
            self.id = LevelOfBiologicalOrganizationId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.term is not None and not isinstance(self.term, BiologicalOrganizationEnum):
            self.term = BiologicalOrganizationEnum(self.term)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AopToEvent(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/AopToEvent")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AopToEvent"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/AopToEvent")

    id: Union[int, AopToEventId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    aop_id: Optional[Union[dict, Aop]] = None
    event_id: Optional[Union[dict, Event]] = None
    type: Optional[str] = None
    essentiality_id: Optional[Union[dict, "ConfidenceLevel"]] = None
    row_order: Optional[int] = None
    sequence: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AopToEventId):
            self.id = AopToEventId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.aop_id is not None and not isinstance(self.aop_id, Aop):
            self.aop_id = Aop(**as_dict(self.aop_id))

        if self.event_id is not None and not isinstance(self.event_id, Event):
            self.event_id = Event(**as_dict(self.event_id))

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.essentiality_id is not None and not isinstance(self.essentiality_id, ConfidenceLevel):
            self.essentiality_id = ConfidenceLevel(**as_dict(self.essentiality_id))

        if self.row_order is not None and not isinstance(self.row_order, int):
            self.row_order = int(self.row_order)

        if self.sequence is not None and not isinstance(self.sequence, int):
            self.sequence = int(self.sequence)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AopToLifeStage(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/AopToLifeStage")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AopToLifeStage"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/AopToLifeStage")

    id: Union[int, AopToLifeStageId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    aop_id: Optional[Union[dict, Aop]] = None
    life_stage_term_id: Optional[Union[dict, "LifeStageTerm"]] = None
    confidence_id: Optional[Union[dict, "ConfidenceLevel"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AopToLifeStageId):
            self.id = AopToLifeStageId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.aop_id is not None and not isinstance(self.aop_id, Aop):
            self.aop_id = Aop(**as_dict(self.aop_id))

        if self.life_stage_term_id is not None and not isinstance(self.life_stage_term_id, LifeStageTerm):
            self.life_stage_term_id = LifeStageTerm(**as_dict(self.life_stage_term_id))

        if self.confidence_id is not None and not isinstance(self.confidence_id, ConfidenceLevel):
            self.confidence_id = ConfidenceLevel(**as_dict(self.confidence_id))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AopToKeRelationship(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/AopToKeRelationship")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AopToKeRelationship"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/AopToKeRelationship")

    id: Union[int, AopToKeRelationshipId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    aop_id: Optional[Union[dict, Aop]] = None
    relationship_id: Optional[Union[dict, KeRelationship]] = None
    confidence_id: Optional[Union[dict, "ConfidenceLevel"]] = None
    quantitative_understanding_id: Optional[Union[dict, "ConfidenceLevel"]] = None
    row_order: Optional[int] = None
    directness_id: Optional[Union[dict, "Directness"]] = None
    type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AopToKeRelationshipId):
            self.id = AopToKeRelationshipId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.aop_id is not None and not isinstance(self.aop_id, Aop):
            self.aop_id = Aop(**as_dict(self.aop_id))

        if self.relationship_id is not None and not isinstance(self.relationship_id, KeRelationship):
            self.relationship_id = KeRelationship(**as_dict(self.relationship_id))

        if self.confidence_id is not None and not isinstance(self.confidence_id, ConfidenceLevel):
            self.confidence_id = ConfidenceLevel(**as_dict(self.confidence_id))

        if self.quantitative_understanding_id is not None and not isinstance(self.quantitative_understanding_id, ConfidenceLevel):
            self.quantitative_understanding_id = ConfidenceLevel(**as_dict(self.quantitative_understanding_id))

        if self.row_order is not None and not isinstance(self.row_order, int):
            self.row_order = int(self.row_order)

        if self.directness_id is not None and not isinstance(self.directness_id, Directness):
            self.directness_id = Directness(**as_dict(self.directness_id))

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AopToSex(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/AopToSex")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AopToSex"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/AopToSex")

    id: Union[int, AopToSexId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    aop_id: Optional[Union[dict, Aop]] = None
    sex_term_id: Optional[Union[dict, "SexTerm"]] = None
    confidence_id: Optional[Union[dict, "ConfidenceLevel"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AopToSexId):
            self.id = AopToSexId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.aop_id is not None and not isinstance(self.aop_id, Aop):
            self.aop_id = Aop(**as_dict(self.aop_id))

        if self.sex_term_id is not None and not isinstance(self.sex_term_id, SexTerm):
            self.sex_term_id = SexTerm(**as_dict(self.sex_term_id))

        if self.confidence_id is not None and not isinstance(self.confidence_id, ConfidenceLevel):
            self.confidence_id = ConfidenceLevel(**as_dict(self.confidence_id))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AopToPrototypicalStressor(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/AopToPrototypicalStressor")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AopToPrototypicalStressor"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/AopToPrototypicalStressor")

    id: Union[int, AopToPrototypicalStressorId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    aop_id: Optional[Union[dict, Aop]] = None
    stressor_id: Optional[Union[dict, Stressor]] = None
    confidence_id: Optional[Union[dict, "ConfidenceLevel"]] = None
    evidence_text: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AopToPrototypicalStressorId):
            self.id = AopToPrototypicalStressorId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.aop_id is not None and not isinstance(self.aop_id, Aop):
            self.aop_id = Aop(**as_dict(self.aop_id))

        if self.stressor_id is not None and not isinstance(self.stressor_id, Stressor):
            self.stressor_id = Stressor(**as_dict(self.stressor_id))

        if self.confidence_id is not None and not isinstance(self.confidence_id, ConfidenceLevel):
            self.confidence_id = ConfidenceLevel(**as_dict(self.confidence_id))

        if self.evidence_text is not None and not isinstance(self.evidence_text, str):
            self.evidence_text = str(self.evidence_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AopToTaxon(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/AopToTaxon")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AopToTaxon"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/AopToTaxon")

    id: Union[int, AopToTaxonId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    aop_id: Optional[Union[dict, Aop]] = None
    taxon_term_id: Optional[Union[dict, "TaxonTerm"]] = None
    confidence_id: Optional[Union[dict, "ConfidenceLevel"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AopToTaxonId):
            self.id = AopToTaxonId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.aop_id is not None and not isinstance(self.aop_id, Aop):
            self.aop_id = Aop(**as_dict(self.aop_id))

        if self.taxon_term_id is not None and not isinstance(self.taxon_term_id, TaxonTerm):
            self.taxon_term_id = TaxonTerm(**as_dict(self.taxon_term_id))

        if self.confidence_id is not None and not isinstance(self.confidence_id, ConfidenceLevel):
            self.confidence_id = ConfidenceLevel(**as_dict(self.confidence_id))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssignedLicense(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/AssignedLicense")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AssignedLicense"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/AssignedLicense")

    id: Union[int, AssignedLicenseId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    license_id: Optional[Union[dict, "License"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssignedLicenseId):
            self.id = AssignedLicenseId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.license_id is not None and not isinstance(self.license_id, License):
            self.license_id = License(**as_dict(self.license_id))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BioTargetFamily(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/BioTargetFamily")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "BioTargetFamily"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/BioTargetFamily")

    id: Union[int, BioTargetFamilyId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    name: Optional[str] = None
    assays: Optional[Union[dict[Union[int, AssayId], Union[dict, Assay]], list[Union[dict, Assay]]]] = empty_dict()
    events: Optional[Union[dict[Union[int, EventId], Union[dict, Event]], list[Union[dict, Event]]]] = empty_dict()
    citations: Optional[Union[dict[Union[int, CitationId], Union[dict, Citation]], list[Union[dict, Citation]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BioTargetFamilyId):
            self.id = BioTargetFamilyId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        self._normalize_inlined_as_list(slot_name="assays", slot_type=Assay, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="events", slot_type=Event, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="citations", slot_type=Citation, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellTerm(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/CellTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CellTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/CellTerm")

    id: Union[int, CellTermId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    source_id: Optional[str] = None
    term: Optional[str] = None
    official_name: Optional[str] = None
    source: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellTermId):
            self.id = CellTermId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.source_id is not None and not isinstance(self.source_id, str):
            self.source_id = str(self.source_id)

        if self.term is not None and not isinstance(self.term, str):
            self.term = str(self.term)

        if self.official_name is not None and not isinstance(self.official_name, str):
            self.official_name = str(self.official_name)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConfidenceLevel(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/ConfidenceLevel")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ConfidenceLevel"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/ConfidenceLevel")

    id: Union[int, ConfidenceLevelId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    term: Optional[Union[str, "ConfidenceLevelEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConfidenceLevelId):
            self.id = ConfidenceLevelId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.term is not None and not isinstance(self.term, ConfidenceLevelEnum):
            self.term = ConfidenceLevelEnum(self.term)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Directness(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/Directness")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Directness"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/Directness")

    id: Union[int, DirectnessId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    term: Optional[Union[str, "DirectnessEnum"]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DirectnessId):
            self.id = DirectnessId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.term is not None and not isinstance(self.term, DirectnessEnum):
            self.term = DirectnessEnum(self.term)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EventToLifeStage(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/EventToLifeStage")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "EventToLifeStage"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/EventToLifeStage")

    id: Union[int, EventToLifeStageId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    event_id: Optional[Union[dict, Event]] = None
    life_stage_term_id: Optional[Union[dict, "LifeStageTerm"]] = None
    confidence_id: Optional[Union[dict, ConfidenceLevel]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventToLifeStageId):
            self.id = EventToLifeStageId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.event_id is not None and not isinstance(self.event_id, Event):
            self.event_id = Event(**as_dict(self.event_id))

        if self.life_stage_term_id is not None and not isinstance(self.life_stage_term_id, LifeStageTerm):
            self.life_stage_term_id = LifeStageTerm(**as_dict(self.life_stage_term_id))

        if self.confidence_id is not None and not isinstance(self.confidence_id, ConfidenceLevel):
            self.confidence_id = ConfidenceLevel(**as_dict(self.confidence_id))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EventToSex(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/EventToSex")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "EventToSex"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/EventToSex")

    id: Union[int, EventToSexId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    event_id: Optional[Union[dict, Event]] = None
    sex_term_id: Optional[Union[dict, "SexTerm"]] = None
    confidence_id: Optional[Union[dict, ConfidenceLevel]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventToSexId):
            self.id = EventToSexId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.event_id is not None and not isinstance(self.event_id, Event):
            self.event_id = Event(**as_dict(self.event_id))

        if self.sex_term_id is not None and not isinstance(self.sex_term_id, SexTerm):
            self.sex_term_id = SexTerm(**as_dict(self.sex_term_id))

        if self.confidence_id is not None and not isinstance(self.confidence_id, ConfidenceLevel):
            self.confidence_id = ConfidenceLevel(**as_dict(self.confidence_id))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EventToTaxon(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/EventToTaxon")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "EventToTaxon"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/EventToTaxon")

    id: Union[int, EventToTaxonId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    event_id: Optional[Union[dict, Event]] = None
    taxon_term_id: Optional[Union[dict, "TaxonTerm"]] = None
    confidence_id: Optional[Union[dict, ConfidenceLevel]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventToTaxonId):
            self.id = EventToTaxonId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.event_id is not None and not isinstance(self.event_id, Event):
            self.event_id = Event(**as_dict(self.event_id))

        if self.taxon_term_id is not None and not isinstance(self.taxon_term_id, TaxonTerm):
            self.taxon_term_id = TaxonTerm(**as_dict(self.taxon_term_id))

        if self.confidence_id is not None and not isinstance(self.confidence_id, ConfidenceLevel):
            self.confidence_id = ConfidenceLevel(**as_dict(self.confidence_id))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExperimentSetup(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/ExperimentSetup")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ExperimentSetup"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/ExperimentSetup")

    id: Union[int, ExperimentSetupId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    assay_id: Optional[Union[dict, Assay]] = None
    causal_agent_id: Optional[Union[dict, Stressor]] = None
    description: Optional[str] = None
    cell_terms: Optional[Union[dict[Union[int, CellTermId], Union[dict, CellTerm]], list[Union[dict, CellTerm]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExperimentSetupId):
            self.id = ExperimentSetupId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.assay_id is not None and not isinstance(self.assay_id, Assay):
            self.assay_id = Assay(**as_dict(self.assay_id))

        if self.causal_agent_id is not None and not isinstance(self.causal_agent_id, Stressor):
            self.causal_agent_id = Stressor(**as_dict(self.causal_agent_id))

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="cell_terms", slot_type=CellTerm, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExperimentType(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/ExperimentType")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ExperimentType"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/ExperimentType")

    id: Union[int, ExperimentTypeId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    exp_type: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExperimentTypeId):
            self.id = ExperimentTypeId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.exp_type is not None and not isinstance(self.exp_type, str):
            self.exp_type = str(self.exp_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Handbook(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/Handbook")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Handbook"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/Handbook")

    id: Union[int, HandbookId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    version: Optional[float] = None
    release_date: Optional[str] = None
    release_notes: Optional[str] = None
    forum_links: Optional[str] = None
    active_version: Optional[str] = None
    released: Optional[str] = None
    pdf_copy_uid: Optional[str] = None
    pdf_only: Optional[str] = None
    release_notes_doc_uid: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HandbookId):
            self.id = HandbookId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.version is not None and not isinstance(self.version, float):
            self.version = float(self.version)

        if self.release_date is not None and not isinstance(self.release_date, str):
            self.release_date = str(self.release_date)

        if self.release_notes is not None and not isinstance(self.release_notes, str):
            self.release_notes = str(self.release_notes)

        if self.forum_links is not None and not isinstance(self.forum_links, str):
            self.forum_links = str(self.forum_links)

        if self.active_version is not None and not isinstance(self.active_version, str):
            self.active_version = str(self.active_version)

        if self.released is not None and not isinstance(self.released, str):
            self.released = str(self.released)

        if self.pdf_copy_uid is not None and not isinstance(self.pdf_copy_uid, str):
            self.pdf_copy_uid = str(self.pdf_copy_uid)

        if self.pdf_only is not None and not isinstance(self.pdf_only, str):
            self.pdf_only = str(self.pdf_only)

        if self.release_notes_doc_uid is not None and not isinstance(self.release_notes_doc_uid, str):
            self.release_notes_doc_uid = str(self.release_notes_doc_uid)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HarmonizedAop(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/HarmonizedAop")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "HarmonizedAop"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/HarmonizedAop")

    id: Union[int, HarmonizedAopId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    tag: Optional[str] = None
    new_aop_id: Optional[Union[dict, Aop]] = None
    source_aop_id: Optional[Union[dict, Aop]] = None
    is_priority: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HarmonizedAopId):
            self.id = HarmonizedAopId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.tag is not None and not isinstance(self.tag, str):
            self.tag = str(self.tag)

        if self.new_aop_id is not None and not isinstance(self.new_aop_id, Aop):
            self.new_aop_id = Aop(**as_dict(self.new_aop_id))

        if self.source_aop_id is not None and not isinstance(self.source_aop_id, Aop):
            self.source_aop_id = Aop(**as_dict(self.source_aop_id))

        if self.is_priority is not None and not isinstance(self.is_priority, str):
            self.is_priority = str(self.is_priority)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HarmonizedEvent(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/HarmonizedEvent")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "HarmonizedEvent"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/HarmonizedEvent")

    id: Union[int, HarmonizedEventId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    source_event_id: Optional[Union[dict, Event]] = None
    source_event_id_text: Optional[str] = None
    source_event_label: Optional[str] = None
    harmonized_label: Optional[str] = None
    harmonized_label_key: Optional[str] = None
    harmonized_event_id: Optional[Union[dict, Event]] = None
    raw_mapping_value: Optional[str] = None
    mapping_status: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HarmonizedEventId):
            self.id = HarmonizedEventId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.source_event_id is not None and not isinstance(self.source_event_id, Event):
            self.source_event_id = Event(**as_dict(self.source_event_id))

        if self.source_event_id_text is not None and not isinstance(self.source_event_id_text, str):
            self.source_event_id_text = str(self.source_event_id_text)

        if self.source_event_label is not None and not isinstance(self.source_event_label, str):
            self.source_event_label = str(self.source_event_label)

        if self.harmonized_label is not None and not isinstance(self.harmonized_label, str):
            self.harmonized_label = str(self.harmonized_label)

        if self.harmonized_label_key is not None and not isinstance(self.harmonized_label_key, str):
            self.harmonized_label_key = str(self.harmonized_label_key)

        if self.harmonized_event_id is not None and not isinstance(self.harmonized_event_id, Event):
            self.harmonized_event_id = Event(**as_dict(self.harmonized_event_id))

        if self.raw_mapping_value is not None and not isinstance(self.raw_mapping_value, str):
            self.raw_mapping_value = str(self.raw_mapping_value)

        if self.mapping_status is not None and not isinstance(self.mapping_status, str):
            self.mapping_status = str(self.mapping_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class License(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/License")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "License"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/License")

    id: Union[int, LicenseId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    label: Optional[str] = None
    logo_uid: Optional[str] = None
    description: Optional[str] = None
    internal_notes: Optional[str] = None
    short_code: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LicenseId):
            self.id = LicenseId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.logo_uid is not None and not isinstance(self.logo_uid, str):
            self.logo_uid = str(self.logo_uid)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.internal_notes is not None and not isinstance(self.internal_notes, str):
            self.internal_notes = str(self.internal_notes)

        if self.short_code is not None and not isinstance(self.short_code, str):
            self.short_code = str(self.short_code)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LifeStageTerm(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/LifeStageTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "LifeStageTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/LifeStageTerm")

    id: Union[int, LifeStageTermId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    term: Optional[Union[str, "LifeStageTermEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LifeStageTermId):
            self.id = LifeStageTermId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.term is not None and not isinstance(self.term, LifeStageTermEnum):
            self.term = LifeStageTermEnum(self.term)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OecdStatus(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/OecdStatus")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "OecdStatus"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/OecdStatus")

    id: Union[int, OecdStatusId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    name: Optional[Union[str, "OecdStatusEnum"]] = None
    description: Optional[str] = None
    sort: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OecdStatusId):
            self.id = OecdStatusId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.name is not None and not isinstance(self.name, OecdStatusEnum):
            self.name = OecdStatusEnum(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.sort is not None and not isinstance(self.sort, int):
            self.sort = int(self.sort)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrganTerm(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/OrganTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "OrganTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/OrganTerm")

    id: Union[int, OrganTermId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    source_id: Optional[str] = None
    term: Optional[str] = None
    official_name: Optional[str] = None
    source: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganTermId):
            self.id = OrganTermId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.source_id is not None and not isinstance(self.source_id, str):
            self.source_id = str(self.source_id)

        if self.term is not None and not isinstance(self.term, str):
            self.term = str(self.term)

        if self.official_name is not None and not isinstance(self.official_name, str):
            self.official_name = str(self.official_name)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KeRelationshipToLifeStage(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/KeRelationshipToLifeStage")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "KeRelationshipToLifeStage"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/KeRelationshipToLifeStage")

    id: Union[int, KeRelationshipToLifeStageId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    relationship_id: Optional[Union[dict, KeRelationship]] = None
    life_stage_term_id: Optional[Union[dict, LifeStageTerm]] = None
    confidence_id: Optional[Union[dict, ConfidenceLevel]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KeRelationshipToLifeStageId):
            self.id = KeRelationshipToLifeStageId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.relationship_id is not None and not isinstance(self.relationship_id, KeRelationship):
            self.relationship_id = KeRelationship(**as_dict(self.relationship_id))

        if self.life_stage_term_id is not None and not isinstance(self.life_stage_term_id, LifeStageTerm):
            self.life_stage_term_id = LifeStageTerm(**as_dict(self.life_stage_term_id))

        if self.confidence_id is not None and not isinstance(self.confidence_id, ConfidenceLevel):
            self.confidence_id = ConfidenceLevel(**as_dict(self.confidence_id))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KeRelationshipToSex(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/KeRelationshipToSex")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "KeRelationshipToSex"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/KeRelationshipToSex")

    id: Union[int, KeRelationshipToSexId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    relationship_id: Optional[Union[dict, KeRelationship]] = None
    sex_term_id: Optional[Union[dict, "SexTerm"]] = None
    confidence_id: Optional[Union[dict, ConfidenceLevel]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KeRelationshipToSexId):
            self.id = KeRelationshipToSexId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.relationship_id is not None and not isinstance(self.relationship_id, KeRelationship):
            self.relationship_id = KeRelationship(**as_dict(self.relationship_id))

        if self.sex_term_id is not None and not isinstance(self.sex_term_id, SexTerm):
            self.sex_term_id = SexTerm(**as_dict(self.sex_term_id))

        if self.confidence_id is not None and not isinstance(self.confidence_id, ConfidenceLevel):
            self.confidence_id = ConfidenceLevel(**as_dict(self.confidence_id))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KeRelationshipToTaxon(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/KeRelationshipToTaxon")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "KeRelationshipToTaxon"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/KeRelationshipToTaxon")

    id: Union[int, KeRelationshipToTaxonId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    relationship_id: Optional[Union[dict, KeRelationship]] = None
    taxon_term_id: Optional[Union[dict, "TaxonTerm"]] = None
    confidence_id: Optional[Union[dict, ConfidenceLevel]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KeRelationshipToTaxonId):
            self.id = KeRelationshipToTaxonId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.relationship_id is not None and not isinstance(self.relationship_id, KeRelationship):
            self.relationship_id = KeRelationship(**as_dict(self.relationship_id))

        if self.taxon_term_id is not None and not isinstance(self.taxon_term_id, TaxonTerm):
            self.taxon_term_id = TaxonTerm(**as_dict(self.taxon_term_id))

        if self.confidence_id is not None and not isinstance(self.confidence_id, ConfidenceLevel):
            self.confidence_id = ConfidenceLevel(**as_dict(self.confidence_id))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SexTerm(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/SexTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SexTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/SexTerm")

    id: Union[int, SexTermId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    term: Optional[Union[str, "SexTermEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SexTermId):
            self.id = SexTermId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.term is not None and not isinstance(self.term, SexTermEnum):
            self.term = SexTermEnum(self.term)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EventComponent(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/EventComponent")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "EventComponent"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/EventComponent")

    id: Union[int, EventComponentId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    biological_action_id: Optional[Union[dict, BiologicalAction]] = None
    biological_object_id: Optional[Union[dict, BiologicalObject]] = None
    biological_process_id: Optional[Union[dict, BiologicalProcess]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EventComponentId):
            self.id = EventComponentId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.biological_action_id is not None and not isinstance(self.biological_action_id, BiologicalAction):
            self.biological_action_id = BiologicalAction(**as_dict(self.biological_action_id))

        if self.biological_object_id is not None and not isinstance(self.biological_object_id, BiologicalObject):
            self.biological_object_id = BiologicalObject(**as_dict(self.biological_object_id))

        if self.biological_process_id is not None and not isinstance(self.biological_process_id, BiologicalProcess):
            self.biological_process_id = BiologicalProcess(**as_dict(self.biological_process_id))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaxonTerm(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/TaxonTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "TaxonTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/TaxonTerm")

    id: Union[int, TaxonTermId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    term_class: Optional[Union[str, "TaxonTermClassEnum"]] = None
    term: Optional[str] = None
    source: Optional[str] = None
    ncbi_id: Optional[str] = None
    scientific_term: Optional[str] = None
    source_id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TaxonTermId):
            self.id = TaxonTermId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.term_class is not None and not isinstance(self.term_class, TaxonTermClassEnum):
            self.term_class = TaxonTermClassEnum(self.term_class)

        if self.term is not None and not isinstance(self.term, str):
            self.term = str(self.term)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.ncbi_id is not None and not isinstance(self.ncbi_id, str):
            self.ncbi_id = str(self.ncbi_id)

        if self.scientific_term is not None and not isinstance(self.scientific_term, str):
            self.scientific_term = str(self.scientific_term)

        if self.source_id is not None and not isinstance(self.source_id, str):
            self.source_id = str(self.source_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TestGuideline(YAMLRoot):
    """
    A standardized test method published by a regulatory or intergovernmental body, such as an OECD Test Guideline or
    an EPA OCSPP test guideline, that specifies how to carry out one or more assays so that the resulting data are
    accepted for regulatory hazard assessment of chemicals. In EMOD, a test guideline is linked to the Assays it
    covers and to the Key Events those Assays measure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/TestGuideline")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "TestGuideline"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/TestGuideline")

    id: Union[int, TestGuidelineId] = None
    created_at: Optional[Union[str, XSDDateTime]] = None
    updated_at: Optional[Union[str, XSDDateTime]] = None
    short_title: Optional[str] = None
    full_title: Optional[str] = None
    citation_id: Optional[Union[dict, Citation]] = None
    assays: Optional[Union[dict[Union[int, AssayId], Union[dict, Assay]], list[Union[dict, Assay]]]] = empty_dict()
    events: Optional[Union[dict[Union[int, EventId], Union[dict, Event]], list[Union[dict, Event]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TestGuidelineId):
            self.id = TestGuidelineId(self.id)

        if self.created_at is not None and not isinstance(self.created_at, XSDDateTime):
            self.created_at = XSDDateTime(self.created_at)

        if self.updated_at is not None and not isinstance(self.updated_at, XSDDateTime):
            self.updated_at = XSDDateTime(self.updated_at)

        if self.short_title is not None and not isinstance(self.short_title, str):
            self.short_title = str(self.short_title)

        if self.full_title is not None and not isinstance(self.full_title, str):
            self.full_title = str(self.full_title)

        if self.citation_id is not None and not isinstance(self.citation_id, Citation):
            self.citation_id = Citation(**as_dict(self.citation_id))

        self._normalize_inlined_as_list(slot_name="assays", slot_type=Assay, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="events", slot_type=Event, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class User(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/User")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "User"
    class_model_uri: ClassVar[URIRef] = URIRef("http://example.org/aopwiki-emod/User")

    id: Union[int, UserId] = None
    email: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UserId):
            self.id = UserId(self.id)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        super().__post_init__(**kwargs)


# Enumerations
class BiologicalActionEnum(EnumDefinitionImpl):

    increased = PermissibleValue(text="increased")
    decreased = PermissibleValue(text="decreased")
    abnormal = PermissibleValue(text="abnormal")
    pathological = PermissibleValue(text="pathological")
    occurrence = PermissibleValue(text="occurrence")
    disrupted = PermissibleValue(text="disrupted")
    arrested = PermissibleValue(text="arrested")
    delayed = PermissibleValue(text="delayed")
    premature = PermissibleValue(text="premature")

    _defn = EnumDefinition(
        name="BiologicalActionEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "functional change",
            PermissibleValue(text="functional change"))
        setattr(cls, "morphological change",
            PermissibleValue(text="morphological change"))

class BiologicalOrganizationEnum(EnumDefinitionImpl):

    Molecular = PermissibleValue(text="Molecular")
    Cellular = PermissibleValue(text="Cellular")
    Tissue = PermissibleValue(text="Tissue")
    Organ = PermissibleValue(text="Organ")
    Individual = PermissibleValue(text="Individual")
    Population = PermissibleValue(text="Population")

    _defn = EnumDefinition(
        name="BiologicalOrganizationEnum",
    )

class BiologicalObjectSourceEnum(EnumDefinitionImpl):

    GO = PermissibleValue(
        text="GO",
        description="Gene Ontology")
    CHEBI = PermissibleValue(
        text="CHEBI",
        description="Chemical Entities of Biological Interest")
    CL = PermissibleValue(
        text="CL",
        description="Cell Ontology")
    PR = PermissibleValue(
        text="PR",
        description="Protein Ontology")
    UBERON = PermissibleValue(
        text="UBERON",
        description="Uber-anatomy Ontology")
    FMA = PermissibleValue(
        text="FMA",
        description="Foundational Model of Anatomy")
    MESH = PermissibleValue(
        text="MESH",
        description="Medical Subject Headings")
    PCO = PermissibleValue(
        text="PCO",
        description="Population and Community Ontology")
    MP = PermissibleValue(
        text="MP",
        description="Mammalian Phenotype Ontology")
    TAIR = PermissibleValue(
        text="TAIR",
        description="The Arabidopsis Information Resource")

    _defn = EnumDefinition(
        name="BiologicalObjectSourceEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "N/A",
            PermissibleValue(
                text="N/A",
                description="Not applicable or not mapped to an ontology"))

class BiologicalProcessSourceEnum(EnumDefinitionImpl):

    GO = PermissibleValue(
        text="GO",
        description="Gene Ontology")
    HP = PermissibleValue(
        text="HP",
        description="Human Phenotype Ontology")
    MP = PermissibleValue(
        text="MP",
        description="Mammalian Phenotype Ontology")
    NBO = PermissibleValue(
        text="NBO",
        description="Neurobehavior Ontology")
    VT = PermissibleValue(
        text="VT",
        description="Vertebrate Trait Ontology")
    MESH = PermissibleValue(
        text="MESH",
        description="Medical Subject Headings")
    PCO = PermissibleValue(
        text="PCO",
        description="Population and Community Ontology")
    MI = PermissibleValue(
        text="MI",
        description="Molecular Interactions Ontology")
    IDO = PermissibleValue(
        text="IDO",
        description="Infectious Disease Ontology")
    NCI = PermissibleValue(
        text="NCI",
        description="NCI Thesaurus")
    RBO = PermissibleValue(
        text="RBO",
        description="Radiation Biology Ontology")

    _defn = EnumDefinition(
        name="BiologicalProcessSourceEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "N/A",
            PermissibleValue(
                text="N/A",
                description="Not applicable or not mapped to an ontology"))

class SexTermEnum(EnumDefinitionImpl):

    Male = PermissibleValue(text="Male")
    Female = PermissibleValue(text="Female")
    Mixed = PermissibleValue(text="Mixed")
    Asexual = PermissibleValue(text="Asexual")
    Hermaphrodite = PermissibleValue(text="Hermaphrodite")
    Unspecific = PermissibleValue(text="Unspecific")

    _defn = EnumDefinition(
        name="SexTermEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Third Gender",
            PermissibleValue(text="Third Gender"))

class LifeStageTermEnum(EnumDefinitionImpl):

    Pregnancy = PermissibleValue(text="Pregnancy")
    Foetal = PermissibleValue(text="Foetal")
    Fetal = PermissibleValue(text="Fetal")
    Embryo = PermissibleValue(text="Embryo")
    Juvenile = PermissibleValue(text="Juvenile")
    Prepubertal = PermissibleValue(text="Prepubertal")
    Perinatal = PermissibleValue(text="Perinatal")
    Adults = PermissibleValue(text="Adults")
    Adult = PermissibleValue(text="Adult")
    Human = PermissibleValue(text="Human")
    Development = PermissibleValue(text="Development")
    Larvae = PermissibleValue(text="Larvae")

    _defn = EnumDefinition(
        name="LifeStageTermEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Birth to < 1 month",
            PermissibleValue(text="Birth to < 1 month"))
        setattr(cls, "1 to < 3 months",
            PermissibleValue(text="1 to < 3 months"))
        setattr(cls, "3 to < 6 months",
            PermissibleValue(text="3 to < 6 months"))
        setattr(cls, "6 to < 12 months",
            PermissibleValue(text="6 to < 12 months"))
        setattr(cls, "1 to < 2 years",
            PermissibleValue(text="1 to < 2 years"))
        setattr(cls, "2 to < 3 years",
            PermissibleValue(text="2 to < 3 years"))
        setattr(cls, "3 to < 6 years",
            PermissibleValue(text="3 to < 6 years"))
        setattr(cls, "6 to < 11 years",
            PermissibleValue(text="6 to < 11 years"))
        setattr(cls, "11 to < 16 years",
            PermissibleValue(text="11 to < 16 years"))
        setattr(cls, "16 to < 21 years",
            PermissibleValue(text="16 to < 21 years"))
        setattr(cls, "Nursing Child",
            PermissibleValue(text="Nursing Child"))
        setattr(cls, "Old Age",
            PermissibleValue(text="Old Age"))
        setattr(cls, "Not Otherwise Specified",
            PermissibleValue(text="Not Otherwise Specified"))
        setattr(cls, "Lactating Mother",
            PermissibleValue(text="Lactating Mother"))
        setattr(cls, "Conception to < Fetal",
            PermissibleValue(text="Conception to < Fetal"))
        setattr(cls, "Fetal to Parturition",
            PermissibleValue(text="Fetal to Parturition"))
        setattr(cls, "Adult, reproductively mature",
            PermissibleValue(text="Adult, reproductively mature"))
        setattr(cls, "During development and at adulthood",
            PermissibleValue(text="During development and at adulthood"))
        setattr(cls, "During brain development, adulthood and aging",
            PermissibleValue(text="During brain development, adulthood and aging"))
        setattr(cls, "During brain development",
            PermissibleValue(text="During brain development"))
        setattr(cls, "All life stages",
            PermissibleValue(text="All life stages"))
        setattr(cls, "Larval development",
            PermissibleValue(text="Larval development"))
        setattr(cls, "before or during gonadal sex differentiation",
            PermissibleValue(text="before or during gonadal sex differentiation"))

class TaxonTermClassEnum(EnumDefinitionImpl):

    synonym = PermissibleValue(text="synonym")

    _defn = EnumDefinition(
        name="TaxonTermClassEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "scientific name",
            PermissibleValue(text="scientific name"))
        setattr(cls, "common name",
            PermissibleValue(text="common name"))

class ConfidenceLevelEnum(EnumDefinitionImpl):

    high = PermissibleValue(text="high")
    moderate = PermissibleValue(text="moderate")
    low = PermissibleValue(text="low")

    _defn = EnumDefinition(
        name="ConfidenceLevelEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "not specified",
            PermissibleValue(text="not specified"))

class DirectnessEnum(EnumDefinitionImpl):

    adjacent = PermissibleValue(text="adjacent")

    _defn = EnumDefinition(
        name="DirectnessEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "non-adjacent",
            PermissibleValue(text="non-adjacent"))

class OecdStatusEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="OecdStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Under development",
            PermissibleValue(text="Under development"))
        setattr(cls, "WPHA/WNT Endorsed",
            PermissibleValue(text="WPHA/WNT Endorsed"))
        setattr(cls, "ESCA Approved",
            PermissibleValue(text="ESCA Approved"))
        setattr(cls, "Under Review",
            PermissibleValue(text="Under Review"))

# Slots
class slots:
    pass

slots.changed_at = Slot(uri=DEFAULT_.changed_at, name="changed_at", curie=DEFAULT_.curie('changed_at'),
                   model_uri=DEFAULT_.changed_at, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.created_at = Slot(uri=DEFAULT_.created_at, name="created_at", curie=DEFAULT_.curie('created_at'),
                   model_uri=DEFAULT_.created_at, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.updated_at = Slot(uri=DEFAULT_.updated_at, name="updated_at", curie=DEFAULT_.curie('updated_at'),
                   model_uri=DEFAULT_.updated_at, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.aop__id = Slot(uri=DEFAULT_.id, name="aop__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.aop__id, domain=None, range=URIRef)

slots.aop__title = Slot(uri=DEFAULT_.title, name="aop__title", curie=DEFAULT_.curie('title'),
                   model_uri=DEFAULT_.aop__title, domain=None, range=Optional[str])

slots.aop__short_name = Slot(uri=DEFAULT_.short_name, name="aop__short_name", curie=DEFAULT_.curie('short_name'),
                   model_uri=DEFAULT_.aop__short_name, domain=None, range=Optional[str])

slots.aop__corresponding_author_id = Slot(uri=DEFAULT_.corresponding_author_id, name="aop__corresponding_author_id", curie=DEFAULT_.curie('corresponding_author_id'),
                   model_uri=DEFAULT_.aop__corresponding_author_id, domain=None, range=Optional[Union[dict, User]])

slots.aop__abstract = Slot(uri=DEFAULT_.abstract, name="aop__abstract", curie=DEFAULT_.curie('abstract'),
                   model_uri=DEFAULT_.aop__abstract, domain=None, range=Optional[str])

slots.aop__authors = Slot(uri=DEFAULT_.authors, name="aop__authors", curie=DEFAULT_.curie('authors'),
                   model_uri=DEFAULT_.aop__authors, domain=None, range=Optional[str])

slots.aop__applicability_of_the_aop = Slot(uri=DEFAULT_.applicability_of_the_aop, name="aop__applicability_of_the_aop", curie=DEFAULT_.curie('applicability_of_the_aop'),
                   model_uri=DEFAULT_.aop__applicability_of_the_aop, domain=None, range=Optional[str])

slots.aop__key_event_essentiality = Slot(uri=DEFAULT_.key_event_essentiality, name="aop__key_event_essentiality", curie=DEFAULT_.curie('key_event_essentiality'),
                   model_uri=DEFAULT_.aop__key_event_essentiality, domain=None, range=Optional[str])

slots.aop__weight_of_evidence_summary = Slot(uri=DEFAULT_.weight_of_evidence_summary, name="aop__weight_of_evidence_summary", curie=DEFAULT_.curie('weight_of_evidence_summary'),
                   model_uri=DEFAULT_.aop__weight_of_evidence_summary, domain=None, range=Optional[str])

slots.aop__quantitative_considerations = Slot(uri=DEFAULT_.quantitative_considerations, name="aop__quantitative_considerations", curie=DEFAULT_.curie('quantitative_considerations'),
                   model_uri=DEFAULT_.aop__quantitative_considerations, domain=None, range=Optional[str])

slots.aop__optional_considerations = Slot(uri=DEFAULT_.optional_considerations, name="aop__optional_considerations", curie=DEFAULT_.curie('optional_considerations'),
                   model_uri=DEFAULT_.aop__optional_considerations, domain=None, range=Optional[str])

slots.aop__overall_assessment = Slot(uri=DEFAULT_.overall_assessment, name="aop__overall_assessment", curie=DEFAULT_.curie('overall_assessment'),
                   model_uri=DEFAULT_.aop__overall_assessment, domain=None, range=Optional[str])

slots.aop__background = Slot(uri=DEFAULT_.background, name="aop__background", curie=DEFAULT_.curie('background'),
                   model_uri=DEFAULT_.aop__background, domain=None, range=Optional[str])

slots.aop__oecd_project = Slot(uri=DEFAULT_.oecd_project, name="aop__oecd_project", curie=DEFAULT_.curie('oecd_project'),
                   model_uri=DEFAULT_.aop__oecd_project, domain=None, range=Optional[str])

slots.aop__oecd_status_id = Slot(uri=DEFAULT_.oecd_status_id, name="aop__oecd_status_id", curie=DEFAULT_.curie('oecd_status_id'),
                   model_uri=DEFAULT_.aop__oecd_status_id, domain=None, range=Optional[Union[dict, OecdStatus]])

slots.aop__graphical_representation_image_uid = Slot(uri=DEFAULT_.graphical_representation_image_uid, name="aop__graphical_representation_image_uid", curie=DEFAULT_.curie('graphical_representation_image_uid'),
                   model_uri=DEFAULT_.aop__graphical_representation_image_uid, domain=None, range=Optional[str])

slots.aop__legacy = Slot(uri=DEFAULT_.legacy, name="aop__legacy", curie=DEFAULT_.curie('legacy'),
                   model_uri=DEFAULT_.aop__legacy, domain=None, range=Optional[int])

slots.aop__overall_assessment_file_uid = Slot(uri=DEFAULT_.overall_assessment_file_uid, name="aop__overall_assessment_file_uid", curie=DEFAULT_.curie('overall_assessment_file_uid'),
                   model_uri=DEFAULT_.aop__overall_assessment_file_uid, domain=None, range=Optional[str])

slots.aop__changed_at = Slot(uri=DEFAULT_.changed_at, name="aop__changed_at", curie=DEFAULT_.curie('changed_at'),
                   model_uri=DEFAULT_.aop__changed_at, domain=None, range=Optional[str])

slots.aop__development_strategy = Slot(uri=DEFAULT_.development_strategy, name="aop__development_strategy", curie=DEFAULT_.curie('development_strategy'),
                   model_uri=DEFAULT_.aop__development_strategy, domain=None, range=Optional[str])

slots.aop__known_modulating_factors = Slot(uri=DEFAULT_.known_modulating_factors, name="aop__known_modulating_factors", curie=DEFAULT_.curie('known_modulating_factors'),
                   model_uri=DEFAULT_.aop__known_modulating_factors, domain=None, range=Optional[str])

slots.aop__assigned_license_id = Slot(uri=DEFAULT_.assigned_license_id, name="aop__assigned_license_id", curie=DEFAULT_.curie('assigned_license_id'),
                   model_uri=DEFAULT_.aop__assigned_license_id, domain=None, range=Optional[Union[dict, AssignedLicense]])

slots.aop__handbook_id = Slot(uri=DEFAULT_.handbook_id, name="aop__handbook_id", curie=DEFAULT_.curie('handbook_id'),
                   model_uri=DEFAULT_.aop__handbook_id, domain=None, range=Optional[Union[dict, Handbook]])

slots.aop__completion_score = Slot(uri=DEFAULT_.completion_score, name="aop__completion_score", curie=DEFAULT_.curie('completion_score'),
                   model_uri=DEFAULT_.aop__completion_score, domain=None, range=Optional[str])

slots.aop__mean_ker_score = Slot(uri=DEFAULT_.mean_ker_score, name="aop__mean_ker_score", curie=DEFAULT_.curie('mean_ker_score'),
                   model_uri=DEFAULT_.aop__mean_ker_score, domain=None, range=Optional[str])

slots.aop__mean_event_score = Slot(uri=DEFAULT_.mean_event_score, name="aop__mean_event_score", curie=DEFAULT_.curie('mean_event_score'),
                   model_uri=DEFAULT_.aop__mean_event_score, domain=None, range=Optional[str])

slots.aop__has_references = Slot(uri=DEFAULT_.has_references, name="aop__has_references", curie=DEFAULT_.curie('has_references'),
                   model_uri=DEFAULT_.aop__has_references, domain=None, range=Optional[str])

slots.aop__project_129 = Slot(uri=DEFAULT_.project_129, name="aop__project_129", curie=DEFAULT_.curie('project_129'),
                   model_uri=DEFAULT_.aop__project_129, domain=None, range=Optional[str])

slots.aop__has_structured_methods = Slot(uri=DEFAULT_.has_structured_methods, name="aop__has_structured_methods", curie=DEFAULT_.curie('has_structured_methods'),
                   model_uri=DEFAULT_.aop__has_structured_methods, domain=None, range=Optional[str])

slots.aop__assays = Slot(uri=DEFAULT_.assays, name="aop__assays", curie=DEFAULT_.curie('assays'),
                   model_uri=DEFAULT_.aop__assays, domain=None, range=Optional[Union[dict[Union[int, AssayId], Union[dict, Assay]], list[Union[dict, Assay]]]])

slots.aop__prototypical_stressors = Slot(uri=DEFAULT_.prototypical_stressors, name="aop__prototypical_stressors", curie=DEFAULT_.curie('prototypical_stressors'),
                   model_uri=DEFAULT_.aop__prototypical_stressors, domain=None, range=Optional[Union[dict[Union[int, AopToPrototypicalStressorId], Union[dict, AopToPrototypicalStressor]], list[Union[dict, AopToPrototypicalStressor]]]])

slots.aop__events = Slot(uri=DEFAULT_.events, name="aop__events", curie=DEFAULT_.curie('events'),
                   model_uri=DEFAULT_.aop__events, domain=None, range=Optional[Union[dict[Union[int, AopToEventId], Union[dict, AopToEvent]], list[Union[dict, AopToEvent]]]])

slots.aop__ke_relationships = Slot(uri=DEFAULT_.ke_relationships, name="aop__ke_relationships", curie=DEFAULT_.curie('ke_relationships'),
                   model_uri=DEFAULT_.aop__ke_relationships, domain=None, range=Optional[Union[dict[Union[int, AopToKeRelationshipId], Union[dict, AopToKeRelationship]], list[Union[dict, AopToKeRelationship]]]])

slots.aop__life_stages = Slot(uri=DEFAULT_.life_stages, name="aop__life_stages", curie=DEFAULT_.curie('life_stages'),
                   model_uri=DEFAULT_.aop__life_stages, domain=None, range=Optional[Union[dict[Union[int, AopToLifeStageId], Union[dict, AopToLifeStage]], list[Union[dict, AopToLifeStage]]]])

slots.aop__sexes = Slot(uri=DEFAULT_.sexes, name="aop__sexes", curie=DEFAULT_.curie('sexes'),
                   model_uri=DEFAULT_.aop__sexes, domain=None, range=Optional[Union[dict[Union[int, AopToSexId], Union[dict, AopToSex]], list[Union[dict, AopToSex]]]])

slots.aop__taxons = Slot(uri=DEFAULT_.taxons, name="aop__taxons", curie=DEFAULT_.curie('taxons'),
                   model_uri=DEFAULT_.aop__taxons, domain=None, range=Optional[Union[dict[Union[int, AopToTaxonId], Union[dict, AopToTaxon]], list[Union[dict, AopToTaxon]]]])

slots.event__id = Slot(uri=DEFAULT_.id, name="event__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.event__id, domain=None, range=URIRef)

slots.event__title = Slot(uri=DEFAULT_.title, name="event__title", curie=DEFAULT_.curie('title'),
                   model_uri=DEFAULT_.event__title, domain=None, range=Optional[str])

slots.event__short_name = Slot(uri=DEFAULT_.short_name, name="event__short_name", curie=DEFAULT_.curie('short_name'),
                   model_uri=DEFAULT_.event__short_name, domain=None, range=Optional[str])

slots.event__biological_organization_id = Slot(uri=DEFAULT_.biological_organization_id, name="event__biological_organization_id", curie=DEFAULT_.curie('biological_organization_id'),
                   model_uri=DEFAULT_.event__biological_organization_id, domain=None, range=Optional[Union[dict, LevelOfBiologicalOrganization]])

slots.event__how_it_works = Slot(uri=DEFAULT_.how_it_works, name="event__how_it_works", curie=DEFAULT_.curie('how_it_works'),
                   model_uri=DEFAULT_.event__how_it_works, domain=None, range=Optional[str])

slots.event__measured_or_detected = Slot(uri=DEFAULT_.measured_or_detected, name="event__measured_or_detected", curie=DEFAULT_.curie('measured_or_detected'),
                   model_uri=DEFAULT_.event__measured_or_detected, domain=None, range=Optional[str])

slots.event__supporting_tax_evidence = Slot(uri=DEFAULT_.supporting_tax_evidence, name="event__supporting_tax_evidence", curie=DEFAULT_.curie('supporting_tax_evidence'),
                   model_uri=DEFAULT_.event__supporting_tax_evidence, domain=None, range=Optional[str])

slots.event__evidence_for_chemical_initiation = Slot(uri=DEFAULT_.evidence_for_chemical_initiation, name="event__evidence_for_chemical_initiation", curie=DEFAULT_.curie('evidence_for_chemical_initiation'),
                   model_uri=DEFAULT_.event__evidence_for_chemical_initiation, domain=None, range=Optional[str])

slots.event__examples_using_ao = Slot(uri=DEFAULT_.examples_using_ao, name="event__examples_using_ao", curie=DEFAULT_.curie('examples_using_ao'),
                   model_uri=DEFAULT_.event__examples_using_ao, domain=None, range=Optional[str])

slots.event__references = Slot(uri=DEFAULT_.references, name="event__references", curie=DEFAULT_.curie('references'),
                   model_uri=DEFAULT_.event__references, domain=None, range=Optional[str])

slots.event__definition = Slot(uri=DEFAULT_.definition, name="event__definition", curie=DEFAULT_.curie('definition'),
                   model_uri=DEFAULT_.event__definition, domain=None, range=Optional[str])

slots.event__organ_term_id = Slot(uri=DEFAULT_.organ_term_id, name="event__organ_term_id", curie=DEFAULT_.curie('organ_term_id'),
                   model_uri=DEFAULT_.event__organ_term_id, domain=None, range=Optional[Union[dict, OrganTerm]])

slots.event__cell_term_id = Slot(uri=DEFAULT_.cell_term_id, name="event__cell_term_id", curie=DEFAULT_.curie('cell_term_id'),
                   model_uri=DEFAULT_.event__cell_term_id, domain=None, range=Optional[Union[dict, CellTerm]])

slots.event__completion_score = Slot(uri=DEFAULT_.completion_score, name="event__completion_score", curie=DEFAULT_.curie('completion_score'),
                   model_uri=DEFAULT_.event__completion_score, domain=None, range=Optional[str])

slots.event__integration_score = Slot(uri=DEFAULT_.integration_score, name="event__integration_score", curie=DEFAULT_.curie('integration_score'),
                   model_uri=DEFAULT_.event__integration_score, domain=None, range=Optional[str])

slots.event__has_method_text = Slot(uri=DEFAULT_.has_method_text, name="event__has_method_text", curie=DEFAULT_.curie('has_method_text'),
                   model_uri=DEFAULT_.event__has_method_text, domain=None, range=Optional[str])

slots.event__aop_open_for_adoption_count = Slot(uri=DEFAULT_.aop_open_for_adoption_count, name="event__aop_open_for_adoption_count", curie=DEFAULT_.curie('aop_open_for_adoption_count'),
                   model_uri=DEFAULT_.event__aop_open_for_adoption_count, domain=None, range=Optional[str])

slots.event__aop_oecd_program_count = Slot(uri=DEFAULT_.aop_oecd_program_count, name="event__aop_oecd_program_count", curie=DEFAULT_.curie('aop_oecd_program_count'),
                   model_uri=DEFAULT_.event__aop_oecd_program_count, domain=None, range=Optional[str])

slots.event__aop_oecd_endorsed_count = Slot(uri=DEFAULT_.aop_oecd_endorsed_count, name="event__aop_oecd_endorsed_count", curie=DEFAULT_.curie('aop_oecd_endorsed_count'),
                   model_uri=DEFAULT_.event__aop_oecd_endorsed_count, domain=None, range=Optional[str])

slots.event__event_components = Slot(uri=DEFAULT_.event_components, name="event__event_components", curie=DEFAULT_.curie('event_components'),
                   model_uri=DEFAULT_.event__event_components, domain=None, range=Optional[Union[dict[Union[int, EventComponentId], Union[dict, EventComponent]], list[Union[dict, EventComponent]]]])

slots.event__assays = Slot(uri=DEFAULT_.assays, name="event__assays", curie=DEFAULT_.curie('assays'),
                   model_uri=DEFAULT_.event__assays, domain=None, range=Optional[Union[dict[Union[int, AssayId], Union[dict, Assay]], list[Union[dict, Assay]]]])

slots.event__observations = Slot(uri=DEFAULT_.observations, name="event__observations", curie=DEFAULT_.curie('observations'),
                   model_uri=DEFAULT_.event__observations, domain=None, range=Optional[Union[dict[Union[int, ObservationId], Union[dict, Observation]], list[Union[dict, Observation]]]])

slots.event__bio_target_families = Slot(uri=DEFAULT_.bio_target_families, name="event__bio_target_families", curie=DEFAULT_.curie('bio_target_families'),
                   model_uri=DEFAULT_.event__bio_target_families, domain=None, range=Optional[Union[dict[Union[int, BioTargetFamilyId], Union[dict, BioTargetFamily]], list[Union[dict, BioTargetFamily]]]])

slots.event__test_guidelines = Slot(uri=DEFAULT_.test_guidelines, name="event__test_guidelines", curie=DEFAULT_.curie('test_guidelines'),
                   model_uri=DEFAULT_.event__test_guidelines, domain=None, range=Optional[Union[dict[Union[int, TestGuidelineId], Union[dict, TestGuideline]], list[Union[dict, TestGuideline]]]])

slots.event__aops = Slot(uri=DEFAULT_.aops, name="event__aops", curie=DEFAULT_.curie('aops'),
                   model_uri=DEFAULT_.event__aops, domain=None, range=Optional[Union[dict[Union[int, AopToEventId], Union[dict, AopToEvent]], list[Union[dict, AopToEvent]]]])

slots.event__life_stages = Slot(uri=DEFAULT_.life_stages, name="event__life_stages", curie=DEFAULT_.curie('life_stages'),
                   model_uri=DEFAULT_.event__life_stages, domain=None, range=Optional[Union[dict[Union[int, EventToLifeStageId], Union[dict, EventToLifeStage]], list[Union[dict, EventToLifeStage]]]])

slots.event__sexes = Slot(uri=DEFAULT_.sexes, name="event__sexes", curie=DEFAULT_.curie('sexes'),
                   model_uri=DEFAULT_.event__sexes, domain=None, range=Optional[Union[dict[Union[int, EventToSexId], Union[dict, EventToSex]], list[Union[dict, EventToSex]]]])

slots.event__taxons = Slot(uri=DEFAULT_.taxons, name="event__taxons", curie=DEFAULT_.curie('taxons'),
                   model_uri=DEFAULT_.event__taxons, domain=None, range=Optional[Union[dict[Union[int, EventToTaxonId], Union[dict, EventToTaxon]], list[Union[dict, EventToTaxon]]]])

slots.keRelationship__id = Slot(uri=DEFAULT_.id, name="keRelationship__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.keRelationship__id, domain=None, range=URIRef)

slots.keRelationship__upstream_event_id = Slot(uri=DEFAULT_.upstream_event_id, name="keRelationship__upstream_event_id", curie=DEFAULT_.curie('upstream_event_id'),
                   model_uri=DEFAULT_.keRelationship__upstream_event_id, domain=None, range=Optional[Union[dict, Event]])

slots.keRelationship__downstream_event_id = Slot(uri=DEFAULT_.downstream_event_id, name="keRelationship__downstream_event_id", curie=DEFAULT_.curie('downstream_event_id'),
                   model_uri=DEFAULT_.keRelationship__downstream_event_id, domain=None, range=Optional[Union[dict, Event]])

slots.keRelationship__how_it_works = Slot(uri=DEFAULT_.how_it_works, name="keRelationship__how_it_works", curie=DEFAULT_.curie('how_it_works'),
                   model_uri=DEFAULT_.keRelationship__how_it_works, domain=None, range=Optional[str])

slots.keRelationship__biological_plausibility = Slot(uri=DEFAULT_.biological_plausibility, name="keRelationship__biological_plausibility", curie=DEFAULT_.curie('biological_plausibility'),
                   model_uri=DEFAULT_.keRelationship__biological_plausibility, domain=None, range=Optional[str])

slots.keRelationship__empirical_support = Slot(uri=DEFAULT_.empirical_support, name="keRelationship__empirical_support", curie=DEFAULT_.curie('empirical_support'),
                   model_uri=DEFAULT_.keRelationship__empirical_support, domain=None, range=Optional[str])

slots.keRelationship__uncertainties = Slot(uri=DEFAULT_.uncertainties, name="keRelationship__uncertainties", curie=DEFAULT_.curie('uncertainties'),
                   model_uri=DEFAULT_.keRelationship__uncertainties, domain=None, range=Optional[str])

slots.keRelationship__quantitative_understanding = Slot(uri=DEFAULT_.quantitative_understanding, name="keRelationship__quantitative_understanding", curie=DEFAULT_.curie('quantitative_understanding'),
                   model_uri=DEFAULT_.keRelationship__quantitative_understanding, domain=None, range=Optional[str])

slots.keRelationship__taxon_evidence = Slot(uri=DEFAULT_.taxon_evidence, name="keRelationship__taxon_evidence", curie=DEFAULT_.curie('taxon_evidence'),
                   model_uri=DEFAULT_.keRelationship__taxon_evidence, domain=None, range=Optional[str])

slots.keRelationship__weight_of_evidence = Slot(uri=DEFAULT_.weight_of_evidence, name="keRelationship__weight_of_evidence", curie=DEFAULT_.curie('weight_of_evidence'),
                   model_uri=DEFAULT_.keRelationship__weight_of_evidence, domain=None, range=Optional[str])

slots.keRelationship__response_relationship = Slot(uri=DEFAULT_.response_relationship, name="keRelationship__response_relationship", curie=DEFAULT_.curie('response_relationship'),
                   model_uri=DEFAULT_.keRelationship__response_relationship, domain=None, range=Optional[str])

slots.keRelationship__time_scale = Slot(uri=DEFAULT_.time_scale, name="keRelationship__time_scale", curie=DEFAULT_.curie('time_scale'),
                   model_uri=DEFAULT_.keRelationship__time_scale, domain=None, range=Optional[str])

slots.keRelationship__modulating_factors = Slot(uri=DEFAULT_.modulating_factors, name="keRelationship__modulating_factors", curie=DEFAULT_.curie('modulating_factors'),
                   model_uri=DEFAULT_.keRelationship__modulating_factors, domain=None, range=Optional[str])

slots.keRelationship__known_loops = Slot(uri=DEFAULT_.known_loops, name="keRelationship__known_loops", curie=DEFAULT_.curie('known_loops'),
                   model_uri=DEFAULT_.keRelationship__known_loops, domain=None, range=Optional[str])

slots.keRelationship__evidence_collection_strategy = Slot(uri=DEFAULT_.evidence_collection_strategy, name="keRelationship__evidence_collection_strategy", curie=DEFAULT_.curie('evidence_collection_strategy'),
                   model_uri=DEFAULT_.keRelationship__evidence_collection_strategy, domain=None, range=Optional[str])

slots.keRelationship__references = Slot(uri=DEFAULT_.references, name="keRelationship__references", curie=DEFAULT_.curie('references'),
                   model_uri=DEFAULT_.keRelationship__references, domain=None, range=Optional[str])

slots.keRelationship__completion_score = Slot(uri=DEFAULT_.completion_score, name="keRelationship__completion_score", curie=DEFAULT_.curie('completion_score'),
                   model_uri=DEFAULT_.keRelationship__completion_score, domain=None, range=Optional[str])

slots.keRelationship__has_tabulated_evidence = Slot(uri=DEFAULT_.has_tabulated_evidence, name="keRelationship__has_tabulated_evidence", curie=DEFAULT_.curie('has_tabulated_evidence'),
                   model_uri=DEFAULT_.keRelationship__has_tabulated_evidence, domain=None, range=Optional[str])

slots.keRelationship__aops = Slot(uri=DEFAULT_.aops, name="keRelationship__aops", curie=DEFAULT_.curie('aops'),
                   model_uri=DEFAULT_.keRelationship__aops, domain=None, range=Optional[Union[dict[Union[int, AopToKeRelationshipId], Union[dict, AopToKeRelationship]], list[Union[dict, AopToKeRelationship]]]])

slots.keRelationship__taxons = Slot(uri=DEFAULT_.taxons, name="keRelationship__taxons", curie=DEFAULT_.curie('taxons'),
                   model_uri=DEFAULT_.keRelationship__taxons, domain=None, range=Optional[Union[dict[Union[int, KeRelationshipToTaxonId], Union[dict, KeRelationshipToTaxon]], list[Union[dict, KeRelationshipToTaxon]]]])

slots.keRelationship__sexes = Slot(uri=DEFAULT_.sexes, name="keRelationship__sexes", curie=DEFAULT_.curie('sexes'),
                   model_uri=DEFAULT_.keRelationship__sexes, domain=None, range=Optional[Union[dict[Union[int, KeRelationshipToSexId], Union[dict, KeRelationshipToSex]], list[Union[dict, KeRelationshipToSex]]]])

slots.keRelationship__life_stages = Slot(uri=DEFAULT_.life_stages, name="keRelationship__life_stages", curie=DEFAULT_.curie('life_stages'),
                   model_uri=DEFAULT_.keRelationship__life_stages, domain=None, range=Optional[Union[dict[Union[int, KeRelationshipToLifeStageId], Union[dict, KeRelationshipToLifeStage]], list[Union[dict, KeRelationshipToLifeStage]]]])

slots.assay__id = Slot(uri=DEFAULT_.id, name="assay__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.assay__id, domain=None, range=URIRef)

slots.assay__title = Slot(uri=DEFAULT_.title, name="assay__title", curie=DEFAULT_.curie('title'),
                   model_uri=DEFAULT_.assay__title, domain=None, range=Optional[str])

slots.assay__description = Slot(uri=DEFAULT_.description, name="assay__description", curie=DEFAULT_.curie('description'),
                   model_uri=DEFAULT_.assay__description, domain=None, range=Optional[str])

slots.assay__detection_technology = Slot(uri=DEFAULT_.detection_technology, name="assay__detection_technology", curie=DEFAULT_.curie('detection_technology'),
                   model_uri=DEFAULT_.assay__detection_technology, domain=None, range=Optional[str])

slots.assay__biological_action_id = Slot(uri=DEFAULT_.biological_action_id, name="assay__biological_action_id", curie=DEFAULT_.curie('biological_action_id'),
                   model_uri=DEFAULT_.assay__biological_action_id, domain=None, range=Optional[Union[dict, BiologicalAction]])

slots.assay__external_assay_id = Slot(uri=DEFAULT_.external_assay_id, name="assay__external_assay_id", curie=DEFAULT_.curie('external_assay_id'),
                   model_uri=DEFAULT_.assay__external_assay_id, domain=None, range=Optional[str])

slots.assay__classification = Slot(uri=DEFAULT_.classification, name="assay__classification", curie=DEFAULT_.curie('classification'),
                   model_uri=DEFAULT_.assay__classification, domain=None, range=Optional[str])

slots.assay__objects = Slot(uri=DEFAULT_.objects, name="assay__objects", curie=DEFAULT_.curie('objects'),
                   model_uri=DEFAULT_.assay__objects, domain=None, range=Optional[Union[dict[Union[int, BiologicalObjectId], Union[dict, BiologicalObject]], list[Union[dict, BiologicalObject]]]])

slots.assay__processes = Slot(uri=DEFAULT_.processes, name="assay__processes", curie=DEFAULT_.curie('processes'),
                   model_uri=DEFAULT_.assay__processes, domain=None, range=Optional[Union[dict[Union[int, BiologicalProcessId], Union[dict, BiologicalProcess]], list[Union[dict, BiologicalProcess]]]])

slots.assay__taxon_terms = Slot(uri=DEFAULT_.taxon_terms, name="assay__taxon_terms", curie=DEFAULT_.curie('taxon_terms'),
                   model_uri=DEFAULT_.assay__taxon_terms, domain=None, range=Optional[Union[dict[Union[int, TaxonTermId], Union[dict, TaxonTerm]], list[Union[dict, TaxonTerm]]]])

slots.assay__events = Slot(uri=DEFAULT_.events, name="assay__events", curie=DEFAULT_.curie('events'),
                   model_uri=DEFAULT_.assay__events, domain=None, range=Optional[Union[dict[Union[int, EventId], Union[dict, Event]], list[Union[dict, Event]]]])

slots.assay__bio_target_families = Slot(uri=DEFAULT_.bio_target_families, name="assay__bio_target_families", curie=DEFAULT_.curie('bio_target_families'),
                   model_uri=DEFAULT_.assay__bio_target_families, domain=None, range=Optional[Union[dict[Union[int, BioTargetFamilyId], Union[dict, BioTargetFamily]], list[Union[dict, BioTargetFamily]]]])

slots.assay__aops = Slot(uri=DEFAULT_.aops, name="assay__aops", curie=DEFAULT_.curie('aops'),
                   model_uri=DEFAULT_.assay__aops, domain=None, range=Optional[Union[dict[Union[int, AopId], Union[dict, Aop]], list[Union[dict, Aop]]]])

slots.assay__citations = Slot(uri=DEFAULT_.citations, name="assay__citations", curie=DEFAULT_.curie('citations'),
                   model_uri=DEFAULT_.assay__citations, domain=None, range=Optional[Union[dict[Union[int, CitationId], Union[dict, Citation]], list[Union[dict, Citation]]]])

slots.assay__test_guidelines = Slot(uri=DEFAULT_.test_guidelines, name="assay__test_guidelines", curie=DEFAULT_.curie('test_guidelines'),
                   model_uri=DEFAULT_.assay__test_guidelines, domain=None, range=Optional[Union[dict[Union[int, TestGuidelineId], Union[dict, TestGuideline]], list[Union[dict, TestGuideline]]]])

slots.observation__id = Slot(uri=DEFAULT_.id, name="observation__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.observation__id, domain=None, range=URIRef)

slots.observation__biological_action_id = Slot(uri=DEFAULT_.biological_action_id, name="observation__biological_action_id", curie=DEFAULT_.curie('biological_action_id'),
                   model_uri=DEFAULT_.observation__biological_action_id, domain=None, range=Optional[Union[dict, BiologicalAction]])

slots.observation__biological_process_id = Slot(uri=DEFAULT_.biological_process_id, name="observation__biological_process_id", curie=DEFAULT_.curie('biological_process_id'),
                   model_uri=DEFAULT_.observation__biological_process_id, domain=None, range=Optional[Union[dict, BiologicalProcess]])

slots.observation__biological_object_id = Slot(uri=DEFAULT_.biological_object_id, name="observation__biological_object_id", curie=DEFAULT_.curie('biological_object_id'),
                   model_uri=DEFAULT_.observation__biological_object_id, domain=None, range=Optional[Union[dict, BiologicalObject]])

slots.observation__assay_id = Slot(uri=DEFAULT_.assay_id, name="observation__assay_id", curie=DEFAULT_.curie('assay_id'),
                   model_uri=DEFAULT_.observation__assay_id, domain=None, range=Optional[Union[dict, Assay]])

slots.observation__stressor_id = Slot(uri=DEFAULT_.stressor_id, name="observation__stressor_id", curie=DEFAULT_.curie('stressor_id'),
                   model_uri=DEFAULT_.observation__stressor_id, domain=None, range=Optional[Union[dict, Stressor]])

slots.observation__phenotype = Slot(uri=DEFAULT_.phenotype, name="observation__phenotype", curie=DEFAULT_.curie('phenotype'),
                   model_uri=DEFAULT_.observation__phenotype, domain=None, range=Optional[str])

slots.observation__experiment_setup_id = Slot(uri=DEFAULT_.experiment_setup_id, name="observation__experiment_setup_id", curie=DEFAULT_.curie('experiment_setup_id'),
                   model_uri=DEFAULT_.observation__experiment_setup_id, domain=None, range=Optional[Union[dict, ExperimentSetup]])

slots.observation__biological_object_str = Slot(uri=DEFAULT_.biological_object_str, name="observation__biological_object_str", curie=DEFAULT_.curie('biological_object_str'),
                   model_uri=DEFAULT_.observation__biological_object_str, domain=None, range=Optional[str])

slots.observation__events = Slot(uri=DEFAULT_.events, name="observation__events", curie=DEFAULT_.curie('events'),
                   model_uri=DEFAULT_.observation__events, domain=None, range=Optional[Union[dict[Union[int, EventId], Union[dict, Event]], list[Union[dict, Event]]]])

slots.observation__citations = Slot(uri=DEFAULT_.citations, name="observation__citations", curie=DEFAULT_.curie('citations'),
                   model_uri=DEFAULT_.observation__citations, domain=None, range=Optional[Union[dict[Union[int, CitationId], Union[dict, Citation]], list[Union[dict, Citation]]]])

slots.evidence__id = Slot(uri=DEFAULT_.id, name="evidence__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.evidence__id, domain=None, range=URIRef)

slots.evidence__upstream_observation_id = Slot(uri=DEFAULT_.upstream_observation_id, name="evidence__upstream_observation_id", curie=DEFAULT_.curie('upstream_observation_id'),
                   model_uri=DEFAULT_.evidence__upstream_observation_id, domain=None, range=Optional[Union[dict, Observation]])

slots.evidence__downstream_observation_id = Slot(uri=DEFAULT_.downstream_observation_id, name="evidence__downstream_observation_id", curie=DEFAULT_.curie('downstream_observation_id'),
                   model_uri=DEFAULT_.evidence__downstream_observation_id, domain=None, range=Optional[Union[dict, Observation]])

slots.evidence__citation_id = Slot(uri=DEFAULT_.citation_id, name="evidence__citation_id", curie=DEFAULT_.curie('citation_id'),
                   model_uri=DEFAULT_.evidence__citation_id, domain=None, range=Optional[Union[dict, Citation]])

slots.evidence__taxon_term_id = Slot(uri=DEFAULT_.taxon_term_id, name="evidence__taxon_term_id", curie=DEFAULT_.curie('taxon_term_id'),
                   model_uri=DEFAULT_.evidence__taxon_term_id, domain=None, range=Optional[Union[dict, TaxonTerm]])

slots.evidence__sex_term_id = Slot(uri=DEFAULT_.sex_term_id, name="evidence__sex_term_id", curie=DEFAULT_.curie('sex_term_id'),
                   model_uri=DEFAULT_.evidence__sex_term_id, domain=None, range=Optional[Union[dict, SexTerm]])

slots.evidence__life_stage_term_id = Slot(uri=DEFAULT_.life_stage_term_id, name="evidence__life_stage_term_id", curie=DEFAULT_.curie('life_stage_term_id'),
                   model_uri=DEFAULT_.evidence__life_stage_term_id, domain=None, range=Optional[Union[dict, LifeStageTerm]])

slots.evidence__relationship_id = Slot(uri=DEFAULT_.relationship_id, name="evidence__relationship_id", curie=DEFAULT_.curie('relationship_id'),
                   model_uri=DEFAULT_.evidence__relationship_id, domain=None, range=Optional[Union[dict, KeRelationship]])

slots.evidence__experimental_design = Slot(uri=DEFAULT_.experimental_design, name="evidence__experimental_design", curie=DEFAULT_.curie('experimental_design'),
                   model_uri=DEFAULT_.evidence__experimental_design, domain=None, range=Optional[str])

slots.evidence__notes = Slot(uri=DEFAULT_.notes, name="evidence__notes", curie=DEFAULT_.curie('notes'),
                   model_uri=DEFAULT_.evidence__notes, domain=None, range=Optional[str])

slots.stressor__id = Slot(uri=DEFAULT_.id, name="stressor__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.stressor__id, domain=None, range=URIRef)

slots.stressor__name = Slot(uri=DEFAULT_.name, name="stressor__name", curie=DEFAULT_.curie('name'),
                   model_uri=DEFAULT_.stressor__name, domain=None, range=Optional[str])

slots.stressor__aops = Slot(uri=DEFAULT_.aops, name="stressor__aops", curie=DEFAULT_.curie('aops'),
                   model_uri=DEFAULT_.stressor__aops, domain=None, range=Optional[Union[dict[Union[int, AopToPrototypicalStressorId], Union[dict, AopToPrototypicalStressor]], list[Union[dict, AopToPrototypicalStressor]]]])

slots.citation__id = Slot(uri=DEFAULT_.id, name="citation__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.citation__id, domain=None, range=URIRef)

slots.citation__doi = Slot(uri=DEFAULT_.doi, name="citation__doi", curie=DEFAULT_.curie('doi'),
                   model_uri=DEFAULT_.citation__doi, domain=None, range=Optional[str])

slots.citation__title = Slot(uri=DEFAULT_.title, name="citation__title", curie=DEFAULT_.curie('title'),
                   model_uri=DEFAULT_.citation__title, domain=None, range=Optional[str])

slots.citation__authors = Slot(uri=DEFAULT_.authors, name="citation__authors", curie=DEFAULT_.curie('authors'),
                   model_uri=DEFAULT_.citation__authors, domain=None, range=Optional[str])

slots.citation__journal = Slot(uri=DEFAULT_.journal, name="citation__journal", curie=DEFAULT_.curie('journal'),
                   model_uri=DEFAULT_.citation__journal, domain=None, range=Optional[str])

slots.citation__year = Slot(uri=DEFAULT_.year, name="citation__year", curie=DEFAULT_.curie('year'),
                   model_uri=DEFAULT_.citation__year, domain=None, range=Optional[str])

slots.citation__publisher = Slot(uri=DEFAULT_.publisher, name="citation__publisher", curie=DEFAULT_.curie('publisher'),
                   model_uri=DEFAULT_.citation__publisher, domain=None, range=Optional[str])

slots.citation__bio_target_families = Slot(uri=DEFAULT_.bio_target_families, name="citation__bio_target_families", curie=DEFAULT_.curie('bio_target_families'),
                   model_uri=DEFAULT_.citation__bio_target_families, domain=None, range=Optional[Union[dict[Union[int, BioTargetFamilyId], Union[dict, BioTargetFamily]], list[Union[dict, BioTargetFamily]]]])

slots.citation__observations = Slot(uri=DEFAULT_.observations, name="citation__observations", curie=DEFAULT_.curie('observations'),
                   model_uri=DEFAULT_.citation__observations, domain=None, range=Optional[Union[dict[Union[int, ObservationId], Union[dict, Observation]], list[Union[dict, Observation]]]])

slots.citation__assays = Slot(uri=DEFAULT_.assays, name="citation__assays", curie=DEFAULT_.curie('assays'),
                   model_uri=DEFAULT_.citation__assays, domain=None, range=Optional[Union[dict[Union[int, AssayId], Union[dict, Assay]], list[Union[dict, Assay]]]])

slots.biologicalAction__id = Slot(uri=DEFAULT_.id, name="biologicalAction__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.biologicalAction__id, domain=None, range=URIRef)

slots.biologicalAction__term = Slot(uri=DEFAULT_.term, name="biologicalAction__term", curie=DEFAULT_.curie('term'),
                   model_uri=DEFAULT_.biologicalAction__term, domain=None, range=Optional[Union[str, "BiologicalActionEnum"]])

slots.biologicalAction__source = Slot(uri=DEFAULT_.source, name="biologicalAction__source", curie=DEFAULT_.curie('source'),
                   model_uri=DEFAULT_.biologicalAction__source, domain=None, range=Optional[str])

slots.biologicalAction__source_id = Slot(uri=DEFAULT_.source_id, name="biologicalAction__source_id", curie=DEFAULT_.curie('source_id'),
                   model_uri=DEFAULT_.biologicalAction__source_id, domain=None, range=Optional[str])

slots.biologicalObject__id = Slot(uri=DEFAULT_.id, name="biologicalObject__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.biologicalObject__id, domain=None, range=URIRef)

slots.biologicalObject__term = Slot(uri=DEFAULT_.term, name="biologicalObject__term", curie=DEFAULT_.curie('term'),
                   model_uri=DEFAULT_.biologicalObject__term, domain=None, range=Optional[str])

slots.biologicalObject__source = Slot(uri=DEFAULT_.source, name="biologicalObject__source", curie=DEFAULT_.curie('source'),
                   model_uri=DEFAULT_.biologicalObject__source, domain=None, range=Optional[Union[str, "BiologicalObjectSourceEnum"]])

slots.biologicalObject__source_id = Slot(uri=DEFAULT_.source_id, name="biologicalObject__source_id", curie=DEFAULT_.curie('source_id'),
                   model_uri=DEFAULT_.biologicalObject__source_id, domain=None, range=Optional[str])

slots.biologicalObject__description = Slot(uri=DEFAULT_.description, name="biologicalObject__description", curie=DEFAULT_.curie('description'),
                   model_uri=DEFAULT_.biologicalObject__description, domain=None, range=Optional[str])

slots.biologicalObject__url = Slot(uri=DEFAULT_.url, name="biologicalObject__url", curie=DEFAULT_.curie('url'),
                   model_uri=DEFAULT_.biologicalObject__url, domain=None, range=Optional[str])

slots.biologicalProcess__id = Slot(uri=DEFAULT_.id, name="biologicalProcess__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.biologicalProcess__id, domain=None, range=URIRef)

slots.biologicalProcess__term = Slot(uri=DEFAULT_.term, name="biologicalProcess__term", curie=DEFAULT_.curie('term'),
                   model_uri=DEFAULT_.biologicalProcess__term, domain=None, range=Optional[str])

slots.biologicalProcess__source = Slot(uri=DEFAULT_.source, name="biologicalProcess__source", curie=DEFAULT_.curie('source'),
                   model_uri=DEFAULT_.biologicalProcess__source, domain=None, range=Optional[Union[str, "BiologicalProcessSourceEnum"]])

slots.biologicalProcess__source_id = Slot(uri=DEFAULT_.source_id, name="biologicalProcess__source_id", curie=DEFAULT_.curie('source_id'),
                   model_uri=DEFAULT_.biologicalProcess__source_id, domain=None, range=Optional[str])

slots.biologicalProcess__description = Slot(uri=DEFAULT_.description, name="biologicalProcess__description", curie=DEFAULT_.curie('description'),
                   model_uri=DEFAULT_.biologicalProcess__description, domain=None, range=Optional[str])

slots.biologicalProcess__url = Slot(uri=DEFAULT_.url, name="biologicalProcess__url", curie=DEFAULT_.curie('url'),
                   model_uri=DEFAULT_.biologicalProcess__url, domain=None, range=Optional[str])

slots.levelOfBiologicalOrganization__id = Slot(uri=DEFAULT_.id, name="levelOfBiologicalOrganization__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.levelOfBiologicalOrganization__id, domain=None, range=URIRef)

slots.levelOfBiologicalOrganization__term = Slot(uri=DEFAULT_.term, name="levelOfBiologicalOrganization__term", curie=DEFAULT_.curie('term'),
                   model_uri=DEFAULT_.levelOfBiologicalOrganization__term, domain=None, range=Optional[Union[str, "BiologicalOrganizationEnum"]])

slots.aopToEvent__id = Slot(uri=DEFAULT_.id, name="aopToEvent__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.aopToEvent__id, domain=None, range=URIRef)

slots.aopToEvent__aop_id = Slot(uri=DEFAULT_.aop_id, name="aopToEvent__aop_id", curie=DEFAULT_.curie('aop_id'),
                   model_uri=DEFAULT_.aopToEvent__aop_id, domain=None, range=Optional[Union[dict, Aop]])

slots.aopToEvent__event_id = Slot(uri=DEFAULT_.event_id, name="aopToEvent__event_id", curie=DEFAULT_.curie('event_id'),
                   model_uri=DEFAULT_.aopToEvent__event_id, domain=None, range=Optional[Union[dict, Event]])

slots.aopToEvent__type = Slot(uri=DEFAULT_.type, name="aopToEvent__type", curie=DEFAULT_.curie('type'),
                   model_uri=DEFAULT_.aopToEvent__type, domain=None, range=Optional[str])

slots.aopToEvent__essentiality_id = Slot(uri=DEFAULT_.essentiality_id, name="aopToEvent__essentiality_id", curie=DEFAULT_.curie('essentiality_id'),
                   model_uri=DEFAULT_.aopToEvent__essentiality_id, domain=None, range=Optional[Union[dict, ConfidenceLevel]])

slots.aopToEvent__row_order = Slot(uri=DEFAULT_.row_order, name="aopToEvent__row_order", curie=DEFAULT_.curie('row_order'),
                   model_uri=DEFAULT_.aopToEvent__row_order, domain=None, range=Optional[int])

slots.aopToEvent__sequence = Slot(uri=DEFAULT_.sequence, name="aopToEvent__sequence", curie=DEFAULT_.curie('sequence'),
                   model_uri=DEFAULT_.aopToEvent__sequence, domain=None, range=Optional[int])

slots.aopToLifeStage__id = Slot(uri=DEFAULT_.id, name="aopToLifeStage__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.aopToLifeStage__id, domain=None, range=URIRef)

slots.aopToLifeStage__aop_id = Slot(uri=DEFAULT_.aop_id, name="aopToLifeStage__aop_id", curie=DEFAULT_.curie('aop_id'),
                   model_uri=DEFAULT_.aopToLifeStage__aop_id, domain=None, range=Optional[Union[dict, Aop]])

slots.aopToLifeStage__life_stage_term_id = Slot(uri=DEFAULT_.life_stage_term_id, name="aopToLifeStage__life_stage_term_id", curie=DEFAULT_.curie('life_stage_term_id'),
                   model_uri=DEFAULT_.aopToLifeStage__life_stage_term_id, domain=None, range=Optional[Union[dict, LifeStageTerm]])

slots.aopToLifeStage__confidence_id = Slot(uri=DEFAULT_.confidence_id, name="aopToLifeStage__confidence_id", curie=DEFAULT_.curie('confidence_id'),
                   model_uri=DEFAULT_.aopToLifeStage__confidence_id, domain=None, range=Optional[Union[dict, ConfidenceLevel]])

slots.aopToKeRelationship__id = Slot(uri=DEFAULT_.id, name="aopToKeRelationship__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.aopToKeRelationship__id, domain=None, range=URIRef)

slots.aopToKeRelationship__aop_id = Slot(uri=DEFAULT_.aop_id, name="aopToKeRelationship__aop_id", curie=DEFAULT_.curie('aop_id'),
                   model_uri=DEFAULT_.aopToKeRelationship__aop_id, domain=None, range=Optional[Union[dict, Aop]])

slots.aopToKeRelationship__relationship_id = Slot(uri=DEFAULT_.relationship_id, name="aopToKeRelationship__relationship_id", curie=DEFAULT_.curie('relationship_id'),
                   model_uri=DEFAULT_.aopToKeRelationship__relationship_id, domain=None, range=Optional[Union[dict, KeRelationship]])

slots.aopToKeRelationship__confidence_id = Slot(uri=DEFAULT_.confidence_id, name="aopToKeRelationship__confidence_id", curie=DEFAULT_.curie('confidence_id'),
                   model_uri=DEFAULT_.aopToKeRelationship__confidence_id, domain=None, range=Optional[Union[dict, ConfidenceLevel]])

slots.aopToKeRelationship__quantitative_understanding_id = Slot(uri=DEFAULT_.quantitative_understanding_id, name="aopToKeRelationship__quantitative_understanding_id", curie=DEFAULT_.curie('quantitative_understanding_id'),
                   model_uri=DEFAULT_.aopToKeRelationship__quantitative_understanding_id, domain=None, range=Optional[Union[dict, ConfidenceLevel]])

slots.aopToKeRelationship__row_order = Slot(uri=DEFAULT_.row_order, name="aopToKeRelationship__row_order", curie=DEFAULT_.curie('row_order'),
                   model_uri=DEFAULT_.aopToKeRelationship__row_order, domain=None, range=Optional[int])

slots.aopToKeRelationship__directness_id = Slot(uri=DEFAULT_.directness_id, name="aopToKeRelationship__directness_id", curie=DEFAULT_.curie('directness_id'),
                   model_uri=DEFAULT_.aopToKeRelationship__directness_id, domain=None, range=Optional[Union[dict, Directness]])

slots.aopToKeRelationship__type = Slot(uri=DEFAULT_.type, name="aopToKeRelationship__type", curie=DEFAULT_.curie('type'),
                   model_uri=DEFAULT_.aopToKeRelationship__type, domain=None, range=Optional[str])

slots.aopToSex__id = Slot(uri=DEFAULT_.id, name="aopToSex__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.aopToSex__id, domain=None, range=URIRef)

slots.aopToSex__aop_id = Slot(uri=DEFAULT_.aop_id, name="aopToSex__aop_id", curie=DEFAULT_.curie('aop_id'),
                   model_uri=DEFAULT_.aopToSex__aop_id, domain=None, range=Optional[Union[dict, Aop]])

slots.aopToSex__sex_term_id = Slot(uri=DEFAULT_.sex_term_id, name="aopToSex__sex_term_id", curie=DEFAULT_.curie('sex_term_id'),
                   model_uri=DEFAULT_.aopToSex__sex_term_id, domain=None, range=Optional[Union[dict, SexTerm]])

slots.aopToSex__confidence_id = Slot(uri=DEFAULT_.confidence_id, name="aopToSex__confidence_id", curie=DEFAULT_.curie('confidence_id'),
                   model_uri=DEFAULT_.aopToSex__confidence_id, domain=None, range=Optional[Union[dict, ConfidenceLevel]])

slots.aopToPrototypicalStressor__id = Slot(uri=DEFAULT_.id, name="aopToPrototypicalStressor__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.aopToPrototypicalStressor__id, domain=None, range=URIRef)

slots.aopToPrototypicalStressor__aop_id = Slot(uri=DEFAULT_.aop_id, name="aopToPrototypicalStressor__aop_id", curie=DEFAULT_.curie('aop_id'),
                   model_uri=DEFAULT_.aopToPrototypicalStressor__aop_id, domain=None, range=Optional[Union[dict, Aop]])

slots.aopToPrototypicalStressor__stressor_id = Slot(uri=DEFAULT_.stressor_id, name="aopToPrototypicalStressor__stressor_id", curie=DEFAULT_.curie('stressor_id'),
                   model_uri=DEFAULT_.aopToPrototypicalStressor__stressor_id, domain=None, range=Optional[Union[dict, Stressor]])

slots.aopToPrototypicalStressor__confidence_id = Slot(uri=DEFAULT_.confidence_id, name="aopToPrototypicalStressor__confidence_id", curie=DEFAULT_.curie('confidence_id'),
                   model_uri=DEFAULT_.aopToPrototypicalStressor__confidence_id, domain=None, range=Optional[Union[dict, ConfidenceLevel]])

slots.aopToPrototypicalStressor__evidence_text = Slot(uri=DEFAULT_.evidence_text, name="aopToPrototypicalStressor__evidence_text", curie=DEFAULT_.curie('evidence_text'),
                   model_uri=DEFAULT_.aopToPrototypicalStressor__evidence_text, domain=None, range=Optional[str])

slots.aopToTaxon__id = Slot(uri=DEFAULT_.id, name="aopToTaxon__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.aopToTaxon__id, domain=None, range=URIRef)

slots.aopToTaxon__aop_id = Slot(uri=DEFAULT_.aop_id, name="aopToTaxon__aop_id", curie=DEFAULT_.curie('aop_id'),
                   model_uri=DEFAULT_.aopToTaxon__aop_id, domain=None, range=Optional[Union[dict, Aop]])

slots.aopToTaxon__taxon_term_id = Slot(uri=DEFAULT_.taxon_term_id, name="aopToTaxon__taxon_term_id", curie=DEFAULT_.curie('taxon_term_id'),
                   model_uri=DEFAULT_.aopToTaxon__taxon_term_id, domain=None, range=Optional[Union[dict, TaxonTerm]])

slots.aopToTaxon__confidence_id = Slot(uri=DEFAULT_.confidence_id, name="aopToTaxon__confidence_id", curie=DEFAULT_.curie('confidence_id'),
                   model_uri=DEFAULT_.aopToTaxon__confidence_id, domain=None, range=Optional[Union[dict, ConfidenceLevel]])

slots.assignedLicense__id = Slot(uri=DEFAULT_.id, name="assignedLicense__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.assignedLicense__id, domain=None, range=URIRef)

slots.assignedLicense__license_id = Slot(uri=DEFAULT_.license_id, name="assignedLicense__license_id", curie=DEFAULT_.curie('license_id'),
                   model_uri=DEFAULT_.assignedLicense__license_id, domain=None, range=Optional[Union[dict, License]])

slots.bioTargetFamily__id = Slot(uri=DEFAULT_.id, name="bioTargetFamily__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.bioTargetFamily__id, domain=None, range=URIRef)

slots.bioTargetFamily__name = Slot(uri=DEFAULT_.name, name="bioTargetFamily__name", curie=DEFAULT_.curie('name'),
                   model_uri=DEFAULT_.bioTargetFamily__name, domain=None, range=Optional[str])

slots.bioTargetFamily__assays = Slot(uri=DEFAULT_.assays, name="bioTargetFamily__assays", curie=DEFAULT_.curie('assays'),
                   model_uri=DEFAULT_.bioTargetFamily__assays, domain=None, range=Optional[Union[dict[Union[int, AssayId], Union[dict, Assay]], list[Union[dict, Assay]]]])

slots.bioTargetFamily__events = Slot(uri=DEFAULT_.events, name="bioTargetFamily__events", curie=DEFAULT_.curie('events'),
                   model_uri=DEFAULT_.bioTargetFamily__events, domain=None, range=Optional[Union[dict[Union[int, EventId], Union[dict, Event]], list[Union[dict, Event]]]])

slots.bioTargetFamily__citations = Slot(uri=DEFAULT_.citations, name="bioTargetFamily__citations", curie=DEFAULT_.curie('citations'),
                   model_uri=DEFAULT_.bioTargetFamily__citations, domain=None, range=Optional[Union[dict[Union[int, CitationId], Union[dict, Citation]], list[Union[dict, Citation]]]])

slots.cellTerm__id = Slot(uri=DEFAULT_.id, name="cellTerm__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.cellTerm__id, domain=None, range=URIRef)

slots.cellTerm__source_id = Slot(uri=DEFAULT_.source_id, name="cellTerm__source_id", curie=DEFAULT_.curie('source_id'),
                   model_uri=DEFAULT_.cellTerm__source_id, domain=None, range=Optional[str])

slots.cellTerm__term = Slot(uri=DEFAULT_.term, name="cellTerm__term", curie=DEFAULT_.curie('term'),
                   model_uri=DEFAULT_.cellTerm__term, domain=None, range=Optional[str])

slots.cellTerm__official_name = Slot(uri=DEFAULT_.official_name, name="cellTerm__official_name", curie=DEFAULT_.curie('official_name'),
                   model_uri=DEFAULT_.cellTerm__official_name, domain=None, range=Optional[str])

slots.cellTerm__source = Slot(uri=DEFAULT_.source, name="cellTerm__source", curie=DEFAULT_.curie('source'),
                   model_uri=DEFAULT_.cellTerm__source, domain=None, range=Optional[str])

slots.cellTerm__description = Slot(uri=DEFAULT_.description, name="cellTerm__description", curie=DEFAULT_.curie('description'),
                   model_uri=DEFAULT_.cellTerm__description, domain=None, range=Optional[str])

slots.cellTerm__url = Slot(uri=DEFAULT_.url, name="cellTerm__url", curie=DEFAULT_.curie('url'),
                   model_uri=DEFAULT_.cellTerm__url, domain=None, range=Optional[str])

slots.confidenceLevel__id = Slot(uri=DEFAULT_.id, name="confidenceLevel__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.confidenceLevel__id, domain=None, range=URIRef)

slots.confidenceLevel__term = Slot(uri=DEFAULT_.term, name="confidenceLevel__term", curie=DEFAULT_.curie('term'),
                   model_uri=DEFAULT_.confidenceLevel__term, domain=None, range=Optional[Union[str, "ConfidenceLevelEnum"]])

slots.directness__id = Slot(uri=DEFAULT_.id, name="directness__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.directness__id, domain=None, range=URIRef)

slots.directness__term = Slot(uri=DEFAULT_.term, name="directness__term", curie=DEFAULT_.curie('term'),
                   model_uri=DEFAULT_.directness__term, domain=None, range=Optional[Union[str, "DirectnessEnum"]])

slots.directness__description = Slot(uri=DEFAULT_.description, name="directness__description", curie=DEFAULT_.curie('description'),
                   model_uri=DEFAULT_.directness__description, domain=None, range=Optional[str])

slots.eventToLifeStage__id = Slot(uri=DEFAULT_.id, name="eventToLifeStage__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.eventToLifeStage__id, domain=None, range=URIRef)

slots.eventToLifeStage__event_id = Slot(uri=DEFAULT_.event_id, name="eventToLifeStage__event_id", curie=DEFAULT_.curie('event_id'),
                   model_uri=DEFAULT_.eventToLifeStage__event_id, domain=None, range=Optional[Union[dict, Event]])

slots.eventToLifeStage__life_stage_term_id = Slot(uri=DEFAULT_.life_stage_term_id, name="eventToLifeStage__life_stage_term_id", curie=DEFAULT_.curie('life_stage_term_id'),
                   model_uri=DEFAULT_.eventToLifeStage__life_stage_term_id, domain=None, range=Optional[Union[dict, LifeStageTerm]])

slots.eventToLifeStage__confidence_id = Slot(uri=DEFAULT_.confidence_id, name="eventToLifeStage__confidence_id", curie=DEFAULT_.curie('confidence_id'),
                   model_uri=DEFAULT_.eventToLifeStage__confidence_id, domain=None, range=Optional[Union[dict, ConfidenceLevel]])

slots.eventToSex__id = Slot(uri=DEFAULT_.id, name="eventToSex__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.eventToSex__id, domain=None, range=URIRef)

slots.eventToSex__event_id = Slot(uri=DEFAULT_.event_id, name="eventToSex__event_id", curie=DEFAULT_.curie('event_id'),
                   model_uri=DEFAULT_.eventToSex__event_id, domain=None, range=Optional[Union[dict, Event]])

slots.eventToSex__sex_term_id = Slot(uri=DEFAULT_.sex_term_id, name="eventToSex__sex_term_id", curie=DEFAULT_.curie('sex_term_id'),
                   model_uri=DEFAULT_.eventToSex__sex_term_id, domain=None, range=Optional[Union[dict, SexTerm]])

slots.eventToSex__confidence_id = Slot(uri=DEFAULT_.confidence_id, name="eventToSex__confidence_id", curie=DEFAULT_.curie('confidence_id'),
                   model_uri=DEFAULT_.eventToSex__confidence_id, domain=None, range=Optional[Union[dict, ConfidenceLevel]])

slots.eventToTaxon__id = Slot(uri=DEFAULT_.id, name="eventToTaxon__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.eventToTaxon__id, domain=None, range=URIRef)

slots.eventToTaxon__event_id = Slot(uri=DEFAULT_.event_id, name="eventToTaxon__event_id", curie=DEFAULT_.curie('event_id'),
                   model_uri=DEFAULT_.eventToTaxon__event_id, domain=None, range=Optional[Union[dict, Event]])

slots.eventToTaxon__taxon_term_id = Slot(uri=DEFAULT_.taxon_term_id, name="eventToTaxon__taxon_term_id", curie=DEFAULT_.curie('taxon_term_id'),
                   model_uri=DEFAULT_.eventToTaxon__taxon_term_id, domain=None, range=Optional[Union[dict, TaxonTerm]])

slots.eventToTaxon__confidence_id = Slot(uri=DEFAULT_.confidence_id, name="eventToTaxon__confidence_id", curie=DEFAULT_.curie('confidence_id'),
                   model_uri=DEFAULT_.eventToTaxon__confidence_id, domain=None, range=Optional[Union[dict, ConfidenceLevel]])

slots.experimentSetup__id = Slot(uri=DEFAULT_.id, name="experimentSetup__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.experimentSetup__id, domain=None, range=URIRef)

slots.experimentSetup__assay_id = Slot(uri=DEFAULT_.assay_id, name="experimentSetup__assay_id", curie=DEFAULT_.curie('assay_id'),
                   model_uri=DEFAULT_.experimentSetup__assay_id, domain=None, range=Optional[Union[dict, Assay]])

slots.experimentSetup__causal_agent_id = Slot(uri=DEFAULT_.causal_agent_id, name="experimentSetup__causal_agent_id", curie=DEFAULT_.curie('causal_agent_id'),
                   model_uri=DEFAULT_.experimentSetup__causal_agent_id, domain=None, range=Optional[Union[dict, Stressor]])

slots.experimentSetup__description = Slot(uri=DEFAULT_.description, name="experimentSetup__description", curie=DEFAULT_.curie('description'),
                   model_uri=DEFAULT_.experimentSetup__description, domain=None, range=Optional[str])

slots.experimentSetup__cell_terms = Slot(uri=DEFAULT_.cell_terms, name="experimentSetup__cell_terms", curie=DEFAULT_.curie('cell_terms'),
                   model_uri=DEFAULT_.experimentSetup__cell_terms, domain=None, range=Optional[Union[dict[Union[int, CellTermId], Union[dict, CellTerm]], list[Union[dict, CellTerm]]]])

slots.experimentType__id = Slot(uri=DEFAULT_.id, name="experimentType__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.experimentType__id, domain=None, range=URIRef)

slots.experimentType__exp_type = Slot(uri=DEFAULT_.exp_type, name="experimentType__exp_type", curie=DEFAULT_.curie('exp_type'),
                   model_uri=DEFAULT_.experimentType__exp_type, domain=None, range=Optional[str])

slots.handbook__id = Slot(uri=DEFAULT_.id, name="handbook__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.handbook__id, domain=None, range=URIRef)

slots.handbook__version = Slot(uri=DEFAULT_.version, name="handbook__version", curie=DEFAULT_.curie('version'),
                   model_uri=DEFAULT_.handbook__version, domain=None, range=Optional[float])

slots.handbook__release_date = Slot(uri=DEFAULT_.release_date, name="handbook__release_date", curie=DEFAULT_.curie('release_date'),
                   model_uri=DEFAULT_.handbook__release_date, domain=None, range=Optional[str])

slots.handbook__release_notes = Slot(uri=DEFAULT_.release_notes, name="handbook__release_notes", curie=DEFAULT_.curie('release_notes'),
                   model_uri=DEFAULT_.handbook__release_notes, domain=None, range=Optional[str])

slots.handbook__forum_links = Slot(uri=DEFAULT_.forum_links, name="handbook__forum_links", curie=DEFAULT_.curie('forum_links'),
                   model_uri=DEFAULT_.handbook__forum_links, domain=None, range=Optional[str])

slots.handbook__active_version = Slot(uri=DEFAULT_.active_version, name="handbook__active_version", curie=DEFAULT_.curie('active_version'),
                   model_uri=DEFAULT_.handbook__active_version, domain=None, range=Optional[str])

slots.handbook__released = Slot(uri=DEFAULT_.released, name="handbook__released", curie=DEFAULT_.curie('released'),
                   model_uri=DEFAULT_.handbook__released, domain=None, range=Optional[str])

slots.handbook__pdf_copy_uid = Slot(uri=DEFAULT_.pdf_copy_uid, name="handbook__pdf_copy_uid", curie=DEFAULT_.curie('pdf_copy_uid'),
                   model_uri=DEFAULT_.handbook__pdf_copy_uid, domain=None, range=Optional[str])

slots.handbook__pdf_only = Slot(uri=DEFAULT_.pdf_only, name="handbook__pdf_only", curie=DEFAULT_.curie('pdf_only'),
                   model_uri=DEFAULT_.handbook__pdf_only, domain=None, range=Optional[str])

slots.handbook__release_notes_doc_uid = Slot(uri=DEFAULT_.release_notes_doc_uid, name="handbook__release_notes_doc_uid", curie=DEFAULT_.curie('release_notes_doc_uid'),
                   model_uri=DEFAULT_.handbook__release_notes_doc_uid, domain=None, range=Optional[str])

slots.harmonizedAop__id = Slot(uri=DEFAULT_.id, name="harmonizedAop__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.harmonizedAop__id, domain=None, range=URIRef)

slots.harmonizedAop__tag = Slot(uri=DEFAULT_.tag, name="harmonizedAop__tag", curie=DEFAULT_.curie('tag'),
                   model_uri=DEFAULT_.harmonizedAop__tag, domain=None, range=Optional[str])

slots.harmonizedAop__new_aop_id = Slot(uri=DEFAULT_.new_aop_id, name="harmonizedAop__new_aop_id", curie=DEFAULT_.curie('new_aop_id'),
                   model_uri=DEFAULT_.harmonizedAop__new_aop_id, domain=None, range=Optional[Union[dict, Aop]])

slots.harmonizedAop__source_aop_id = Slot(uri=DEFAULT_.source_aop_id, name="harmonizedAop__source_aop_id", curie=DEFAULT_.curie('source_aop_id'),
                   model_uri=DEFAULT_.harmonizedAop__source_aop_id, domain=None, range=Optional[Union[dict, Aop]])

slots.harmonizedAop__is_priority = Slot(uri=DEFAULT_.is_priority, name="harmonizedAop__is_priority", curie=DEFAULT_.curie('is_priority'),
                   model_uri=DEFAULT_.harmonizedAop__is_priority, domain=None, range=Optional[str])

slots.harmonizedEvent__id = Slot(uri=DEFAULT_.id, name="harmonizedEvent__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.harmonizedEvent__id, domain=None, range=URIRef)

slots.harmonizedEvent__source_event_id = Slot(uri=DEFAULT_.source_event_id, name="harmonizedEvent__source_event_id", curie=DEFAULT_.curie('source_event_id'),
                   model_uri=DEFAULT_.harmonizedEvent__source_event_id, domain=None, range=Optional[Union[dict, Event]])

slots.harmonizedEvent__source_event_id_text = Slot(uri=DEFAULT_.source_event_id_text, name="harmonizedEvent__source_event_id_text", curie=DEFAULT_.curie('source_event_id_text'),
                   model_uri=DEFAULT_.harmonizedEvent__source_event_id_text, domain=None, range=Optional[str])

slots.harmonizedEvent__source_event_label = Slot(uri=DEFAULT_.source_event_label, name="harmonizedEvent__source_event_label", curie=DEFAULT_.curie('source_event_label'),
                   model_uri=DEFAULT_.harmonizedEvent__source_event_label, domain=None, range=Optional[str])

slots.harmonizedEvent__harmonized_label = Slot(uri=DEFAULT_.harmonized_label, name="harmonizedEvent__harmonized_label", curie=DEFAULT_.curie('harmonized_label'),
                   model_uri=DEFAULT_.harmonizedEvent__harmonized_label, domain=None, range=Optional[str])

slots.harmonizedEvent__harmonized_label_key = Slot(uri=DEFAULT_.harmonized_label_key, name="harmonizedEvent__harmonized_label_key", curie=DEFAULT_.curie('harmonized_label_key'),
                   model_uri=DEFAULT_.harmonizedEvent__harmonized_label_key, domain=None, range=Optional[str])

slots.harmonizedEvent__harmonized_event_id = Slot(uri=DEFAULT_.harmonized_event_id, name="harmonizedEvent__harmonized_event_id", curie=DEFAULT_.curie('harmonized_event_id'),
                   model_uri=DEFAULT_.harmonizedEvent__harmonized_event_id, domain=None, range=Optional[Union[dict, Event]])

slots.harmonizedEvent__raw_mapping_value = Slot(uri=DEFAULT_.raw_mapping_value, name="harmonizedEvent__raw_mapping_value", curie=DEFAULT_.curie('raw_mapping_value'),
                   model_uri=DEFAULT_.harmonizedEvent__raw_mapping_value, domain=None, range=Optional[str])

slots.harmonizedEvent__mapping_status = Slot(uri=DEFAULT_.mapping_status, name="harmonizedEvent__mapping_status", curie=DEFAULT_.curie('mapping_status'),
                   model_uri=DEFAULT_.harmonizedEvent__mapping_status, domain=None, range=Optional[str])

slots.license__id = Slot(uri=DEFAULT_.id, name="license__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.license__id, domain=None, range=URIRef)

slots.license__label = Slot(uri=DEFAULT_.label, name="license__label", curie=DEFAULT_.curie('label'),
                   model_uri=DEFAULT_.license__label, domain=None, range=Optional[str])

slots.license__logo_uid = Slot(uri=DEFAULT_.logo_uid, name="license__logo_uid", curie=DEFAULT_.curie('logo_uid'),
                   model_uri=DEFAULT_.license__logo_uid, domain=None, range=Optional[str])

slots.license__description = Slot(uri=DEFAULT_.description, name="license__description", curie=DEFAULT_.curie('description'),
                   model_uri=DEFAULT_.license__description, domain=None, range=Optional[str])

slots.license__internal_notes = Slot(uri=DEFAULT_.internal_notes, name="license__internal_notes", curie=DEFAULT_.curie('internal_notes'),
                   model_uri=DEFAULT_.license__internal_notes, domain=None, range=Optional[str])

slots.license__short_code = Slot(uri=DEFAULT_.short_code, name="license__short_code", curie=DEFAULT_.curie('short_code'),
                   model_uri=DEFAULT_.license__short_code, domain=None, range=Optional[str])

slots.lifeStageTerm__id = Slot(uri=DEFAULT_.id, name="lifeStageTerm__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.lifeStageTerm__id, domain=None, range=URIRef)

slots.lifeStageTerm__term = Slot(uri=DEFAULT_.term, name="lifeStageTerm__term", curie=DEFAULT_.curie('term'),
                   model_uri=DEFAULT_.lifeStageTerm__term, domain=None, range=Optional[Union[str, "LifeStageTermEnum"]])

slots.oecdStatus__id = Slot(uri=DEFAULT_.id, name="oecdStatus__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.oecdStatus__id, domain=None, range=URIRef)

slots.oecdStatus__name = Slot(uri=DEFAULT_.name, name="oecdStatus__name", curie=DEFAULT_.curie('name'),
                   model_uri=DEFAULT_.oecdStatus__name, domain=None, range=Optional[Union[str, "OecdStatusEnum"]])

slots.oecdStatus__description = Slot(uri=DEFAULT_.description, name="oecdStatus__description", curie=DEFAULT_.curie('description'),
                   model_uri=DEFAULT_.oecdStatus__description, domain=None, range=Optional[str])

slots.oecdStatus__sort = Slot(uri=DEFAULT_.sort, name="oecdStatus__sort", curie=DEFAULT_.curie('sort'),
                   model_uri=DEFAULT_.oecdStatus__sort, domain=None, range=Optional[int])

slots.organTerm__id = Slot(uri=DEFAULT_.id, name="organTerm__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.organTerm__id, domain=None, range=URIRef)

slots.organTerm__source_id = Slot(uri=DEFAULT_.source_id, name="organTerm__source_id", curie=DEFAULT_.curie('source_id'),
                   model_uri=DEFAULT_.organTerm__source_id, domain=None, range=Optional[str])

slots.organTerm__term = Slot(uri=DEFAULT_.term, name="organTerm__term", curie=DEFAULT_.curie('term'),
                   model_uri=DEFAULT_.organTerm__term, domain=None, range=Optional[str])

slots.organTerm__official_name = Slot(uri=DEFAULT_.official_name, name="organTerm__official_name", curie=DEFAULT_.curie('official_name'),
                   model_uri=DEFAULT_.organTerm__official_name, domain=None, range=Optional[str])

slots.organTerm__source = Slot(uri=DEFAULT_.source, name="organTerm__source", curie=DEFAULT_.curie('source'),
                   model_uri=DEFAULT_.organTerm__source, domain=None, range=Optional[str])

slots.organTerm__description = Slot(uri=DEFAULT_.description, name="organTerm__description", curie=DEFAULT_.curie('description'),
                   model_uri=DEFAULT_.organTerm__description, domain=None, range=Optional[str])

slots.organTerm__url = Slot(uri=DEFAULT_.url, name="organTerm__url", curie=DEFAULT_.curie('url'),
                   model_uri=DEFAULT_.organTerm__url, domain=None, range=Optional[str])

slots.keRelationshipToLifeStage__id = Slot(uri=DEFAULT_.id, name="keRelationshipToLifeStage__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.keRelationshipToLifeStage__id, domain=None, range=URIRef)

slots.keRelationshipToLifeStage__relationship_id = Slot(uri=DEFAULT_.relationship_id, name="keRelationshipToLifeStage__relationship_id", curie=DEFAULT_.curie('relationship_id'),
                   model_uri=DEFAULT_.keRelationshipToLifeStage__relationship_id, domain=None, range=Optional[Union[dict, KeRelationship]])

slots.keRelationshipToLifeStage__life_stage_term_id = Slot(uri=DEFAULT_.life_stage_term_id, name="keRelationshipToLifeStage__life_stage_term_id", curie=DEFAULT_.curie('life_stage_term_id'),
                   model_uri=DEFAULT_.keRelationshipToLifeStage__life_stage_term_id, domain=None, range=Optional[Union[dict, LifeStageTerm]])

slots.keRelationshipToLifeStage__confidence_id = Slot(uri=DEFAULT_.confidence_id, name="keRelationshipToLifeStage__confidence_id", curie=DEFAULT_.curie('confidence_id'),
                   model_uri=DEFAULT_.keRelationshipToLifeStage__confidence_id, domain=None, range=Optional[Union[dict, ConfidenceLevel]])

slots.keRelationshipToSex__id = Slot(uri=DEFAULT_.id, name="keRelationshipToSex__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.keRelationshipToSex__id, domain=None, range=URIRef)

slots.keRelationshipToSex__relationship_id = Slot(uri=DEFAULT_.relationship_id, name="keRelationshipToSex__relationship_id", curie=DEFAULT_.curie('relationship_id'),
                   model_uri=DEFAULT_.keRelationshipToSex__relationship_id, domain=None, range=Optional[Union[dict, KeRelationship]])

slots.keRelationshipToSex__sex_term_id = Slot(uri=DEFAULT_.sex_term_id, name="keRelationshipToSex__sex_term_id", curie=DEFAULT_.curie('sex_term_id'),
                   model_uri=DEFAULT_.keRelationshipToSex__sex_term_id, domain=None, range=Optional[Union[dict, SexTerm]])

slots.keRelationshipToSex__confidence_id = Slot(uri=DEFAULT_.confidence_id, name="keRelationshipToSex__confidence_id", curie=DEFAULT_.curie('confidence_id'),
                   model_uri=DEFAULT_.keRelationshipToSex__confidence_id, domain=None, range=Optional[Union[dict, ConfidenceLevel]])

slots.keRelationshipToTaxon__id = Slot(uri=DEFAULT_.id, name="keRelationshipToTaxon__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.keRelationshipToTaxon__id, domain=None, range=URIRef)

slots.keRelationshipToTaxon__relationship_id = Slot(uri=DEFAULT_.relationship_id, name="keRelationshipToTaxon__relationship_id", curie=DEFAULT_.curie('relationship_id'),
                   model_uri=DEFAULT_.keRelationshipToTaxon__relationship_id, domain=None, range=Optional[Union[dict, KeRelationship]])

slots.keRelationshipToTaxon__taxon_term_id = Slot(uri=DEFAULT_.taxon_term_id, name="keRelationshipToTaxon__taxon_term_id", curie=DEFAULT_.curie('taxon_term_id'),
                   model_uri=DEFAULT_.keRelationshipToTaxon__taxon_term_id, domain=None, range=Optional[Union[dict, TaxonTerm]])

slots.keRelationshipToTaxon__confidence_id = Slot(uri=DEFAULT_.confidence_id, name="keRelationshipToTaxon__confidence_id", curie=DEFAULT_.curie('confidence_id'),
                   model_uri=DEFAULT_.keRelationshipToTaxon__confidence_id, domain=None, range=Optional[Union[dict, ConfidenceLevel]])

slots.sexTerm__id = Slot(uri=DEFAULT_.id, name="sexTerm__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.sexTerm__id, domain=None, range=URIRef)

slots.sexTerm__term = Slot(uri=DEFAULT_.term, name="sexTerm__term", curie=DEFAULT_.curie('term'),
                   model_uri=DEFAULT_.sexTerm__term, domain=None, range=Optional[Union[str, "SexTermEnum"]])

slots.eventComponent__id = Slot(uri=DEFAULT_.id, name="eventComponent__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.eventComponent__id, domain=None, range=URIRef)

slots.eventComponent__biological_action_id = Slot(uri=DEFAULT_.biological_action_id, name="eventComponent__biological_action_id", curie=DEFAULT_.curie('biological_action_id'),
                   model_uri=DEFAULT_.eventComponent__biological_action_id, domain=None, range=Optional[Union[dict, BiologicalAction]])

slots.eventComponent__biological_object_id = Slot(uri=DEFAULT_.biological_object_id, name="eventComponent__biological_object_id", curie=DEFAULT_.curie('biological_object_id'),
                   model_uri=DEFAULT_.eventComponent__biological_object_id, domain=None, range=Optional[Union[dict, BiologicalObject]])

slots.eventComponent__biological_process_id = Slot(uri=DEFAULT_.biological_process_id, name="eventComponent__biological_process_id", curie=DEFAULT_.curie('biological_process_id'),
                   model_uri=DEFAULT_.eventComponent__biological_process_id, domain=None, range=Optional[Union[dict, BiologicalProcess]])

slots.taxonTerm__id = Slot(uri=DEFAULT_.id, name="taxonTerm__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.taxonTerm__id, domain=None, range=URIRef)

slots.taxonTerm__term_class = Slot(uri=DEFAULT_.term_class, name="taxonTerm__term_class", curie=DEFAULT_.curie('term_class'),
                   model_uri=DEFAULT_.taxonTerm__term_class, domain=None, range=Optional[Union[str, "TaxonTermClassEnum"]])

slots.taxonTerm__term = Slot(uri=DEFAULT_.term, name="taxonTerm__term", curie=DEFAULT_.curie('term'),
                   model_uri=DEFAULT_.taxonTerm__term, domain=None, range=Optional[str])

slots.taxonTerm__source = Slot(uri=DEFAULT_.source, name="taxonTerm__source", curie=DEFAULT_.curie('source'),
                   model_uri=DEFAULT_.taxonTerm__source, domain=None, range=Optional[str])

slots.taxonTerm__ncbi_id = Slot(uri=DEFAULT_.ncbi_id, name="taxonTerm__ncbi_id", curie=DEFAULT_.curie('ncbi_id'),
                   model_uri=DEFAULT_.taxonTerm__ncbi_id, domain=None, range=Optional[str])

slots.taxonTerm__scientific_term = Slot(uri=DEFAULT_.scientific_term, name="taxonTerm__scientific_term", curie=DEFAULT_.curie('scientific_term'),
                   model_uri=DEFAULT_.taxonTerm__scientific_term, domain=None, range=Optional[str])

slots.taxonTerm__source_id = Slot(uri=DEFAULT_.source_id, name="taxonTerm__source_id", curie=DEFAULT_.curie('source_id'),
                   model_uri=DEFAULT_.taxonTerm__source_id, domain=None, range=Optional[str])

slots.testGuideline__id = Slot(uri=DEFAULT_.id, name="testGuideline__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.testGuideline__id, domain=None, range=URIRef)

slots.testGuideline__short_title = Slot(uri=DEFAULT_.short_title, name="testGuideline__short_title", curie=DEFAULT_.curie('short_title'),
                   model_uri=DEFAULT_.testGuideline__short_title, domain=None, range=Optional[str])

slots.testGuideline__full_title = Slot(uri=DEFAULT_.full_title, name="testGuideline__full_title", curie=DEFAULT_.curie('full_title'),
                   model_uri=DEFAULT_.testGuideline__full_title, domain=None, range=Optional[str])

slots.testGuideline__citation_id = Slot(uri=DEFAULT_.citation_id, name="testGuideline__citation_id", curie=DEFAULT_.curie('citation_id'),
                   model_uri=DEFAULT_.testGuideline__citation_id, domain=None, range=Optional[Union[dict, Citation]])

slots.testGuideline__assays = Slot(uri=DEFAULT_.assays, name="testGuideline__assays", curie=DEFAULT_.curie('assays'),
                   model_uri=DEFAULT_.testGuideline__assays, domain=None, range=Optional[Union[dict[Union[int, AssayId], Union[dict, Assay]], list[Union[dict, Assay]]]])

slots.testGuideline__events = Slot(uri=DEFAULT_.events, name="testGuideline__events", curie=DEFAULT_.curie('events'),
                   model_uri=DEFAULT_.testGuideline__events, domain=None, range=Optional[Union[dict[Union[int, EventId], Union[dict, Event]], list[Union[dict, Event]]]])

slots.user__id = Slot(uri=DEFAULT_.id, name="user__id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.user__id, domain=None, range=URIRef)

slots.user__email = Slot(uri=DEFAULT_.email, name="user__email", curie=DEFAULT_.curie('email'),
                   model_uri=DEFAULT_.user__email, domain=None, range=Optional[str])
