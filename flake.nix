{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = {
    self,
    nixpkgs,
  }: let
    pkgs = nixpkgs.legacyPackages.x86_64-linux;
  in {
    devShells."x86_64-linux".default = pkgs.mkShell {
      packages = with pkgs; [(python311.withPackages (ps: [ps.pygame-ce]))];
    };

    #pkgs.mkShell {
    #      # could also be buildInputs,, for my purposes it do not matter: https://discourse.nixos.org/t/difference-between-buildinputs-and-packages-in-mkshell/60598/2
    #      buildInputs = with pkgs; [
    #        python315.withPackages
    #        (ps: [
    #          #pygame-ce
    #          ps.numpy
    #        ])
    #      ];
    #      # env variables..
    #      #env.RUST_SRC_PATH = "${pkgs.rust.blablabla.rustLibSrc}";
    #    };
  };
}
