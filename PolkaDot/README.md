
Installation

# install rust and update environment
curl https://sh.rustup.rs -sSf | sh
source ~/.cargo/env

# run rust updates and add WebAssembly target support
rustup update nightly
rustup target add wasm32-unknown-unknown --toolchain nightly

# Substrate
Install Substrate with the following command:
```
curl https://getsubstrate.io -sSf | bash
```

# Wasm Utilies

apt install binaryen
apt install wabt
cargo install pwasm-utils-cli --bin wasm-prune

References


Smart Contracts
https://medium.com/block-journal/introducing-substrate-smart-contracts-with-ink-d486289e2b59