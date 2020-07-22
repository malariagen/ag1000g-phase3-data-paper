READ ME 
Supplementary sampling location table
22/07/2020

Rows:
- one row per AG1000G Phase 3 sample.

Columns:
- "sample_id" - unique sample code (generated at Sanger).
- "partner_sample_id" - sample code provided by contributor.
- "sample_set" - samples are grouped into sets by their submission to the project, each set has a unique code (generated at Sanger).
- "country" - country where the sample was collected.
- "site" - site where the sample was collected (provided by contributor).
- "year" - year that the sample was collected.
- "month" - month that the sample was collected. Month is represented numerically from 1-12 with 1 being January, 2 February etc.
- "latitude" - geographic coordinate specifying the north–south position of a sample's collection site.
- "longitude" - geographic coordinate specifying the west–east position of a sample's collection site.
- "sex_call" - sample's sex call based on sex-calling pipeline described in methods.
- "aim_fraction_colu" - proportion of An. coluzzii ancestry informative markers, see methods.
- "aim_fraction_arab" - proportion of An. arabiensis ancestry informative markers, see methods.
- "species_gambcolu_arabiensis" - species call. "gambcolu" = An. gambiae or An. coluzzii; "arabiensis" = An. arabiensis; "intermediate" = An. gambiae/coluzzii x An. arabiensis hybrid. See methods.
- "species_gambiae_coluzzii" - species call. "gambiae" = An. gambiae; "coluzzii" = An. coluzzii; "intermediate" = An. gambiae x An. coluzzii hybrid. See methods.
- "is_arabiensis" - boolean species call. True = An. arabiensis.
- "is_gamb_colu" - boolean species call. True = either An. gambiae, An. coluzzii or An. gambiae x An. coluzzii hybrid.
- "is_gambiae" - boolean species call. True = An. gambiae.
- "is_coluzzii" - boolean species call. True = An. coluzzii.