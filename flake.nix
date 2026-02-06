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
    }
    # pkgs = nixpkgs.legacyPackages.${system};
  in {
    devShells.${system}.default = pkgs.mkShell {
      packages = [
        pkgs.nixgl.auto.nixGLDefault
        (pkgs.python314.withPackages (ps: with ps; [pygame-ce numpy]))
      ];
      shellHook = ''
          echo "Entered Nix devShell for AMD iGPU"
          echo "Use 'nixGL python <file>.py' to run with hardware acceleration."

          alias npy="nixGL python"

          echo "Aliased: `npy="nixGL python"`"
        '';
      };
    };
  };
}
