## Aop-003
### Input
```yaml
authors: Anna Bal-Price, European Commission, Joint Research Centre (JRC), Ispra,
  Italy; Marcel Leist, University of Konstanz, Konstanz, Germany
id: 3
short_name: Mitochondrial dysfunction and Neurotoxicity
title: Inhibition of the mitochondrial complex I of nigro-striatal neurons leads to
  parkinsonian motor deficits

```
## KeRelationship-933
### Input
```yaml
downstream_event_id: 887
id: 933
upstream_event_id: 888

```
## Event-887
### Input
```yaml
id: 887
short_name: Inhibition, complex I
title: Inhibition, mitochondrial complex I

```
## Aop-587
### Input
```yaml
events:
- event_id: 1542
  type: MolecularInitiatingEvent
- event_id: 177
  type: KeyEvent
- event_id: 890
  type: KeyEvent
- event_id: 896
  type: AdverseOutcome
id: 587
ke_relationships:
- directness_id:
    term: adjacent
  relationship_id: 3637
- directness_id:
    term: adjacent
  relationship_id: 908
- directness_id:
    term: adjacent
  relationship_id: 910
short_name: Mitochondrial dysfunction and Neurotoxicity (cIII)
title: Inhibition of the mitochondrial complex III of nigro-striatal neurons leads
  to parkinsonian motor deficits

```
## Aop-003
### Input
```yaml
id: three
title: Inhibition of the mitochondrial complex I of nigro-striatal neurons leads to
  parkinsonian motor deficits

```
## Aop-587
### Input
```yaml
events:
- event_id: 1542
  type: MIE
id: 587

```
