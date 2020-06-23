import numpy as np
import MySQLdb
from pathlib import Path
import pandas as pd
import query_mlwh                                                                                                                                                                

sset = snakemake.params.sample_set

tracking = Path(snakemake.params.vobs_path, f"tracking/release/v3/wgs_sequence_qc/sequence_qc_filters_{sset}.tsv")
df = pd.read_csv(tracking, sep="\t", index_col=0)

deri_fn = Path(snakemake.params.vobs_path, f"tracking/{sset}/derived_samples.tsv")
deri = pd.read_csv(deri_fn, sep="\t", index_col=0)

df = df.join(deri[["ebi_sample_acc", "seq_state"]], how="left")

# Hmm, multiple sample IDs.
df["seq_tech"] = ""

for ix in df.index:

    accession = df.ebi_sample_acc.loc[ix]

    if not isinstance(accession, str):
        seq_state = df.seq_state.loc[ix]
        if seq_state != "failed":
            print(ix, seq_state, accession, "accession missing")
            df.at[ix, "seq_tech"] = "unsequenced"
        else:
            df.at[ix, "seq_tech"] = "failed"
        continue
        

    try:
        x = query_mlwh.select_samples_and_runs(snakemake.input.sql_config, [accession], "accession_number")

    except:
        print(accession, ix)
        raise ValueError()
    assert x.shape[0] > 0, accession

    x = x.loc[x.run_complete.notna()]
    
    name = x.instrument_name.unique()
    model = x.instrument_model.unique()

    assert len(model) == 1, x
      
    df.at[ix, "seq_tech"] = model[0]

    
df.to_csv(snakemake.output.csv, sep="\t", columns=["seq_tech", "ebi_sample_acc"], index=True)
