event_definitions = {
    "title": "A descriptive phrase which defines a discrete biological change that can be measured.",
    "short_name": "A reasonable abbreviation of the Key Event title, used in labelling throughout AOP-Wiki.",
    "biological_organization_id": "The level of biological organization at which the Key Event occurs (e.g., molecular, cellular, tissue, organ, organism).",
    "how_it_works": "The mechanistic basis explaining how perturbation of this Key Event leads to downstream effects.",
    "measured_or_detected": "A description of the type(s) of measurements that can be employed to evaluate the Key Event and the relative level of scientific confidence in those measurements.",
    "supporting_tax_evidence": "Evidence describing the taxonomic applicability of the Key Event, using Latin or common names of species or broader taxonomic groupings.",
    "evidence_for_chemical_initiation": "Documentation of how specific prototypical stressors (generally chemicals) can trigger or perturb this Key Event.",
    "examples_using_ao": "Examples illustrating the regulatory significance of this Key Event when it serves as an adverse outcome.",
    "references": "Literature cited in support of this Key Event description.",
    "definition": "A description of the biological state being observed or measured, the biological compartment in which it is measured, and its general role in the biology.",
    "organ_term_id": "The organ or tissue in which the Key Event takes place.",
    "cell_term_id": "The cell type in which the Key Event takes place.",
    "completion_score": "Calculated metric indicating how complete the Key Event documentation is.",
    "integration_score": "Calculated metric for integration and priority assessment of the Key Event.",
    "has_method_text": "Indicates whether method text has been provided for this Key Event.",
    "onto_components": "The biological components (e.g., biological objects, actions, processes) that are involved in this Key Event.",
}

# Maps class name to the enum used for its controlled-vocabulary field (term, source, or name).
class_to_enum = {
    "BiologicalActions":       ("term",       "BiologicalActionEnum"),
    "BiologicalOrganizations": ("term",       "BiologicalOrganizationEnum"),
    "BiologicalObjects":       ("source",     "BiologicalObjectSourceEnum"),
    "BiologicalProcesses":     ("source",     "BiologicalProcessSourceEnum"),
    "SexTerms":                ("term",       "SexTermEnum"),
    "LifeStageTerms":          ("term",       "LifeStageTermEnum"),
    "TaxonTerms":              ("term_class", "TaxonTermClassEnum"),
    "ConfidenceLevels":        ("term",       "ConfidenceLevelEnum"),
    "Directnesses":            ("term",       "DirectnessEnum"),
    "OecdStatuses":            ("name",       "OecdStatusEnum"),
}

biological_action_enum_list = [
    "increased",
    "decreased",
    "functional change",
    "abnormal",
    "pathological",
    "occurrence",
    "disrupted",
    "morphological change",
    "arrested",
    "delayed",
    "premature",
]

biological_organization_enum_list = [
    "Molecular",
    "Cellular",
    "Tissue",
    "Organ",
    "Individual",
    "Population",
]

# Source ontology enums: key = abbreviation, value = full name
biological_object_source_enum_list = {
    "GO":    "Gene Ontology",
    "CHEBI": "Chemical Entities of Biological Interest",
    "CL":    "Cell Ontology",
    "PR":    "Protein Ontology",
    "UBERON":"Uber-anatomy Ontology",
    "FMA":   "Foundational Model of Anatomy",
    "MESH":  "Medical Subject Headings",
    "PCO":   "Population and Community Ontology",
    "MP":    "Mammalian Phenotype Ontology",
    "TAIR":  "The Arabidopsis Information Resource",
    "N/A":   "Not applicable or not mapped to an ontology",
}

biological_process_source_enum_list = {
    "GO":   "Gene Ontology",
    "HP":   "Human Phenotype Ontology",
    "MP":   "Mammalian Phenotype Ontology",
    "NBO":  "Neurobehavior Ontology",
    "VT":   "Vertebrate Trait Ontology",
    "MESH": "Medical Subject Headings",
    "PCO":  "Population and Community Ontology",
    "MI":   "Molecular Interactions Ontology",
    "N/A":  "Not applicable or not mapped to an ontology",
    "IDO":  "Infectious Disease Ontology",
    "NCI":  "NCI Thesaurus",
    "RBO":  "Radiation Biology Ontology",
}

