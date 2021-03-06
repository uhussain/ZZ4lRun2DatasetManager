info = {
    "qqZZ_powheg" : {
        "Name" : "q#bar{q} #rightarrow ZZ,Z#gamma^{*}",
        "Style" : "fill-lightblue",
        "add_perc_error" : 0.0,
        "Members" : [
            "zz4l-powheg"
        ]
    },
    "qqZZ_amcnlo":{
        "Name" : "q#bar{q} #rightarrow ZZ,Z#gamma^{*} (NLO)",
        "Style" : "fill-lightblue",
        "add_perc_error" : 0.0,
        "Members" : [
            "zz4l-amcatnlo"
        ]
    },
    "zz_powheg_mcfm" : {
        "Name" : "q#bar{q} #rightarrow ZZ,Z#gamma^{*}",
        "Style" : "fill-lightblue",
        "add_perc_error" : 0.0,
        "Members" : [
            "zz4l-powheg",
            "ggZZ4e",
            "ggZZ4m",
            "ggZZ4t",
            "ggZZ2e2mu",
            "ggZZ2e2tau",
            "ggZZ2mu2tau"
        ]
    },
    "zzjj4l_ewk" : {
        "Name" : "ZZ + 2 jets EW",
        "Style" : "fill-darkblue",
        "add_perc_error" : 0.0,
        "Members" : [
           "ZZJJTo4L-EWK"
        ]
    },
    "HZZ_signal" : {
        "Name" : "H #rightarrow ZZ",
        "Style" : "fill-lightred",
        "add_perc_error" : 0.0,
        "Members" : [
            "ggHZZ",
            "vbfHZZ",
            "ttH_HToZZ_4L",
            "WminusHToZZ",
            "WplusHToZZ",
            "ZHToZZ_4L"

        ]
    },
    "ggZZ" : {
        "Name" : "gg #rightarrow ZZ,Z#gamma^{*}",
        "Style" : "fill-blue",
        "add_perc_error" : 0.0,
        "Members" : [
            "ggZZ4e",
            "ggZZ4m",
            "ggZZ4t",
            "ggZZ2e2mu",
            "ggZZ2e2tau"
        ]
    },
    "GGZZ" : {
        "Name" : "gg #rightarrow ZZ,Z#gamma^{*}",
        "Style" : "fill-blue",
        "add_perc_error" : 0.0,
        "Members" : [
            "GGZZ4e",
            "GGZZ4m",
            "GGZZ4t",
            "GGZZ2e2mu"
        ]
    },
    "dy-jets" : {
        "Name" : "Drell-Yan",
        "Style" : "fill-green",
        "Members" : [
            "DYJetsToLLM-50"
        ]
    },
    "top" : {
        "Name" : "TT",
        "Style" : "fill-red",
        "add_perc_error" : 0.0,
        "Members" : [
            "tt-jets"
        ]
    },
    "wz3lnu-powheg" : {
        "Name" : "WZ",
        "Style" : "fill-maroon",
        "add_perc_error" : 0.0,
        "Members" : [
            "wz3lnu-powheg"
        ]
    },
    "VVV" : {
        "Name" : "t#bar{t}Z,VVV",
        "Style" : "fill-yellow",
        "add_perc_error" : 0.0,
        "Members" : [
            "ZZZ",
            "WZZ",
            "WWZ",
            "ttZ-jets"
        ]
    },
    "nonprompt" : {
        "Name" : "Z+X",
        "Style" : "fill-green",
        "add_perc_error" : 0.3,
        "Members" : [
            "DataEWKCorrected"
        ]
    },
    "data" : {
        "Name" : "Data",
        "Style" : "data",
        "Members" : [
            "AllData"
        ]
    },
    "data_all" : {
        "Name" : "Data",
        "Style" : "data",
        "Members" : [
            "AllData"
        ]
    },
    "f4_fg-0_fz-0p0015" : {
        "Name" : "f_{4}^{\\gamma} = 0,f_{4}^{Z} = 0.0015",
        "Style" : "nofill-pink-dotdash",
        "Members" : [
            "zz4l-atgc_1"
            ]
    },
    "f5_fg_0_fz_0p0015" : {
        "Name" : "f_{5}^{\\gamma} = 0,f_{5}^{Z} = 0.0015",
        "Style" : "nofill-darkpurple-dotdash",
        "Members" : [
            "zz4l-atgc_48"
            ]
    },
    "f4_fg_0p0019_fz_0p0015" : {
        "Name" : "f_{4}^{\\gamma} = 0.0019,f_{4}^{Z} = 0.0015",
        "Style" : "nofill-pink-dotdash",
        "Members" : [
            "zz4l-atgc_5"
            ]
    },
    "f5_fg_0p0019_fz_0p0015" : {
        "Name" : "f_{5}^{\\gamma} = 0.0019,f_{5}^{Z} = 0.0015",
        "Style" : "nofill-darkpurple-dotdash",
        "Members" : [
            "zz4l-atgc_27"
            ]
    },
    "sherpa_scaled" : {
        "Name" : "q#bar{q} #rightarrow ZZ (SHERPA)",
        "Style" : "nofill-black",
        "Members" : [
            "newsherpa"
            ]
    },
}

tmpinfo = {}
for key, value in info.iteritems():
    tmpinfo.update({key.replace("-", "_") : value})

info.update(tmpinfo)
