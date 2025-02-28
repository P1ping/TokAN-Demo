from dominate.tags import *


systems = [
    ("Source", "source", "{spk}_{sid}.wav"),
    ("Ours w/ 0.5x dur.", "dur_x0.5", "{spk}_{sid}.wav"),
    ("Ours w/ 1.0x dur.", "dur_x1.0", "{spk}_{sid}.wav"),
    ("Ours w/ 1.5x dur.", "dur_x1.5", "{spk}_{sid}.wav"),
]


samples = [
    ("BWC", "Chinese", "arctic_b0025", "Now, you understand."),
    (
        "BWC",
        "Chinese",
        "arctic_a0463",
        "They are his tongue, by which he makes his knowledge articulate.",
    ),
    ("LXC", "Chinese", "arctic_a0589", "I was sick once -- typhoid."),
    ("LXC", "Chinese", "arctic_b0383", "A bush chief had died a natural death."),
    (
        "NCC",
        "Chinese",
        "arctic_b0141",
        "It was beating and waiting in the ambush of those black pits.",
    ),
    (
        "TXHC",
        "Chinese",
        "arctic_a0109",
        "Do you know that you are shaking my confidence in you.",
    ),
    (
        "TXHC",
        "Chinese",
        "arctic_a0252",
        "O'Brien had been a clean living young man with ideals.",
    ),
    ("ASI", "Hindi", "arctic_a0296", "Bassett was a fastidious man."),
    (
        "ASI",
        "Hindi",
        "arctic_a0154",
        "He was smooth-shaven, and his hair and eyes were black.",
    ),
    ("RRBI", "Hindi", "arctic_b0375", "Man could not conquer them."),
    ("RRBI", "Hindi", "arctic_a0521", "Without them he could not run his empire."),
    ("SVBI", "Hindi", "arctic_b0353", "I want to know how all this is possible."),
    (
        "SVBI",
        "Hindi",
        "arctic_a0103",
        "But there came no promise from the bow of the canoe.",
    ),
    (
        "TNI",
        "Hindi",
        "arctic_b0095",
        "He heard a sound which brought him quickly into consciousness of day.",
    ),
    (
        "TNI",
        "Hindi",
        "arctic_b0038",
        "In her haste to get away she had forgotten these things.",
    ),
    ("ABA", "Arabic", "arctic_a0059", "His immaculate appearance was gone."),
    (
        "ABA",
        "Arabic",
        "arctic_a0312",
        "It lived in perpetual apprehension of that quarter of the compass.",
    ),
    ("YBAA", "Arabic", "arctic_a0396", "A rising tide of fat had submerged them."),
    (
        "YBAA",
        "Arabic",
        "arctic_a0026",
        "It occurred to me that there would have to be an accounting.",
    ),
    ("ZHAA", "Arabic", "arctic_b0032", "He caught himself with a jerk."),
    ("ZHAA", "Arabic", "arctic_b0107", "He was sure, now, of but few things."),
    (
        "HJK",
        "Korean",
        "arctic_a0088",
        "He made sure that the magazine was loaded, and resumed his paddling.",
    ),
    (
        "HJK",
        "Korean",
        "arctic_a0175",
        "Down there the earth was already swelling with life.",
    ),
    ("HKK", "Korean", "arctic_a0045", "He moved away as quietly as he had come."),
    ("HKK", "Korean", "arctic_a0290", "One by one the boys were captured."),
    (
        "YDCK",
        "Korean",
        "arctic_a0046",
        "The girl faced him, her eyes shining with sudden fear.",
    ),
    (
        "YDCK",
        "Korean",
        "arctic_a0300",
        "From my earliest recollection my sleep was a period of terror.",
    ),
    (
        "YKWK",
        "Korean",
        "arctic_a0368",
        "I just do appreciate it without being able to express my feelings.",
    ),
    ("YKWK", "Korean", "arctic_b0419", "Your father's fifth command, he nodded."),
    (
        "EBVS",
        "Spanish",
        "arctic_a0216",
        "The other felt a sudden wave of irritation rush through him.",
    ),
    ("ERMS", "Spanish", "arctic_b0515", "But already he had composed himself."),
    ("ERMS", "Spanish", "arctic_b0154", "That is the strange part of it."),
    ("MBMPS", "Spanish", "arctic_a0354", "Fresh meat they failed to obtain."),
    (
        "MBMPS",
        "Spanish",
        "arctic_a0268",
        "Now go ahead and tell me in a straightforward way what has happened.",
    ),
    (
        "NJS",
        "Spanish",
        "arctic_b0048",
        "He looked like one who had passed through an uncomfortable hour or two.",
    ),
    (
        "NJS",
        "Spanish",
        "arctic_b0421",
        "She is essentially the life-giving, life-conserving female of the species.",
    ),
    (
        "PNV",
        "Vietnamese",
        "arctic_a0053",
        "Suddenly his fingers closed tightly over the handkerchief.",
    ),
    (
        "PNV",
        "Vietnamese",
        "arctic_a0391",
        "But he reconciled himself to it by an act of faith.",
    ),
    ("THV", "Vietnamese", "arctic_a0209", "It was not a large lake, and almost round."),
    ("THV", "Vietnamese", "arctic_b0037", "Philip knew that she was not an Indian."),
    (
        "TLV",
        "Vietnamese",
        "arctic_b0238",
        "The very thought of the effort to swim over was nauseating.",
    ),
    ("TLV", "Vietnamese", "arctic_b0343", "But how are you going to do it."),
    (
        "BDL",
        "American",
        "arctic_b0450",
        "To my dearest and always appreciated friend, I submit myself.",
    ),
    (
        "BDL",
        "American",
        "arctic_b0441",
        "And there was Ethel Baird, whom also you must remember.",
    ),
    ("CLB", "American", "arctic_b0346", "There's not an iota of truth in it."),
    (
        "CLB",
        "American",
        "arctic_b0407",
        "Of course much grumbling went on, and little outbursts were continually occurring.",
    ),
    (
        "RMS",
        "American",
        "arctic_b0490",
        "What an excited whispering and conferring took place.",
    ),
    (
        "RMS",
        "American",
        "arctic_a0199",
        "Thus had the raw wilderness prepared him for this day.",
    ),
    ("SLT", "American", "arctic_a0554", "Jack London, Waikiki Beach, Honolulu, Oahu."),
    (
        "SLT",
        "American",
        "arctic_b0031",
        "Gregson had seated himself under the lamp and was sharpening a pencil.",
    ),
]


def get_table(
    root: str = "./samples",
    control_width_px=240,
) -> html_tag:
    _div = div(cls="table-responsive", style="overflow-x: scroll").add(
        table(cls="table table-sm")
    )
    with _div:
        with thead():
            with tr():
                th("Speaker", scope="col")
                for spk, act, _, _ in samples:
                    th(f"{spk} ({act})", scope="col")
        with tbody():
            with tr():
                th(
                    "Text",
                    scope="row",
                    style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                )
                for _, _, _, text in samples:
                    td(p(text))

            for sys_name, sys_id, fname_pattern in systems:
                with tr():
                    th(
                        sys_name,
                        scope="row",
                        style="white-space: nowrap; position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                    )
                    for spk, _, key, _ in samples:
                        fname = fname_pattern.format(spk=spk, sid=key)
                        td(
                            audio(
                                source(
                                    src=f"{root}/{sys_id}/{fname}",
                                    type="audio/wav",
                                ),
                                controls="",
                                style=f"width: {control_width_px:d}px",
                                preload="none",
                            )
                        )
