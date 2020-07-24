cmake_minimum_required(VERSION 3.10)

project(Speculos C)

if (${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
  set(PLATFORM_BUILD darwin64-x86_64-cc)
elseif (${CMAKE_SYSTEM_NAME} MATCHES "Linux")
  set(PLATFORM_BUILD linux-x86_64)
  set(CMAKE_EXE_LINKER_FLAGS -static)
endif()

include(ExternalProject)

add_compile_options(-W -Wall -fPIC)
add_definitions(-DOS_LITTLE_ENDIAN -DNATIVE_64BITS)

include_directories(src)

if (PRECOMPILED_DEPENDENCIES_DIR)
  message(STATUS "Using OpenSSL from ${PRECOMPILED_DEPENDENCIES_DIR}")
  set(INSTALL_DIR ${PRECOMPILED_DEPENDENCIES_DIR})
  add_library(openssl STATIC IMPORTED)
else()
  message(STATUS "Building OpenSSL...")
  set(INSTALL_DIR ${CMAKE_CURRENT_BINARY_DIR}/install)

  ExternalProject_Add(
    openssl
    URL https://www.openssl.org/source/openssl-1.1.1f.tar.gz
    URL_HASH SHA256=186c6bfe6ecfba7a5b48c47f8a1673d0f3b0e5ba2e25602dd23b629975da3f35
    CONFIGURE_COMMAND ./Configure no-afalgeng no-aria no-asan no-asm no-async no-autoalginit no-autoerrinit no-autoload-config no-bf no-buildtest-c++ no-camellia no-capieng no-cast no-chacha no-cmac no-cms no-comp no-crypto-mdebug no-crypto-mdebug-backtrace no-ct no-deprecated no-des no-devcryptoeng no-dgram no-dh no-dsa no-dso no-dtls no-ec2m no-ecdh no-egd no-engine no-err no-external-tests no-filenames no-fuzz-afl no-fuzz-libfuzzer no-gost no-heartbeats no-hw no-idea no-makedepend no-md2 no-md4 no-mdc2 no-msan no-multiblock no-nextprotoneg no-ocb no-ocsp no-pinshared no-poly1305 no-posix-io no-psk no-rc2 no-rc4 no-rc5 no-rdrand no-rfc3779 no-scrypt no-sctp no-seed no-shared no-siphash no-sm2 no-sm3 no-sm4 no-sock no-srp no-srtp no-sse2 no-ssl no-ssl3-method no-ssl-trace no-stdio no-tests no-threads no-tls no-ts no-ubsan no-ui-console no-unit-test no-whirlpool no-zlib no-zlib-dynamic ${PLATFORM_BUILD} --prefix=${INSTALL_DIR}
    BUILD_COMMAND $(MAKE)
    INSTALL_COMMAND $(MAKE) install_sw
    BUILD_IN_SOURCE 1
  )

endif()

include_directories(${INSTALL_DIR}/include)
link_directories(${INSTALL_DIR}/lib)

link_libraries(ssl crypto dl)

add_subdirectory(src)

