{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    nixgl.url = "github:nix-community/nixGL";
    nixgl.inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = {
    self,
    nixpkgs,
    nixgl,
  }: let
    system = "x86_64-linux";
    pkgs = import nixpkgs {
      inherit system;
      overlays = [ nixgl.overlay ];
    };
    # pkgs = nixpkgs.legacyPackages.${system};
  in {
    devShells.${system}.default = pkgs.mkShell {
      packages = [
        pkgs.nixgl.nixGLIntel
        (pkgs.python314.withPackages (ps: with ps; [pygame-ce pillow]))
      ];
      shellHook = ''
        echo "Entered Nix devShell."
        echo "Use 'nixGLIntel python <file>.py' to run with hardware acceleration."

        alias npy="nixGLIntel python"

        echo "Aliased: \`npy=\"nixGLIntel python\"\`"
      '';
    };
  };
}