sex_terms_enum_list = [
    "Male",
    "Female",
    "Mixed",
    "Asexual",
    "Third Gender",
    "Hermaphrodite",
    "Unspecific",
]

life_stage_terms_enum_list = [
    "Birth to < 1 month",
    "1 to < 3 months",
    "3 to < 6 months",
    "6 to < 12 months",
    "1 to < 2 years",
    "2 to < 3 years",
    "3 to < 6 years",
    "6 to < 11 years",
    "11 to < 16 years",
    "16 to < 21 years",
    "Nursing Child",
    "Pregnancy",
    "Old Age",
    "Not Otherwise Specified",
    "Lactating Mother",
    "Conception to < Fetal",
    "Fetal to Parturition",
    "Foetal",
    "Fetal",
    "Embryo",
    "Juvenile",
    "Prepubertal",
    "Perinatal",
    "Adult, reproductively mature",
    "Adults",
    "Adult",
    "During development and at adulthood",
    "During brain development, adulthood and aging",
    "During brain development",
    "Human",
    "Development",
    "All life stages",
    "Larvae",
    "Larval development",
    "before or during gonadal sex differentiation",
]

taxon_term_classes_enum_list = [
    "scientific name",
    "common name",
    "synonym",
]

confidence_levels_enum_list = [
    "high",
    "moderate",
    "low",
    "not specified",
]

directnesses_enum_list = [
    "adjacent",
    "non-adjacent",
]

oecd_status_enum_list = [
    "Under development",
    "WPHA/WNT Endorsed",
    "ESCA Approved",
    "Under Review",
]

# Class-level descriptions sourced from AOP-Wiki handbook and info pages.
# Keys are sql-based class names (pre-rename, pre-PascalCase).
class_descriptions = {
    "aops": (
        "An AOP describes a sequence of events starting with initial interaction(s) between a stressor and a"
        " biomolecule within an organism that causes a perturbation in its biology (i.e., molecular initiating"
        " event, MIE), which can progress through a dependent series of intermediate key events (KEs) and culminate"
        " in an adverse outcome (AO) considered relevant to risk assessment or regulatory decision-making. AOPs are"
        " composed of a causal sequence of upstream to downstream KEs, representing a cascading series of measurable"
        " biological changes that can be expected to occur if the perturbation is sufficiently severe (i.e., in terms"
        " of potency, duration, frequency) to drive the pathway all the way to the AO. Importantly, AOPs do not describe"
        " every detail of the biology but instead focus on describing critical steps or check-points along the path"
        " to adversity, which are both measurable and have potential predictive value for regulatory application."
    ),
    "events": (
        "A change in biological or physiological state that is both measurable and essential to the progression"
        " of a defined biological perturbation leading to a specific adverse outcome."
    ),
    "relationships": (
        "A scientifically-based relationship that connects one key event to another, defines a causal"
        " and predictive relationship between the upstream and downstream event, and thereby facilitates"
        " inference or extrapolation of the state of the downstream key event from the known, measured,"
        "or predicted state of the upstream key event."
    ),
    "stressors": (
        "An external or internal factor that induces a perturbation to a biological system, potentially"
        " initiating a molecular initiating event (MIE) but could also impact a biological process"
        " represented by a key event. Stressors may include chemical, physical, or biological agents"
        " capable of eliciting measurable changes in the biological system relevant to the AOP."
    ),
    "citations": (),
    "evidences": (),
    "observations": (),
    "assays": (),
    "chemicals": (),
    "biological_target_families": (),
    "biological_objects": (),
    "biological_processes": (),
    "biological_actions": (),
    "biological_organizations": (),
    "confidence_levels": (),
    "directnesses": (),
    "life_stage_terms": (),
    "sex_terms": (),
    "taxon_terms": (),
    "organ_terms": (),
    "cell_terms": (),
    "oecd_statuses": (),
    "users": (),
}
