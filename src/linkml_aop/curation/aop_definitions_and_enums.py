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
    "SexTerms":                ("term",       "SexTermsEnum"),
    "LifeStageTerms":          ("term",       "LifeStageTermsEnum"),
    "TaxonTerms":              ("term_class", "TaxonTermClassesEnum"),
    "ConfidenceLevels":        ("term",       "ConfidenceLevelsEnum"),
    "Directnesses":            ("term",       "DirectnessesEnum"),
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
