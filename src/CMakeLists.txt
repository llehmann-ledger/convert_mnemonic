add_library(emu
        cx_ec.c
        cx_ed25519.c
        cx_hmac.c
        cx_rng_rfc6979.c
        cx_sha256.c
        cx_sha512.c
        cx_utils.c
        emu_cx_hash.c
        emu_cx_math.c
        emu_os_bip32.c
        )

add_dependencies(emu openssl)
add_executable(privkey_algorand test_algorand.c)
target_link_libraries(privkey_algorand PRIVATE emu)
