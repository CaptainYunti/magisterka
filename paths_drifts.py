
# 1. Hells Bells
# 2. Shoot to Thrill
# 3. What Do You Do for Money Honey
# 4. Givin' the Dog a Bone
# 5. Let Me Put My Love into You
# 6. Back in Black
# 7. You Shook Me All Night Long
# 8. Have a Drink on Me
# 9. Shake a Leg
# 10. Rock and Roll Ain't Noise Pollution

paths = [
    "./music/01 Hells Bells.mp3","./music/02 Shoot to Thrill.mp3",
    "./music/03 What Do You Do For Money Honey.mp3","./music/04 Given the Dog a Bone.mp3",
    "./music/05 Let Me Put My Love Into You.mp3", "./music/06 Back in Black.mp3",
    "./music/07 You Shook Me All Night Long.mp3", "./music/08 Have a Drink on Me.mp3",
    "./music/09 Shake a Leg.mp3", "./music/10 Rock and Roll Ain't Noise Pollution.mp3",
        ]
drifts_long = [
    (
        (0, 20, 57, 78, 87, 105, 122, 141, 149, 168, 185, 202, 211, 247, 282, 294),
        ("bells", "intro", "fast-intro", "pre-verse 1", "verse 1", "verse-fast 1", "chorus",
       "pre-verse 2", "verse 2", "verse-fast 2", "chorus", "interlude", "solo", "chorus", "outro", "outro-slow")
    ),
    (
        (0, 21, 35, 49, 58, 62, 75, 82, 96, 106, 110, 133, 150, 163, 177, 204, 231, 258, 302),
        ("intro", "fast-intro", "verse", "pre-chorus", "pre-chorus scream", "chorus", "chorus without vocal", "verse",
          "pre-chorus", "pre-chorus scream", "chorus", "post-chorus", "solo 1", "solo 2", "chorus", "interlude", "interlude-vocal", "outro", "slowdown")
    ),
    (
        (0, 16, 23, 46, 56, 71, 78, 100, 110, 125, 133, 172, 200),
        ("intro", "intro 2", "verse", "pre-chorus", "chorus", "fill", "verse", "pre-chorus", "chorus", "bridge", "solo", "chorus", "ending")
    ),
    (
        (0, 15, 22, 44, 55, 69, 76, 91, 102, 116, 152, 167, 192),
        ("intro", "pre-verse", "verse 1", "pre-chorus", "chorus", "solo 1", "verse 2", "pre-chorus", "chorus", "solo 2", "verse 3", "chorus", "outro")
    ),
    (
        (0, 20, 39, 57, 76, 85, 102, 112, 130, 139, 159, 176, 196, 226),
        ("intro", "fast-intro", "verse", "high-verse", "pre-chorus", "chorus", "after-chorus", "high-verse", "pre-chorus", "chorus", 
         "solo part 1", "solo part 2", "chorus", "outro")
    ),
    (
        (0, 6, 26, 47, 67, 88, 108, 148, 168, 188, 208),
        ("intro 1", "intro 2", "verse 1", "chorus", "verse 2", "chorus", "solo 1", "chorus", "bridge", "chorus", "solo 2")
    ),
    (
        (0, 16, 30, 46, 57, 61, 75, 102, 105, 131, 139, 147, 153, 168, 200),
        ("intro", "intro 2", "verse 1", "verse 1 - 2 guitars", "verse 1 - bass (pre-chorus)", "chorus 1", "verse 2", "pre-chorus",
         "chorus 2", "bridge", "solo", "solo part 1", "solo part 2", "solo part 3", "chorus 3", "outro")
    ),
    (
        (0, 7, 13, 19, 24, 39, 55, 67, 71, 87, 95, 110, 122, 126, 141, 162, 170, 189, 216),
        ("intro - guitar", "intro - drums", "intro - bass", "intro - riff", "riff", "verse", "rich verse", "pre-chorus", "chorus", "riff", 
         "verse", "rich verse", "pre-chorus", "chorus", "solo", "solo-end", "outro 1", "outro 2/chorus", "outro 3")
    ),
    (
        (0, 14, 34, 44, 57, 82, 95, 101, 126, 139, 148, 173, 186, 211, 233),
        ("intro", "slow-verse", "proto-chorus", "riff", "verse", "chorus", "riff", "verse", "chorus", "after-chorus", "solo 1",
         "solo 2", "verse", "chorus", "outro") # czy zwrotka ma 2 czesci?
    ),
    (
        (0, 21, 46, 67, 87, 99, 120, 140, 151, 171, 192, 203, 223, 238),
        ("intro", "intro - talking", "pre-verse", "verse", "pre-chorus", "chorus", "verse", "pre-chorus", "chorus", "solo 1", 
         "solo 2", "chorus", "chorus/outro", "outro")
    )
    ]

# short: 0 - other, 1 - verse, 2 - chorus, 3 - other vocals

drifts_short = [
    (
        (0, 87, 122, 140, 149, 184, 200, 247, 282),
        (0, 1, 2, 0, 1, 2, 0, 2, 3)
    ),
    (
        (0, 35, 62, 82, 110, 133, 177, 203),
        (0, 1, 2, 1, 2, 0, 2, 3)
    ),
    (
        (0, 23, 56, 71, 78, 110, 125, 132, 172, 200),
        (0, 1, 2, 0, 1, 2, 3, 0, 2, 3)
    ),
    (
        (0, 22, 44, 69, 76, 91, 116, 152, 167, 192),
        (0, 1, 2, 0, 1, 2, 0, 1, 2, 3)
    ),
    (
        (0, 39, 85, 102, 112, 139, 159, 196, 226),
        (0, 1, 2, 0, 1, 2, 0, 2, 3)
    ),
    (
        (0, 26, 47, 67, 88, 108, 148, 168, 188, 208),
        (0, 1, 2, 1, 2, 0, 2, 3, 2, 0)
    ),
    (
        (0, 30, 61, 75, 105, 139, 166),
        (0, 1, 2, 1, 2, 0, 2)
    ),
    (
        (0, 39, 71, 87, 95, 125, 142, 170),
        (0, 1, 2, 0, 1, 2, 0, 3)
    ),
    (
        (0, 14, 44, 57, 82, 95, 101, 126, 139, 148, 186, 210, 233),
        (0, 3, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3)
    ),
    (
        (0, 21, 46, 67, 99, 120, 151, 170, 203, 238),
        (0, 3, 0, 1, 2, 1, 2, 0, 2, 3)
    )
    ]

titles = [
    "Hells Bells", "Shoot to Thrill", "What Do You Do for Money Honey", "Givin' the Dog a Bone",
    "Let Me Put My Love into You", "Back in Black", "You Shook Me All Night Long", 
    "Have a Drink on Me", "Shake a Leg", "Rock and Roll Ain't Noise Pollution"
    ]

album = [{"title" : titles[i], "path" : paths[i], "drift" : drifts_long[i]} for i in range(len(titles))]

album_short = [{"title" : titles[i], "path" : paths[i], "drift" : drifts_short[i]} for i in range(len(titles))]


