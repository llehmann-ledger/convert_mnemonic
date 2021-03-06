#ifndef _EMU_OS_BIP32_H
#define _EMU_OS_BIP32_H

#include <stdint.h>

/* for cx_curve_t */
#include "cx_ec.h"

#define HDW_NORMAL 0
#define HDW_ED25519_SLIP10 1
#define HDW_SLIP21 2

typedef struct {
  uint8_t private_key[64];
  uint8_t chain_code[32];
} extended_private_key;

unsigned long sys_os_perso_derive_node_bip32(cx_curve_t curve, const uint32_t *path, size_t length, uint8_t *private_key, uint8_t* chain);
void expand_seed_bip32(const cx_curve_domain_t *domain, uint8_t *seed, unsigned int seed_length, extended_private_key *key);
int unhex(uint8_t *dst, size_t dst_size, const char *src, size_t src_size);

#endif // _EMU_OS_BIP32_H
